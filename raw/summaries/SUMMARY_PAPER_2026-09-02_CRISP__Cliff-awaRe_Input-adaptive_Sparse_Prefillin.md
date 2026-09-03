---
title: CRISP: Cliff-awaRe Input-adaptive Sparse Prefilling with Structural-Mass-Motivated Routing
url: http://arxiv.org/abs/2609.01925v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-01_22-49-46Z_CRISP_Cliff_awaReInput_adaptiveSparsePrefillingwit.md
generated_at: 2026-09-02 20:54
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CRISP (Cliff-awaRe Input-adaptive Sparse Prefilling) to alleviate the quadratic bottleneck of attention prefilling in long-context LLM inference. By replacing costly routing proxies with a structural proxy and a sink‑aware threshold, CRISP eliminates both pooled matrix multiplications and KL divergences while preserving routing decisions.

## Key Takeaways
- CRISP replaces Jensen-Shannon Divergence routing with C_struct, which measures mass at vertical‑slash compatible positions, reproducing JSD’s routing outcomes without the overhead of a pooled matmul or subsequent KL divergence.  
- The method formalizes the post‑softmax mass cliff and employs a sink‑aware threshold that prevents O(n) background noise accumulation as context length grows.  
- Empirically CRISP matches or exceeds exact dense attention on retrieval‑heavy benchmarks, delivering up to +28.0 pp gain and a 5.3× speedup at 512k tokens.

## Context
Long‑context LLM inference is limited by the quadratic cost of self‑attention, which makes sparse methods that rely on fixed patterns or offline profiling impractical for dynamic inputs. Recent dynamic routing approaches introduce overheads such as pooled matmuls and KL divergences, while also ignoring the accumulation of background noise at long sequences.

## Implications
CRISP offers a scalable solution for industry‑grade inference, allowing real‑time processing of very long documents without sacrificing performance. The O(n) noise elimination and structural integrity make it suitable for high‑throughput applications where compute budgets are tight.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01925v1)
