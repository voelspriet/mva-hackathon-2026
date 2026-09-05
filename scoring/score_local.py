"""Rehearse a Track 1 CSV against the Space's own scorer, offline.

Usage:
  python3 scoring/score_local.py submission.csv                 # format check only
  python3 scoring/score_local.py submission.csv chr15:40183000:C:T chr15:40196000:G:A
      # score against a hypothetical answer (one or two chrom:pos:ref:alt)

The scorer is the unmodified evaluation.py copied from the hackathon Space.
The real answer key is private; this only proves the file parses, sorts and
would score as intended IF the answer were the given variants.
"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from evaluation import load_submission, score_proband

def parse(v):
    c, p, r, a = v.split(":")
    return (c, int(p), r.upper(), a.upper())

def main():
    csv_path = sys.argv[1]
    subs = load_submission(csv_path)
    for pid, rows in subs.items():
        print(f"proband {pid}: {len(rows)} rows")
        for r in rows:
            vs = " + ".join(f"{c}:{p}:{ref}>{alt}" for c, p, ref, alt in sorted(r.variants))
            bad = [c for c, *_ in r.variants if not c.startswith("chr")]
            flag = "  <-- contig lacks chr prefix, scorer will never match" if bad else ""
            print(f"  rank {r.rank:2d} epcr={r.epcr:.3f} {r.finding_type:9s} {vs}{flag}")
        if len(sys.argv) > 2:
            truth = frozenset(parse(v) for v in sys.argv[2:])
            res = score_proband(pid, rows, truth)
            print(f"  IF truth = {sorted(truth)}:")
            print(f"    full_match_rank={res.full_match_rank} partial={res.partial_match_rank} "
                  f"rank_points={res.rank_points} f_max={res.f_max:.3f}")

if __name__ == "__main__":
    main()
