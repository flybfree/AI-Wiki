---
title: SciDocBench: A Workflow-Centered Benchmark and Data Pipeline for Scientific Document Understanding
published: 2026-09-04T13:39:48Z
authors: Shenxi Wu, Yuhong Liu, Haosong Zhang, Tongjin Zou, Yanxun Zhang, Gaochang Chen, Dun Liang, Jiaqi Wang, Zhecan James Wang, Yuhang Zang, Dahua Lin
url: http://arxiv.org/abs/2609.05141v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SciDocBench: A Workflow-Centered Benchmark and Data Pipeline for Scientific Document Understanding

## Abstract
Scientific papers require models to reason jointly over text, equations, figures, tables, code, and datasets while preserving the provenance of supporting evidence. Existing benchmarks typically evaluate these capabilities in isolation, leaving unclear whether multimodal models can support realistic scientific-reading workflows. We introduce SciDocBench, a workflow-centered benchmark for scientific document understanding. It contains 124 expert-authored and difficulty-screened questions organized into seven research-assistant capability groups and 19 subtasks across five scientific domains. Each question is instantiated under four matched conditions combining English or Chinese questions with all-images-first or interleaved document representations, yielding 496 evaluation instances for controlled analysis. The strongest evaluated system achieves only 62.6/100, with pronounced weaknesses in document perception, evidence grounding, verification, and cross-document reasoning. To translate these diagnostics into scalable training signals, we introduce SciDocIR, a typed evidence-graph representation that preserves scientific document objects, layout and cross-reference relations, and provenance. Building on SciDocIR, we construct SciDocDataset, comprising approximately 15K supervised fine-tuning samples and 8K reinforcement-learning samples across 14 verifiable subtasks. Together, SciDocBench, SciDocIR, and SciDocDataset form an evaluation-to-training framework for diagnosing and improving scientific-document assistants. The project page is available at https://github.com/InternLM/SciDocBench.

## Metadata
- **Published**: 2026-09-04T13:39:48Z
- **Authors**: Shenxi Wu, Yuhong Liu, Haosong Zhang, Tongjin Zou, Yanxun Zhang, Gaochang Chen, Dun Liang, Jiaqi Wang, Zhecan James Wang, Yuhang Zang, Dahua Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05141v1)