---
title: Language Models are not Equally Robust to Non-Canonical Tokenization across Languages
url: http://arxiv.org/abs/2607.26831v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_12-23-15Z_LanguageModelsarenotEquallyRobusttoNon_CanonicalTo.md
generated_at: 2026-07-29 20:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether language models maintain tokenization invariance across non‑canonical tokenizations beyond English, finding that such invariance is not universal and varies by language. The study shows a significant performance drop for instruction‑tuned models when alternative tokenizations are used, with average relative drops of 23.7% (Llama‑3.1‑8B), 11.4% (Qwen3‑8B) and 9.9% (Gemma‑3‑12B). Tokenization robustness is linked to language‑specific token fragmentation.

## Key Takeaways
- Non‑canonical tokenizations cause substantial performance degradation in multilingual models, disproving the assumption of universal tokenization invariance.
- Languages with higher token fragmentation exhibit greater sensitivity to alternative tokenizations, indicating a tight coupling between model and tokenizer.
- LoRA fine‑tuning on diverse non‑canonical tokenization data improves robustness more than English‑only fine‑tuning.

## Context
Understanding tokenization robustness is crucial for evaluating the reliability of multilingual language models across heterogeneous scripts. This work highlights that tokenization effects are not abstract but tied to real‑world linguistic structures, affecting downstream task performance in a measurable way.

## Implications
Practitioners must consider tokenization variability when deploying models in diverse languages, as it directly impacts model utility and fairness. Mitigation strategies such as multi‑tokenization training can enhance robustness, informing both research directions and industry practices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26831v1)
