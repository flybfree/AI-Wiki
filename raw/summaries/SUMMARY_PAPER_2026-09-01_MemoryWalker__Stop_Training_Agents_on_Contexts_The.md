---
title: MemoryWalker: Stop Training Agents on Contexts They Never Saw
url: http://arxiv.org/abs/2609.00865v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_08-01-27Z_MemoryWalker_StopTrainingAgentsonContextsTheyNever.md
generated_at: 2026-09-01 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper tackles the conditioning problem that arises when agent training uses compressed context from harnesses such as Claude Code or Qwen‑Agent, where eviction creates a tree rather than a sequence. It introduces two exact gradient‑equivalent corrections—LogitTree and a packed 4D attention mask—and a single‑backward‑pass variational relaxation called SDCC that minimizes the KL divergence between the compressed student and a stop‑gradient teacher on the pre‑eviction prefix.

## Key Takeaways
- LogitTree traverses the eviction tree with K+1 backward passes, ensuring gradient flow follows each segment exactly.  
- The packed 4D attention mask needs a custom kernel and stores white‑box eviction records to keep conditioning exact.  
- SDCC relaxes training to one backward pass by minimizing forward KL between the student’s compressed representation and a teacher’s stop‑gradient reconstruction, yielding an O(√ε_KL) bound on total‑variation error.

## Context
Agent harnesses compress context during rollout to save memory, but this compression fragments history into a branching tree. Existing linearizations either leak information by keeping only the rightmost path or mismatch training and inference by replaying depth‑first traversals, limiting performance on benchmarks like TC‑RAG, AgentFold, MemexRL, Claude Code, and OpenCode.

## Implications
For practitioners deploying compressed agents, these methods preserve training fidelity without sacrificing deployment efficiency. The results show that exact corrections keep the log‑probability gap at zero while SDCC dramatically reduces drift, offering a reliable path to higher rollout rewards in real‑world AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00865v1)
