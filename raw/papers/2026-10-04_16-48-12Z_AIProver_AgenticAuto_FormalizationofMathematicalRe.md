---
title: AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness
published: 2026-10-04T16:48:12Z
authors: Prithwish Jana, Viet Bach Hoang, Logan Luna, Viresh Pati, Akash Singirikonda, Cy Xie, Lisa Carbone, Wuyang Chen, Walter Moreira, Joe Stubbs, Sriram Vishwanath, Vijay Ganesh
url: http://arxiv.org/abs/2610.05367v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AIProver: Agentic Auto-Formalization of Mathematical Research via Certificate-Driven Evolving Harness

## Abstract
Proof auto-formalization translates natural-language (NL) theorems and proofs into a formal language (FL) such as Lean, enabling mechanical verification. Despite rapid progress, research-level proofs often depend on concepts missing from leading proof assistant libraries (e.g., Lean's Mathlib), and successful compilation does not guarantee that a translation preserves the theorem's meaning or the proof's reasoning. Furthermore, aligned NL-FL training data are scarce, and leading agents often rely on costly frontier models and manually engineered harnesses.   To address the above issues, we present AIProver, an agentic framework for autonomous proof auto-formalization and proof synthesis (AFPS) that jointly post-trains a 119B open-weight language model and evolves its agentic, tool-calling harness with HarnessEvolve. Verifiers assess type correctness, proof completeness, and semantic correctness, returning rewards and diagnostic certificates that drive model fine-tuning and alternating reinforcement learning via symbolic feedback and HarnessEvolve, a certificate-driven evolutionary search over the whole harness control flow that re-tailors the harness to the updated model. For research-level training and evaluation, we introduce LoCoBench, 58.9k instances from Mathlib, CSLib, Mizar Math Library, and a bounded-arithmetic textbook, with a 771-instance validation split whose theorem-proof pairs have no public Lean formalization. Against 39 frameworks spanning AFPS agents, frontier LLMs, and coding agents, AIProver lifts pass@4 semantic correctness over its Leanstral-1.5 base from 15.7% to 36.7% and outperforms every other open-weight system and Aristotle. As a Claude Code and Codex skill, it lifts their semantic correctness from 41.9% and 34.1% to 79.8% and 62.4%, respectively. Further, it is also 24% cheaper than Numina-Lean-Agent, pushing the accuracy-cost frontier of research-level AFPS.

## Metadata
- **Published**: 2026-10-04T16:48:12Z
- **Authors**: Prithwish Jana, Viet Bach Hoang, Logan Luna, Viresh Pati, Akash Singirikonda, Cy Xie, Lisa Carbone, Wuyang Chen, Walter Moreira, Joe Stubbs, Sriram Vishwanath, Vijay Ganesh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05367v1)