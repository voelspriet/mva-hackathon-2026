---
## GENERAL METADATA
license: cc-by-4.0
tags:
- hackathon
- rare-disease
size_categories:
- n<1K
pretty_name: "Rare Disease, Real Kid: MVA Hackathon 2026"
viewer: false

## CUSTOM GATED ACCESS CONFIG
extra_gated_prompt: "You must understand and agree to follow the Hackathon Rules."
extra_gated_fields:
  Institution:
    type: text
    required: true
  City and Country:
    type: text
    required: true
  Specific date:
    type: date_picker
    required: true
  I want to use this dataset for:
    type: select
    required: true
    options:
      - "Rare Disease, Real Kid: MVA Hackathon 2026"
  I am 18 years old or older:
    type: checkbox
  I understand and agree that I must delete all data after I have completed the Hackathon:
    type: checkbox
  I agree to email MVAHackathon2026@synapse.org to notify Sage Bionetworks when data has been deleted from personal compute environments:
    type: checkbox
  I agree that I will not attempt to recontact the data subject, data subject family members, or any points of contact at the MVA Society:
    type: checkbox
  I agree that my use of the Data will be in compliance with all applicable laws, rules, regulations, and professional standards and I agree to contact Sage Bionetworks Privacy and Compliance Office via Sage Help Center (https://sagebionetworks.jira.com/servicedesk/customer/portal/20) if any unauthorized disclosure of the data occurs:
    type: checkbox
  I will not release or otherwise grant data access to anyone and I will establish appropriate safeguards to prevent unauthorized data use. Each member of my Hackathon team will be registered as a participant and agree to the Hackathon terms:
    type: checkbox
  I acknowledge that by registering for this Hackathon, submissions may be rerun by the Hackathon organizers, including Sage Bionetworks, Hugging Face, and the MVA Society. Submissions will be subject to a CC-BY 4.0 license and my name will be shared as part of the open-access information for the license to be implemented:
    type: checkbox
  I understand that by providing my email address and participating in the Hackathon, I consent to being recontacted by the Hackathon Organizers for purposes related to the Hackathon, including follow-up communications, feedback requests, and potential future research opportunities:
    type: checkbox
  I understand that all submitted results will be accessible to the broader research community to foster collaboration and innovation. Leading submissions may be prominently featured on the Hugging Face, Sage Bionetworks, or various Synapse-based websites, ensuring visibility and recognition for impactful contributions:
    type: checkbox
  "I agree to follow the official hackathon rules published on the Rare Disease, Real Kid: MVA Hackathon 2026 page.":
    type: checkbox
  I agree to follow the acknowledgement and citation requirements if I publish on my work and to follow additional requirements specified in the official hackathon rules:
    type: checkbox
extra_gated_button_content: "I understand and agree to follow the Hackathon Rules"
---

<h1 align="center">Rare Disease, Real Kid: MVA Hackathon 2026 - Dataset</h1>


* **Challenge Space:** [SageBio/rare-disease-real-kid-mva-hackathon-2026](https://sagebio-rare-disease-real-kid-mva-hackathon-2026.hf.space/)
* **Submission Period:** 24 August 2026 – 24 October 2026
* **Dataset Size:** ~85 GB

---

## Quickstart

* ### Python

```python
from huggingface_hub import hf_hub_download

# Download a specific file into a local './data' folder
file_path = hf_hub_download(
    repo_id="SageBio/mva-hackathon-2026-data",
    filename="WGS_EX2312012_HGWCNDSX7.vcf.gz",  # Replace with target file
    repo_type="dataset",
    local_dir="./data",
    token="YOUR_HF_TOKEN"
)

print(f"File downloaded to: {file_path}")
```

* ### CLI

```bash
# Download a specific file into a local './data' folder
hf download SageBio/mva-hackathon-2026-data \
  WGS_EX2312012_HGWCNDSX7.vcf.gz \
  --repo-type dataset \
  --local-dir ./data \
  --token YOUR_HF_TOKEN
```

**Note:** `YOUR_HF_TOKEN` can be omitted from either approach if you've previously logged in (either via
`hf auth login` or by setting the `HF_TOKEN` environment variable).

## Full Data Download

The compressed dataset is ~85 GB across 11 files. We strongly recommend having at least 100 - 150 GB
of storage to account for file caching, indexing, and pipeline intermediate files.

* ### Python

```python
from huggingface_hub import snapshot_download

# Download challenge files into a local './data' folder
dataset_dir = snapshot_download(
    repo_id="SageBio/mva-hackathon-2026-data",
    repo_type="dataset",
    local_dir="./data",
    ignore_patterns=["README.md", ".gitattributes"],
    token="YOUR_HF_TOKEN"
)

print(f"Dataset downloaded to: {dataset_dir}")
```

* ### CLI

```bash
# Download challenge files into a local './data' folder
hf download \
  SageBio/mva-hackathon-2026-data \
  --repo-type dataset \
  --local-dir ./data \
  --exclude "README.md" ".gitattributes" \
  --token YOUR_HF_TOKEN
```

