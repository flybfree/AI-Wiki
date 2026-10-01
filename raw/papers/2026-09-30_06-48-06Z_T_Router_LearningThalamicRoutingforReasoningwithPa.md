---
title: T-Router: Learning Thalamic Routing for Reasoning with Parameter-Efficient Reinforcement Learning
published: 2026-09-30T06:48:06Z
authors: Liuxian Ma, Jiale Dai, Jiaqi Li, Lu Mi
url: http://arxiv.org/abs/2609.39109v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# T-Router: Learning Thalamic Routing for Reasoning with Parameter-Efficient Reinforcement Learning

## Abstract
Parameter-efficient reinforcement learning aims to improve reasoning with a compact trainable interface to a pretrained model. We introduce the Thalamic Router (T-Router), which concentrates adaptation on the reuse of completed computations. A compressed, addressable bank preserves block changes; a depth-recurrent controller conditions their selection and relative-scale writeback. This coupling gives thalamic context-dependent routing a concrete computational form: learn which earlier contributions a receiving layer uses, and with what influence. Correctness rewards train the interface while preserving backbone parameters and layer order. On an 8.95B-parameter backbone, T-Router allocates 41.73M parameters (0.466% of the backbone) and achieves 83.64 +/- 1.16 MathAvg after GSM8K RL, compared with 73.79 +/- 1.83 for full-parameter GRPO across three evaluation rounds. At a comparable parameter budget and with matched retries, it exceeds LoRA's 77.28 +/- 1.95 MathAvg, improving all three task families and raising mean AIME accuracy from 48.33 to 60.56. Capacity-controlled comparisons favor addressable block changes and recurrent context; separate search training extends the interface to tool-mediated reasoning. These results establish controlled computation reuse as an effective route to parameter-efficient reasoning reinforcement learning.

## Metadata
- **Published**: 2026-09-30T06:48:06Z
- **Authors**: Liuxian Ma, Jiale Dai, Jiaqi Li, Lu Mi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39109v1)