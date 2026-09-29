---
title: Contract Memory Compiler: Resolve, Then Traverse
published: 2026-09-26T14:17:22Z
authors: Zhi Song, XiMing Xing, Chunhan Li, Weian Mao, Zhenchao Tang, Hanbo Huang, Fan Xu, Jiale Zhou, Jiahui Guan, Zejian Ding, Chen Ma, Lusheng Wang
url: http://arxiv.org/abs/2609.32658v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contract Memory Compiler: Resolve, Then Traverse

## Abstract
External memory lets language-model agents answer questions about histories too long for the answer model's context window. Updates create a harder problem than retrieving a recent fact: changing one relation can redirect a multi-hop question to records about an entity absent from the question. We study this update-dependent evidence selection problem and introduce the Contract Memory Compiler (CMC). Before seeing a question, CMC uses a language model to identify relations in the history and record where each one was stated. It applies later updates to determine the current relations, follows them from entities named in the question, and passes the corresponding original records to the answer model in one call. Thus the current state determines which evidence is read, rather than merely refreshing values in a previously selected context. To the best of our knowledge, CMC achieves state-of-the-art multi-hop accuracy on FactConsolidation, reaching 78.25% overall and 61.0% at 262K. With the extracted relations and answer model held fixed, selecting evidence before resolving updates reduces multi-hop accuracy to 21.50%. We also introduce MQuAKE-MemStream, a derived dataset of ordered memory streams built from MQuAKE-Remastered counterfactual cases.

## Metadata
- **Published**: 2026-09-26T14:17:22Z
- **Authors**: Zhi Song, XiMing Xing, Chunhan Li, Weian Mao, Zhenchao Tang, Hanbo Huang, Fan Xu, Jiale Zhou, Jiahui Guan, Zejian Ding, Chen Ma, Lusheng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32658v1)