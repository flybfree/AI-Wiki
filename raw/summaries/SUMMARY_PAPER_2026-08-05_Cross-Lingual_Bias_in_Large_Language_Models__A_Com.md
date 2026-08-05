---
title: Cross-Lingual Bias in Large Language Models: A Comparative Analysis of English and Swahili
url: http://arxiv.org/abs/2608.03532v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_12-13-43Z_Cross_LingualBiasinLargeLanguageModels_AComparativ.md
generated_at: 2026-08-05 01:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether social biases persist across English and Swahili when large language models such as GPT‑5.2 and Gemini 2.5 Flash generate completions for 4,900 symmetric prompt pairs. The study finds that bias transforms rather than transfers, with notable shifts in stereotype rates, doubled neutral sentiment in Swahili, and refusal behaviour confined to English prompts.

## Key Takeaways
- Stereotype prevalence changed by up to twelve percentage points on specific axes when models produced Swahili outputs compared to English ones.  
- Gemini 2.5 Flash showed a doubled neutral‑sentiment rate for Swahili completions, indicating language‑specific bias amplification.  
- GPT‑5.2 refused 169 English prompts but zero Swahili prompts, revealing refusal behaviour anchored to English surface forms.

## Context
Multilingual AI systems are expected to be fair and unbiased across languages, yet most bias audits focus solely on English data, ignoring how model outputs may behave differently in other tongues. This research highlights the gap between English‑centric evaluations and real‑world multilingual deployment scenarios.

## Implications
Practitioners must expand bias assessments to include non‑English languages to avoid deploying models that perpetuate harmful stereotypes or produce semantically mismatched responses. Ignoring cross‑lingual bias can lead to inequitable user experiences and regulatory non‑compliance in global markets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03532v1)
