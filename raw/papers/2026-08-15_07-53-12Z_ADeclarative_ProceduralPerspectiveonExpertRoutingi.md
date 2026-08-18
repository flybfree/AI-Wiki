---
title: A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models
published: 2026-08-15T07:53:12Z
authors: Amrit Gopinath,  Raghul, Durairaj Thenmozhi
url: http://arxiv.org/abs/2608.15102v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models

## Abstract
We investigate whether Mixture-of-Experts (MoE) language models develop linguistically structured expert routing during bilingual language acquisition. Inspired by the Declarative-Procedural framework, we analyze lexical, grammatical, and syntactic processing in a decoder-only English-German MoE Transformer trained under sequential language exposure. We construct a probe-based validation set and extract token-level routing distributions to quantify category-dependent specialisation using mutual information, routing entropy, and Jensen-Shannon distance. The curriculum-trained model exhibits a peak mutual information of 0.1148 at layer 5, indicating category-dependent differences in routing distributions across linguistic categories. Surprisingly, a no-curriculum baseline trained on mixed English-German data shows stronger aggregate specialisation, reaching a peak mutual information of 0.2599 at the same layer. These results suggest that interpretable linguistic organization emerges within MoE routing patterns even without sequential language exposure. A replication at a second training seed shows that the no-curriculum condition's specialisation concentrates on a single language whose identity is seed-dependent, whereas the curriculum consistently yields a stable, language-balanced routing profile; rather than uniformly increasing specialisation, staged bilingual exposure reduces single-language dominance. The official Github repository: https://github.com/Amrit828/DP-Theory-MOE-Interpretability-Research

## Metadata
- **Published**: 2026-08-15T07:53:12Z
- **Authors**: Amrit Gopinath,  Raghul, Durairaj Thenmozhi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15102v1)