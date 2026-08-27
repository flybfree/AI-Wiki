---
title: Can your AI agent be cheaper? Investigating the effects of task specifications on token spend in agentic coding tasks
published: 2026-08-26T05:58:12Z
authors: Jakub Smékal
url: http://arxiv.org/abs/2608.25399v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can your AI agent be cheaper? Investigating the effects of task specifications on token spend in agentic coding tasks

## Abstract
Agentic coding workflows are now widely deployed in real-world systems. With long-horizon reasoning and tool use, token usage has become an important consideration for both cost and efficiency. Two engineers using AI will solve the same problem differently. How the specification of a task shapes an agent's token spend, and whether that spend can be predicted in advance, are open questions. Here, we study the effects of different task specifications on agentic token spend with the Kimi K3 model at three thinking efforts. Across $2,700$ runs, we show that reducing a full task specification to a bare user story raises token spend by $29.7\%$, while run-to-run variance remains unaffected by any prompt changes. We show that prompt-sensitivity is task-dependent, running from $13\%$ to $115\%$. We fit a simple predictor that can price a full distribution of task specifications and thinking effort configurations from a single cheap probe on an unseen task within $36\%$, improving over prior work in predicting token spend. Our work provides initial results quantifying the effects of task specification on agentic token spend and introduces a method that can be used to systematically evaluate the cost of AI coding workflows.

## Metadata
- **Published**: 2026-08-26T05:58:12Z
- **Authors**: Jakub Smékal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25399v1)