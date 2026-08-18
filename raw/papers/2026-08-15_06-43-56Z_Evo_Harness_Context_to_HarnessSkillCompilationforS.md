---
title: Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents
published: 2026-08-15T06:43:56Z
authors: Tianxin Wei, Zhan Shi, Minhua Lin, Bing He, Zewen Liu, Yisi Sang, Yuanchen Bei, Xuying Ning, Jiaru Zou, Ting-Wei Li, Xiao Lin, Yanjun Zhao, Chi Wang, Benoit Dumoulin, Dakuo Wang, Jingrui He, Hanqing Lu
url: http://arxiv.org/abs/2608.15071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evo-Harness: Context-to-Harness Skill Compilation for Self-Evolving Agents

## Abstract
Learning from experience is critical for developing capable, self-improving large language model (LLM) agents. Existing methods typically extract knowledge from accumulated trajectories via reflection, memory, rules, or skills. However, agents in realistic environments continuously encounter novel tasks, often offering only a one-shot opportunity to improve. These executions yield rich but highly noisy contexts, entangling broadly useful lessons with task-specific artifacts. Critically, prior works rarely validate their effectiveness on complex real-world tasks or isolate the underlying drivers of improvement. To address these gaps, we formulate online harness learning, where a frozen agent improves by continually updating a structured harness across sequential tasks. This formulation enables a systematic study of key self-improvement factors through our proposed Evo-Harness. At its core, context-to-harness skill compilation distills noisy, single-shot executions into reusable skill harnesses for cross-domain and topic-level adaptation. To demonstrate the efficacy of one-shot skill compilation, we evaluate across five realistic benchmarks (TerminalBench2, SWE-bench, CL-Bench, -bench, WebArena-Infinity). Our extensive analysis demonstrates the effectiveness of Evo-Harness and provides a principled understanding of how LLM agents can effectively learn on the fly. Our code is available at https://github.com/A-EVO-Lab/a-evolve/tree/release/evo-harness.

## Metadata
- **Published**: 2026-08-15T06:43:56Z
- **Authors**: Tianxin Wei, Zhan Shi, Minhua Lin, Bing He, Zewen Liu, Yisi Sang, Yuanchen Bei, Xuying Ning, Jiaru Zou, Ting-Wei Li, Xiao Lin, Yanjun Zhao, Chi Wang, Benoit Dumoulin, Dakuo Wang, Jingrui He, Hanqing Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15071v1)