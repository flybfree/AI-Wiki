---
title: APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces
published: 2026-10-09T14:05:47Z
authors: Ziyi Yang, Adel Bibi, Guohao Li, Bernard Ghanem, Carlos Hinojosa
url: http://arxiv.org/abs/2610.13623v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APEX-Harm: Evaluating Agent Safety in Shared Professional Workspaces

## Abstract
Professional agents increasingly work through command-line interfaces and multiple tools over shared workspaces containing files, messages, and business applications. These environments create safety risks that are difficult to capture with attacks placed at a single, known read location. We introduce APEX-Harm, a benchmark for evaluating prompt and script injection against long-horizon agents performing finance, consulting, and legal tasks in large workspaces. Each task contains 115 to 328 files, together with email, calendar, chat, document, spreadsheet, PDF, and code-execution tools exposed through MCP servers. The benchmark includes six attack categories covering static and dynamic injections, task-specific script replacement, and attacker-provided generic scripts, and evaluates attack success, exposure, and task performance. We evaluate 12 frontier models on 180 task instances per model. Opus 5 and Sonnet 5 have the lowest overall attack success rates (8% and 20%), while task-specific script replacement and attacker-provided generic script attacks remain substantially more effective, averaging 81-84% and 73% attack success, respectively. Gemini 3.8 Flash achieves the highest mean task score (0.877) while still exhibiting a 33% attack success rate. These results show that completing the requested task is not sufficient evidence of safe behavior: an agent can produce a correct deliverable while also performing an unauthorized action in the workspace.

## Metadata
- **Published**: 2026-10-09T14:05:47Z
- **Authors**: Ziyi Yang, Adel Bibi, Guohao Li, Bernard Ghanem, Carlos Hinojosa
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.13623v1)