---
title: Reroute, Don't Remove: Recoverable Visual Token Routing for Vision-Language Models
url: http://arxiv.org/abs/2606.12412v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_17-59-57Z_Reroute_Don_tRemove_RecoverableVisualTokenRoutingf.md
generated_at: 2026-06-11 10:57
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Reroute, a training‑free plug‑in that replaces the irreversible token removal used in vision‑language models with recoverable routing. By letting low‑ranked tokens bypass certain decoder stages and re‑enter later candidate pools, Reroute maintains the attention‑budget and KV‑cache limits of existing pruning methods while improving grounding performance.

## Key Takeaways
- Visual‑token importance varies across decoder depth; tokens ranked low early may become relevant in later layers.  
- Reroute reuses existing ranking rules and stage‑wise schedules, preserving the theoretical TFLOPs and KV‑cache budget class of the pruning method it augments.  
- Experiments on FastV, PDrop, and Nüwa variants show improved grounding under aggressive token reduction while keeping general VQA performance.

## Context
Vision‑language models generate hundreds to thousands of visual tokens, causing heavy attention computation and large KV‑cache memory usage. Traditional rank‑and‑remove pruning permanently discards irrelevant tokens, which limits flexibility and can hurt downstream tasks that depend on fine‑grained visual cues.

## Implications
Reroute demonstrates that token reduction need not be a one‑way cut but a recoverable process, offering more efficient inference for resource‑constrained deployments. Practitioners can adopt this approach to scale VLMs without sacrificing grounding accuracy or overall quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12412v1)
