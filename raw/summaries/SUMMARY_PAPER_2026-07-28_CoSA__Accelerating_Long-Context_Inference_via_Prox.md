---
title: CoSA: Accelerating Long-Context Inference via Proxy-Kernel Co-Designed Sparse Attention
url: http://arxiv.org/abs/2607.25291v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_04-57-19Z_CoSA_AcceleratingLong_ContextInferenceviaProxy_Ker.md
generated_at: 2026-07-28 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
CoSA introduces a two‑stage training‑free sparse attention framework that pairs a Kernel‑Aware Proxy (KAP) with an Ordered‑Skipping Kernel (OSK). The KAP creates an ordered mask for moderate budgets, while the OSK tightens the budget using online‑softmax statistics and skips additional blocks. On LLM backbones and long‑context benchmarks CoSA delivers higher accuracy at lower compute, achieving a 4.93× attention speedup and a 2.53× reduction in time‑to‑first‑token with negligible performance loss.

## Key Takeaways
- The KAP selects blocks under a moderate budget and produces an ordered mask that prescribes the order in which KV pages are visited during kernel execution.
- The OSK applies this mask and, when the budget is tightened, skips more blocks by leveraging online‑softmax statistics to estimate block relevance.
- CoSA attains higher accuracy at lower budgets, delivering a 4.93× attention speedup and a 2.53× reduction in time‑to‑first‑token while keeping performance degradation minimal.

## Context
Long‑context inference suffers from quadratic self‑attention costs, limiting model size and latency. Proxy‑based sparse attention mitigates this but often sacrifices accuracy as budgets shrink. CoSA’s co‑designed proxy‑kernel approach addresses the trade‑off by dynamically ordering block visits and adaptively skipping less salient blocks.

## Implications
For researchers, CoSA demonstrates that training‑free sparse mechanisms can be both accurate and fast, encouraging adoption of efficient attention in large language models. For industry practitioners, it offers a practical path to deploy long‑context systems with reduced compute budgets and lower latency, aligning with the demand for scalable AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25291v1)
