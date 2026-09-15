---
title: Loop-Back Authority in LLM Agent Teams: A Paired Experiment on Flat and Hierarchical Coordination
published: 2026-09-13T19:58:54Z
authors: Burak Agachan, Max van Duijn, Amirhossein Zohrehvand
url: http://arxiv.org/abs/2609.14767v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Loop-Back Authority in LLM Agent Teams: A Paired Experiment on Flat and Hierarchical Coordination

## Abstract
Hierarchical orchestration, in which a Manager agent reviews worker output and can send it back for revision, is the default coordination pattern in production multi-agent LLM frameworks. Classical organizational theory predicts that the authority link speeds convergence on decisive output; work on sycophancy and Degeneration-of-Thought predicts that authoritative critique makes LLM output worse. Prior comparisons vary whole frameworks on tasks with checkable answers, leaving the authority link untested on open-ended work. We present a paired experiment that holds five LLM agents, their roles, prompts, tools, models, and data fixed and varies one link: whether the Manager may reject a worker's output and oblige a revision. Across 43 paired products and 86 runs of a business-intelligence reporting task, a five-model judge panel and a deterministic specification check score every report. The flat organization scores higher on Utility (d = 0.42, p = 0.009) and on Writing Clarity (d = 0.34, p = 0.030); the classical prediction fails. The reports are the same length, but hierarchical reports hedge 53% more, each revision loop is associated with a 0.14-point drop in Writing Clarity, and the hierarchical Writer's first draft is indistinguishable from the flat report: the gap opens inside the revision loop. Specification accuracy is at ceiling in both organizations, and the supervisory tier costs 51.5% more tokens for no quality gain. A supervisor pays for itself when it can verify and becomes a liability when it can only opine.

## Metadata
- **Published**: 2026-09-13T19:58:54Z
- **Authors**: Burak Agachan, Max van Duijn, Amirhossein Zohrehvand
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14767v1)