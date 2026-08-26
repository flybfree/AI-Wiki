---
title: Paritok-4B: Intent-Conditioned Context Compression for Coding Agents
url: http://arxiv.org/abs/2608.24188v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_07-53-30Z_Paritok_4B_Intent_ConditionedContextCompressionfor.md
generated_at: 2026-08-25 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents Paritok-4B, an extractive intent‑conditioned context compressor for coding agents that cuts token usage to 25.7% of the original size while preserving most solve quality. It achieves this by selecting spans rather than rewriting them and by conditioning on the agent’s current task to retain only lines that are most relevant.

## Key Takeaways
- The model retains 96.0 % of identifiers, paths, and numbers from its input, holding at 96.2 % on held‑out SWE‑bench Lite output.  
- Intent conditioning raises retained line relevance by +0.067 (paired 95 % CI [+0.056, +0.078]) compared with a non‑conditioned approach.  
- Compression reduces context size to 25.7 %, which is 2.0× harder than gpt‑4.1‑mini (50.2 %) and 2.4× harder than gpt‑5 (61.9 %), yet single‑shot solve quality stays at 86.5 %.

## Context
Coding agents repeatedly send large file reads and tool outputs to frontier LLMs, causing context costs that limit throughput. General‑purpose compressors trained on prose often misbehave with code, rewriting identifiers or dropping needed spans. Paritok-4B addresses this gap by offering a lightweight, code‑aware compressor.

## Implications
The 264 MB adapter can run on a single 24 GB GPU without per‑token fees, making it economically superior to cloud services that charge for compression. This enables scalable deployment of efficient compressors and reduces overall token expenses in coding workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24188v1)
