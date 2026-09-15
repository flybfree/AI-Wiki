---
title: Stellar Colosseum: A Many-Agent Harness for Long-Horizon Research in Mathematics and Theoretical Computer Science
url: http://arxiv.org/abs/2609.15983v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_17-58-55Z_StellarColosseum_AMany_AgentHarnessforLong_Horizon.md
generated_at: 2026-09-15 00:27
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces Stellar Colosseum, a model-agnostic multi-agent framework designed to tackle long-horizon research problems in mathematics and theoretical computer science. By orchestrating parallel strategy exploration, readiness gating, and iterative falsification, the harness significantly improves the reliability of large language models when constructing complex, interdependent proofs. Evaluations on TCS-Bench and Codeforces demonstrate its effectiveness, yielding new results on open problems from top-tier venues.

## Key Takeaways
- Stellar Colosseum employs a readiness gate to determine when an exploratory route is sufficiently mature before decomposing it into section-level subproblems, ensuring that proof plans are structured around interdependent tasks rather than linear sequences.
- The framework utilizes parallel candidate generation combined with targeted falsification attacks, routing verifier feedback directly back to the relevant sections of the argument to iteratively refine and correct the mathematical reasoning.
- Through overlapping random-sample tree aggregation, the system synthesizes multiple candidates and their critiques into a single cohesive research artifact, achieving 71.0% accuracy on TCS-Bench and solving 218 out of 222 Codeforces problems when paired with execution feedback.

## Context
Large language models have shown remarkable capability in generating short, plausible mathematical proofs, yet they consistently struggle with long-horizon research tasks that require sustained, interdependent reasoning over extended sequences. This paper addresses a critical gap in AI-assisted mathematics by introducing an architecture specifically designed to manage uncertainty and complex dependency chains inherent in advanced theoretical computer science and pure mathematics research.

## Implications
The successful integration of this many-agent harness into Google Antigravity’s Teamwork framework suggests that modular, multi-agent orchestration will become a standard paradigm for automating high-level mathematical discovery. Practitioners and researchers can leverage these iterative verification and falsification techniques to accelerate theorem proving, competitive programming solutions, and open-ended research workflows, ultimately reducing the manual burden of long-form

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15983v1)
