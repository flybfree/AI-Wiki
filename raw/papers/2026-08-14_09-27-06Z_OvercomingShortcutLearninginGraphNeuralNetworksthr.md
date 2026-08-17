---
title: Overcoming Shortcut Learning in Graph Neural Networks through Active Explanation Guidance
published: 2026-08-14T09:27:06Z
authors: Taraneh Younesian, Steve Azzolin, Antonio Longa, Francesco Ferrini, Vincenzo Marco De Luca, Stefano Teso
url: http://arxiv.org/abs/2608.14121v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Overcoming Shortcut Learning in Graph Neural Networks through Active Explanation Guidance

## Abstract
Graph Neural Networks (GNNs) can solve prediction tasks by unintentionally exploiting shortcuts---that is, edges, nodes, and features that correlate with but are not causal for the prediction---which compromise their reliability in out-of-distribution tasks. We introduce XIGL, an architecture-agnostic human-in-the-loop strategy for removing such shortcuts from GNNs. Our key insight is twofold. On the one hand, reliance on shortcuts can be detected by inspecting GNN explanations. On the other hand, once made aware of such shortcuts, sufficiently expert users can provide tailored corrective feedback, which helps deconfound the model. XIGL supports any query strategy; however, since corrective feedback can be expensive to acquire, we develop an active learning strategy for prioritizing explanations that are more likely to display shortcut behavior, lowering annotation and cognitive costs. We showcase the effectiveness of XIGL, including both existing and proposed explanation-based strategies, on several GNN architectures. Our implementation is available online.

## Metadata
- **Published**: 2026-08-14T09:27:06Z
- **Authors**: Taraneh Younesian, Steve Azzolin, Antonio Longa, Francesco Ferrini, Vincenzo Marco De Luca, Stefano Teso
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14121v1)