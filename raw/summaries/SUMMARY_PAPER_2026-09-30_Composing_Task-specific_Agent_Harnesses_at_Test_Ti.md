---
title: Composing Task-specific Agent Harnesses at Test Time with Reusable Primitives
url: http://arxiv.org/abs/2609.38912v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_03-57-46Z_ComposingTask_specificAgentHarnessesatTestTimewith.md
generated_at: 2026-09-30 20:54
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces STITCH, a framework that constructs task-specific agent harnesses at test time using reusable "Harness Primitives" rather than generating code from scratch. By mining primitives from failed trajectories and selecting the optimal combination based on task information, STITCH addresses the suboptimality of fixed global harnesses while minimizing generation costs and execution risks. Experiments demonstrate that this approach significantly improves task success rates, outperforming fixed baselines and human-designed harnesses with minimal overhead.

## Key Takeaways
- Fixed harness mechanisms often lead to suboptimal performance because their effectiveness varies across heterogeneous tasks; a mechanism beneficial for one task may introduce overhead or context distraction in another, creating a mismatch that STITCH resolves by enabling dynamic, task-specific harness construction without the risks of code generation.
- The authors propose Harness Primitives as reusable mechanisms with clear application scopes and composition contracts mined from failed task trajectories, allowing STITCH to compile safe and effective harnesses at test time while avoiding the debugging costs and execution hazards associated with generating new mechanism code.
- STITCH scales effectively with primitive library size, boosting task success rates by up to 12 points over fixed baselines and surpassing human-designed harnesses like Codex CLI, all while maintaining a minimal test-time composition overhead of only 2.7%, which is 638 times more efficient than generating task-specific harnesses from scratch.

## Context
As L

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.38912v1)
