---
title: Routing Is Not Enough: Diagnosing Intra-Adapter Subspace Contention in MoE+LoRA Fine-Tuning
url: http://arxiv.org/abs/2609.03150v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_20-32-58Z_RoutingIsNotEnough_DiagnosingIntra_AdapterSubspace.md
generated_at: 2026-09-03 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why fine‑tuning a mixture‑of‑experts (MoE) model combined with low‑rank adapters (LoRA) can still suffer negative transfer even when domains are routed to different experts. By measuring routing overlap and adapter‑gradient similarity, the authors show that nearly orthogonal domain gradients compete within the same low‑rank subspace, causing perplexity spikes in biomedical code. They propose SpawnLoRA, a method that adds gated sub‑adapters inside MoE experts only when contention is detected, thereby preserving router structure while mitigating interference.

## Key Takeaways
- Biomedical data increases code perplexity despite near‑disjoint expert routing, indicating routing separation alone does not prevent negative transfer.  
- Interference originates from nearly orthogonal domain gradients that compete within the same low‑rank adapter subspace.  
- SpawnLoRA dynamically inserts gated sub‑adapters inside MoE experts when adapter‑level contention is detected, keeping the router unchanged.

## Context
Multi‑domain fine‑tuning aims to isolate updates per domain by routing tokens to different MoE experts and using lightweight LoRA adapters. However, real‑world data often contain subtle gradient conflicts that are invisible at the token level but degrade performance when domains share low‑rank parameter spaces. This work uncovers a previously unnoticed source of interference.

## Implications
For practitioners, SpawnLoRA offers a practical way to reduce negative transfer without retraining the entire MoE or expanding adapter ranks. The findings suggest that structural separation inside experts is as crucial as routing alone for effective multi‑domain adaptation in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03150v1)
