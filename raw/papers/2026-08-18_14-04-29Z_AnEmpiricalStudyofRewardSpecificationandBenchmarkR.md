---
title: An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning
published: 2026-08-18T14:04:29Z
authors: Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez
url: http://arxiv.org/abs/2608.17804v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Empirical Study of Reward Specification and Benchmark Reliability in GRPO-based LLM Unlearning

## Abstract
Practical LLM unlearning is usually evaluated through two objectives: suppress target-specific knowledge and preserve non-target utility. In generative QA, this leaves a third behavior underspecified: when a target-adjacent prompt admits a broader answer without target-specific leakage, the model should answer at that level rather than leak, evade, or refuse. We study this specification problem in a controlled LoRA-GRPO RWKU setting, comparing four reward designs that span lexical suppression, anti-refusal shaping, rubric-based broad answering, and an explicit refusal contrast, with and without SFT warm-up. The experiments show that optimization success is not equivalent to behavioral unlearning: RWKU forget scores, held-out completion audits, terminal training-rollout audits, and training dynamics can point to different conclusions. We trace these disagreements to reward-hacking endpoints, policy-support limits in GRPO, benchmark probes that miss endpoint changes, and rewards that can select broad-topic answering with low semantic leakage during optimization.

## Metadata
- **Published**: 2026-08-18T14:04:29Z
- **Authors**: Rubén Balbastre, Juan Manuel Orduña, Mariano Pérez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17804v1)