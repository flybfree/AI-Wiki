---
title: Aligned in Form, Not in Meaning: The Comprehension - Containment Decoupling of LLM Safety in Low-Resource Bangla Derogatory Speech
published: 2026-08-03T23:09:19Z
authors: Shadab Bin Habib, A K M Ferdous Reza Habib, Subarno Neel, Adib Sakhawat
url: http://arxiv.org/abs/2608.02941v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Aligned in Form, Not in Meaning: The Comprehension - Containment Decoupling of LLM Safety in Low-Resource Bangla Derogatory Speech

## Abstract
We audit five frontier large language models on native Bangla derogatory speech (gali) across six protocols to test a single hypothesis: Comprehension-Containment Decoupling. We propose that contemporary safety alignment is bound to high-resource surface forms rather than harmful meaning, causing a model's capacity to comprehend a low-resource slur and its capacity to contain it to operate independently. Every protocol corroborates this hypothesis against a human-calibrated baseline (kappa = 0.84). At baseline, models exhibit a 7.92 percentage point comprehension deficit in Bangla while maintaining an identical 92.83% token leakage rate across both languages. Severity calibration tracks surface anatomical cues over compositional harm (+4.00 error on mild slang; -2.00 on threats), while apparent containment gains under orthographic perturbation prove to be a tokenizer-driven "containment mirage." Crucially, explicit Chain-of-Thought reasoning rescues comprehension (94.72% Pass) while systematically dismantling containment (96.23% Use). Furthermore, expert-persona framing collapses refusal to 6.57%, revealing that keyword-based filters ignore dehumanizing communal slurs entirely. Our findings demonstrate that high-resource benchmarks cannot certify low-resource safety, necessitating meaning-grounded containment.

## Metadata
- **Published**: 2026-08-03T23:09:19Z
- **Authors**: Shadab Bin Habib, A K M Ferdous Reza Habib, Subarno Neel, Adib Sakhawat
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02941v1)