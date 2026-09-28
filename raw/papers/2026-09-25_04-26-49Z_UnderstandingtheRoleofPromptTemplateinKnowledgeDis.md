---
title: Understanding the Role of Prompt Template in Knowledge Distillation for Safety Alignment
published: 2026-09-25T04:26:49Z
authors: Anjila Budathoki, Manish Dhakal, Benjamin M. Ampel, Yi Ding
url: http://arxiv.org/abs/2609.30802v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding the Role of Prompt Template in Knowledge Distillation for Safety Alignment

## Abstract
Prior research has demonstrated that the choice of prompt template during Supervised Fine-Tuning (SFT) significantly impacts the robustness of safety alignment afterwards. However, the influence of template selection during Knowledge Distillation (KD) from teacher to student remains largely unexplored. Thus, we fill this gap by analyzing how different template configurations influence the pre-existing safety alignment of the student. We observe a significant degradation of safety alignment present in the aligned base instruct-tuned model. Specifically, we find that utilizing chat templates renders the model more compliant with harmful queries compared to a non-chat template. These findings are consistent across three models: LLaMA, Gemma and Qwen model families and are evaluated across multiple safety benchmarks. We further show that using a non-chat template during distillation better preserves the base student's internal representations, while chat template distillation induces a larger representational shift. Code: https://github.com/anjilab/role-of-prompt-template-in-kd

## Metadata
- **Published**: 2026-09-25T04:26:49Z
- **Authors**: Anjila Budathoki, Manish Dhakal, Benjamin M. Ampel, Yi Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.30802v1)