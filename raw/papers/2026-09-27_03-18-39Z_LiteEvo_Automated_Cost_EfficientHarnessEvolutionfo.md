---
title: LiteEvo: Automated, Cost-Efficient Harness Evolution for Generalization to Unseen Tasks
published: 2026-09-27T03:18:39Z
authors: Euntae Choi, Sumin Song, Sungjoo Yoo
url: http://arxiv.org/abs/2609.33146v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LiteEvo: Automated, Cost-Efficient Harness Evolution for Generalization to Unseen Tasks

## Abstract
An LLM agent is defined by two things: the weights inside its model and the harness of components assembled around it. Harnesses are still handcrafted, and HarnessX, which evolves them automatically, starts each benchmark from a handcrafted harness, reports gains on the tasks it evolved on, and budgets 100 to 175 million meta-agent tokens per benchmark. We propose LiteEvo, a lightweight harness-evolution algorithm whose tool-free meta-agents mine agent trajectories for reusable components, curate them into a versioned library, and compose each round's harness from it, starting every benchmark from the same neutral harness and never naming the benchmark. Evolving on the graded tasks of five agentic benchmarks with a frozen Qwen3.5-9B, LiteEvo lifts pass@2 by 10.5 to 67.7pp and reaches comparable or higher pass@2 than a reproduction of HarnessX (71.0 against 67.3 on average) at 13.0 lower mean API cost. Harnesses evolved on train tasks keep their gains on unseen test tasks of four benchmarks, and LiteEvo also lifts Claude Code with Sonnet 4.6 by 1.2 to 71.4pp.

## Metadata
- **Published**: 2026-09-27T03:18:39Z
- **Authors**: Euntae Choi, Sumin Song, Sungjoo Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33146v1)