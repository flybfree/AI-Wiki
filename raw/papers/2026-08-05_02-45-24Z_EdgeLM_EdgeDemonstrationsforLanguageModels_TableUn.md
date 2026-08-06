---
title: EdgeLM: Edge Demonstrations for Language Models' Table Understanding
published: 2026-08-05T02:45:24Z
authors: Soroush Omidvartehrani, Mohammadamin Habibollah, Mohammadreza Daviran, Davood Rafiei
url: http://arxiv.org/abs/2608.04390v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EdgeLM: Edge Demonstrations for Language Models' Table Understanding

## Abstract
Large language models (LLMs) perform table-centric prediction through in-context learning, making demonstration selection critical to performance. Existing retrieval methods prioritize similarity to the query, but similar demonstrations often reinforce the model's likely prediction rather than reveal the distinctions needed for difficult decisions. We propose EdgeLM, a retrieval framework that instead selects edge evidence, demonstrations that are both relevant to the query and informative about the decision boundary. EdgeLM retrieves two complementary forms of edge evidence by selecting data edges, nearby examples with different ground-truth labels, and model edges, similar examples previously misclassified by the deployed model. EdgeLM requires neither model retraining nor task-specific engineering. Across five data wrangling tasks, fifteen datasets, and five open-weight and proprietary LLMs, EdgeLM consistently achieves the best or near-best performance in every setting, while ablations show that the two forms of edge evidence provide complementary benefits. Our code and datasets are publicly available at https://github.com/soroushomidvar/EdgeLM.

## Metadata
- **Published**: 2026-08-05T02:45:24Z
- **Authors**: Soroush Omidvartehrani, Mohammadamin Habibollah, Mohammadreza Daviran, Davood Rafiei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04390v1)