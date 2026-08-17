---
title: P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems
published: 2026-08-14T08:56:11Z
authors: Myunghoon Ryu, Geunpyo Park, Sungjoon Lee, XinYu Piao, Jong-Kook Kim
url: http://arxiv.org/abs/2608.14094v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems

## Abstract
Cloud-local LLM inference systems have the potential to use the reasoning capability of large cloud models while protecting sensitive user data on personal devices. Cloud-bound requests must exclude personally identifiable information (PII) to prevent external data leakage. Existing privacy-preserving methods rely on prompt perturbation, entity masking, or model fine-tuning, but these approaches may distort contextual semantics or require additional training. This paper proposes P2Skill, a prompt-based skill distillation method in which a local small language model (SLM) autonomously performs decomposition, PII-aware routing, paraphrasing, and reconstruction by following the skill prompts. Skills are iteratively refined from execution failures by a cloud LLM, enabling the local SLM to generalize beyond memorized PII patterns, and therefore P2Skill requires no privacy-specific fine-tuning or learned auxiliary detectors. Evaluation on a four-domain benchmark shows that P2Skill achieves $1.69\times$ and $3.66\times$ higher privacy-preserved inference quality than previous baselines.

## Metadata
- **Published**: 2026-08-14T08:56:11Z
- **Authors**: Myunghoon Ryu, Geunpyo Park, Sungjoon Lee, XinYu Piao, Jong-Kook Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14094v1)