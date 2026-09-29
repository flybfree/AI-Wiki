---
title: Knowing When Thinking Is Not Enough: Teaching Small Reasoning Models to Reason Beyond Their Parametric Knowledge
url: http://arxiv.org/abs/2609.34327v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_05-07-24Z_KnowingWhenThinkingIsNotEnough_TeachingSmallReason.md
generated_at: 2026-09-28 23:04
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the limitations of scaling test-time computation for small reasoning models by analyzing intermediate states, revealing that self-refinement often fails to overcome knowledge bottlenecks where external information is required rather than just more thinking. To address this, the authors propose FlyBy, a selective querying framework that trains models to diagnose unresolved issues and query stronger external models only when parametric knowledge is insufficient. Experimental results demonstrate that FlyBy-4B and FlyBy-8B significantly outperform larger baseline models like Qwen3-14B while maintaining substantially lower serving costs.

## Key Takeaways
- Interventions across model families show that self-refinement primarily consolidates probability

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34327v1)
