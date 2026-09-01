---
title: Generative vs. Encoder Models for Multilingual NER: A Comprehensive Empirical Study on Naamapadam
published: 2026-08-30T18:41:04Z
authors: Jakkala Mahesh, Jatavath Shravan Kumar, Komalla Shivani, Sujoy Sarkar
url: http://arxiv.org/abs/2608.29959v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generative vs. Encoder Models for Multilingual NER: A Comprehensive Empirical Study on Naamapadam

## Abstract
Language is humanity's most consequential technology, yet for over a billion speakers across India's twenty-two constitutionally recognised languages, its digital layer remains structurally incomplete. Named Entity Recognition (NER), the foundational step in transforming raw text into machine-interpretable knowledge, has been studied exhaustively for English but remains largely unsolved across most Indic languages. This paper presents a rigorous comparative study of generative and encoder-based neural architectures for NER on all eleven languages of the Naamapadam benchmark. We evaluate five classic model families spanning sequence-to-sequence transformers and multilingual encoders; four decoder-only large language models (LLMs) fine-tuned with LoRA and 4-bit NF4 quantisation; and nine generative models in zero-to-5-shot inference. Under strict CoNLL span-level evaluation, encoder-based models (mBERT and XLM-R, both F1=0.675 on Hindi) substantially outperform every generative architecture in ten of eleven languages, with gaps of 7.5-40 percentage points against the strongest competitor (Gemma-2-2B: avg F1=0.427). The best few-shot result reaches only 28% of the encoder baseline. We identify three language clusters--encoder-dominant, partial-coverage, and failure-zone; and provide actionable deployment guidelines grounded in transfer learning and low-resource NLP principles.

## Metadata
- **Published**: 2026-08-30T18:41:04Z
- **Authors**: Jakkala Mahesh, Jatavath Shravan Kumar, Komalla Shivani, Sujoy Sarkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29959v1)