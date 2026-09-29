---
title: Beyond Skill Evolution: Self-Evolving Context Management Policies for Long-Horizon Agent Harnesses
url: http://arxiv.org/abs/2609.34649v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_08-57-52Z_BeyondSkillEvolution_Self_EvolvingContextManagemen.md
generated_at: 2026-09-28 22:55
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces ContextEvo, a framework designed to address the context management bottleneck in long-horizon LLM agent tasks by learning self-evolving policies from execution trajectories. By reconstructing model-visible contexts at critical decision points and applying targeted updates based on identified failures, ContextEvo significantly enhances agent performance across multiple benchmarks. The results demonstrate that this adaptive approach outperforms fixed or locally evolved strategies and matches or exceeds prominent harnesses like Codex and OpenCode in handling extended interaction sequences.

## Key Takeaways
- Existing experience- and skill-based evolution methods struggle with long-horizon tasks because growing interactions cause useful evidence to be buried by redundant or outdated context, making dynamic context management a critical performance bottleneck that static strategies cannot resolve.
- ContextEvo operates by learning a context policy directly from long-horizon trajectories; it reconstructs the model-visible context at key decision points, detects failures specifically related to context issues, and executes targeted policy updates to optimize information retention and relevance over time.
- Evaluated starting from the Pi-agent harness, ContextEvo achieves performance comparable to or superior to leading agent harnesses such

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34649v1)
