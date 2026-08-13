---
title: Disentangling the Expressivity of RoPE
url: http://arxiv.org/abs/2608.11909v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_10-37-21Z_DisentanglingtheExpressivityofRoPE.md
generated_at: 2026-08-12 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates the theoretical expressivity of rotary position embeddings (RoPE) in fully uniform, finite‑precision soft‑attention transformers. It formalizes two competing accounts: one linking periodic RoPE components to modular predicates from temporal logic, and another emphasizing fixed positional anchors and local offsets.

## Key Takeaways
- If every rotary component is made periodic, the transformer can recognize exactly the languages definable by past temporal logic with modular predicates.
- Conventional RoPE computes non‑repeating rotations, producing a precision‑dependent bounded simulation of fixed‑offset look‑back operators rather than an all‑length modular characterization.
- Experimental schedules that are periodic generalize on modular tasks, whereas conventional RoPE exhibits a locality bias that can hinder position‑invariant access to distant context.

## Context
Understanding the expressive power of attention mechanisms is crucial for designing scalable language models. This work bridges theory and practice by clarifying how embedding strategies affect model capabilities across varying sequence lengths.

## Implications
Practitioners should consider periodic embeddings when they need long‑range, position‑invariant reasoning, while conventional RoPE may be preferable for tasks with strong locality constraints. The distinction influences architecture choices in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11909v1)
