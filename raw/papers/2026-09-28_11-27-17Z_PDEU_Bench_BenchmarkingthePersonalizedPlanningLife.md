---
title: PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents
published: 2026-09-28T11:27:17Z
authors: Huayi Lai, Shichao Song, Qingchen Yu, Simin Niu, Mengwei Wang, Hanyu Wang, Xun Liang
url: http://arxiv.org/abs/2609.34930v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents

## Abstract
Large language model (LLM) agents are evolving from tool-calling systems that execute isolated instructions into task-oriented agents that pursue user goals through sustained, multi-step interactions. However, existing benchmarks for personalized tool use largely assess isolated calls or reactive execution, leaving unclear whether agents can formulate, execute, and revise an explicit plan while preserving user preferences throughout long-term interaction. To address this gap, we introduce \textbf{PDEU-Bench} (\textbf{P}ersonalized plan \textbf{D}efinition, plan \textbf{E}xecution, and plan \textbf{U}pdate \textbf{Bench}mark), a benchmark for evaluating the complete planning lifecycle of personalized tool-using agents. PDEU-Bench comprises 214 long-horizon interaction tasks spanning 12 everyday domains and 94 tools, with stage-specific assessments of preference adherence and plan quality. Extensive evaluations of 15 representative open-source and closed-source LLMs reveal a pronounced gap between local tool execution and dynamic planning: LLMs can often instantiate preferences in individual calls, yet struggle to construct coherent plan definition and plan update. We further evaluate mainstream personalization and memory-augmentation methods. Although these methods improve particular stages, none of the evaluated methods reliably propagates user preferences throughout the complete lifecycle, and their gains frequently fail to transfer to subsequent execution. Fine-grained error analysis further reveals that preference omissions and conflicts persist throughout the planning lifecycle, highlighting the need for future research to parameterize LLMs with preference-aware information retrieval and memory capabilities. We provide the relevant code and data in the appendix to support future research.

## Metadata
- **Published**: 2026-09-28T11:27:17Z
- **Authors**: Huayi Lai, Shichao Song, Qingchen Yu, Simin Niu, Mengwei Wang, Hanyu Wang, Xun Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34930v1)