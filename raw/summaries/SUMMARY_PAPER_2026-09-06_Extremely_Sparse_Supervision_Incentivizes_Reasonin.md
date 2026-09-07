---
title: Extremely Sparse Supervision Incentivizes Reasoning Ability
url: http://arxiv.org/abs/2609.04565v1
type: paper-summary
date: 2026-09-06
source_paper: 2026-09-03_23-38-48Z_ExtremelySparseSupervisionIncentivizesReasoningAbi.md
generated_at: 2026-09-06 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the effect of extremely sparse supervision on post‑training reasoning improvement in large language models. Using Qwen3 and other teacher–student configurations, it shows that reasoning can be effectively enhanced with only a few generated tokens per trajectory—about 0.05 % of all tokens—matching or exceeding gains from full‑token training.

## Key Takeaways
- Reasoning ability improves when the training objective is based on just one or two tokens per trajectory, despite the vast majority of generated tokens being ignored.
- Sparse supervision yields results comparable to dense token‑level fine‑tuning across nine model scales and diverse tasks such as math reasoning, coding, and PPO‑RLVR.
- The findings suggest that learning may rely on a few critical steps rather than micro‑corrections at every word level.

## Context
Current post‑training methods assume that effective learning requires processing many tokens, which drives the design of dense teacher‑student distillation pipelines. This work challenges that assumption by demonstrating that a minimal amount of supervision can suffice for reasoning tasks, aligning more closely with how humans reflect on and refine complex problems.

## Implications
The results imply that future post‑training algorithms need not be token‑intensive, potentially reducing computational cost and enabling faster iteration cycles. Practitioners may adopt sparse supervision strategies to improve model performance while conserving resources in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04565v1)
