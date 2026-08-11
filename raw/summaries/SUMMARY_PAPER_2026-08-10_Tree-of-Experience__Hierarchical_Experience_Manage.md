---
title: Tree-of-Experience: Hierarchical Experience Management for Self-Evolving Agents
url: http://arxiv.org/abs/2608.09044v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_02-49-38Z_Tree_of_Experience_HierarchicalExperienceManagemen.md
generated_at: 2026-08-10 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Tree-of-Experience, a framework that organizes LLM agent experiences into a hierarchical tree aligned with reasoning processes. It demonstrates that this structured experience improves problem-solving accuracy and efficiency on benchmark tasks. The results show substantial gains over baseline methods.

## Key Takeaways
- ToE creates a shared analytical perspective tree where each node represents a reasoning path, enabling feedback calibration through environmental outcomes.
- The framework enables systematic updating of experiences based on outcome-level feedback, which is crucial for complex reasoning tasks.
- Compared to experience-free baselines, ToE achieves a 31.4% relative accuracy boost in Game of 24 and a 41.24% average improvement in tsIC across FinEvolveBench.

## Context
Continual self-evolution demands that LLM agents retain and reuse experiences effectively as they adapt to new tasks. Traditional approaches often treat experience as flat data, limiting how feedback is attributed or transferred. This paper addresses the need for a structured representation that mirrors hierarchical reasoning.

## Implications
For practitioners developing adaptive AI systems, ToE offers a method to organize experience in a way that enhances reliability and transferability. The approach can be integrated into agents to improve performance without sacrificing efficiency, offering a scalable solution for complex environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09044v1)
