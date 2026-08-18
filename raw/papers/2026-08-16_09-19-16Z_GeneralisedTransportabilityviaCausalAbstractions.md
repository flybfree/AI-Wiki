---
title: Generalised Transportability via Causal Abstractions
published: 2026-08-16T09:19:16Z
authors: Yorgos Felekis, Paris Giampouras, Fabio Massimo Zennaro, Theodoros Damoulas
url: http://arxiv.org/abs/2608.15645v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generalised Transportability via Causal Abstractions

## Abstract
Transporting a causal conclusion from a source study population to a target one is a fundamental problem in causal inference. The theory of transportability provides a criterion for when this is possible: given experimental data from the source and observational data from the target, it determines whether a target query is identifiable and does so completely; i.e. if the query can be transported, the criterion finds the exact formula. However, it works one query at a time and returns an expression rather than the value itself. It is also silent in two practically important regimes: when the query is not transportable and when no target data exist at all. To tackle both, we take a model-level perspective grounded in Causal Abstraction theory. Source and target share variables, graph, and interventions, differing only at a known set of mechanisms, which makes transportability a special case of same-level abstraction. Thus, instead of asking whether one query transports, we ask whether a single map aligns the source and target across their interventional behaviour. We characterise when such a map exists in both the Markovian and semi-Markovian settings; when it does, every target query transports at once. Our main contribution lies in the approximate case. When no exact map exists, the best approximate one still yields certified query intervals, recasting abstraction error as a quantitative notion of approximate transportability. We formulate model-level transport as distributionally robust optimisation over mechanism and environment perturbations of the unseen target and derive certificates for both challenging regimes: bounds for non-transportable queries, and guarantees under target-agnostic settings. We evaluate our framework on synthetic Markovian and semi-Markovian benchmarks and a real ecological dataset, and we show that the certified intervals bracket the true interventional query.

## Metadata
- **Published**: 2026-08-16T09:19:16Z
- **Authors**: Yorgos Felekis, Paris Giampouras, Fabio Massimo Zennaro, Theodoros Damoulas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15645v1)