---
title: WidgetVA: A Widget-Centric Framework and Benchmark for Agentic Visual Analytics
published: 2026-09-21T04:27:36Z
authors: Yutong Chen, Zhike Tang, Zhihao Mai, Zhihao Shuai, Danli Luo, Jing Xu, Weikai Yang
url: http://arxiv.org/abs/2609.24094v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WidgetVA: A Widget-Centric Framework and Benchmark for Agentic Visual Analytics

## Abstract
Visual analytics (VA) enables sensemaking through interactive visualization, but effective analysis often requires experts to translate high-level intents into long sequences of interface operations and iteratively interpret visual feedback. We study whether modern vision-language models (VLMs) can take on this role as autonomous VA operators that observe the interface, plan multi-step exploration, execute interactions, and adapt based on intermediate visual feedback. To support systematic development and evaluation, we first introduce WidgetVA, a widget-centric agentic VA framework that standardizes interactive components as structured widgets with unified action (e.g., filter and zoom) and perception-query (e.g., selection summaries) APIs. This standardization supports two modes of system construction: wrapping an existing VA system to make it agent-operable without rebuilding it, and composing a new system from widgets as modular building blocks. To help agents coordinate across widgets rather than plan each interaction from scratch, each widget further packages reusable analytical workflows, giving agents more than a bare set of callable functions to plan over. Building on this framework, we present WidgetVABench, a benchmark of single- and multi-widget VA tasks that require agents to perform multi-step interactions to uncover evidence and produce verifiable results. Each task also provides fine-grained reference annotations so that WidgetVABench can score Answer, Reference Trace Similarity, and State separately rather than collapsing agent performance into one success score. Experiments across multiple VLMs show that our framework provides an effective scaffold for agentic VA, while the diagnostic measures expose persistent limitations for future work. The WidgetVA framework and WidgetVABench have been released in https://github.com/Hiverwin/widgetva.

## Metadata
- **Published**: 2026-09-21T04:27:36Z
- **Authors**: Yutong Chen, Zhike Tang, Zhihao Mai, Zhihao Shuai, Danli Luo, Jing Xu, Weikai Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24094v1)