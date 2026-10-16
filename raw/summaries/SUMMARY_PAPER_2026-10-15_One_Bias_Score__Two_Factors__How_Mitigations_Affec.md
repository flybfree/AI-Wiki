---
title: One Bias Score, Two Factors: How Mitigations Affect Option Bias in Multiple-Choice Evaluation
url: http://arxiv.org/abs/2610.20993v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_22-13-28Z_OneBiasScore_TwoFactors_HowMitigationsAffectOption.md
generated_at: 2026-10-15 22:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper unifies two previously studied phenomena in multiple-choice evaluation of language models—selection bias (a preference for certain option letters) and order sensitivity (answer changes when options are reordered)—by introducing a single metric called the pooled selection-rate standard deviation (pooled SD). The authors demonstrate that this metric decomposes exactly into two label-free factors: the flip rate (how often answers change across orderings) and the positional skew (how unevenly option letters are chosen among those changed questions). Across 41 model checkpoints and 12 benchmarks, they show that different mitigation strategies target different factors, and that reporting both factors is essential for understanding whether a mitigation improves stability or merely masks errors.

## Key Takeaways
- The pooled SD provides a rigorous mathematical bridge between selection bias and order sensitivity: when every option appears equally often at each position, the pooled SD equals the product of the flip rate and the positional skew. This decomposition allows researchers to diagnose which component of option bias a given mitigation actually addresses, rather than treating all option-bias effects as a single undifferentiated problem.
- The flip rate correlates with model accuracy and output uncertainty, while the positional skew correlates with the estimated option-symbol prior. Prior correction techniques primarily reduce positional skew, whereas aggregating each ordering with its reversal primarily reduces the flip rate. Both approaches narrow the accuracy range across correct-answer letters by similar amounts, but aggregation produces fewer model-rank reversals, meaning it can obscure genuine performance differences between models.
- A critical caveat is that aggregation lowers the flip rate partly by settling questions on the same wrong option across orderings, effectively hiding errors rather than correcting them. The authors recommend applying prior correction before aggregation to reduce both factors simultaneously and further narrow the accuracy range, and they advocate reporting both factors alongside accuracy to distinguish model stability from actual correctness.

## Context
Multiple-choice evaluation remains a dominant paradigm for benchmarking large language models, yet its reliability is compromised when models exhibit systematic preferences for particular option letters or produce different answers depending on option ordering. Prior work treated selection bias and order sensitivity as separate concerns with separate mitigation strategies, leaving practitioners without a unified diagnostic framework. This paper matters because it provides a principled decomposition that reveals what each mitigation actually does, preventing the common practice of reporting a single accuracy number that conflates genuine improvement with superficial stabilization.

## Implications
For benchmark developers and model evaluators, this work implies that current mitigation practices—such as option shuffling or answer aggregation—may produce misleadingly stable scores while quietly entrenching wrong answers. Practitioners should adopt the two-factor reporting protocol to audit whether their evaluation pipelines are genuinely improving model correctness or merely reducing apparent variance. For the broader AI safety and evaluation community, the findings underscore that robust benchmarking requires disentangling model uncertainty from positional artifacts, a distinction that becomes increasingly critical as multiple-choice formats are used for high-stakes model comparisons and regulatory assessments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20993v1)
