---
title: Talaria: Session-Aware Serverless Serving of Hundred-Billion-Parameter LLMs
url: http://arxiv.org/abs/2607.17181v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-19_10-37-33Z_Talaria_Session_AwareServerlessServingofHundred_Bi.md
generated_at: 2026-07-23 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
Talaria introduces a session‑aware serverless system for serving hundred‑billion‑parameter LLMs that improves continuity across model switches and long KV prefixes. By jointly placing models and admitting continuations, Talaria reduces session completion time dramatically compared to existing round‑based schedulers.

## Key Takeaways
- Session‑prefill admits budget‑eligible continuations before the active model slot closes, preventing costly re‑routing.  
- Host‑restorable KV is kept on a stable substrate so that long prefixes survive model switches without reconstruction.  
- Soft reservations reserve admission slots for likely returns, balancing instance pressure with session continuity.

## Context
Serving massive language models in serverless environments faces challenges from popularity skew and limited GPU resources. Existing schedulers treat each request independently, leading to high latency when a session spans multiple calls. Talaria’s approach addresses these bottlenecks by preserving session state across model transitions.

## Implications
The results show up to 2.6× speedup for the worst‑case 95th percentile SCT, offering a practical path toward real‑time interaction with large models in cloud services. Practitioners can adopt similar session‑aware placement strategies to reduce operational costs and improve user experience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17181v1)
