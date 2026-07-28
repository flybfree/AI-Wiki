---
title: Do Small Models Use the Law You Give Them? Context-Injected Fine-Tuning for Legal QA in Bangladesh
published: 2026-07-26T04:06:13Z
authors: Moniruzzaman Mahadi, Abrar Mohammed Tanzim Alam, Sayma Siddika Monalisa, Mir Mohammad Asif Abdullah, Swakkhar Shatabda, Md Adnan Arefeen
url: http://arxiv.org/abs/2607.23446v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Small Models Use the Law You Give Them? Context-Injected Fine-Tuning for Legal QA in Bangladesh

## Abstract
A small language model can receive the governing statutory provision and still answer incorrectly. We test whether fine-tuning on examples containing relevant law improves later use of retrieved law. We curate 2{,}165 bilingual QA records from six Bangladeshi acts and three schedules, then fine-tune Qwen3.5 at 0.8B, 2B, and 4B. Evaluation uses the 2022 and 2023 Bangladesh Bar Council exams in Bangla and machine-translated English, with no retrieval, BM25, or FAISS, scored by strict consistency over three seeded runs. At 0.8B, fine-tuning raises the 2022 English FAISS score from 2 to 34 of 100. Gains at 0.8B and 2B survive paired testing, but the 4B model has no detectable net gain: Bangla improves while several English conditions regress. Fine-tuning also reduces answers that drift from Bangla into mostly English from 44.0--53.2\% to 0.2--0.7\%, with adjusted $p<.001$ at every scale. Retrieval quality is therefore not the only bottleneck. Small bilingual legal models also differ in how they use supplied law and whether they answer in the requested language. The dataset is publicly available at https://huggingface.co/datasets/momahadi/bangladesh-legal-qa-dataset.

## Metadata
- **Published**: 2026-07-26T04:06:13Z
- **Authors**: Moniruzzaman Mahadi, Abrar Mohammed Tanzim Alam, Sayma Siddika Monalisa, Mir Mohammad Asif Abdullah, Swakkhar Shatabda, Md Adnan Arefeen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23446v1)