---
title: Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents
published: 2026-10-20T21:13:31Z
authors: Xu Li, Simon Yu, Minzhou Pan, Yiyou Sun, Zhaorun Chen, Bo Li, Weiyan Shi
url: http://arxiv.org/abs/2610.28934v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Back Up Before You Regret: Measuring Backup Awareness and Automating Backup in Coding Agents

## Abstract
Coding agents now complete tasks autonomously, modifying real-world state such as artifacts, software environments, and configurations along the way. Yet they show limited backup awareness: recognizing that an action will modify state that may later be needed, and preserving it beforehand. To evaluate backup awareness, we introduce RegretBench, a benchmark of 205 executable tasks grounded in regret moments reported on platforms such as X.com, GitHub, and Stack Overflow, where users explicitly regretted not preserving state they later needed. Across six frontier models, agents complete 86.1% of tasks on average yet back up before these moments in only 15.2%, showing that task completion ability does not imply backup awareness. Because it is hard to predict which changes will be regretted, we propose BackUpper, a harness plug-in backup layer that checks every tool call and preserves affected state before modification. It combines rule-based strategies for common operations with a lightweight subagent for complex cases, and its rule table can expand with subagent decisions over time. On RegretBench, BackUpper covers every regret moment action and restores states with 92.2% average similarity to the original. Achieving this costs only $0.014 per task, with 7x fewer tokens than the main-agent self-backup baseline. When users have preferences on what to back up, BackUpper can also narrow its scope accordingly, matching human annotations on whether an action is worth preserving with an 84.5% F1 score. These results suggest that agents can keep actions reversible at low cost while respecting users' preferences.

## Metadata
- **Published**: 2026-10-20T21:13:31Z
- **Authors**: Xu Li, Simon Yu, Minzhou Pan, Yiyou Sun, Zhaorun Chen, Bo Li, Weiyan Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28934v1)