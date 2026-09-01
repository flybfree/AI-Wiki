---
title: Beyond Correctness: Validity-Oriented Evaluation of Biomedical LLM Judges
published: 2026-08-29T08:09:29Z
authors: Rodrigo de Oliveira, Federico Pittino, James Gwinnutt, Jay Nanavati
url: http://arxiv.org/abs/2608.29127v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Correctness: Validity-Oriented Evaluation of Biomedical LLM Judges

## Abstract
We propose a scalable, validity-oriented pipeline for evaluating biomedical LLM judges when high-quality human judgments are scarce. First, we augment existing human-labelled biomedical benchmarks with deterministic, metric-grounded mutations that produce auditable preference pairs. Second, we evaluate judges beyond aggregate correctness using three deployment-relevant dimensions: correctness against metric-derived gold labels, robustness under repeated stochastic sampling, and compliance with the requested output format. We use this pipeline to assess Llama-3.1-8B-Instruct under four regimes: (1) base, using the instruct model as is; (2) SFT, distillation-based supervised fine-tuning only; (3) RL, GRPO-based reinforcement learning only; and (4) SFT$\rightarrow$RL, SFT followed by RL. The base and single-stage regimes struggle on structured medical discrimination such as PICO extraction and clinical calculations, whereas SFT$\rightarrow$RL performs best across correctness, compliance, and robustness; gains concentrate on decomposable tasks (PICO, MedCalc), at times matching or outperforming frontier models.

## Metadata
- **Published**: 2026-08-29T08:09:29Z
- **Authors**: Rodrigo de Oliveira, Federico Pittino, James Gwinnutt, Jay Nanavati
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29127v1)