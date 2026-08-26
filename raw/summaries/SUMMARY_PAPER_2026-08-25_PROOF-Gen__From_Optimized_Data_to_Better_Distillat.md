---
title: PROOF-Gen: From Optimized Data to Better Distillation
url: http://arxiv.org/abs/2608.23911v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_23-33-56Z_PROOF_Gen_FromOptimizedDatatoBetterDistillation.md
generated_at: 2026-08-25 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces PROOF-Gen, a method that recovers teacher‑generated trajectories from failed generations using per‑scenario prompt optimization, and demonstrates substantial performance improvements for Qwen3-4B-Instruct-2507 and Gemma 4 E4B-it on benchmark tasks. Fine‑tuning on the combined data lifts goal completion by six point three percent in deployed pipelines and transfers to on‑device models across locales.

## Key Takeaways
- PROOF-Gen recovers 93% of failed τ2-bench scenarios through per‑scenario prompt optimization that writes corrective guidance stripped before training.  
- Fine‑tuning Qwen3-4B-Instruct-2507 raises Pass^1 from 0.132 to 0.529 and Gemma 4 E4B-it gains +7.2pp on BFCL v4 multi‑turn.  
- Deployment lifts trajectory quality by +6.3pp goal completion with positive transfer across response metrics in every locale.

## Context
This work addresses a bottleneck in tool‑call agent training where daily retraining of teacher models is costly and leaves stale failure data, limiting progress. By extracting actionable insights from failures, PROOF-Gen enables continuous improvement without recomputing the full teacher dataset each cycle.

## Implications
Practitioners can reduce reliance on expensive fine‑tuning cycles, embed reflective optimization into automated pipelines, and achieve measurable gains in deployed agent capabilities across diverse locales, supporting more reliable and efficient AI assistants.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23911v1)
