# Summary: 2026-07-26_04-06-13Z_DoSmallModelsUsetheLawYouGiveThem_Context_Injected.md
Saved: 2026-07-27 22:41
Source: 2026-07-26_04-06-13Z_DoSmallModelsUsetheLawYouGiveThem_Context_Injected.md
Model: None

---

## Summary  
The paper investigates whether small language models can incorporate statutory law into their responses when fine‑tuned with context‑injected examples, focusing on legal QA in Bangladesh. It curates a bilingual dataset of 2 165 records from Bangladeshi acts and schedules, fine‑tunes Qwen3.5 at three sizes (0.8B, 2B, 4B), and evaluates performance using exam questions without external retrieval. The study shows that fine‑tuning improves low‑size models’ use of supplied law and reduces language drift, but benefits plateau or vanish for the largest model. This work demonstrates that small legal models can be made to respect contextual statutes when fine‑tuned appropriately.

## Key Contributions  
- Fine‑tuning a 0.8B Qwen3.5 model on Bangladesh legal QA raises its English FAISS score from 2 to 34/100, indicating substantial improvement in law usage.  
- The gains persist across paired testing but the 4B model shows no net gain and even regresses in some conditions, suggesting diminishing returns for larger models.  
- Fine‑tuning reduces language drift (Bangla→English) from ~50% to <1%, with statistically significant p<0.001 improvement.

## Methodology  
The authors collected 2 165 bilingual QA pairs covering six Bangladeshi acts and three schedules, fine‑tuned Qwen3.5 at 0.8B, 2B, and 4B using the dataset, evaluated on 2022/2023 Bangladesh Bar Council exams in Bangla and English (no retrieval), scored by strict consistency over three seeded runs.

## Results  
At 0.8B fine‑tuning improves English FAISS score dramatically; at 2B similar gains but less pronounced; the 4B model shows no net gain, with Bangla performance up but English regresses. Fine‑tuned models answer in requested language far more often (0.2–0.7% drift vs 44–53%). Statistical significance confirmed.

## Significance  
This work proves that small legal language models can be conditioned to respect statutory context when fine‑tuned, offering a path for cost‑effective legal QA systems in low‑resource settings like Bangladesh.

## Related Concepts  
Context‑injected fine‑tuning, bilingual legal QA, law usage in LLMs, retrieval bottleneck, model size effects, language drift.
