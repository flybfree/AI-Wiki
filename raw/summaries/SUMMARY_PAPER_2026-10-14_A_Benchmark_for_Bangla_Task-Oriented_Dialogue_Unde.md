---
title: A Benchmark for Bangla Task-Oriented Dialogue Understanding
url: http://arxiv.org/abs/2610.18060v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_09-47-39Z_ABenchmarkforBanglaTask_OrientedDialogueUnderstand.md
generated_at: 2026-10-14 01:02
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces BanglaTOD, a parallel tri-lingual benchmark for task-oriented dialogue understanding in Bangla, English, and romanized Bangla (Banglish). The benchmark comprises 209 multi-turn dialogues spanning nine Bangladesh-specific service domains with 64 intents, yielding 4,689 language-specific turn records annotated with intents, token-level slots, state updates, and accumulated dialogue states. The authors establish context-aware baselines using mBERT, BERT-base-uncased, and BanglaBERT, revealing substantial performance differences across models and linguistic representations, and demonstrating that removing dialogue history reduces intent accuracy by 19.0 to 25.7 percentage points.

## Key Takeaways
- BanglaTOD is the first parallel tri-lingual benchmark for Bangla task-oriented dialogue, covering 209 multi-turn dialogues across nine Bangladesh-specific service domains and 64 intents, with each conversational turn aligned across Bangla, English, and Banglish to produce 4,689 annotated turn records including intents, token-level slots, state updates, and accumulated dialogue states.
- Cross-language analysis using mBERT, BERT-base-uncased, and BanglaBERT reveals substantial performance differences across models and linguistic representations, highlighting that no single model or language representation uniformly outperforms others, and that Banglish (romanized Bangla) poses unique challenges for multilingual NLP systems.
- Dialogue history is critical for accurate understanding: removing conversational context reduces intent classification accuracy by 19.0 to 25.7 percentage points, underscoring the necessity of state tracking and multi-turn context modeling in task-oriented dialogue systems for low-resource languages.

## Context
Task-oriented dialogue systems have seen significant progress for high-resource languages like English, but low-resource languages such as Bangla remain severely underexplored, particularly in multilingual settings where code-switching between Bangla, English, and romanized transliteration is common in everyday digital communication in Bangladesh. This gap limits the deployment of conversational AI services for over 230 million Bangla speakers. BanglaTOD addresses this gap by providing structured, annotated dialogue data that enables rigorous evaluation of multilingual dialogue understanding models in a linguistically complex and culturally specific setting.

## Implications
For the research community, BanglaTOD provides a reproducible foundation for advancing multilingual dialogue state tracking, intent classification, and slot filling in low-resource and code-switched language environments, potentially inspiring similar benchmarks for other underrepresented languages. For industry practitioners building conversational AI products for South Asian markets, the findings demonstrate that monolingual or English-centric models perform poorly on Bangla and Banglish inputs, and that incorporating dialogue history is essential for production-grade accuracy. The publicly available dataset on Hugging Face lowers the barrier for researchers and developers to build and evaluate Bangladesh-specific conversational applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18060v1)
