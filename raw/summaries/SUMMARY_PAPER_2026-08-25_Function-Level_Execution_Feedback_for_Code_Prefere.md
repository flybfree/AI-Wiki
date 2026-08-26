---
title: Function-Level Execution Feedback for Code Preference Optimization
url: http://arxiv.org/abs/2608.23632v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-23_13-53-47Z_Function_LevelExecutionFeedbackforCodePreferenceOp.md
generated_at: 2026-08-25 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces STEP-KTODER, a framework that defines code steps as module‑level functions in decomposed programs and labels them with binary correctness using automatically generated unit tests. The method combines function‑level process supervision with outcome‑level feedback on the full program, achieving better performance than prior outcome‑only KTO or DPO baselines across multiple benchmark suites.

## Key Takeaways
- STEP-KTODER treats each module function as a discrete step, enabling clear labeling and optimization of code generation.  
- The framework leverages automatically generated unit tests to produce binary correctness labels that guide preference optimization at the function level.  
- Execution‑based label assignment is essential; LLM‑as‑a‑judge annotations over‑predict failures, corrupt positive labels, and harm downstream performance.

## Context
Code generation remains a challenge because standard supervision lacks a notion of intermediate steps, unlike mathematical reasoning where chain‑of‑thought is natural. This work addresses that gap by formalizing stepwise supervision for code, aligning with trends toward process‑oriented model training in AI research.

## Implications
For practitioners, STEP-KTODER offers a practical way to improve code quality through fine‑grained feedback, reducing reliance on costly human annotations. In industry, adopting such stepwise supervision could lead to more robust and maintainable software products while lowering annotation costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23632v1)
