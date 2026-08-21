---
title: Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models
url: http://arxiv.org/abs/2608.19680v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_06-14-31Z_Frequency_AwareContinualLearningforSmartContractVu.md
generated_at: 2026-08-20 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents Frequency-Aware Continual Learning for Smart Contract Vulnerability Detection with Large Language Models, a three-stage pipeline that tackles parameter efficiency, catastrophic forgetting, and model consolidation in sequential tasks. The framework achieves Micro-F1 scores of 0.8022 during continual learning and 0.8085 after merging adapters, outperforming prior methods while using only 0.4% trainable parameters. Experiments on DIVE demonstrate success across evolving blockchain ecosystems.

## Key Takeaways
- FA‑LoRA performs adaptation in the Fourier domain with per‑frequency importance gates, requiring only 0.4% trainable parameters and beating standard LoRA and QLoRA.
- Forget‑Aware Replay leverages these frequency gates to estimate forgetting risk via loss dynamics, prioritizing vulnerable knowledge for rehearsal, yielding an average Micro‑F1 of 0.8022 across tasks.
- Anchor‑Protected Progressive Merging consolidates all adapters into a single model using the strongest‑generalizing adapter as an anchor and frequency‑domain gate competition, achieving a final Micro‑F1 of 0.8085 within 2.7% of the per‑task upper bound.

## Context
Continual learning in large language models is challenged by the need to adapt to new tasks without full retraining while preserving prior knowledge. Smart contract vulnerability detection adds domain specificity and sequential updates, making efficient, reliable adaptation crucial for real‑world blockchain applications. This work bridges these challenges with a novel frequency‑aware approach.

## Implications
The framework offers a scalable solution for continuously improving AI models in security‑critical domains where model updates are frequent and resource limited. Practitioners can adopt the pipeline to maintain high detection performance across evolving smart contract ecosystems without costly retraining or memory overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19680v1)
