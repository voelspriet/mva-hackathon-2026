"""Build track2/audit/AUDIT_SUMMARY.md from the five partition tables.

Prompt A asked for a consolidated table of every non-supported verdict and the
partitions were delivered without one. Building it by script rather than by hand
means it cannot drift from the partitions it summarises.
Run from the repository root: python3 track2/audit/build_summary.py
"""
import glob, os, re
from collections import Counter

KEYS = ['CONTRADICTED', 'MISATTRIBUTED', 'OVERSTATED', 'NO SOURCE CITED', 'UNVERIFIABLE']
VMAP = {'S': 'SUPPORTED', 'O': 'OVERSTATED', 'C': 'CONTRADICTED',
        'M': 'MISATTRIBUTED', 'U': 'UNVERIFIABLE'}
STATED = {'a': 28, 'b': 22, 'c': 31, 'de': 54, 'fg': 49}   # each partition's own count
# fg was 50 until 6 Sep 2026. Row fg.B54 (RBM8A gnomAD frequencies) moved UNVERIFIABLE to
# SUPPORTED when the figures were retrieved; see track2/reanalysis/R7_genomewide_clinvar.md.


def bucket(v):
    """A split verdict is filed under the half that failed, as the partitions counted it."""
    vu = v.upper()
    for k in KEYS:
        if k in vu:
            return k
    return None


def rows():
    out = []
    for f in sorted(glob.glob('track2/audit/AUDIT_*.md')):
        part = os.path.basename(f).replace('AUDIT_', '').replace('.md', '').split('_')[0]
        for line in open(f):
            if not line.startswith('|'):
                continue
            c = [x.strip() for x in line.strip().strip('|').split('|')]
            if len(c) < 7 or c[0] in ('#', '') or set(c[0]) <= set('-: '):
                continue
            # quoted table rows inside a claim carry their own pipes, so anchor on both ends
            num, fix, verdict, acc, src, fl = c[0], c[-1], c[-2], c[-3], c[-4], c[-5]
            claim = ' / '.join(c[1:-5])
            v = VMAP.get(verdict.replace('*', '').strip(), verdict.replace('*', '').strip())
            b = bucket(v)
            if b:
                out.append(dict(part=part, num=num, claim=claim, fl=fl,
                                src=src, acc=acc, v=v, b=b, fix=fix))
    return out


def tier(fl):
    for i, pats in enumerate([('REPORT_track2',), ('REPORT_track1',),
                              ('gate/', 'G1', 'G2', 'G3'), ('verify', 'referee'),
                              ('research',), ('creative', 'F_math')]):
        if any(p in fl for p in pats):
            return i
    return 6


def status(r):
    if 'REPORT_track' in r['fl']:
        return 'report corrected'
    if 'F_math' in r['fl'] or 'f_math' in r['fl']:
        return 'appendix corrected'
    if 'gate/' in r['fl'] or re.match(r'^G[123]', r['fl']):
        return 'gate corrected'
    return 'working file, left as the record'


def cut(s, n):
    s = s.replace('\n', ' ').replace('|', '/')
    return s if len(s) <= n else s[:n - 1].rstrip() + '…'


def main():
    rs = rows()
    sev = {k: i for i, k in enumerate(KEYS)}
    rs.sort(key=lambda r: (tier(r['fl']), sev[r['b']], r['part'], r['num']))
    cnt = Counter(r['b'] for r in rs)
    per = Counter(r['part'] for r in rs)
    missing = {k: STATED[k] - per[k] for k in STATED if STATED[k] != per[k]}
    o = ["# AUDIT_SUMMARY: every non-supported verdict, in one table", "",
         "Prompt A asked for this file and the five partitions were delivered without it. "
         "It is built from the partition tables by script, so it cannot drift from them. "
         "Build: `track2/audit/build_summary.py`.", "",
         "**%d non-supported verdicts appear as table rows here, against the %d the five "
         "partitions count.** The difference is claims the partitions recorded in a prose "
         "list rather than in a table row: %s. Split verdicts, where one half of a sentence "
         "is supported and the other is not, are filed under the half that failed, which is "
         "the counting rule the partitions used."
         % (len(rs), sum(STATED.values()),
            ', '.join('%d in partition (%s)' % (v, k) for k, v in sorted(missing.items()))),
         "", "| Verdict | Count |", "|---|---|"]
    for k in KEYS:
        o.append("| %s | %d |" % (k, cnt.get(k, 0)))
    o += ["",
          "Ordering is by the weight a claim carries, which here means the file it sits in: "
          "the two reports first, then the gate files, then the verification and referee "
          "files, then the dossiers and the divergent lenses. Within each, by verdict "
          "severity.", "",
          "**Status column.** Every finding against `REPORT_track1.md` and "
          "`REPORT_track2.md` was applied in commit 76e8e48, with three retained "
          "deliberately and marked in the report as declared limitations rather than "
          "corrected: the inferred cystatin C statement, the NMD machinery screen, which is "
          "a project computation already labelled an assumption, and the metformin "
          "concentration, which is carried as a stated input because that partition did not "
          "re-open the supplement. Working files were left uncorrected on purpose. They are "
          "the record of what each seat wrote at the time, and correcting them would erase "
          "the thing the audit measures.", "",
          "| # | Verdict | Claim | File and line | Source cited | Access reached | "
          "Correcting sentence | Status |",
          "|---|---|---|---|---|---|---|---|"]
    for r in rs:
        o.append("| %s.%s | %s | %s | %s | %s | %s | %s | %s |" % (
            r['part'], r['num'], r['v'], cut(r['claim'], 300), cut(r['fl'], 60),
            cut(r['src'], 80), cut(r['acc'], 60), cut(r['fix'], 400), status(r)))
    open('track2/audit/AUDIT_SUMMARY.md', 'w').write("\n".join(o) + "\n")
    print("rows %d  per-partition %s  missing %s" % (len(rs), dict(per), missing))


if __name__ == '__main__':
    main()
