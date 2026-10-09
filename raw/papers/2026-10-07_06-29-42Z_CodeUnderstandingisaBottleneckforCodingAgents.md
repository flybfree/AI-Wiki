---
title: Code Understanding is a Bottleneck for Coding Agents
published: 2026-10-07T06:29:42Z
authors: Nishant Balepur, Kiran Tomlinson, Tobias Schnabel
url: http://arxiv.org/abs/2610.10610v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Code Understanding is a Bottleneck for Coding Agents

## Abstract
Repository benchmarks (e.g., SWE-bench) for coding agents often assume that lines of code edited can predict task difficulty, but such datasets' poor control over code and task types makes it hard to know which abilities truly drive agent errors. We present CABRA: a Coding Ability Blueprint for Rigorous Agent evaluation. CABRA builds tasks from scratch as call graph transformations and scales difficulty via a task size parameter on four axes: function traversal, search, runtime resolution, and instruction following. We run eight LLMs and six coding agents on 6,840 CABRA tasks to show: 1) LLM accuracy falls as task size~grows, but agents stay near-perfect by offloading work to tools (e.g., grep); 2) Larger CABRA tasks elicit more tool calls for reading and analysis, while a separate study on SWE-bench Verified shows these tool call counts predict agents' accuracy better than lines of code edited, suggesting task difficulty for agents can lie in understanding code to edit, not just in making edits; 3) Extending CABRA to an intense understanding task where models analyze divergent logic across two classes backs this finding, as agent accuracy finally falls. More broadly, we argue for synthetic evaluations like CABRA to unmask LLM weaknesses trivialized by tools (e.g., needle-in-a-haystack) and abilities beyond just editing (e.g., understanding) that coding agents still find difficult, pairing SWE-bench-style tasks with controlled diagnosis.

## Metadata
- **Published**: 2026-10-07T06:29:42Z
- **Authors**: Nishant Balepur, Kiran Tomlinson, Tobias Schnabel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.10610v1)