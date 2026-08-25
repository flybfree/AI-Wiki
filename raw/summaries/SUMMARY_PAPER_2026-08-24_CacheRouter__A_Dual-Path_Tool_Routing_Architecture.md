---
title: CacheRouter: A Dual-Path Tool Routing Architecture with Cache-Preserving Main-Model Isolation for Long-Tail Tool Discovery
url: http://arxiv.org/abs/2608.22708v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_01-56-01Z_CacheRouter_ADual_PathToolRoutingArchitecturewithC.md
generated_at: 2026-08-24 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CacheRouter, a dual‑path routing architecture that decouples tool selection from tool delivery in large language model systems. By keeping the main model’s request prefix fixed and handling additional tools through an independent router sub‑model, the system achieves high cache‑hit rates while supporting progressive disclosure and runtime updates.

## Key Takeaways
- The main model always sees a small, fixed set of core tools, so its request head remains unchanged across calls, preserving cache continuity.  
- A separate routing channel uses a router sub‑model to search the full tool list, execute a single tool, and return results, allowing dynamic tool discovery without affecting the cached prefix.  
- Automated tool registration from source code enables runtime updates, letting the tool set grow without modifying the main model’s request structure.

## Context
Current LLM tool use balances prompt size and caching efficiency, but any change to the visible tool list invalidates cached prefixes, increasing input costs. This paper addresses that trade‑off by redesigning the interaction pipeline rather than merely adjusting prompts or caches.

## Implications
CacheRouter reduces token consumption for long‑tail queries by up to 12 % under DeepSeek pricing, offering a scalable solution for enterprise deployments where tool sets evolve frequently and prompt length must stay minimal. Practitioners can implement this architecture to maintain high performance while supporting continuous tool updates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22708v1)
