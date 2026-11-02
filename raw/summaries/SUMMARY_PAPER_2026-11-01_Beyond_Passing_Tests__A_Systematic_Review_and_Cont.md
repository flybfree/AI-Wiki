---
title: Beyond Passing Tests: A Systematic Review and Controlled Re-evaluation of Techniques for Improving the Quality of LLM-Generated Code
url: http://arxiv.org/abs/2610.38977v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-28_22-02-40Z_BeyondPassingTests_ASystematicReviewandControlledR.md
generated_at: 2026-11-01 21:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a systematic review of 628 primary studies (July 2021–October 2026) on techniques for improving the quality of LLM-generated code beyond functional correctness, alongside a controlled re-evaluation that benchmarks ten techniques across four models at matched compute budgets. The central finding is that most claimed quality improvements are either unmeasured against correctness, gamed by single automated signals, or disappear when compared against a budget-matched best-of-n sampling baseline, suggesting that the field's reported gains are largely artifacts of unequal evaluation rather than genuine advances.

## Key Takeaways
- The systematic review reveals a structural weakness in the literature: most studies measure only the single quality dimension they target (readability, efficiency, or security), rarely report whether correctness is preserved, and seldom disclose compute budgets, variance, or data contamination. This makes cross-technique comparison nearly impossible and inflates apparent gains.
- In the controlled re-evaluation, best-of-n sampling with an analyzer-weighted ranker matches or outperforms prompting, planning, self-refinement, reviewer agents, and retrieval-augmented generation on measures the ranker does not explicitly optimize. Only an analyzer feedback loop and fine-tuning surpass it, and only on analyzer issue counts specifically, indicating that many sophisticated techniques offer no advantage over simple sampling when budgets are equalized.
- Large correctness losses observed on HumanEval+ do not replicate on contests held after the models' training cutoffs, strongly suggesting benchmark contamination rather than a genuine capability regression. In a head-to-head comparison of 66 techniques on Gemma 4 31B, only 1 of 66 beats best-of-n beyond the 95% confidence interval on its primary target—a rate statistically consistent with chance.

## Context
The rapid adoption of LLMs for code generation has spawned a dense ecosystem of prompting strategies, agent architectures, retrieval pipelines, and fine-tuning methods, each claiming to improve code quality along dimensions such as maintainability, efficiency, and security. However, the evaluation infrastructure has lagged behind: benchmarks like HumanEval and MBPP measure functional correctness almost exclusively, and quality-specific metrics are often proprietary, single-signal, and susceptible to gaming. This paper addresses a critical gap in the field by providing both a taxonomic review and a controlled experimental comparison that normalizes compute budgets and separates genuine improvements from measurement artifacts.

## Implications
For practitioners and tool builders, the findings caution against adopting complex quality-improvement pipelines without first establishing a budget-matched sampling baseline and evaluating on metrics independent of the technique's own optimization signal. For the research community, the paper sets a methodological standard: future claims of code-quality improvement should report correctness deltas, variance, contamination status, and comparisons against best-of-n sampling at equal compute. Industry teams deploying LLM code assistants should treat single-analyzer score improvements as necessary but insufficient evidence of real-world quality gains, and should prioritize multi-dimensional, contamination-aware evaluation before integrating new techniques into production workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.38977v1)
