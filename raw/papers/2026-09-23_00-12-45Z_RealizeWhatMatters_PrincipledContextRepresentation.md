---
title: Realize What Matters: Principled Context Representation for Large-Scale Reasoning
published: 2026-09-23T00:12:45Z
authors: Michael Theologitis, Dean Light, Shuyue Stella Li, Benjamin Newman, Yulia Tsvetkov, Dan Suciu
url: http://arxiv.org/abs/2609.27173v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Realize What Matters: Principled Context Representation for Large-Scale Reasoning

## Abstract
Solving complex tasks in domains such as science, medicine, law, and finance often requires assembling interdependent information scattered across vast, heterogeneous sources far beyond model context limits. Existing approaches tackle this challenge by organizing information into more manageable representations over which models can reason, such as graphs, textual memories, and retrieval collections. These representations dictate what downstream reasoning is possible and, ultimately, whether it succeeds; yet their design and construction remain largely ad hoc. In this work, drawing on the cognitive theory of relevance realization, we propose concrete principles for designing AI systems that construct effective representations of very large contexts. We analyze existing approaches and show how their successes and failures map onto their alignment with these principles, and introduce R3Con, a harness designed to operationalize the principles more systematically. We evaluate R3Con against nine state-of-the-art baselines on two recent benchmarks of reasoning over large document corpora. On these benchmarks, R3Con substantially outperforms the strongest baseline, by $20$ and $8.4$ percentage points. It also enables smaller models to outperform much larger ones: R3Con with 4B and 9B models outperforms all evaluated 35B baselines, while R3Con with a 35B-A3B model outperforms Claude Code with Claude-Sonnet-5 at $3.7\times$ lower cost. Our results show that context representations following our principled approach can reduce reliance on model scale, pointing toward a future of AI systems with frontier-level performance powered by smaller models. Our code is available at https://github.com/michaeltheologitis/r3con

## Metadata
- **Published**: 2026-09-23T00:12:45Z
- **Authors**: Michael Theologitis, Dean Light, Shuyue Stella Li, Benjamin Newman, Yulia Tsvetkov, Dan Suciu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.27173v1)