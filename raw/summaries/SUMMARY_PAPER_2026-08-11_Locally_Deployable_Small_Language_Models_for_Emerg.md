---
title: Locally Deployable Small Language Models for Emergency Department Decision Support: A Systematic Benchmark of Fine-Tuning Strategies
url: http://arxiv.org/abs/2608.10273v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_22-15-21Z_LocallyDeployableSmallLanguageModelsforEmergencyDe.md
generated_at: 2026-08-11 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates eight open-source small language models for emergency department decision support by comparing zero-shot prompting, prefix tuning, LoRA fine‑tuning, and full fine‑tuning against commercial baselines like Claude Haiku 4.5 and Sonnet 4.5 on triage prediction, specialist referral, and diagnosis tasks using MIMIC‑IV‑ED data. The results show that LoRA‑fine‑tuned open‑source models match or exceed commercial performance in two key areas while highlighting remaining challenges.

## Key Takeaways
- LoRA fine‑tuned open‑source SLMs outperform commercial baselines on triage level prediction and specialist referral recommendation, achieving clinically competitive accuracy.  
- Diagnosis prediction remains a weak point for open‑source SLMs, indicating current models still struggle with this task.  
- Fine‑tuned open‑source SLMs can identify highest‑severity patients that commercial baselines miss, suggesting added diagnostic value.

## Context
The rapid adoption of large language models in healthcare raises concerns about data privacy and vendor lock‑in, prompting a need for locally deployable solutions. This study provides the first systematic benchmark of fine‑tuning strategies for small language models, offering guidance on how to balance performance with operational constraints.

## Implications
These findings suggest that open‑source SLMs can serve as viable alternatives to commercial systems in emergency departments without compromising patient privacy or requiring costly infrastructure. Practitioners and developers should prioritize LoRA fine‑tuning for triage and referral tasks while addressing diagnostic limitations through further research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10273v1)
