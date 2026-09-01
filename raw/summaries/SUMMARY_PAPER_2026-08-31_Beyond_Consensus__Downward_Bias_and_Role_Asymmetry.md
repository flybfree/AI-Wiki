---
title: Beyond Consensus: Downward Bias and Role Asymmetry in Multi-Agent LLM Judges for Subjective Evaluation
url: http://arxiv.org/abs/2608.30373v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_07-28-55Z_BeyondConsensus_DownwardBiasandRoleAsymmetryinMult.md
generated_at: 2026-08-31 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates Multi-Agent Debate (MAD) for subjective LLM evaluation and finds that consensus-based MAD degrades human alignment due to role asymmetry. It compares a single-judge baseline with MAD across six models and shows the latter performs worse on average.

## Key Takeaways
- Assigning a strict judge role creates a systematic downward bias that consensus cannot correct, causing scores to fall below the arithmetic midpoint.
- Removing role asymmetry (Symmetric MAD) restores baseline performance, indicating the issue is not interaction but role imbalance.
- Masking peer scores widens inter-agent disagreement and worsens average human alignment.

## Context
Subjective evaluation of LLM outputs remains challenging because human judgments are nuanced. Traditional single-judge baselines provide a reference for consensus methods, highlighting limitations in automated agreement protocols.

## Implications
Practitioners should avoid role-specialized MAD when accuracy is critical, as it may produce artificial consensus at the cost of fidelity to human preferences. Future work must address bias mitigation and symmetric interaction design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30373v1)
