---
title: Can a System-One LLM Perform Knowledge Tracing When Few or No Learners Are Logged?
url: http://arxiv.org/abs/2610.11135v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_02-59-20Z_CanaSystem_OneLLMPerformKnowledgeTracingWhenFeworN.md
generated_at: 2026-10-08 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether an off-the-shelf System-One LLM—one that returns a probability estimate for a typed question in a single forward pass—can perform Knowledge Tracing (KT) on new courses or platforms where few or no learner interaction logs exist. The authors find that a specific model, referred to as Jev, achieves a mean AUC of 0.706 with zero target-platform data, outperforming 28 deep KT models trained on 8 learners and a System-Two reasoning-based KT approach, while costing roughly 1/100 as much in API calls. Adding minimal logged examples and a similar-learner statistic (JevKT) pushes performance to 0.722, maintaining a significant lead over deep KT up to 16 learners and an average lead up to 64 learners before supervised KT methods catch up.

## Key Takeaways
- A System-One LLM (Jev) with no target-platform training data achieves a mean AUC of 0.706 across seven KT datasets, surpassing the best of 28 deep KT models trained on 8 logged learners (0.689) and a System-Two Thinking-KT approach (0.650), at approximately 1/100 of the API cost, demonstrating that cold-start KT is feasible without any platform-specific fine-tuning or multi-sample reasoning.
- The performance gain is model-specific: three other LLMs queried with byte-identical typed requests through the official System-One adapter fall below Jev on all seven datasets, and reader-swap and contamination checks rule out input-format artifacts or memorized training data as explanations, suggesting a genuine capability difference in how Jev processes probabilistic reasoning over learner performance.
- The cold-start advantage is strongest for brand-new learners from their very first interactions, but on unseen items where all learners are already logged, traditional deep KT models retain their superiority, indicating that System-One LLMs complement rather than replace supervised KT pipelines once sufficient data accumulates.

## Context
Knowledge Tracing has long depended on large logged datasets to train deep models such as BKT, DKT, or SAKT, creating a cold-start problem for every new course, platform, or adaptive learning system. LLM-based KT approaches have attempted to sidestep this by fine-tuning on target data or by prompting a model to reason and vote over many samples (System-Two), but these methods are slow, expensive, and produce coarse probability estimates. This paper reframes the problem by asking whether the fast, single-pass probability output of a System-One LLM can serve as a viable zero-shot or few-shot KT mechanism, challenging the assumption that KT inherently requires supervised training on learner logs.

## Implications
For ed-tech practitioners and platform operators, this finding suggests that new courses or adaptive learning products can deploy a usable KT signal from day one without waiting to accumulate thousands of learner logs, dramatically reducing time-to-value and infrastructure cost. The 1/100 API-cost advantage over System-Two reasoning pipelines makes continuous, real-time KT feasible at scale for resource-constrained deployments. However, the advantage is bounded: once 64–128 learners are logged, supervised deep KT models regain superiority, so practitioners should treat System-One LLM KT as a cold-start bootstrap that transitions to traditional pipelines as data accumulates, rather than a permanent replacement.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11135v1)
