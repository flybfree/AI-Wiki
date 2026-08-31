---
title: CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents
published: 2026-08-28T14:44:28Z
authors: Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee
url: http://arxiv.org/abs/2608.28389v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CamoDocs: A Poisoning Attack Against Retrieval-Augmented Language Models Using Camouflaged Documents

## Abstract
Retrieval-augmented generation (RAG) augments LLMs with external documents, but public or user-editable sources expose RAG systems to data poisoning: attackers can inject malicious documents to steer outputs toward targeted answers. Existing poisoning attacks often rely on query inclusion, inserting the target query into poisoned documents to improve retrieval; however, this creates lexical and embedding-space artifacts that make them easy to filter. We propose CamoDocs, a poisoning attack that avoids direct query inclusion by camouflaging adversarial documents among benign content. CamoDocs chunks synthesized benign and adversarial drafts, replaces selected tokens in benign chunks with dispersion tokens that spread poisoned-document embeddings, and applies coherence filtering to limit readability degradation. Across seven RAG defenses, three open-weight LLMs, and three benchmarks, CamoDocs achieves strong average ASR while avoiding query-overlap artifacts exploited by simple query detection. It also remains effective against proprietary models, achieving average ASRs of 61.80% on GPT-5.4-mini and 55.09% on Claude-Haiku-4.5. Finally, we show that erasure-heavy clustering defenses such as TrustRAG can reduce ASR, but only with substantial utility drops on retrieval-dependent benchmarks such as NeoQA. Code is available at https://github.com/jaewonalive/CamoDocs.

## Metadata
- **Published**: 2026-08-28T14:44:28Z
- **Authors**: Jaewon Jung, Haizhong Zheng, Hongsun Jang, Jaeyong Song, Beidi Chen, Jinho Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28389v1)