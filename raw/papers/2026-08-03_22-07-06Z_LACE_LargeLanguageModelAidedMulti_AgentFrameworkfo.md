---
title: LACE: Large Language Model Aided Multi-Agent Framework for Agile RISC-V Instruction Extension
published: 2026-08-03T22:07:06Z
authors: Pingqing Zheng, Jiayin Qin, Fuqi Zhang, Zishen Wan, Shang Wu, Yu Cao, Caiwen Ding, Yang Katie Zhao
url: http://arxiv.org/abs/2608.02915v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LACE: Large Language Model Aided Multi-Agent Framework for Agile RISC-V Instruction Extension

## Abstract
Domain-specific Instruction Set Architecture eXtensions (ISAX) are widely adopted in the RISC-V ecosystem to accelerate emerging workloads, but implementing and validating ISAXes across different cores remains slow and fragmented. Existing frameworks still require per-core interface adaptation, and differential testing often breaks once either the microarchitecture or the ISAX changes. We present LACE, an LLM-aided multi-agent workflow that translates natural-language ISAX intents into a compact two-level IR (operation-level and HDL task-level), performs retrieval-guided localized RTL edits over large repositories, and closes the loop with a compiler-agnostic riscv-formal checking flow (assuming RVFI availability or instrumentation). Across four embedded RISC-V cores, LACE raises pass@1 generation accuracy from near-zero to 72.8\% within our evaluation setup, while improving code localization and reducing integration rework. The code of LACE is available at https://github.com/UMN-ZhaoLab/LACE.

## Metadata
- **Published**: 2026-08-03T22:07:06Z
- **Authors**: Pingqing Zheng, Jiayin Qin, Fuqi Zhang, Zishen Wan, Shang Wu, Yu Cao, Caiwen Ding, Yang Katie Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02915v1)