---
title: Do Small Models Use the Law You Give Them? Measuring Context Use on a Bilingual Bangladesh Legal Benchmark
published: 2026-08-31T06:45:16Z
authors: Moniruzzaman Mahadi, Abrar Mohammed Tanzim Alam, Sayma Siddika Monalisa, Mir Mohammad Asif Abdullah, Swakkhar Shatabda, Md Adnan Arefeen
url: http://arxiv.org/abs/2608.30327v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Small Models Use the Law You Give Them? Measuring Context Use on a Bilingual Bangladesh Legal Benchmark

## Abstract
Fine-tuning can improve legal question-answering accuracy without improving how models use law supplied in context. We study this distinction in bilingual Bangladeshi legal QA, where observed errors can arise from answer scoring, retrieval, or failure to use relevant law. We construct a hierarchy-preserving statutory corpus, 2,165 reviewed bilingual fine-tuning examples, and a 150-item supplied-law control. We evaluate six instruction-tuned models: Llama-3.2-1B, Llama-3.2-3B, Qwen3.5-0.8B, Qwen3.5-2B, Qwen3.5-4B, and Gemma-4-E2B, with three LoRA seeds per model. To separate effects, we combine constrained option-letter scoring, cyclic option rotation, and controlled removal of the governing provision. On 398 Bar Council outputs, an exact-line parser attributes an accuracy gain of 50.0\% to the Qwen3.5-2B seed-42 adapter, whereas option scoring yields only $3.0\%$. For Gemma-4-E2B, the two scoring methods favor different systems. When the governing provision is guaranteed to be present, five of six reference models improve by $14.7\%-19.3\%$ under the four-order criterion. Removing that provision reduces accuracy by $8.0\%-15.3\%$ for models and by $13.8\%-14.9\%$ points for their adapters. However, difference-in differences estimates show no increase in reliance on the governing provision after fine-tuning. Results show that legal adaptation claims require separating scorer, retriever, and model effects. Our Code and data are available at https://anonymous.4open.science/r/bangladesh-legal-qa-11E3

## Metadata
- **Published**: 2026-08-31T06:45:16Z
- **Authors**: Moniruzzaman Mahadi, Abrar Mohammed Tanzim Alam, Sayma Siddika Monalisa, Mir Mohammad Asif Abdullah, Swakkhar Shatabda, Md Adnan Arefeen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30327v1)