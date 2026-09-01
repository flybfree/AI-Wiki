---
title: StageWell: A Process-Aligned Chinese Corpus for Positive-Psychology Support Dialogue
url: http://arxiv.org/abs/2608.29326v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_15-13-11Z_StageWell_AProcess_AlignedChineseCorpusforPositive.md
generated_at: 2026-08-31 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
StageWell is a process‑aligned Chinese corpus for positive psychology dialogue that introduces a six‑stage support framework and a multi‑agent rewriting protocol to generate supervised data. The dataset includes 12,445 SFT instances, 1,849 DPO preference pairs, and expert‑revised ground truth. Experiments on four open‑source LLMs show measurable improvements in process control, response quality, and safety, with BERTScore rising by 0.037 and Q‑Overall increasing by 1.32 points.

## Key Takeaways
- Process‑localized repairs are built using flawed model outputs as rejected responses and targeted rewrites under the same context and stage constraint as chosen responses.
- Supervision yields robust gains across models, improving BERTScore (0.037), Q‑Overall (+1.32 points), S‑exact (+0.236) while reducing H‑critical rate (‑0.167).
- The work demonstrates that modeling supportive dialogue as a structured multi‑turn support process yields better results than treating it as single‑turn response generation.

## Context
Current AI research often treats dialogue supervision at the turn level or with holistic preference labels, leaving the underlying support function and local repair targets implicit. This paper addresses that gap by providing a corpus that explicitly models each stage of emotional support, enabling more precise alignment between model behavior and therapeutic intent.

## Implications
The findings suggest that industry practitioners can adopt process‑aligned datasets to enhance both user experience and safety in mental‑health chatbots. By focusing on structured multi‑turn processes rather than isolated responses, developers can produce more coherent, empathetic, and reliable support systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29326v1)
