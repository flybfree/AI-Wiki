---
title: SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents
published: 2026-07-16T03:59:44Z
authors: Huaigang Yang, Ya Li, Min Ren, Bo Dai, Zhenliang Zhang, Zhaofeng He
url: http://arxiv.org/abs/2607.14543v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SafeRelBench: A Spatial-Relation-Aware Benchmark for Process-Level Safety in VLM-Driven Embodied Agents

## Abstract
Vision-language models (VLMs) are increasingly used as the reasoning backbone of embodied agents, enabling robots to interpret visual scenes, follow language instructions, and plan multi-step actions. In household environments, however, safety depends not only on recognizing objects, but also on how actions change the physical scene over time. Existing embodied safety evaluations largely focus on static risk recognition, unsafe instruction refusal, or final-state task completion. As a result, process-level safety failures induced by spatial relations such as support, containment, and proximity remain insufficiently studied. To address this gap, we introduce SAFERELBENCH, a spatial-relation-aware safety benchmark with 507 executable evaluation samples, including 248 spatial-relation samples and 259 non-spatial control samples. Using SAFERELBENCH to evaluate seven open- and closed-source VLM-driven embodied agents, we find a substantial gap between task success and process-level safety compliance: models often complete the requested task while violating process-level safety constraints. Unlike prior benchmarks, SAFERELBENCH explicitly tests whether agents satisfy safety conditions before risk-prone actions, making spatial relations a core dimension in embodied safety assessment. More broadly, our results show that safe embodied intelligence requires not only stronger perception and planning, but also reliable reasoning about how object relations shape risk during interaction.

## Metadata
- **Published**: 2026-07-16T03:59:44Z
- **Authors**: Huaigang Yang, Ya Li, Min Ren, Bo Dai, Zhenliang Zhang, Zhaofeng He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14543v1)