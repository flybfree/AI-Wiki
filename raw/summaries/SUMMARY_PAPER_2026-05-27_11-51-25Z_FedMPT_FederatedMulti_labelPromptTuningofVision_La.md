---
title: FedMPT: Federated Multi-label Prompt Tuning of Vision-Language Models
url: http://arxiv.org/abs/2605.28347v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-27_11-51-25Z_FedMPT_FederatedMulti_labelPromptTuningofVision_La.md
generated_at: 2026-06-11 10:48
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FedMPT, a federated multi‑label prompt tuning method for vision‑language models that addresses overfitting to spurious label correlations in decentralized settings. Experiments on several benchmark datasets show that FedMPT achieves competitive performance and surpasses state‑of‑the‑art approaches under varied conditions.

## Key Takeaways
- The method uses a causal model with front‑door adjustment to decouple MLR modeling, preventing overfitting to client‑specific label correlations.  
- It employs an LLM‑driven pipeline that identifies generalizable conditions governing label dependencies and maps them to image patches via optimal transport.  
- A gating mechanism combines synergistic predictions from multiple condition‑enriched prompts to generate robust multi‑label outputs.

## Context
Federated learning is increasingly vital for privacy‑preserving AI, yet adapting vision‑language models to heterogeneous client data often leads to overfitting and unreliable label predictions. This work contributes a principled framework that leverages language model reasoning to stabilize federated MLR, aligning with trends toward explainable and robust deep learning.

## Implications
For practitioners, FedMPT offers a practical solution to improve model generalization in privacy‑sensitive deployments without sacrificing performance. The approach can be adopted by companies seeking reliable multi‑label recognition across distributed data sources while maintaining user confidentiality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.28347v1)
