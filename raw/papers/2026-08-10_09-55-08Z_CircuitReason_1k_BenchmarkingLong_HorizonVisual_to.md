---
title: CircuitReason-1k: Benchmarking Long-Horizon Visual-to-Symbolic Reasoning inElectrical Circuits
published: 2026-08-10T09:55:08Z
authors: Xinqi Yang, Kang An, Tengyue Wang, Zhongyu Yang, Chenxu Du, Yuanchi Zhu, Hebao Zhu, Ziliang Wang, Faqiang Qian, Yunli Yang, Qibing Ren
url: http://arxiv.org/abs/2608.09374v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CircuitReason-1k: Benchmarking Long-Horizon Visual-to-Symbolic Reasoning inElectrical Circuits

## Abstract
Electrical circuit analysis requires more than recognizing components in an image. A solver must ground symbols and labels, recover latent topology, select a physical model, formulate coupled equations, propagate intermediate quantities, and preserve units, signs, directions, and phase conventions. We introduce \benchmark, a benchmark of 1,000 authentic textbook problems for evaluating this complete long-horizon visual-to-symbolic reasoning process. Each problem pairs one or more circuit diagrams with a self-contained question, a typed or semantically specified answer, and a reference worked solution. An evidence-first construction pipeline aligns questions, figures, and solutions, while a reasoning-oriented taxonomy organizes problems by circuit type and dependency depth. Evaluation combines conservative typed scoring with identity-blinded multi-model semantic consensus, retaining every problem in the denominator. Across three commercial chatbot systems and six open-source multimodal large language models, the highest-scoring system reaches 84.8\% accuracy. However, performance consistently deteriorates on long-horizon problems, and qualitative analysis exposes persistent failures in topology-to-target binding, physical conventions, and late-stage output propagation. \benchmark{} provides a focused testbed for measuring whether multimodal models can transform technical visual evidence into sustained, physically valid symbolic reasoning. Code are available at GitHub - CircuitReason/CircuitReason1K.

## Metadata
- **Published**: 2026-08-10T09:55:08Z
- **Authors**: Xinqi Yang, Kang An, Tengyue Wang, Zhongyu Yang, Chenxu Du, Yuanchi Zhu, Hebao Zhu, Ziliang Wang, Faqiang Qian, Yunli Yang, Qibing Ren
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09374v1)