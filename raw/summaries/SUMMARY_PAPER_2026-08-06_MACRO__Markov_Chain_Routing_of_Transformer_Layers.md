---
title: MACRO: Markov Chain Routing of Transformer Layers
url: http://arxiv.org/abs/2608.05872v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_10-51-34Z_MACRO_MarkovChainRoutingofTransformerLayers.md
generated_at: 2026-08-06 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MACRO, a Markov Chain Routing framework that learns task-specific layer execution paths for transformer models without altering weights. It improves accuracy by 5% on average and outperforms Dr. LLM by 7.2%, while cutting search time ninefold.

## Key Takeaways
- MACRO learns dynamic layer routes as a context-dependent Markov policy, enabling skip, repeat, and residual hidden-state addition operations.
- The route distribution is updated via training feedback and decoded with top‑k Viterbi to isolate high‑probability programs.
- Results show the largest gains on small models, achieving +5% average accuracy improvement over unrouted baselines.

## Context
Large language models currently process layers sequentially, limiting efficiency. Dynamic routing seeks to adapt execution paths per task, but prior methods often incur heavy computation or require external labels. MACRO addresses these bottlenecks with a lightweight, parameter‑free approach that integrates seamlessly into existing inference pipelines.

## Implications
This work demonstrates that non‑intrusive layer routing can boost reasoning performance across diverse benchmarks, offering a scalable improvement for both research and industry practitioners. By reducing search time dramatically, MACRO makes high‑quality dynamic routing feasible at scale without costly hardware upgrades.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05872v1)
