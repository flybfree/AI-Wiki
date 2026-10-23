---
title: ALIAS: Evaluating Performance and Memorization in LLM-Written TLA+ Specifications
url: http://arxiv.org/abs/2610.29767v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-21_14-02-02Z_ALIAS_EvaluatingPerformanceandMemorizationinLLM_Wr.md
generated_at: 2026-10-22 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ALIAS, a framework that tests whether consistent identifier renaming (CIR)—a common method for detecting memorization in LLM benchmarks—accurately measures true recall on formal specification tasks written in TLA+. By leveraging TLA+'s model checker as a behavioral oracle across 111 TLA+-Bench tasks, the authors demonstrate that the apparent performance drop after renaming is largely an artifact of name-based grading rather than genuine memorization, and that behavior-based evaluation reveals far smaller gaps for frontier models like Claude Opus 4.8 and GPT-5.

## Key Takeaways
- Renaming identifiers in TLA+ tasks drops Claude Opus 4.8's correctness from 28% to 18% and GPT-5's from 9% to 7% under name-matching grading, but when grading is switched to behavioral equivalence verified by the TLA+ model checker, the drop shrinks to roughly 3 percentage points for Opus 4.8 and to 0 for GPT-5, showing that most of the "memorization signal" is a grading artifact.
- For two model families (Qwen and Gemma) fine-tuned on disjoint halves of the benchmark, renaming removes about half of the training gain in likelihood and costs 4.9 percentage points (Qwen) and 1.3 percentage points (Gemma) on held-out tasks, confirming that renaming does carry a real cost beyond pure memorization but that the magnitude is far smaller than name-based scores suggest.
- The authors conclude that a lower score after renaming conflates three distinct effects—true memorization, brittle name-based grading, and the intrinsic difficulty of reasoning under novel identifiers—making CIR an unreliable standalone memorization detector for formal-language tasks.

## Context
Memorization contamination is a central concern in LLM evaluation, and CIR has become a go-to technique for flagging models that simply regurgitate training data. This paper matters because it applies the technique to a formally verifiable domain—TLA+—where a model checker provides ground-truth behavioral equivalence, enabling researchers to separate genuine recall from evaluation-methodology artifacts. It highlights a broader methodological vulnerability: many benchmark scoring schemes reward surface-level identifier matching rather than semantic correctness, inflating apparent memorization signals across the field.

## Implications
For benchmark designers and model evaluators, the findings argue for replacing name-matching correctness checks with behavior-preserving verification wherever a formal oracle exists, since doing so can dramatically change conclusions about whether a model has memorized a task. For practitioners deploying LLMs on formal specification or verification workloads, the results caution against over-interpreting CIR-based scores as evidence of memorization and instead recommend behavior-based evaluation pipelines. The work also signals that fine-tuning gains on formal-language tasks are partially fragile under identifier perturbation, motivating more robust training strategies for code and specification generation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.29767v1)
