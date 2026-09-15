---
title: Lightning Weave: Improving the Accuracy-Efficiency Frontier of Reasoning Models through Capability Composition
url: http://arxiv.org/abs/2609.14708v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-13_18-05-58Z_LightningWeave_ImprovingtheAccuracy_EfficiencyFron.md
generated_at: 2026-09-15 03:31
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
Lightning Weave is a post-training framework designed to simultaneously enhance both reasoning accuracy and inference efficiency in large language models. By extracting and composing independently learned capabilities from specialist models into a single student through on-policy distillation, the method successfully navigates the inherent trade-off between performance and computational cost. Empirical results demonstrate substantial gains across mathematics and code benchmarks while significantly reducing response token consumption.

## Key Takeaways
- The framework leverages policy shifts from pre- to post-training specialist models to represent distinct accuracy and efficiency capabilities, which are then composed into a unified student model via on-policy distillation.
- Lightning Weave employs aligned log-ratio shifts at shared token states combined with Tilted-Target DOPD to generate stable learning targets, allowing cached trajectories to be scored once without requiring multiple live anchor models during training.
- On the Qwen3.5-4B model, the approach increases HMMT 2025 accuracy from 59.2% to 64.0% while cutting response tokens by 10.7%, and boosts LiveCodeBench v5 accuracy from 41.7% to 54.2% with a 9.6% token reduction, establishing a new Pareto frontier for efficient reasoning.

## Context
The rapid scaling of large language models has intensified the challenge of balancing high reasoning performance with practical inference costs. As applications demand faster and cheaper deployment, researchers are increasingly exploring post-training techniques that decouple accuracy and efficiency objectives rather than treating them as mutually exclusive goals. This work directly addresses a critical bottleneck in modern AI system design by demonstrating how specialized capabilities can be systematically combined to push the boundaries of model optimization.

## Implications
By enabling practitioners to achieve state-of-the-art reasoning performance with fewer computational resources, Lightning Weave offers a scalable pathway for deploying advanced models in resource-constrained environments like edge devices or high-throughput cloud services. The ability to adjust anchor signal strengths also provides a tunable mechanism for optimizing the accuracy-efficiency trade-off according to specific application requirements. Ultimately, this capability composition approach could accelerate the adoption of complex reasoning models across industries where latency and cost are primary constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.14708v1)
