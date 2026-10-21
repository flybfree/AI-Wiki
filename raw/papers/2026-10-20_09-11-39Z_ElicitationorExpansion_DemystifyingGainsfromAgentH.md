---
title: Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization
published: 2026-10-20T09:11:39Z
authors: Younghyun Kim, Wooseok Seo, Minseo Kim, Seunghyuk Oh, Minjae Lee, Donghoon Kim, Hyung Il Koo, Jaehyung Kim, Wonjun Kang
url: http://arxiv.org/abs/2610.27889v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Elicitation or Expansion? Demystifying Gains from Agent Harness Optimization

## Abstract
Recent studies in harness optimization have shown substantial performance gains in language model agents without updating model weights. A well-designed harness more effectively leverages the underlying model's capabilities by shaping context, tool use, and execution workflows. However, naïve success rates alone do not fully characterize whether optimized harness yields more reliable success on tasks already within reach (elicitation) or a broader range of solvable tasks (expansion). This distinction is crucial for recursive self-improvement and evolutionary search, as expansion may provide a broader range of successful experiences to push the capability boundaries. Despite the growing significance, this distinction remains underexplored in harness optimization. We conduct a systematic analysis to study the effect of gains from harness optimization. Building on pass@k analyses in the reinforcement learning (RL) literature that compare models before and after RL training, we compare optimized harnesses with their pre-optimization counterparts. Specifically, we assess changes in reachable task coverage, compare harness optimization with model scaling and increased inference-time compute, and examine how gains vary with task difficulty. Across static prediction and dynamic tasks, we find that pass@1 advantages of harness over stronger interventions can reverse at larger attempt budgets and aggregate gains conceal shortfalls on hard tasks, underscoring the need for a fine-grained diagnosis.

## Metadata
- **Published**: 2026-10-20T09:11:39Z
- **Authors**: Younghyun Kim, Wooseok Seo, Minseo Kim, Seunghyuk Oh, Minjae Lee, Donghoon Kim, Hyung Il Koo, Jaehyung Kim, Wonjun Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27889v1)