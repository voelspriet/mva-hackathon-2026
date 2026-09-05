"""Run Prompt E on one provider against the de-identified package in pkg/."""
import os,sys,json,ssl,glob,urllib.request,certifi
keys={}
for line in open(os.path.expanduser("~/.env.digging")):
    if "=" in line and not line.startswith("#"):
        k,v=line.strip().split("=",1); keys[k.strip()]=v.strip().strip('"').strip("'")
CTX=ssl.create_default_context(cafile=certifi.where())
prompt=open("../track2/audit/PROMPT_E_external_read.md").read()
parts=[]
for f in sorted(glob.glob("pkg/*.md")):
    parts.append("<<<FILE: %s>>>\n\n%s"%(os.path.basename(f),open(f).read()))
text=prompt+"\n\n===== ATTACHED MATERIAL =====\n\n"+"\n\n".join(parts)
prov,model=sys.argv[1],sys.argv[2]
print("input %d chars (~%d tokens)"%(len(text),len(text)//4))
if prov=="anthropic":
    body={"model":model,"max_tokens":40000,"messages":[{"role":"user","content":text}]}
    req=urllib.request.Request("https://api.anthropic.com/v1/messages",data=json.dumps(body).encode(),
        headers={"Content-Type":"application/json","x-api-key":keys["ANTHROPIC_API_KEY"],
                 "anthropic-version":"2023-06-01"})
else:
    body={"model":model,"max_completion_tokens":16000,"messages":[{"role":"user","content":text}]}
    req=urllib.request.Request("https://api.openai.com/v1/chat/completions",data=json.dumps(body).encode(),
        headers={"Content-Type":"application/json","Authorization":"Bearer "+keys["OPENAI_API_KEY"]})
try:
    with urllib.request.urlopen(req,context=CTX,timeout=1800) as r: d=json.load(r)
except Exception as e:
    print("HTTP FAIL",e, e.read().decode()[:400] if hasattr(e,"read") else ""); sys.exit(1)
if prov=="anthropic":
    out="".join(b.get("text","") for b in d.get("content",[]))
    print("stop_reason:",d.get("stop_reason"),"| usage:",d.get("usage",{}).get("output_tokens"))
else:
    out=d["choices"][0]["message"]["content"]
    print("finish:",d["choices"][0].get("finish_reason"))
open("out/promptE__%s.md"%prov,"w").write(out)
print("output %d chars -> out/promptE__%s.md"%(len(out),prov))
