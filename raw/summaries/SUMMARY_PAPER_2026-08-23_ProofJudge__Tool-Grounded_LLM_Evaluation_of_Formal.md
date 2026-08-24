---
title: ProofJudge: Tool-Grounded LLM Evaluation of Formal Proof Quality in Mathlib
url: http://arxiv.org/abs/2608.20432v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-20_02-39-40Z_ProofJudge_Tool_GroundedLLMEvaluationofFormalProof.md
generated_at: 2026-08-23 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ProofJudge, an agentic LLM that evaluates formal proofs in Lean 4 beyond mere correctness. It scores five dimensions such as library leverage and structural clarity using a tool-grounded system. On a dataset of 218 Mathlib PRs, the judge aligns with human preferences at rates above chance.

## Key Takeaways
- The judge’s alignment with human reviewers exceeds random guessing, ranging from 80.8% to 63.5%, indicating strong predictive power.
- Two open-weight judges achieve around 70% accuracy while using only a tenth of the cost of the best model, showing efficiency gains.
- ProofJudge is released as open-source hardware and data, enabling further research.

## Context
This work addresses a gap in automated evaluation where tools can verify correctness but not quality. By integrating LLM judgment with direct access to library states, it bridges theory and practice in formal verification. The approach exemplifies the trend of tool-grounded AI systems that adapt to specific software ecosystems.

## Implications
For researchers, ProofJudge provides a benchmark for evaluating AI’s role in mathematical proof generation. For practitioners, it offers an automated feedback loop that can improve Mathlib contributions without manual review. The release supports open collaboration and rapid iteration in the formal verification community.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20432v1)
