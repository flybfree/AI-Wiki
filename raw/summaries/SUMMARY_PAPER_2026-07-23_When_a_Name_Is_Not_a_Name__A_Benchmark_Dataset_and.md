---
title: When a Name Is Not a Name: A Benchmark Dataset and Distilled Reasoning for Culturally Entangled Bangla Homographs in Low-Resource LLMs
url: http://arxiv.org/abs/2607.17828v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_11-17-19Z_WhenaNameIsNotaName_ABenchmarkDatasetandDistilledR.md
generated_at: 2026-07-23 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the Culturally Entangled Homograph (CEH) benchmark for Bangla language models, a dataset of 1,516 expert‑verified sentences where a single word functions both as a personal name and a culturally loaded common noun. Experiments across open‑ and closed‑source models reveal that these systems consistently default to the common‑noun sense, ignoring the name reading, even when prompted. A Bangla‑specific model fails under all prompting regimes, highlighting that language‑specific pretraining alone cannot provide cultural grounding.

## Key Takeaways
- Models exhibit a systematic dominant‑meaning bias: they favor the common‑noun interpretation of CEH words and rarely select the personal name reading, sometimes achieving 100 % failure on this task.  
- Contrastive chain‑of‑thought prompting dramatically reduces this bias without any additional training, lowering error rates to under 5 %.  
- Distilling cultural explanations into model fine‑tuning teaches small (1–3B) models to reason toward the correct reading rather than memorize labels, turning a previously failed Bangla‑specific model into the strongest system.

## Context
The paper addresses a persistent challenge in low‑resource language AI: cultural knowledge is often absent from pretraining data, leading to misinterpretations of words that carry dual meanings. By demonstrating that prompting strategies and explanation distillation can mitigate this bias, the work contributes to broader efforts on culturally aware NLP for multilingual models.

## Implications
For practitioners developing Bangla‑focused AI systems, the findings suggest that cultural grounding must be explicitly taught rather than assumed from data alone. The success of contrastive reasoning prompts offers a scalable approach to improve performance across low‑resource languages without large fine‑tuning budgets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17828v1)
