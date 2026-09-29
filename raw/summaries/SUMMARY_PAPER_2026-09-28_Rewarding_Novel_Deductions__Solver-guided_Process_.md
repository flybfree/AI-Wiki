---
title: Rewarding Novel Deductions: Solver-guided Process Rewards for Logical Reasoning
url: http://arxiv.org/abs/2609.34660v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_09-01-24Z_RewardingNovelDeductions_Solver_guidedProcessRewar.md
generated_at: 2026-09-28 23:00
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces SPRING, a solver-guided process reward mechanism designed to enhance logical reasoning in large language models by providing granular supervision over intermediate inference steps rather than relying solely on final-answer correctness. By leveraging an SMT solver to verify reasoning trajectories and rewarding "novel" deductions that make consistent inferential progress while penalizing contradictions or redundancies, SPRING significantly improves puzzle accuracy across multiple benchmarks compared to base models and outcome-only reward baselines.

## Key Takeaways
- SPRING employs an SMT solver as a training-time verifier to evaluate intermediate reasoning steps, defining a "novel" step as one that is logically valid, consistent with the evolving state, and not implied by previous deductions, thereby enabling precise process-level supervision.
- The method designs specific process rewards that actively encourage novel inferential progress while simultaneously penalizing contradictory or uninformative reasoning steps, addressing the brittleness and inconsistency issues prevalent in small-scale LLMs during multi-step deduction tasks.
- Evaluations on ZebraLogic, AR-LSAT, and Knights and Knaves benchmarks demonstrate that SPRING consistently outperforms base LLMs, outcome-only reward baselines, and Logic-LM, achieving substantial accuracy gains such as a 49.71-point improvement over the base model on ZebraLogic and up to 93.14 puzzle accuracy on Knights and Knaves.

## Context
Logical reasoning remains a persistent bottleneck for large language models, particularly when handling structured problems that demand strict constraint tracking and consistency preservation across long chains of thought. While recent advancements have focused on outcome-based rewards or external tools, there is a critical gap in providing robust, automated supervision for the intermediate steps of complex deduction processes, which often leads to hallucinated or brittle reasoning trajectories in resource-constrained models.

## Implications
The

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34660v1)
