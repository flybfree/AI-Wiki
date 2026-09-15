---
title: MTAC-IFBench: Benchmarking Instruction-Following in Multi-Turn Agentic Coding
published: 2026-09-14T03:57:37Z
authors: Bosi Wen, Cunxiang Wang, Jiayi Gui, Haoke Zhang, Yilin Niu, Pei Ke, Dayong Yang, Hongning Wang, Minlie Huang
url: http://arxiv.org/abs/2609.14992v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MTAC-IFBench: Benchmarking Instruction-Following in Multi-Turn Agentic Coding

## Abstract
Recently, the rapid development of large language models (LLMs) has reshaped software engineering by enabling autonomous code agents that plan, execute, and utilize external tools iteratively to tackle complex tasks. Beyond achieving functional correctness, these agents must faithfully follow process instructions and constraints throughout the development lifecycle. However, existing benchmarks typically focus on final functional correctness or confine instruction-following evaluation to single-turn, general chat or simple code generation scenarios, leaving instruction-following in multi-turn agentic coding underexplored. To bridge this gap, we propose MTAC-IFBench, a comprehensive benchmark for this critical capability. It features multi-turn progressive software development instructions with diverse constraints spanning 6 primary and 18 secondary categories. With an average of 7.04 turns and 91.33 constraints per instance, it poses a rigorous challenge to current LLMs. To make the evaluation reliable, we construct a checklist for each constraint and functional requirement, and integrate verification scripts and judge agents to verify each checklist item. MTAC-IFBench identifies significant deficiencies in existing code agents in multi-turn instruction-following, with their performance degrading rapidly as the interaction session grows longer.

## Metadata
- **Published**: 2026-09-14T03:57:37Z
- **Authors**: Bosi Wen, Cunxiang Wang, Jiayi Gui, Haoke Zhang, Yilin Niu, Pei Ke, Dayong Yang, Hongning Wang, Minlie Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14992v1)