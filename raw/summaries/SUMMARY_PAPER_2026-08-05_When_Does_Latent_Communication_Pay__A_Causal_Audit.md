---
title: When Does Latent Communication Pay? A Causal Audit of Relayed KV Caches in Multi-Agent LLMs
url: http://arxiv.org/abs/2608.04893v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_14-18-42Z_WhenDoesLatentCommunicationPay_ACausalAuditofRelay.md
generated_at: 2026-08-05 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper audits multi-agent LLM systems to determine when relayed key-value caches actually convey private information, finding that gains are not automatic but depend on whether receivers need sender-specific data and on specific protocol design. It shows that under certain conditions the cache can be replaced with random or deranged versions without affecting performance, while other regimes reveal genuine example‑specific benefits.

## Key Takeaways
- The battery reads ceiling: 100% against 23–25% for answer‑irrelevant relays on the primary backbone, a contrast replicated across three families, five checkpoints, and a prose document‑QA surface.  
- Where it does not need private information, a pre‑registered five‑seed protocol establishes equivalence within 2.8 points, a margin anchored to the audited system's reported gain, under Holm-corrected TOST on GSM8K and ARC-Challenge across three Qwen3 scales and on MedQA at 8B (one cell shows a small detected advantage inside the margin); a second family shows no detected advantage.  
- A large cache effect need not be a pairing effect; zeroing the relay costs 14.7 points while a mismatched cache costs only 0.4, and need is insufficient: delivered channels span ceiling (LatentMAS's native relay), partial (KVComm's layer subset), and no detected example‑specific transfer (C2C's released projector).

## Context
This work addresses the growing reliance on hidden data structures in large language models to reduce compute and memory costs, questioning whether such optimizations truly reflect meaningful communication between agents. By exposing the causal mechanisms behind reported gains, it contributes to a more honest evaluation of model efficiency claims.

## Implications
For researchers, the findings suggest that performance improvements from KV cache relaying may be overstated if not verified through rigorous audits. For industry practitioners, adopting similar audit protocols could prevent misleading benchmarks and guide responsible deployment of multi‑agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04893v1)
