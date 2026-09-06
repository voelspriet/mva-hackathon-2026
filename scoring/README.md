# Offline rehearsal of the Track 1 scorer

`score_local.py` runs a Track 1 submission CSV through the challenge's own scoring function before upload, so a format error or a wrong rank is found here rather than on the leaderboard.

It imports `load_submission` and `score_proband` from `evaluation.py`, which is the organisers' code from the challenge Space, together with `groundtruth.py` and `utils.py` that it depends on. **Those files are not in this repository.** They belong to the organisers and are not ours to redistribute under this repository's licence. An earlier version of this repository had them committed; that was wrong and they were removed.

To run the rehearsal, copy `evaluation.py`, `groundtruth.py` and `utils.py` from the Space into this directory. They are ignored by git here.

```
python3 scoring/score_local.py submission.csv
python3 scoring/score_local.py submission.csv chr15:40183000:C:T chr15:40196000:G:A
```
