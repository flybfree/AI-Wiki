---
title: CORE: Conflict-Oriented Reasoning Elimination for Verifiable Language-Model Search
url: http://arxiv.org/abs/2609.39069v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_06-06-51Z_CORE_Conflict_OrientedReasoningEliminationforVerif.md
generated_at: 2026-09-30 20:59
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces CORE, a search controller designed to improve verifiable language-model reasoning by leveraging certified conflict cores from a verifier to guide the search process. Instead of merely revising the most recent step upon failure, CORE backjumps to the latest decision within the identified conflict core and caches conflicts to prevent repetition. Experimental results demonstrate that CORE significantly reduces verifier calls and generated tokens while achieving higher success rates compared to Tree of Thoughts across multiple reasoning tasks and graph-coloring instances.

## Key Takeaways
- CORE employs a conflict-directed backjumping strategy where the controller requests a certified conflict core from the verifier, allowing the model to backtrack directly to the most recent decision responsible for the error rather than performing inefficient chronological repair. Additionally, the system caches these conflicts to ensure that previously identified failure modes are never repeated during the search process.
- Under conditions of sound verification, finite branching and depth, and exhaustive proposals, CORE guarantees completeness by ensuring the uncapped search never prunes a valid solution, providing a rigorous theoretical foundation for its search efficiency without sacrificing correctness.
- Evaluations on 2,000 graph-coloring instances show CORE reduces median verifier calls by up to 39.8% compared to chronological repair, while tests across five reasoning tasks reveal superior performance with Qwen models, achieving

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39069v1)
