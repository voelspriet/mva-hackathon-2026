import json, subprocess, time, sys
rows = [l.rstrip('\n').split('\t') for l in open('to_query.tsv')]
rows = [r for r in rows if len(r) == 5]
print("te bevragen:", len(rows), flush=True)
out = {}
BATCH = 20
for i in range(0, len(rows), BATCH):
    chunk = rows[i:i+BATCH]
    parts = []
    for j, (c, p, ref, alt, g) in enumerate(chunk):
        vid = "%s-%s-%s-%s" % (c.replace('chr',''), p, ref, alt)
        parts.append('v%d: variant(variantId: "%s", dataset: gnomad_r4) { exome { af an } genome { af an } }' % (j, vid))
    q = json.dumps({"query": "{ " + " ".join(parts) + " }"})
    for attempt in range(4):
        r = subprocess.run(["curl","-s","--max-time","60","-X","POST",
                            "https://gnomad.broadinstitute.org/api",
                            "-H","Content-Type: application/json","-d",q],
                           capture_output=True, text=True)
        try:
            d = json.loads(r.stdout).get("data") or {}
            break
        except Exception:
            time.sleep(3 * (attempt + 1)); d = {}
    for j, (c, p, ref, alt, g) in enumerate(chunk):
        v = d.get("v%d" % j)
        af = None
        if v:
            ex, ge = v.get("exome"), v.get("genome")
            cands = [x["af"] for x in (ex, ge) if x and x.get("af") is not None]
            af = max(cands) if cands else 0.0
        out["%s:%s:%s:%s" % (c, p, ref, alt)] = (g, af)
    if (i // BATCH) % 5 == 0:
        print("  %d/%d" % (i + len(chunk), len(rows)), flush=True)
    time.sleep(0.7)
json.dump(out, open('gnomad_af.json','w'))
print("klaar, opgehaald:", len(out))
