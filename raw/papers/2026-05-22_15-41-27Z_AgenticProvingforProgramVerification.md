---
title: Agentic Proving for Program Verification
published: 2026-05-22T15:41:27Z
authors: Alessandro Sosso, Akhil Arora, Bas Spitters
url: http://arxiv.org/abs/2605.23772v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Proving for Program Verification

## Abstract
Agentic systems have recently emerged as state-of-the-art approaches for automated theorem proving in formal mathematics. To assess how far these capabilities extend to program verification, we evaluate Claude Code in an agentic proving framework on CLEVER, a Lean 4 benchmark for verifiable code generation. Our results show that Claude generates arguably valid specifications for 98.8% of problems (with 81.3% also accepted by CLEVER's isomorphism-based scoring on the correct portion of the benchmark), certifies implementations against correct ground-truth specifications for 87.5% of problems, and reaches a 98.1% success rate on the end-to-end program generation and verification pipeline over entries with self-consistent premises. Across all stages, Claude further provides high-quality feedback on its own attempts (as confirmed under manual review), identifying underlying causes of failure and lingering bugs in the dataset. These findings highlight a growing mismatch between the difficulty of existing program verification benchmarks and the capabilities of modern agentic provers, and point to the need for more rigorous, bug-resilient evaluation methodologies, and in particular for alternatives to isomorphism-based scoring of generated specifications. More broadly, our results provide empirical evidence that tight compiler-in-the-loop agentic paradigms are currently the most effective approach for foundational program verification.

## Metadata
- **Published**: 2026-05-22T15:41:27Z
- **Authors**: Alessandro Sosso, Akhil Arora, Bas Spitters
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23772v1)