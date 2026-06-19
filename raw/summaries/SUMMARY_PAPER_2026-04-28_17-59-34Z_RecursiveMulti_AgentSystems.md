---

title: Recursive Multi-Agent Systems
url: http://arxiv.org/abs/2604.25917v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-28_17-59-34Z_RecursiveMulti_AgentSystems.md
generated_at: "2026-06-11 10:28"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces RecursiveMAS a framework that lets multi‑agent systems scale by nesting loops of model computation. It shows the approach improves accuracy and reduces token usage compared with existing methods.

## Key Takeaways
- The framework casts agents as a single recursive computation using lightweight RecursiveLink to share latent thoughts.
- An inner‑outer loop learning algorithm assigns shared gradients across recursion rounds for whole‑system co‑optimization.
- Empirically RecursiveMAS raises average accuracy by about 8.3% while speeding inference 1.2×–2.4× and cutting token usage 34.6%–75.6%.

## Context
Recursive language models have become a scaling axis in AI, but extending recursion to collaborative agents remains unexplored. This work bridges that gap by treating agent interaction as part of the recursive loop.

## Implications
Practitioners can design more efficient multi‑agent pipelines without sacrificing performance. The reduction in token usage and speed gains make large‑scale reasoning feasible for industry applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.25917v1)
