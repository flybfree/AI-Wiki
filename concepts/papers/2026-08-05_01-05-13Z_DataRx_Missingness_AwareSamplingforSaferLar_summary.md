# Summary: 2026-08-05_01-05-13Z_DataRx_Missingness_AwareSamplingforSaferLargeLangu.md
Saved: 2026-08-05 22:22
Source: 2026-08-05_01-05-13Z_DataRx_Missingness_AwareSamplingforSaferLargeLangu.md
Model: None

---

## Summary  
Task‑specific fine‑tuning of large language models (LLMs) can degrade their safety guardrails, prompting the need for strategies that preserve alignment while improving performance. The authors propose **DataRx**, a missingness‑aware sampling method that selects safety examples based on how well they fill the “missing” parts of an LLM’s safety capabilities. By quantifying the safety signal gap using high‑dimensional hidden representations rather than discrete tokens, DataRx enables efficient selection of only a tiny fraction of safety data. The proposed approach reduces the average attack success rate across seven downstream tasks from 59.23 % to 13.70 % with just 1 % additional safety samples from BeaverTails.

## Key Contributions  
- **DataRx** introduces a missingness‑aware sampling framework that prioritizes safety examples capable of filling gaps in the model’s safety representation.  
- The method quantifies the safety signal gap between the target model’s native response and the safety reference using high‑dimensional hidden vectors, providing an objective measure for sample selection.  
- Empirically, DataRx cuts the average attack success rate from 59.23 % to 13.70 % on Llama3‑8B‑Instruct across seven tasks while using only a 1 % increase in safety data.

## Methodology  
The authors start with the hypothesis that a safety sample is more effective when it supplies missing safety signals, i.e., information that the model lacks to reach the desired safe output. Instead of treating safety examples as discrete token pairs, DataRx leverages the continuous hidden representations (e.g., from transformer layers) of both the target response and the safety reference. The gap between these vectors is computed in a high‑dimensional space; larger gaps indicate samples that are more likely to fill missing safety capabilities. Sampling is then performed by selecting examples with the largest gap values, thereby focusing on those that provide the greatest “missingness” coverage.

## Results  
Experimental evaluation on Llama3‑8B‑Instruct across seven downstream tasks shows a dramatic improvement: random mixing of safety data yields an average attack success rate of 59.23 %, whereas DataRx reduces it to 13.70 % with only a 1 % increase in the number of safety samples from BeaverTails. The authors also demonstrate that DataRx can be combined with existing safety‑data synthesis techniques, further boosting defense without substantially expanding the dataset.

## Significance  
DataRx offers a data‑centric solution to preserve LLM alignment during fine‑tuning, reducing reliance on large synthetic safety corpora and enabling more efficient, targeted sampling. By focusing on the most informative missingness signals, it lowers computational cost while significantly enhancing safety robustness—critical as LLMs become more widely deployed in high‑stakes applications.

## Related Concepts  
- Missingness‑aware sampling  
- Safety guardrails / alignment constraints  
- High‑dimensional hidden representations  
- Task‑specific fine‑tuning of LLMs  
- BeaverTails safety dataset  
- Data synthesis for safety augmentation
