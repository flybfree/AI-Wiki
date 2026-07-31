---
title: Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold
url: http://arxiv.org/abs/2607.27770v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_07-05-37Z_BeyondtheBestTeacher_ExpandingandCompressingtheRea.md
generated_at: 2026-07-30 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a two-stage method for building teacher unions that improve reinforcement learning agents by expanding coverage and compressing reliable teachers. Experiments show Qwen3-1.7B outperforms top individual teachers in math, code, and instruction tasks with modest gains while using only one model. The method demonstrates that stronger students can be achieved by deliberately constructing complementary teacher unions.

## Key Takeaways
- The expand-then-compress framework trains a sequence of teachers via RGRPO to cover diverse solution modes.
- Teacher-Union On-policy Distillation uses reliability gates so only high-quality teacher responses affect student learning.
- Consensus-Residual Decomposition keeps the best teacher's token preferences intact during aggregation.

## Context
Current RL training often yields a single teacher that misses many valid reasoning paths, limiting performance. This work addresses the need for richer, more representative knowledge bases in language models. The approach aligns with trends toward modular, composable AI systems where specialized components collaborate.

## Implications
Building teacher unions can boost model capabilities without extra compute or hardware. Practitioners may adopt this approach to enhance instruction following and code generation with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27770v1)
