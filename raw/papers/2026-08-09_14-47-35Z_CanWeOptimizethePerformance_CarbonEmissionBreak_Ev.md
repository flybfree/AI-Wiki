---
title: Can We Optimize the Performance-Carbon Emission Break-Even Point?: The Quest for Greener LLMs
published: 2026-08-09T14:47:35Z
authors: Sourav Das, Tanmay Joshi, Kripabandhu Ghosh
url: http://arxiv.org/abs/2608.08744v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can We Optimize the Performance-Carbon Emission Break-Even Point?: The Quest for Greener LLMs

## Abstract
The carbon footprint of any deployed Large Language Model (LLM) accumulates during inference, where repeated use of the model substantially exceeds the one-time cost of fine-tuning. Yet most efficiency interventions target either pre-training scale or post-hoc compression. We ask whether folding a calibrated, differentiable energy surrogate into the fine-tuning objective can produce inference behavior that gains task accuracy at zero or near-zero carbon cost, a break-even configuration. We propose a joint loss mechanism with a per-model carbon-emission parameter, a linear surrogate over parameter norm, FLOP proxy, and a memory proxy, fit from on-hardware energy profiling. We fine-tune three architecturally distinct families: Gemma-2 2B, Llama-3.1 8B, and Qwen-2.5 14B, and evaluate inference F1 and CO$_2$ emissions on three MMLU subjects: abstract algebra, philosophy, and formal logic. We discover from several outcomes that the carbon term behaves as either harmful interference or beneficial regularization depending on the task structure. We position calibrated carbon-aware fine-tuning as a lightweight, drop-in regularizer with a non-empty but model and task-dependent break-even region. This is an ongoing work, and we will release our codebase soon.

## Metadata
- **Published**: 2026-08-09T14:47:35Z
- **Authors**: Sourav Das, Tanmay Joshi, Kripabandhu Ghosh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08744v1)