---
title: CONTRAMEM: Learning Self-Evolving Procedural Memory from Contrasting Multi-Model Trajectories
url: http://arxiv.org/abs/2608.22533v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_18-11-26Z_CONTRAMEM_LearningSelf_EvolvingProceduralMemoryfro.md
generated_at: 2026-08-24 21:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CONTRAMEM, a source‑flexible, training‑free framework that builds self‑evolving procedural memory by treating differences in task outcomes as supervision. On GAIA2/ARE tasks the method boosts success rates from 26 % to over 55 % across three source models and transfers unchanged to Qwen3.7 Plus, demonstrating robust transferable knowledge.

## Key Takeaways
- The framework creates a compact bank of Function Cards and Skill Cards that evolves through localized curation rather than appending or rewriting the entire bank.
- This memory bank remains unchanged when transferred between different source models, indicating that procedural knowledge is not model‑specific but task‑focused.
- Heterogeneous multi‑model trajectories provide stronger memory performance than self‑ or same‑model multi‑rollout approaches because contrastive behavioral diversity matters more than stronger agents.

## Context
Autonomous computer‑use agents must maintain consistent decisions over long tasks, yet they often fail due to procedural errors. Building high‑quality memory without retraining is a key challenge in the field of AI‑assisted automation.

## Implications
The CONTRAMEM approach enables developers to deploy more reliable autonomous agents with minimal ongoing training, which could lower costs and improve deployment speed for industry applications. This work suggests that contrastive learning from outcome variation can be leveraged as a practical pathway toward robust procedural memory in real‑world AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22533v1)
