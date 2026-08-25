---
title: Can LLMs Truly Forget? Revealing Unlearning Gaps Through Adversarial Evaluation
url: http://arxiv.org/abs/2608.21606v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-21_20-19-22Z_CanLLMsTrulyForget_RevealingUnlearningGapsThroughA.md
generated_at: 2026-08-24 21:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether large language models can truly forget targeted information after unlearning, and it finds that while standard metrics show high forgetting quality, adversarial prompts can still recover the data. The authors introduce Attack Success Rate (ASR) to measure leakage in adversarial responses and report recovery rates close to those of the untrained model.

## Key Takeaways
- Clean query forgetting yields low ASR but fine‑tuning methods achieve Forget Quality above 0.91, yet targeted facts are still recoverable with ASRs between 72.8% and 84.3%, indicating that unlearning does not eliminate adversarial leakage.
- Adversarial robustness remains high because the base model’s ASR is around 87.5%, showing that strong standard‑metric performance alone cannot guarantee true forgetting.
- Manual audits confirm agreement between binary ASR decisions and human factual assessments in seven of ten cases, suggesting ASR is a useful but imperfect proxy for recoverability.

## Context
LLM unlearning aims to remove the influence of specific training data while preserving overall capability. Existing benchmarks rely on clean queries, which may mask vulnerabilities exploitable via adversarial prompting. This work bridges that gap by evaluating both prompt‑based and fine‑tuning approaches under realistic attack scenarios.

## Implications
For practitioners, standard forgetting metrics are insufficient; they must complement them with adversarial stress tests to ensure robustness. The field should adopt multi‑dimensional evaluation frameworks that combine quantitative leakage scores with human audits to assess true unlearning effectiveness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21606v1)
