---
title: A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation
url: http://arxiv.org/abs/2608.14329v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_14-20-38Z_AFour_AxisTrustworthinessBenchmarkforLLM_as_Judgei.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a four‑axis trustworthiness benchmark for LLM‑as‑judge in principle‑based regulation. It evaluates models on accuracy, paraphrase robustness, adversarial robustness and calibration using 168 cryptoasset scenarios mapped to UK FCA principles.

## Key Takeaways
- Accuracy drops sharply when LLMs are faced with adversarial keyword stuffing, such as the “compliance theatre” example, indicating a severe failure mode.  
- No single evaluation method dominates across all four axes, showing that accuracy alone is insufficient for regulatory trust.  
- The benchmark demonstrates that model‑specific failures can be isolated, suggesting that performance issues are not universal but tied to particular data or prompts.

## Context
In AI governance, regulators increasingly rely on automated decision‑makers, yet trustworthiness remains unmeasured. This benchmark addresses the gap by providing a systematic test of LLM performance under regulatory constraints. The results show that no single method dominates across all axes, highlighting the complexity of aligning AI with legal principles.

## Implications
For practitioners, the need to report per‑principle adversarial deception and calibration signals that model selection must consider both capability and transparency. Deploying LLMs without such reporting could erode regulatory confidence. This framework encourages regulators to demand calibrated audit trails rather than aggregate scores alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14329v1)
