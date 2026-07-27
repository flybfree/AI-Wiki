---
title: Biomedical Machine Translation for Low-Resource Arabic-Script Languages via Cross-Lingual Transfer and LoRA Adapter Merging
url: http://arxiv.org/abs/2607.22300v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-24_13-44-50Z_BiomedicalMachineTranslationforLow_ResourceArabic_.md
generated_at: 2026-07-26 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a systematic study of biomedical machine translation for low-resource Arabic-script languages using Arabic and Persian as high-resource pivots. It evaluates three transfer strategies including few-shot in-context learning, minimal supervised adaptation with 500 sentences, and zero-data LoRA adapter merging. The results show that adapter merging achieves near pivot-quality performance at no extra cost.

## Key Takeaways
- Supervised adaptation with only 500 sentences reaches CHrF++ 41.01 for Dari which is comparable to the high-resource pivot.
- Zero-data LoRA adapter merging improves Dari translation within 3.5 CHrF++ of supervised results at no additional cost.
- Languages such as Pashto and Sorani Kurdish remain unsuitable for clinical use, indicating limits when structural distance from pivots is large.

## Context
Cross-lingual transfer in medical NMT remains challenging due to scarcity of parallel data especially for Arabic-script languages. This work demonstrates how low-resource language models can leverage high-resource pivot languages through lightweight LoRA adapters. The approach aligns with broader efforts to make AI translation accessible across diverse linguistic and cultural domains.

## Implications
For healthcare providers, accurate translation is critical for patient safety and effective communication. By enabling reliable translation without large annotated datasets, this method lowers deployment costs and supports equitable access to medical information in underserved regions. Practitioners can adopt LoRA merging as a practical solution for expanding biomedical NMT capabilities beyond high-resource languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22300v1)
