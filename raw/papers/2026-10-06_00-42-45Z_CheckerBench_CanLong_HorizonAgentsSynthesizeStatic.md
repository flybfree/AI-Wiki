---
title: CheckerBench: Can Long-Horizon Agents Synthesize Static-Analysis Checkers?
published: 2026-10-06T00:42:45Z
authors: Hang He, Li Wang, Hao Chen, Yuchen Shao, Yuling Shi, Lisheng Wang, Peiyang Liu, Goose Lin, Zaiyuan Wang, Haiying Sun, Ting Su, Chengcheng Wan
url: http://arxiv.org/abs/2610.07557v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CheckerBench: Can Long-Horizon Agents Synthesize Static-Analysis Checkers?

## Abstract
Static-analysis checker synthesis requires agents to interpret a defect specification, inspect a repository, implement analyzer-specific logic, and refine the checker through repeated compilation and analysis feedback. Existing coding-agent benchmarks focus on tasks such as patch generation or vulnerability detection and rarely assess whether an agent can develop a working checker in a repository from start to finish. We introduce CheckerBench, an executable benchmark of 300 tasks derived from 297 CVEs across 167 repositories, 85 CWEs, and five language ecosystems. Each task includes vulnerable and fixed revisions, a pinned analysis environment, and a checker scaffold. We further introduce CheckerLab, a common evaluation framework that independently rebuilds submitted checkers and measures vulnerable-fixed diagnostic contrast, patch localization, false positives, and tool use. Across 21 model-harness configurations and three independent repeats per configuration, mean Pass@1 is 32.30%, while the best reaches 45.33%. These results show that reliable, reusable checker development remains challenging for current coding agents.

## Metadata
- **Published**: 2026-10-06T00:42:45Z
- **Authors**: Hang He, Li Wang, Hao Chen, Yuchen Shao, Yuling Shi, Lisheng Wang, Peiyang Liu, Goose Lin, Zaiyuan Wang, Haiying Sun, Ting Su, Chengcheng Wan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07557v1)