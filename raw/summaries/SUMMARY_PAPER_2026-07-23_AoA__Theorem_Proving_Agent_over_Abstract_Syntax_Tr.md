---
title: AoA: Theorem Proving Agent over Abstract Syntax Tree of Redesigned Language
url: http://arxiv.org/abs/2607.16372v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-17_14-43-43Z_AoA_TheoremProvingAgentoverAbstractSyntaxTreeofRed.md
generated_at: 2026-07-23 23:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces AoA, an interactive theorem proving agent that operates on the abstract syntax tree (AST) of Minilang instead of raw source text. By representing proofs as JSON ASTs and using a unified proof‑tree model, AoA reduces token usage, API calls, and runtime compared to existing agents like Isabelle’s. Experiments show up to 4.7× lower cost and faster execution on benchmark suites.

## Key Takeaways
- The agent eliminates the need for line‑number based state queries by embedding subgoal states directly within each tree node, allowing immediate access without relocation.
- Proofs are emitted as JSON AST structures, which native tool‑calling LLMs can parse efficiently, cutting token consumption by 2.9–6.9× and tool calls by 3.9–8.9×.
- AoA achieves a 1.4–2.0× speedup on verification benchmarks while solving more problems than prior methods.

## Context
Current ITP systems are limited by the cost of serializing proofs and maintaining state across line edits, which hampers scalability for large programs. Minilang represents a promising proof language but is not yet in LLM training data, creating a gap between language capability and model performance. AoA bridges this gap by leveraging AST‑centric design.

## Implications
The approach lowers the barrier for deploying AI agents in formal verification workflows, making them more cost‑effective and faster to run. Practitioners can adopt AoA without retraining models on raw source code, opening new possibilities for automated proof generation across diverse domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16372v1)
