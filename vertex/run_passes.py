"""Run the four passes against a de-identified corpus on two providers.

Reads keys from ~/.env.digging at runtime. Writes each response to
vertex/out/<provider>__<pass>.md. No patient data is sent: the corpus is the
redacted bundle, leak-checked before this script runs.
"""
import os, sys, json, ssl, time, glob, urllib.request, certifi

ENV = os.path.expanduser("~/.env.digging")
keys = {}
for line in open(ENV):
    line = line.strip()
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        keys[k.strip()] = v.strip().strip('"').strip("'")

CTX = ssl.create_default_context(cafile=certifi.where())

def corpus():
    parts = []
    for f in sorted(glob.glob("bundle/*.md")):
        parts.append(open(f).read())
    return "\n\n".join(parts)

def post(url, payload, headers):
    req = urllib.request.Request(url, data=json.dumps(payload).encode(),
                                 headers={"Content-Type": "application/json", **headers})
    with urllib.request.urlopen(req, context=CTX, timeout=1800) as r:
        return json.load(r)

def anthropic(model, prompt, text):
    d = post("https://api.anthropic.com/v1/messages",
             {"model": model, "max_tokens": 16000,
              "messages": [{"role": "user", "content": f"{prompt}\n\n===== CORPUS =====\n\n{text}"}]},
             {"x-api-key": keys["ANTHROPIC_API_KEY"], "anthropic-version": "2023-06-01",
              "anthropic-beta": "context-1m-2025-08-07"})
    u = d.get("usage", {})
    return "".join(b.get("text", "") for b in d.get("content", [])), u

def openai(model, prompt, text):
    d = post("https://api.openai.com/v1/chat/completions",
             {"model": model, "max_completion_tokens": 16000,
              "messages": [{"role": "user", "content": f"{prompt}\n\n===== CORPUS =====\n\n{text}"}]},
             {"Authorization": "Bearer " + keys["OPENAI_API_KEY"]})
    return d["choices"][0]["message"]["content"], d.get("usage", {})

if __name__ == "__main__":
    provider, model = sys.argv[1], sys.argv[2]
    text = corpus()
    print(f"corpus {len(text):,} chars (~{len(text)//4:,} tokens)", flush=True)
    os.makedirs("out", exist_ok=True)
    for pf in sorted(glob.glob("pass*.txt")):
        name = os.path.basename(pf).replace(".txt", "")
        dst = f"out/{provider}__{name}.md"
        if os.path.exists(dst):
            print(f"skip {dst}"); continue
        prompt = open(pf).read()
        t0 = time.time()
        try:
            out, usage = (anthropic if provider == "anthropic" else openai)(model, prompt, text)
            open(dst, "w").write(f"# {provider} / {model} / {name}\n\n{out}\n")
            print(f"OK   {dst}  {len(out):,} chars  {time.time()-t0:.0f}s  usage={usage}", flush=True)
        except Exception as e:
            body = e.read().decode()[:400] if hasattr(e, "read") else ""
            print(f"FAIL {dst}: {e} {body}", flush=True)
