---
title: Do Small Models Use the Law You Give Them? Context-Injected Fine-Tuning for Legal QA in Bangladesh
url: http://arxiv.org/abs/2607.23446v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_04-06-13Z_DoSmallModelsUsetheLawYouGiveThem_Context_Injected.md
generated_at: 2026-07-27 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether fine‑tuning a small legal language model on context‑injected examples improves its use of statutory law in Bangladesh. It compares three model sizes at 0.8B, 2B and 4B using the 2022 and 2023 Bar Council exams. Fine‑tuning boosts performance for smaller models while larger ones show no net gain.

## Key Takeaways
- At the 0.8B scale fine‑tuning raises the English FAISS score from 2 to 34 out of 100, indicating a substantial improvement when law is supplied as context.
- The 4B model shows no detectable increase in either Bangla or English scores across paired tests, suggesting diminishing returns for very large models on this task.
- Fine‑tuning also cuts the proportion of answers that drift from Bangla to English from over 50% down to under 1%, with statistical significance at every scale.

## Context
Legal question answering in low‑resource languages remains a challenge because models often ignore provided statutes. This study demonstrates that even modestly fine‑tuned small models can learn to incorporate legal text, offering a path for deployment where large models are impractical.

## Implications
For practitioners building cost‑effective legal assistants, the findings suggest focusing on fine‑tuning smaller models with rich context rather than relying solely on retrieval. The work also highlights language preservation as a critical quality metric in bilingual legal AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23446v1)
