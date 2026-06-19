---

title: "UniPool: A Globally Shared Expert Pool for Mixture-of-Experts"
url: http://arxiv.org/abs/2605.06665v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-07_17-59-44Z_UniPool_AGloballySharedExpertPoolforMixture_of_Exp.md
generated_at: "2026-06-11 10:30"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces UniPool, a new Mixture‑of‑Experts architecture that replaces per‑layer expert ownership with a single shared expert pool accessed by independent routers. Experiments on multiple LLaMA scales show that UniPool consistently lowers validation loss and improves perplexity compared to the standard vanilla MoE baseline.

## Key Takeaways
- The per‑layer rule of MoE creates redundancy, as shown by routing probes where random routing only reduces accuracy by 1–2 points.  
- A pool‑level auxiliary loss balances expert utilization across the whole model, enabling stable and balanced training under sharing.  
- Pool size acts as an explicit depth‑scaling hyperparameter; reduced‑pool UniPool variants using 41.6 % to 66.7 % of the vanilla budget match or beat layer‑wise MoE.

## Context
Mixture‑of‑Experts is a popular scaling technique for large language models, but its linear growth in expert parameters limits efficiency. Recent work reveals that sharing experts globally can mitigate this inefficiency without sacrificing performance.

## Implications
For practitioners, UniPool offers a path to cheaper and more scalable model development by decoupling expert count from layer depth. This could enable broader deployment of high‑capacity AI systems with lower resource footprints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.06665v1)
