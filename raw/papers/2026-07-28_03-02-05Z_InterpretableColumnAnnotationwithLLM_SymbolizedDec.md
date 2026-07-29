---
title: Interpretable Column Annotation with LLM-Symbolized Decision Process Materialization
published: 2026-07-28T03:02:05Z
authors: Mengqi Wang, Jianwei Wang, Qing Liu, Xiwei Xu, Zhenchang Xing, Michael Bain, Liming Zhu, Wenjie Zhang
url: http://arxiv.org/abs/2607.25228v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpretable Column Annotation with LLM-Symbolized Decision Process Materialization

## Abstract
Column annotation (CA), including column type annotation (CTA) and column property annotation (CPA), aims to identify the meanings of table columns and the semantic relationships among them. Recent CA methods usually use various neural models to learn column representations and directly map them to label categories, thereby (1) sacrificing model interpretability and adaptivity, and (2) overlooking rich label semantics and ultimately limiting accuracy. To address these limitations, we propose SymCA, an LLM-empowered interpretable CA framework that materializes column annotation as a global-to-local symbolic decision process. SymCA consists of two components: (1) global skeleton induction, which constructs a semantic skeleton over the label space, and (2) local substrate evolution, which evolves predictive substrates within the skeleton. Specifically, to exploit label semantics while preserving an interpretable decision process, the global skeleton induction module leverages LLMs to generate candidate hypernym-inspired tree-structured semantic skeletons and employs a Minimum Bayes Risk (MBR)-based consensus strategy to select a robust skeleton against generation variance. Since different internal nodes require different evidence to distinguish among their child nodes, the local substrate evolution module materializes each internal node as an executable and evolvable predictive substrate. Over multiple evolution rounds, each substrate trains an interpretable random forest classifier with the current operator set, leverages the LLM to propose node-specific operator modifications, and uses an exploration-exploitation strategy to prioritize promising substrates. Extensive experiments demonstrate that SymCA is accurate, robust, and interpretable, outperforming the strongest baselines by an average of 6.42% in Micro-F1 and 11.03% in Macro-F1.

## Metadata
- **Published**: 2026-07-28T03:02:05Z
- **Authors**: Mengqi Wang, Jianwei Wang, Qing Liu, Xiwei Xu, Zhenchang Xing, Michael Bain, Liming Zhu, Wenjie Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25228v1)