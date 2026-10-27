---
title: AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction?
published: 2026-10-24T00:08:11Z
authors: Zijie Liu, Qi Yang Huang, Jinhao Duan, Yueh Che Lee, Thomas A. Joseph, Zayne Turner, Adam Seligman, Tianlong Chen, Zhaozhuo Xu
url: http://arxiv.org/abs/2610.33375v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentOrch: How Close Can Global Orchestration Come to Step-by-Step Interaction?

## Abstract
Enterprise workflow agents typically rely on step-by-step interaction (Step-by-Step): the agent executes an action, observes its result, and invokes a large language model (LLM) again to decide the next step. Global orchestration (Global) instead generates a complete executable workflow in advance and executes it without further LLM calls, substantially reducing inference overhead, but it remains less accurate than Step-by-Step. We study how close Global can come to Step-by-Step and what narrows the remaining gap. We introduce AgentOrch, a benchmark that directly compares global orchestration with step-by-step interaction on 650 enterprise SOPs and 3,220 runtime variants under matched tools, environments, and evaluation. Step-by-Step remains more accurate for every evaluated model, but the gap has shrunk by about 79% from early models to the strongest recent model. We identify three routes to further narrowing this gap. Incremental workflow construction improves Global accuracy by an average of 9.98 percentage points (pp) without runtime execution feedback. Revising complete workflows with execution feedback improves all evaluated models, including 6.13 pp on held-out runtime variants. Targeted training on complete workflows improves accuracy by an average of 12.18 pp across all five trained models. Although a gap remains, global orchestration offers a promising path toward enterprise agents that deliver higher accuracy with fewer LLM calls.

## Metadata
- **Published**: 2026-10-24T00:08:11Z
- **Authors**: Zijie Liu, Qi Yang Huang, Jinhao Duan, Yueh Che Lee, Thomas A. Joseph, Zayne Turner, Adam Seligman, Tianlong Chen, Zhaozhuo Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33375v1)