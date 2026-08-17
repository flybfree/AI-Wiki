---
title: SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Reasoning
published: 2026-08-14T12:57:02Z
authors: Haonan He, Haodi Lei, Yun Luo, Haoran Zhang, Shunkai Zhang, Yizhuo Li, Shengji Tang, Zhilin Wang, Runzhe Zhan, Lei Bai, Ganqu Cui, Fangchen Yu, Yafu Li, Peng Ye, Ning Ding, Yu Cheng
url: http://arxiv.org/abs/2608.14277v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SimpleOPD: Simple Tokenizer-Agnostic On-Policy Distillation for Long-Context Reasoning

## Abstract
On-policy distillation (OPD) offers a promising way to transfer reasoning capabilities from stronger teacher models, but applying it to long-context reasoning teachers and short-context students introduces practical challenges, including tokenizer mismatch, teacher-student distribution mismatch, response length explosion, and training instability. In this work, we study this setting by transferring proof-reasoning capabilities from the long-context reasoning model SU-01 to short-context student models. To handle tokenizer differences, we perform OPD in a shared text space and align only tokens that occupy identical text spans under the student and teacher tokenizers. To mitigate the problem of excessive generation length and frequent truncation, we introduce a student reference KL loss and mask the advantages of special termination tokens such as </think> and <|im_end|>. This strategy constrains the student from drifting excessively from its initial policy, thereby mitigating the teacher-student distribution mismatch problem and fostering steady length growth. Experiments on both same-family and different-family student models, including Qwen3, Qwen3.5, Intern-S2, GLM-4.7, Gemma-4, show consistent gains in mathematical reasoning, especially natural-language math proving. Notably, Intern-S2-Preview improves by 21.2 points on ProofBench, reaching 55.2 and surpassing Gemini-2.5-Pro. It also improves on science benchmarks such as HLE and HiPhO, suggesting that OPD transfers reasoning capabilities that generalize beyond the mathematical training domain.

## Metadata
- **Published**: 2026-08-14T12:57:02Z
- **Authors**: Haonan He, Haodi Lei, Yun Luo, Haoran Zhang, Shunkai Zhang, Yizhuo Li, Shengji Tang, Zhilin Wang, Runzhe Zhan, Lei Bai, Ganqu Cui, Fangchen Yu, Yafu Li, Peng Ye, Ning Ding, Yu Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14277v1)