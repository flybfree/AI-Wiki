---
title: MILES: Modular Instruction Memory with Learnable Selection for Self-Improving LLM Reasoning
url: http://arxiv.org/abs/2607.06974v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-08_03-51-37Z_MILES_ModularInstructionMemorywithLearnableSelecti.md
generated_at: 2026-07-23 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
MILES introduces a memory‑based framework for self‑improving LLM reasoning that dynamically expands step‑wise memory while applying correctness‑optimized selection. The approach matches or exceeds prior methods and achieves superior accuracy‑efficiency tradeoffs. The framework is designed to work within realistic test‑time constraints, limiting memory expansion and computation.

## Key Takeaways
- modular memory units consist of asymmetric pairs of sub‑goal embeddings and sub‑instructions each paired with a learnable selection head  
- the coarse level enables memory expansion and collects supervision for training selection heads from confident samples while the fine stage applies learned heads to rerank candidates and guide reasoning for uncertain samples  
- MILES consistently matches or outperforms prior methods while delivering superior accuracy‑efficiency tradeoffs

## Context
Memory‑based approaches in LLMs aim to retain useful reasoning steps across problems. This work addresses limitations of fixed action spaces and large training data by enabling incremental memory growth at test time, making it suitable for real‑world inference where supervision is limited.

## Implications
The framework reduces the need for extensive pre‑training on diverse tasks, offering a scalable solution for real‑time reasoning where memory can be built gradually. Practitioners can integrate MILES to enhance model performance without sacrificing inference speed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.06974v1)
