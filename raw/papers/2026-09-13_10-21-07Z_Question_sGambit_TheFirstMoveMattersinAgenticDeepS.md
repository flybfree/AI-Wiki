---
title: Question's Gambit: The First Move Matters in Agentic Deep Search
published: 2026-09-13T10:21:07Z
authors: Radin Hamidi Rad, Amin Bigdeli, Negar Arabzadeh, Sajad Ebrahimi, Charles L. A. Clarke, Benjamin C. M. Fung, Ebrahim Bagheri
url: http://arxiv.org/abs/2609.14412v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Question's Gambit: The First Move Matters in Agentic Deep Search

## Abstract
Deep research agents answer complex questions through iterative loops of searching, reading, and reasoning. Recent work on reasoning-intensive benchmarks such as BrowseComp-Plus shows that well-configured lexical retrieval can surface high-quality evidence, yet agents may still fail to connect documents carrying evidence to the gold documents. We identify a deep research agent's first retrieval move as an important design decision for this setting. We introduce Question's Gambit, a first-move retrieval module that decomposes the question into a set of clues, reformulates them into complementary searches, consolidates the retrieved results, and reranks the candidate pool before the agent begins its iterative search-and-reasoning process. This produces an opening context designed to support both clue aggregation and final-answer verification. We further evaluate on MultiHop-RAG to test whether these benefits transfer beyond BrowseComp-Plus to a more conventional multi-hop question structure. Experiments on BrowseComp-Plus show that Question's Gambit improves retrieval recall and downstream agent accuracy over strong baselines, improving answer accuracy from 83.1% to 90.5% with gpt-5.5 over Pi-Serini, the strongest reported agentic baseline. Our results confirm that effective agentic deep research depends not only on the tools available inside the loop, but also on the quality of the first move. We published our implementation publicly at https://github.com/radinhamidi/Question-s-Gambit.

## Metadata
- **Published**: 2026-09-13T10:21:07Z
- **Authors**: Radin Hamidi Rad, Amin Bigdeli, Negar Arabzadeh, Sajad Ebrahimi, Charles L. A. Clarke, Benjamin C. M. Fung, Ebrahim Bagheri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14412v1)