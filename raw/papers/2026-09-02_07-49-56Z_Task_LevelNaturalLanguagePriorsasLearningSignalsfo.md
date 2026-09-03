---
title: Task-Level Natural Language Priors as Learning Signals for Low-Resource LLM Training
published: 2026-09-02T07:49:56Z
authors: Jian Gao, Xiao Zhang, Xun Zhu, Miao Li, Ji Wu
url: http://arxiv.org/abs/2609.02244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Task-Level Natural Language Priors as Learning Signals for Low-Resource LLM Training

## Abstract
Large language models (LLMs) often struggle when low-resource training data are ambiguous or incomplete. Task-level natural-language priors can provide useful guidance in such settings, but existing approaches usually treat these priors as input context rather than as learning signals during training. We propose Prior-Guided Tuning (PGT), a training perspective that incorporates natural-language priors as auxiliary learning signals for low-resource LLM training. Under this perspective, we introduce Contrastive Prior Steering (CPS), which keeps the original supervised objective intact while adding positive and negative prior-conditioned auxiliary losses to encourage task-consistent learning and discourage plausible but misleading alternatives. Experiments on AmbiMath, Jigsaw, and MNLI/HANS show that CPS consistently improves over plain and prompt fine-tuning. On AmbiMath, CPS achieves 97.6% average exact-match accuracy. On Jigsaw, CPS improves average Macro F1 by 9.5 percentage points over standard fine-tuning, and with 1/10 of the experimental training data slightly exceeds full-data plain fine-tuning. On HANS, CPS improves non-entailment accuracy by 8.3 and 5.2 percentage points for LLaMA 3.1 8B and Qwen 2.5 7B, respectively, while maintaining comparable in-domain MNLI accuracy. These results support our central claim: task-level natural-language priors can provide useful guidance as auxiliary learning signals for low-resource LLM training. Our code and data will be publicly available.

## Metadata
- **Published**: 2026-09-02T07:49:56Z
- **Authors**: Jian Gao, Xiao Zhang, Xun Zhu, Miao Li, Ji Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02244v1)