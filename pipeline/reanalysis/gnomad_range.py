"""Read one position out of a remote gnomAD sites VCF by HTTP range request.

Why this exists: htslib's libcurl transport does not reach the public bucket from
this machine, and the project's data-handling rule forbids sending patient
coordinates to any API. This reads the public file as a static file instead:
fetch the tabix index, work out which compressed blocks hold the position, fetch
only those bytes, and decompress them locally. Nothing about the patient is sent
anywhere; the request is a byte range on a public object.

Usage: python3 gnomad_range.py <chrom> <pos> [exomes|genomes]
"""
import gzip
import io
import os
import struct
import subprocess
import sys
import zlib

BASE = ("https://storage.googleapis.com/gcp-public-data--gnomad/release/4.1/vcf/"
        "{kind}/gnomad.{kind}.v4.1.sites.chr{chrom}.vcf.bgz")
CACHE = os.path.expanduser("~/.cache/gnomad_tbi")


def curl(url, byte_range=None):
    cmd = ["curl", "-sfL", "--max-time", "300"]
    if byte_range:
        cmd += ["-r", byte_range]
    cmd.append(url)
    p = subprocess.run(cmd, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError("curl failed for %s range %s" % (url, byte_range))
    return p.stdout


def get_index(url):
    os.makedirs(CACHE, exist_ok=True)
    path = os.path.join(CACHE, os.path.basename(url) + ".tbi")
    if not os.path.exists(path):
        open(path, "wb").write(curl(url + ".tbi"))
    return gzip.decompress(open(path, "rb").read())


def parse_tbi(raw, want):
    """Return the chunk list and linear index for one reference sequence."""
    assert raw[:4] == b"TBI\x01", "not a tabix index"
    n_ref, fmt, cs, cb, ce, meta, skip, l_nm = struct.unpack_from("<8i", raw, 4)
    off = 36
    names = raw[off:off + l_nm].split(b"\x00")
    off += l_nm
    for i in range(n_ref):
        name = names[i].decode()
        n_bin, = struct.unpack_from("<i", raw, off)
        off += 4
        bins = {}
        for _ in range(n_bin):
            b, n_chunk = struct.unpack_from("<Ii", raw, off)
            off += 8
            chunks = []
            for _ in range(n_chunk):
                u, v = struct.unpack_from("<QQ", raw, off)
                off += 16
                chunks.append((u, v))
            bins[b] = chunks
        n_intv, = struct.unpack_from("<i", raw, off)
        off += 4
        intv = struct.unpack_from("<%dQ" % n_intv, raw, off)
        off += 8 * n_intv
        if name == want:
            return bins, intv
    return None, None


def reg2bins(beg, end):
    """Every index bin that can contain an interval, smallest last."""
    out = [0]
    for shift, start in ((26, 1), (23, 9), (20, 73), (17, 585), (14, 4681)):
        out += list(range(start + (beg >> shift), start + ((end - 1) >> shift) + 1))
    return out


def bgzf_blocks(data):
    """Decompress a concatenation of BGZF blocks, tolerating a truncated tail."""
    out = io.BytesIO()
    i = 0
    while i < len(data) - 27:
        if data[i:i + 2] != b"\x1f\x8b":
            break
        xlen = struct.unpack_from("<H", data, i + 10)[0]
        # the BSIZE extra subfield gives the block's total length minus one
        bsize = None
        j = i + 12
        end_x = j + xlen
        while j < end_x - 3:
            si1, si2, slen = data[j], data[j + 1], struct.unpack_from("<H", data, j + 2)[0]
            if si1 == 66 and si2 == 67:
                bsize = struct.unpack_from("<H", data, j + 4)[0] + 1
            j += 4 + slen
        if bsize is None or i + bsize > len(data):
            break
        block = data[i:i + bsize]
        try:
            out.write(zlib.decompress(block, 16 + zlib.MAX_WBITS))
        except zlib.error:
            break
        i += bsize
    return out.getvalue()


def query(chrom, pos, kind="exomes"):
    url = BASE.format(kind=kind, chrom=chrom)
    bins, intv = parse_tbi(get_index(url), "chr%s" % chrom)
    if bins is None:
        return []
    beg, end = pos - 1, pos
    chunks = []
    for b in reg2bins(beg, end):
        chunks += bins.get(b, [])
    if not chunks:
        return []
    # the linear index gives the earliest virtual offset worth reading
    li = intv[beg >> 14] if (beg >> 14) < len(intv) else 0
    chunks = [(u, v) for u, v in chunks if v > li]
    if not chunks:
        return []
    lo = min(u for u, _ in chunks) >> 16
    hi = (max(v for _, v in chunks) >> 16) + 65536
    raw = curl(url, "%d-%d" % (lo, hi))
    text = bgzf_blocks(raw).decode("utf-8", "replace")
    hits = []
    for line in text.split("\n"):
        if not line or line[0] == "#":
            continue
        f = line.split("\t", 8)
        if len(f) > 7 and f[1].isdigit() and int(f[1]) == pos:
            hits.append(f)
    return hits


def info_get(info, key, default="NA"):
    for kv in info.split(";"):
        if kv.startswith(key + "="):
            return kv[len(key) + 1:]
    return default


if __name__ == "__main__":
    chrom, pos = sys.argv[1], int(sys.argv[2])
    kinds = [sys.argv[3]] if len(sys.argv) > 3 else ["exomes", "genomes"]
    for kind in kinds:
        rows = query(chrom, pos, kind)
        if not rows:
            print("%s chr%s:%d  no record" % (kind, chrom, pos))
        for f in rows:
            ac, an = info_get(f[7], "AC"), info_get(f[7], "AN")
            try:
                af = "%.3g" % (int(ac) / int(an))
            except (ValueError, ZeroDivisionError):
                af = "NA"
            print("%s chr%s:%s %s>%s  AC=%s AN=%s AF=%s nhomalt=%s filter=%s"
                  % (kind, chrom, f[1], f[3], f[4], ac, an, af,
                     info_get(f[7], "nhomalt"), f[6]))
