---
title: Identify, Classify, Act: Per-Instruction Controlled Compliance for LLMs over External Data
published: 2026-10-16T03:24:08Z
authors: Zesheng Shi, Xue Li, Chenrui Dai, Jing Li
url: http://arxiv.org/abs/2610.22874v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Identify, Classify, Act: Per-Instruction Controlled Compliance for LLMs over External Data

## Abstract
LLMs over external data face a per-instruction tension: a single document or tool return often interleaves legitimate directives with adversarial prompt injections, and the model must follow the former while rejecting the latter. Existing defenses suppress or trust all external instructions, collapsing the safety-utility frontier and forcing a choice between over-refusal and over-compliance. We argue the missing capability is \textbf{per-instruction credit attribution} and formalize it as External-Data Instruction Classification, an identify-classify-act decision over each embedded directive. We propose \textbf{EDIC}, a decomposed reward framework for per-instruction compliance. A scene-grounded pipeline injects mixed beneficial and harmful instructions with counterfactual filtering, while a generative judge is initialized by SFT and refined with GRPO to attribute compliance at the instruction level. The judge then produces a reward that separately encourages beneficial compliance and penalizes harmful compliance for RL training. Across two backbones and five benchmarks, EDIC improves both safety and utility over the strongest prior defense, lifting harmful-rejection by up to 7.7\% and Arena-Hard-Auto utility by 12.5\% on Qwen3-4B. The code repository is hosted at https://github.com/yingyingxia666/EDIC.

## Metadata
- **Published**: 2026-10-16T03:24:08Z
- **Authors**: Zesheng Shi, Xue Li, Chenrui Dai, Jing Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22874v1)