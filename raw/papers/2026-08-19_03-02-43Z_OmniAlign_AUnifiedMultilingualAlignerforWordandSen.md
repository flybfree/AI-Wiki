---
title: OmniAlign: A Unified Multilingual Aligner for Word and Sentence Alignment
published: 2026-08-19T03:02:43Z
authors: Mengpeng Yang, Jingxu Yang, Chao Chen, Tian Xia, Yabo Sun, Qiang Liu
url: http://arxiv.org/abs/2608.18474v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OmniAlign: A Unified Multilingual Aligner for Word and Sentence Alignment

## Abstract
Cross-lingual sequence alignment is fundamental for building and exploiting parallel corpora, spanning mappings from documents and sentences down to words and subwords. Existing tools, however, typically specialize in a single granularity, so practitioners often need separate systems for word- and sentence-level alignment---especially in multilingual and long-text settings. We present OmniAlign, a unified multilingual aligner that supports both word-level and sentence-level alignment with a single lightweight model. Built on an encoder-only backbone with strong long-context modeling, OmniAlign induces word alignments from contextualized token similarity matrices, and obtains document-level $m$--$n$ sentence alignments via sentence embeddings combined with dynamic programming. To balance fine-grained alignment accuracy and sentence-representation quality, we use a four-stage training pipeline: alignment-oriented continued pre-training, self-supervised learning, supervised fine-tuning on human annotations, and sentence-embedding distillation from a strong multilingual teacher. Experiments show that OmniAlign achieves highly competitive performance on both word- and sentence-alignment benchmarks and generalizes well to unseen language pairs. Surprisingly, later-stage supervised fine-tuning on short texts further improves alignment quality while retaining the long-context understanding acquired in earlier training, keeping the model robust on long-text word alignment.   \normalsize {\color{blue}\textbf{Code}: https://github.com/MilkDargon/OmniAlign}\par {\color{blue}\textbf{Model}: https://huggingface.co/WPS-Qingqiu/OmniAlign}

## Metadata
- **Published**: 2026-08-19T03:02:43Z
- **Authors**: Mengpeng Yang, Jingxu Yang, Chao Chen, Tian Xia, Yabo Sun, Qiang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18474v1)