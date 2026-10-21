---
title: Polarity Blindness in LLM Safety: A Systematic Study of Negation, Antonym Substitution, and Adversarial Framing
url: http://arxiv.org/abs/2610.27908v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_09-22-50Z_PolarityBlindnessinLLMSafety_ASystematicStudyofNeg.md
generated_at: 2026-10-20 22:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates a structural vulnerability in large language model safety guardrails termed "polarity blindness," which refers to the failure of LLMs to recognize harmful intent after polarity-altering linguistic transformations such as grammatical negation or antonym replacement. Through a systematic benchmark of 260 prompts across 10 state-of-the-art LLMs in three languages (English, Spanish, Czech), the authors demonstrate that this weakness is widespread, with mean harm scores reaching 4.12 on a validated 0-5 scale for the most vulnerable model, and that the effect persists across typologically distinct negation systems.

## Key Takeaways
- The study identifies two forms of polarity inversion—grammatical negation and antonym replacement—as mechanisms that systematically undermine LLM safety guardrails, while using synonym replacement as a polarity-preserving control to isolate the specific effect of polarity alteration rather than mere paraphrasing.
- Across 10 state-of-the-art LLMs evaluated in English, Spanish, and Czech, polarity blindness affects most models, with the most vulnerable model reaching a mean harm score of 4.12 on a validated 0-5 harm scale, indicating that harmful content can slip past safety filters when its polarity is inverted.
- The effect persists across typologically differing negation systems, suggesting that polarity blindness is not a language-specific or grammar-specific failure but rather reflects a broader limitation in the semantic robustness of current language models, pointing to a fundamental gap in how these models process negation and oppositional meaning.

## Context
Negation has long been recognized as a persistent challenge across NLP tasks and modalities, yet its implications for LLM safety guardrails have not been systematically studied until now. As LLMs are increasingly deployed in production systems where safety filtering is a critical gatekeeping function, understanding how simple linguistic transformations can bypass these guardrails is essential. This paper bridges the gap between known NLP weaknesses in negation handling and the practical safety concerns that arise when users or adversaries exploit these weaknesses to elicit harmful outputs from otherwise well-guarded models.

## Implications
For practitioners deploying LLM-based safety systems, polarity blindness represents a practical attack surface: adversarial users can reframe harmful prompts through negation or antonym substitution to evade current guardrails, potentially allowing harmful content to reach end users. The cross-linguistic persistence of the effect implies that safety mitigations cannot be language-specific patches but must address deeper semantic robustness in model architectures and training. For the broader field, these findings underscore the need for safety evaluation benchmarks that explicitly test polarity-altering transformations rather than relying solely on direct harmful prompts, and they highlight an ongoing gap between model capability and model safety that remains unresolved even in state-of-the-art systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27908v1)
