---
title: DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents
published: 2026-09-02T03:35:12Z
authors: Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park, Xinyi Gu, Zexue He, Soochahn Lee, Rogerio Feris, Yong Jae Lee
url: http://arxiv.org/abs/2609.02059v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DocHop: Benchmarking Out-of-domain Multi-hop Reasoning in Information-Dense Documents

## Abstract
Multimodal Large Language Models (MLLMs) have achieved strong performance on structured visual understanding tasks such as chart and document question answering. However, existing benchmarks typically evaluate these domains in isolation, leaving underexplored a key capability: whether models can use textual context to determine how chart evidence should be selected, interpreted, and aggregated. We introduce DocHop, a benchmark for integrated chart--context reasoning in document-style images. In DocHop, the document narrative specifies multi-step compositional constraints, while charts provide the corresponding data values. Questions are grounded on a semantic reference label defined in the narrative, requiring models to resolve target entities from context before aggregating evidence across multiple charts. To enable systematic evaluation, we construct DocHop via a stochastic logic-first generation pipeline with controllable reasoning depth and visual density, covering 2,074 examples across six task categories. Experiments on a wide range of proprietary and open-source MLLMs show a substantial gap to human performance: annotators achieve over 90% accuracy, while the best model reaches only 62.83%. Reasoning-enhanced models consistently show improved results, but performance degrades as reasoning complexity increases. Overall, DocHop provides a controlled testbed for challenging multi-hop document reasoning.

## Metadata
- **Published**: 2026-09-02T03:35:12Z
- **Authors**: Zhuoran Yu, Le Thien Phuc Nguyen, Jaden Park, Xinyi Gu, Zexue He, Soochahn Lee, Rogerio Feris, Yong Jae Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02059v1)