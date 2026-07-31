---
title: Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation for Long-CoT Reasoning
published: 2026-07-30T09:03:33Z
authors: Qiangqiang He, Zhongheng Wu, ZiJian Wang
url: http://arxiv.org/abs/2607.27888v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Not All Tokens Deserve Equal Credit: Counterfactual Sensitivity Credit Reallocation for Long-CoT Reasoning

## Abstract
Reinforcement learning with verifiable rewards (RLVR) is central to improving long-CoT reasoning in large language models. Critic-free methods such as GRPO convert response-level rewards into advantages and uniformly broadcast them across tokens, overlooking their unequal contributions to the final outcome. On-policy self-distillation (OPSD) instead provides dense distributional supervision by minimizing the forward KL divergence between an unprivileged policy and a privileged self-teacher, implicitly assuming that the resulting likelihood shifts encode reliable answer-aligned information. We test this premise by fixing each sampled trajectory and re-scoring it under two opposing outcome conditions, one asserting correctness and the other incorrectness. Most affected tokens shift in the same direction under both conditions, with few sign reversals and substantial overlap in the induced optimization signals. Large shifts also concentrate on highly substitutable surface-form tokens, whereas tokens carrying problem-specific reasoning content are less sensitive. These findings show that privileged shifts fail to provide reliable answer-aligned directions, while their magnitudes primarily reflect counterfactual sensitivity rather than token-level learning value. Based on these observations, we propose Counterfactual Sensitivity Credit Reallocation (CSCR), a simple extension of GRPO that reduces credit for highly sensitive tokens and renormalizes token-level advantages to preserve both the original credit budget and verifier-determined direction. On long-CoT mathematical reasoning benchmarks, CSCR consistently outperforms GRPO baseline with the same number of policy updates. Targeted ablations further corroborate our diagnosis: privilege-induced directions are unreliable, moderate downweighting is most effective, and stronger modulation destabilizes optimization.

## Metadata
- **Published**: 2026-07-30T09:03:33Z
- **Authors**: Qiangqiang He, Zhongheng Wu, ZiJian Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27888v1)