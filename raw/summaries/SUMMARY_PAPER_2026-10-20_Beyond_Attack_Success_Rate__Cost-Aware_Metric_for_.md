---
title: Beyond Attack Success Rate: Cost-Aware Metric for Evaluating Iterative LLM Jailbreaks
url: http://arxiv.org/abs/2610.26589v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_15-36-41Z_BeyondAttackSuccessRate_Cost_AwareMetricforEvaluat.md
generated_at: 2026-10-20 00:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ASR_STEP, a cost-aware evaluation metric for iterative jailbreak attacks against large language models that penalizes the number of additional victim-model calls required to achieve a successful attack. The authors demonstrate that standard Attack Success Rate (ASR) overstates the effectiveness of iterative jailbreak methods by ignoring the repeated interactions with the target model, and they show that discounting these extra calls reduces reported success rates by 3.4 to 12 percentage points depending on the strategy used.

## Key Takeaways
- Standard ASR evaluation treats a jailbreak as successful regardless of how many times the victim model was queried, yet each additional call gives the deployed system another opportunity to detect the attack and intervene, meaning ASR overstates real-world robustness. ASR_STEP addresses this by penalizing additional victim-model calls while retaining binary success judgments, making the true cost of iterative attacks transparent.
- The discounting effect varies significantly across jailbreak strategies: GCG scores decrease by 7.0 to 8.7 percentage points after discounting, PAIR shows a wider range of 3.4 to 12 percentage points, and the single-step PAP baseline remains unchanged. This demonstrates that the hidden "step" quantity differs per iterative strategy, and a single aggregate ASR number conceals these operational differences.
- The evaluation spans JailBreakBench across three model families, providing a cross-model comparison that strengthens the generalizability of the findings. The authors advocate reporting both ASR and ASR_STEP side by side so that the discount due to repeated victim-model interaction is made explicit to readers and practitioners.

## Context
Jailbreak research has proliferated rapidly, with methods like GCG, PAIR, and PAP each claiming high attack success rates against aligned language models. However, the community has largely relied on a single binary metric (ASR) that does not account for the computational and operational cost of iterative querying. As LLMs are increasingly deployed in production systems with rate limits, latency budgets, and monitoring layers, understanding the true interaction cost of an attack becomes critical for both security evaluation and practical defense design. This paper fills a gap in the evaluation methodology by formalizing a step-aware discount that reflects realistic deployment constraints.

## Implications
For researchers, adopting ASR_STEP alongside traditional ASR will expose which jailbreak methods are genuinely efficient versus those that rely on brute-force iteration, reshaping how attack effectiveness is compared across papers. For practitioners deploying LLMs in production, the findings highlight that defenses can exploit the repeated-call overhead of iterative attacks, suggesting that monitoring systems with per-query detection budgets may neutralize many "successful" jailbreaks in practice. The open-source code release enables the community to audit and extend the metric, potentially establishing a new standard for cost-aware robustness evaluation in the LLM safety literature.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26589v1)
