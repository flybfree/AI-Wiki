---
title: Safe at One Loop, Risky at Another: Aligning Safety Across Recurrent Depths in Looped Language Models
published: 2026-10-07T10:48:43Z
authors: Yi Wang, Xiuyuan Qi, Dongqi Han, Dongsheng Li, Wenjie Wang
url: http://arxiv.org/abs/2610.10625v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safe at One Loop, Risky at Another: Aligning Safety Across Recurrent Depths in Looped Language Models

## Abstract
Looped Language Models (LoopLMs) provide a parameter efficient approach to scaling model capabilities through repeated use of shared parameters across recurrent steps. Since each recurrent depth can be read out independently, a single LoopLM exposes a broader output space across inference depths, raising an important question: whether safety is preserved throughout recurrent computation. Prior evaluations suggest that deeper recurrence can improve safety on harmful queries, but robustness under jailbreak attacks remains unclear. We therefore conduct a comprehensive safety evaluation of LoopLMs under jailbreak attacks targeting different recurrent depths. We find that attack success can increase at deeper inference depths, the same query can elicit different safety behaviors across depths, and attacks constructed against one depth can transfer to others. Moreover, SFT and preference alignment do not eliminate these safety gaps, motivating an alignment method designed for LoopLMs. We introduce SafeBridge, which combines lightweight depth specific control of shared recurrent layers, selective state bridging, and joint safety supervision across recurrent depths. Across model scales, multiple attack methods, and safety benchmarks, SafeBridge substantially reduces attack success for both matched-depth and cross-depth attacks. It also improves general utility over the vanilla models while maintaining comparable over-refusal behavior. Our results show that the safety of a LoopLM cannot be inferred from a single recurrent depth, motivating safety alignment across recurrent computation. Our code and model checkpoints will be released upon acceptance.

## Metadata
- **Published**: 2026-10-07T10:48:43Z
- **Authors**: Yi Wang, Xiuyuan Qi, Dongqi Han, Dongsheng Li, Wenjie Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10625v1)