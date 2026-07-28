---
title: DualityCert: Verifier-Gated Language-Model Repair of Broken Duality Claims in Quantum Field Theory
url: http://arxiv.org/abs/2607.23614v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_11-39-49Z_DualityCert_Verifier_GatedLanguage_ModelRepairofBr.md
generated_at: 2026-07-27 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DualityCert, a symbolic verifier that checks Seiberg‑duality claims in four‑dimensional N=1 quiver gauge theories by testing anomaly matching, superpotential R‑charge consistency, central‑charge alignment and a chiral‑ring proxy. The verification provides a certificate indicating no inconsistency was found rather than a full proof, and the authors use it to repair deliberately broken duality statements from language‑model agents. Experiments on 145 broken claims show that verifier‑gated retries improve final repair success by about 8 percentage points over a single attempt.

## Key Takeaways
- The DualityCert verifier is designed to evaluate specific invariants of Seiberg duality, issuing a certificate when all tests pass but not claiming proof.  
- Verifier‑guided retries raise repair success rates by roughly 8 pp on both deepseek‑chat and qwen‑plus compared with a single attempt.  
- Category‑level feedback yields an additional 8.7 pp improvement for qwen‑plus, while interpretable obligation identities add 6.4 pp; neither effect is observed on deepseek‑chat.

## Context
This work bridges automated verification and language model training, demonstrating how a formal consistency check can serve as a repair environment to correct hallucinated scientific claims. It highlights the potential of integrating symbolic reasoning into AI pipelines to enhance factual accuracy in complex domains.

## Implications
For researchers, DualityCert offers a reusable tool that could be extended to other theoretical physics conjectures, fostering more reliable model outputs. In industry, the approach suggests that automated verification mechanisms can reduce costly errors and improve trustworthiness of AI‑generated scientific content.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23614v1)
