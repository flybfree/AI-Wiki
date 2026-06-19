---

title: "Summary: Automated ICD Classification of Psychiatric Diagnoses: From Classical NLP to Large Language Models"
url: http://arxiv.org/abs/2605.21154v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-20_13-26-05Z_AutomatedICDClassificationofPsychiatricDiagnoses_F.md
generated_at: "2026-06-11 10:44"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper aims to automate the mapping of free‑text psychiatric descriptions to ICD codes using NLP and ML. It evaluates classical models such as BoW and TF‑IDF against state‑of‑the‑art LLMs like e5_large, BioLORD, and Llama‑3-8B on a dataset of 145 513 Spanish psychiatric notes. The best result comes from fine‑tuned e5_large achieving a micro F1 of 0.866.

## Key Takeaways
- Classical frequency models like BoW and TF‑IDF underperform because they cannot capture the implicit semantic cues present in medical language.
- Transformer‑based embeddings consistently outperform traditional methods by better representing nuanced psychiatric terminology.
- The e5_large model, when fine‑tuned end‑to‑end, reaches a micro F1 of 0.866, showing that adapting LLMs to ICD nomenclature is crucial for handling long‑tail label distributions.

## Context
Automating diagnostic coding is a growing challenge in mental health administration where manual classification creates high costs and errors. This study contributes to the shift from handcrafted features to deep learning representations that understand clinical nuance. The work aligns with broader efforts to integrate LLMs into healthcare informatics pipelines.

## Implications
For clinicians, automated ICD mapping can reduce administrative burden and improve coding accuracy. For industry stakeholders, the findings suggest that fine‑tuned LLMs are a viable path for scalable mental health data processing. Practitioners should consider LLM adaptation as a future standard in clinical NLP solutions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.21154v1)
