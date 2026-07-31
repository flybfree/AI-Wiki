---
title: SciDataSailor: Deep Scientific Data Exploring
published: 2026-07-29T05:08:21Z
authors: Jiyong Rao, Yicheng Qiu, Chi Zhang, Chunfeng Song, Runkai Zhao
url: http://arxiv.org/abs/2607.28098v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SciDataSailor: Deep Scientific Data Exploring

## Abstract
Scientific datasets are commonly organized as hierarchical repositories containing heterogeneous and interdependent files, making their inspection, integration, and analysis labor-intensive and reliant on domain expertise. Although large language model (LLM) agents have advanced substantially in planning, reasoning, and tool use, existing research has largely overlooked their ability to interact with real scientific data assets through executable environments. We introduce Deep Scientific Data Exploration, an agentic task paradigm in which agents navigate repositories, interpret heterogeneous files and schemas, execute analyses, integrate cross-file evidence, and produce conclusions grounded in executed observations. To operationalize this paradigm, we present SciDataSailor, a framework for synthesizing tool-interactive trajectories by balancing broad exploration with targeted exploitation. SciDataSailor instantiates trajectory synthesis as Monte Carlo Tree Search (MCTS) with four task-specific mechanisms: difficulty-stratified exploration seeds, dual-feedback first-play urgency, hierarchical strategy-to-tool action generation, and entropy-guided branching. Using this framework, we construct SciDataSailor-SFT-2K for supervised fine-tuning and SciDataSailor-Bench for evaluation, with the latter comprising 627 meta-information summarization tasks and 586 scientific question-answering tasks across 27 datasets spanning the life, earth, and physical sciences.

## Metadata
- **Published**: 2026-07-29T05:08:21Z
- **Authors**: Jiyong Rao, Yicheng Qiu, Chi Zhang, Chunfeng Song, Runkai Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28098v1)