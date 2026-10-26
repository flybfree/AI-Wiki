---
title: SWE-Shift: Evaluating Coding Agents in Evolving Workspaces
published: 2026-10-23T05:47:59Z
authors: Victor Shea-Jay Huang, Rongqing Li, Zhangyue Yin, Kelong Mao, Yaqi Zhao, Xinyuan Wang, Yao Yin, Lirui Luo, Renrui Zhang, Hongsheng Li
url: http://arxiv.org/abs/2610.32196v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SWE-Shift: Evaluating Coding Agents in Evolving Workspaces

## Abstract
Repository-level coding benchmarks largely assume that tasks and environments remain unchanged throughout execution. In software development, code, dependencies, runtime state, and requirements can change while an agent is still working. We introduce SWE-Shift, a benchmark for evaluating coding agents under such mid-execution changes. From the same saved history and workspace, a Clean continuation proceeds without intervention, while a matched Shifted continuation receives a task-relevant update. Success requires completing the current task, preserving still-valid work, and satisfying the applicable state and evidence checks. The benchmark contains 120 scenarios across 12 change families, each evaluated at nine scheduled intervention positions. We evaluate 17 coding-agent systems, all of which have lower Shifted than Clean success. GPT-6 Astra drops from 67.35% to 24.79%, with 20.34% paired success. Tool/session changes and stale evidence yield zero paired success across all systems. Late-position paired success is lower for some systems and higher for others. These results show that success on the unchanged task can coexist with failures to preserve work, recover state, or refresh evidence after an update.

## Metadata
- **Published**: 2026-10-23T05:47:59Z
- **Authors**: Victor Shea-Jay Huang, Rongqing Li, Zhangyue Yin, Kelong Mao, Yaqi Zhao, Xinyuan Wang, Yao Yin, Lirui Luo, Renrui Zhang, Hongsheng Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32196v1)