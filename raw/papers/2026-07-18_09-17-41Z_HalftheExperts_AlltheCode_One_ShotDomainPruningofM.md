---
title: Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding
published: 2026-07-18T09:17:41Z
authors: Anik Jha
url: http://arxiv.org/abs/2607.16721v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Half the Experts, All the Code: One-Shot Domain Pruning of Mixture-of-Experts LLMs for Coding

## Abstract
The strongest open-weight coding models are mixture-of-experts (MoE) networks: most of their size comes from large pools of "expert" subnetworks, of which only a few act on any token. That pool is why these models do not fit on the machines most developers own, yet for a user who only wants coding help, most experts encode abilities that will never be invoked. We ask how many experts can be removed, and which, by pruning two recent open-weight MoE models from different families (Qwen3.6-35B-A3B and Gemma-4-26B-A4B) under five selection strategies, judged the way a user would: by whether the model still writes correct code. Half the experts can be removed from either model with no statistically detectable loss on the primary code benchmark, and the damage lands almost entirely on abilities outside coding, the intended trade. But the winning strategy flips between the two models, so a recipe validated on one family cannot be assumed to work on another. We further show that perplexity, the metric much of the pruning literature leans on, can rate a broken model above an intact one; that a lightweight fine-tune recovers about half of what aggressive pruning loses; and that against quantizing the full model to the same memory, pruning wins only where quantization would have to drop below 3 bits per weight. Five attempts to overturn that crossover, with failure criteria fixed in advance (better calibration, guarded selection, causal expert importance, failure attribution, and an agentic evaluation letting each model repair its failures from execution feedback), all leave it standing; the last shows single-shot benchmarks overstate compression penalties broadly, as one repair turn erases the 2-bit quantization penalty entirely. Expert pruning works, but it demands per-model validation on the task the model will actually serve.

## Metadata
- **Published**: 2026-07-18T09:17:41Z
- **Authors**: Anik Jha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16721v1)