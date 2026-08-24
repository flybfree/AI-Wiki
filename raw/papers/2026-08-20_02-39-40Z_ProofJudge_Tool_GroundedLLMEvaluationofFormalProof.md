---
title: ProofJudge: Tool-Grounded LLM Evaluation of Formal Proof Quality in Mathlib
published: 2026-08-20T02:39:40Z
authors: Shane Caldwell
url: http://arxiv.org/abs/2608.20432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProofJudge: Tool-Grounded LLM Evaluation of Formal Proof Quality in Mathlib

## Abstract
Formal proofs in Lean 4 that pass the kernel's type checker can nonetheless vary widely in quality. We introduce ProofJudge, an agentic LLM-as-judge system that scores formal proof quality along five dimensions beyond correctness: library leverage, automation fit, structural clarity, statement quality, and Mathlib conventions. We evaluate ProofJudge on a novel dataset of 218 declarations drawn from distinct Mathlib PRs. The judge agent is grounded by tool access to the commit the PR is applied to, enabling it to query the library state when scoring. A judge is considered aligned with human preferences when it rates the version of the PR Mathlib accepted above the initial version that was sent back for revision. All six judge models evaluated recover the reviewers' preference well above chance, from 80.8% to 63.5%, and two open-weight judges reach roughly 70% at a tenth of the best judge's cost. We release the judge harness, evaluation dataset, and evaluation traces as open-source artifacts to support further research.

## Metadata
- **Published**: 2026-08-20T02:39:40Z
- **Authors**: Shane Caldwell
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20432v1)