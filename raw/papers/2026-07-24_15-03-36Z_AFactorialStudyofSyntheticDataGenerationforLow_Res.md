---
title: A Factorial Study of Synthetic Data Generation for Low-Resource Machine Translation using Grammar Books
published: 2026-07-24T15:03:36Z
authors: Varun Ghat Ravikumar, Sina Ahmadi, Lena Jäger, Rico Sennrich
url: http://arxiv.org/abs/2607.22376v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Factorial Study of Synthetic Data Generation for Low-Resource Machine Translation using Grammar Books

## Abstract
Most endangered languages lack the parallel data required for machine translation, despite the existence of descriptive grammar books. We introduce a pipeline that uses large language models to extract grammatical rules, example sentences, and lexicons from grammar books and generate synthetic parallel corpora for fine-tuning-rather than feeding grammar content into prompts at inference time, as in prior work. Validated on three typologically diverse low-resource languages-Kalamang (Papuan), Tuatschin (Romance), and Mandan (Siouan)-we show that fine-tuning on synthetic data improves over seed-data baselines in 75% of configurations for Kalamang and 59% for Tuatschin, with best-case ChrF++ gains of +8.8, +5.3, and +3.3 respectively. Through a systematic factorial study across 96 configurations varying target part-of-speech, retrieval granularity, and sample volume, we identify which factor combinations drive gains and where they break down. Our results demonstrate that static linguistic documentation can be repurposed for machine translation fine-tuning, offering a practical path towards translation tools for severely under-resourced languages.

## Metadata
- **Published**: 2026-07-24T15:03:36Z
- **Authors**: Varun Ghat Ravikumar, Sina Ahmadi, Lena Jäger, Rico Sennrich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22376v1)