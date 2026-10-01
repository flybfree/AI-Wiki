---
title: GraphForge: Training Working Agents with Graph-Anchored Workspace Synthesis
url: http://arxiv.org/abs/2609.38923v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_04-07-17Z_GraphForge_TrainingWorkingAgentswithGraph_Anchored.md
generated_at: 2026-09-30 20:43
model: qwen3.6-35b-a3b
---

## Summary
GraphForge introduces a graph-anchored workspace synthesis framework designed to train working agents capable of reading diverse files, coordinating tools, and producing verifiable deliverables. By constructing evidence graphs over real-world file workspaces derived from occupation-grounded seeds, the method ensures that task requirements and verification rubrics are strictly grounded in authentic data. Fine-tuning Qwen3.6-27B on GraphForge-generated trajectories yields substantial performance gains across multiple benchmarks, with rejection fine-tuning further enhancing results through evidence-anchored selection signals.

## Key Takeaways
- GraphForge addresses limitations in existing training pipelines where model-generated files lack realism or real-file tasks lack verifiers by assembling workspaces of real files and building an evidence graph over their relations; task statements and rubrics are derived from this graph, ensuring every criterion is anchored to specific workspace files for rigorous verification.
- The framework incorporates a quality assurance loop where an initial rollout tests executability, followed by a revision agent that repairs tasks and rubrics against the original files before trajectory collection, thereby guaranteeing that generated data is both executable and faithful to the source material.
- Empirical results demonstrate that fine-tuning Qwen3.6-27B on 2,169 GraphForge trajectories significantly improves performance under OpenHands (GDPVal: +65.7) and Claude Code (Workspace-Bench-Lite: +7.7, SpreadsheetBench II: +13.7), while rejection fine-tuning using evidence-anchored rubrics as a candidate selection signal provides additional improvements across all benchmarks.

## Context
The development of autonomous agents capable of executing complex workflows is hindered by the scarcity of training data that combines realistic file interactions with verifiable outcomes. Current approaches often rely on synthetic files that fail to capture real-world diversity or use real files without robust verification mechanisms, leading to poor generalization and unchecked result quality in practical scenarios. GraphForge contributes a novel synthesis methodology that leverages evidence graphs to bridge this gap, enabling the creation of high-fidelity training data grounded

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38923v1)
