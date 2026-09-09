---
title: In-Place Instruction Following in Diffusion Language Models
published: 2026-09-07T07:55:40Z
authors: Zheng Nie, Zherui Li, Jiaming Zhang, Kun Wang, Zhenhong Zhou, Yufei Guo
url: http://arxiv.org/abs/2609.07160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# In-Place Instruction Following in Diffusion Language Models

## Abstract
Diffusion Large Language Models (dLLMs) generate text via bidirectional iterative denoising, naturally supporting user-specified constraints anchored at arbitrary output positions, a paradigm known as In-place Prompting (IPP). We formalize this as the In-place Instruction Following (IIF) task and construct IIF-Bench, a hierarchical benchmark spanning literal, style, and discourse-function constraints, paired with a rubric-based local-global evaluation protocol. An inference-time attention-bias probe suggests that vanilla dLLMs often under-prioritize constraint spans during denoising. We then propose GRAFT, an IPP-oriented post-training framework combining constraint-aware SFT and preference optimization. On four representative dLLMs, GRAFT raises the average IIF score from 57.75 to 73.10 (+15.35 points), with absolute gains of 15.91 and 15.57 points on literal and discourse-function constraints, while preserving general generation ability.

## Metadata
- **Published**: 2026-09-07T07:55:40Z
- **Authors**: Zheng Nie, Zherui Li, Jiaming Zhang, Kun Wang, Zhenhong Zhou, Yufei Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07160v1)