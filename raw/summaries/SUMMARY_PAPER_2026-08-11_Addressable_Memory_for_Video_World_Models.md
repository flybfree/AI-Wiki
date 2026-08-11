---
title: Addressable Memory for Video World Models
url: http://arxiv.org/abs/2608.07408v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-07_16-55-57Z_AddressableMemoryforVideoWorldModels.md
generated_at: 2026-08-11 12:16
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates why interactive video world models lose the ability to retrieve stored visual information as rollouts exceed their training horizon, due to temporal Rotary Positional Embedding offsets falling outside the trained range. It introduces WorldTrace, a memory framework that makes compressed caches addressable and evaluates two compression methods on LoopBench, showing significant gains in temporal consistency and episodic recall.

## Key Takeaways  
- The model’s attention mechanism fails when RoPE‑rotated positions are out of distribution because it cannot locate the correct key‑value pairs.  
- WorldTrace solves this by assigning each summary slot a distinct virtual position within an addressable cache, preserving the original positional phase.  
- WorldTrace‑Field improves temporal consistency by 15.5% and WorldTrace‑Landmark boosts episodic recall by 19.5% on LoopBench.

## Context  
Visual persistence in interactive video generation is a central challenge for world models that must remember past scenes without retraining. Existing solutions often rely on fixed positional encodings, which degrade when the sequence length grows beyond what was seen during training.

## Implications  
This work provides a practical path to longer‑horizon visual memory by decoupling compression from positional encoding, enabling industry practitioners to generate coherent and recallable video sequences at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07408v1)
