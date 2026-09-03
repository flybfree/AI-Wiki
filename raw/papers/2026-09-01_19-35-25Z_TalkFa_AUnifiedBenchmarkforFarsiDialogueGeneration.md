---
title: TalkFa: A Unified Benchmark for Farsi Dialogue Generation and Understanding
published: 2026-09-01T19:35:25Z
authors: Neda Jamshidi, Kamyar Zeinalipour, Fahimeh Akbari, Monica Bianchini, Marco Maggini, Marco Gori
url: http://arxiv.org/abs/2609.01810v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TalkFa: A Unified Benchmark for Farsi Dialogue Generation and Understanding

## Abstract
Farsi, spoken by more than 120 million people, lacks a comprehensive benchmark for dialogue generation and understanding. We introduce TALKFA, a unified benchmark comprising three complementary datasets: (1) WIKI-FADIAL, 4.2K Wikipedia-grounded dialogues for knowledge-grounded generation; (2) DAILYDIALOG-FA, 6.6K dialogues annotated for dialogue acts and emotions; and (3) PLAYDIAL-FA, 2.1K theatrical dialogues with sentiment labels. While LLMs assist data construction, every dialogue undergoes multi-stage review and revision by native Farsi speakers, and only the final human-approved dialogues are released. Experiments with six LLAMA and MISTRAL models show that LoRA substantially improves dialogue generation while requiring only 25-50% of the training data to recover over 90% of the final performance gains. Across classification tasks, FABERT achieves the best dialogue-act performance, LORA-MISTRAL-7B performs best on emotion recognition, and MISTRAL-24B achieves the highest sentiment score. Human evaluation and independent external validation demonstrate the reliability of the benchmark, while comparisons with GPT-4.1 as an LLM judge reveal that automatic metrics substantially overestimate dialogue quality. Zero-shot evaluation with frontier LLMs further shows that TalkFa remains a challenging benchmark. We will release all datasets, annotation guidelines, code, and checkpoints.

## Metadata
- **Published**: 2026-09-01T19:35:25Z
- **Authors**: Neda Jamshidi, Kamyar Zeinalipour, Fahimeh Akbari, Monica Bianchini, Marco Maggini, Marco Gori
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01810v1)