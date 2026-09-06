"""Diagnose why the Anthropic pass returned empty content, and test whether
challenge context fixes it. Prints the full response envelope, not just the text."""
import os, sys, json, ssl, glob, urllib.request, certifi

ENV = os.path.expanduser("~/.env.digging")
keys = {}
for line in open(ENV):
    line = line.strip()
    if "=" in line and not line.startswith("#"):
        k, v = line.split("=", 1)
        keys[k.strip()] = v.strip().strip('"').strip("'")
CTX = ssl.create_default_context(cafile=certifi.where())

def call(model, text, preamble=""):
    body = {"model": model, "max_tokens": 4000,
            "messages": [{"role": "user", "content": preamble + text}]}
    req = urllib.request.Request("https://api.anthropic.com/v1/messages",
        data=json.dumps(body).encode(),
        headers={"Content-Type": "application/json",
                 "x-api-key": keys["ANTHROPIC_API_KEY"],
                 "anthropic-version": "2023-06-01",
                 "anthropic-beta": "context-1m-2025-08-07"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=900) as r:
            return json.load(r)
    except Exception as e:
        return {"ERROR": str(e), "body": e.read().decode()[:600] if hasattr(e, "read") else ""}

if __name__ == "__main__":
    model = sys.argv[1]
    mode = sys.argv[2]            # bare | context
    files = sys.argv[3:]
    prompt = open("pass1_contradictions.txt").read()
    corpus = "\n\n".join(open(f).read() for f in files)
    pre = ""
    if mode == "context":
        pre = open("PREAMBLE.md").read() + "\n\n"
    text = f"{prompt}\n\n===== CORPUS =====\n\n{corpus}"
    print(f"model={model} mode={mode} chars={len(pre)+len(text):,}")
    d = call(model, text, pre)
    if "ERROR" in d:
        print("HTTP ERROR:", d["ERROR"], d["body"]); sys.exit(1)
    out = "".join(b.get("text", "") for b in d.get("content", []))
    print("stop_reason:", d.get("stop_reason"))
    print("stop_sequence:", d.get("stop_sequence"))
    print("content blocks:", [b.get("type") for b in d.get("content", [])])
    print("usage:", d.get("usage"))
    print("output chars:", len(out))
    print("---- first 600 chars ----")
    print(out[:600])
