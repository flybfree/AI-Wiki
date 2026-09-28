---
title: Recursive Self-Improvement via On-Policy Distillation for Reasoning
url: http://arxiv.org/abs/2609.30652v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-25_00-42-31Z_RecursiveSelf_ImprovementviaOn_PolicyDistillationf.md
generated_at: 2026-09-28 14:22
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces a recursive framework for on-policy self-distillation that overcomes the limitations of frozen teachers by enabling dynamic co-evolution between student and teacher models to improve reasoning capabilities. The authors propose Dynamic Co-Evolution (DCE), which allows the privileged teacher to incorporate student improvements across training rounds, alongside Self-Refined Concise Learning (SRCL) to mitigate verbosity issues arising from stronger revisions. Evaluations demonstrate that DCE+SRCL significantly outperforms standard OPSD on competition-level mathematics benchmarks, achieving superior accuracy with reduced output lengths across multiple model scales.

## Key Takeaways
- Dynamic Co-Evolution (DCE) enables the privileged teacher model to co-evolve with the student rather than remaining frozen, ensuring that revisions learned in one training round effectively guide subsequent iterations and prevent knowledge transfer stagnation caused by static supervision.
- Self-Refined Concise Learning (SRCL) introduces a complementary objective by training on shorter, verified rewrites of the model's own responses to counteract the tendency for stronger revisions to become overly verbose and self-critical, thereby optimizing both performance and efficiency.
- Comprehensive evaluations show that DCE+SRCL surpasses OPSD across various model scales and four competition-level mathematics benchmarks; notably, Qwen3-8B with this method achieves a 65.97% Average@12 score, improving by 35.62 percentage points over OPSD while reducing mean output length by 7.80% compared to DCE alone.

## Context
On-policy distillation has emerged as a powerful paradigm for enhancing reasoning capabilities in large language models by leveraging dense token-level supervision without relying on external teachers, yet previous self-distillation approaches often sacrificed teacher adaptability to ensure training stability. This limitation created a bottleneck where students could not benefit from their own evolving insights during the learning process, restricting the potential gains of recursive improvement strategies in current AI research.

## Implications
This work suggests that recursive self-improvement loops can be stabilized and enhanced by allowing controlled co-evolution of teacher models, potentially unlocking higher performance ceilings in reasoning tasks without the computational overhead of maintaining separate external teachers. Practitioners can adopt these techniques to train more efficient and accurate reasoning models that produce concise outputs, addressing common deployment challenges related to latency and token costs associated with verbose chain-of-th

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30652v1)
