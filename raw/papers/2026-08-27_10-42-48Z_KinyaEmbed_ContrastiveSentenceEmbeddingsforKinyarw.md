---
title: KinyaEmbed: Contrastive Sentence Embeddings for Kinyarwanda via Multi-Stage Curriculum Training
published: 2026-08-27T10:42:48Z
authors: Ireddi Rakshitha, Devavarapu Yashwanth, Ntakirutimana Pierre
url: http://arxiv.org/abs/2608.26941v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KinyaEmbed: Contrastive Sentence Embeddings for Kinyarwanda via Multi-Stage Curriculum Training

## Abstract
We present KinyaEmbed, the first dedicated sentence embedding model for Kinyarwanda, a morphologically rich Bantu language spoken by over 12 million people in Rwanda. Existing multilingual embedding models such as LaBSE, mE5-large, and OpenAI text-embedding-3-large perform poorly on Kinyarwanda due to severe under-representation in their pre-training corpora. KinyaEmbed is built on KinyaBERT-large and trained via a four-stage curriculum using MultipleNegativesRankingLoss (MNRL): Stage 1 leverages ~18,000 paraphrase pairs from the Official Gazette of Rwanda with three temperature scales; Stage 2 fine-tunes on 715 NLLB-translated MNLI triplets for entailment structure; Stage 3 aligns representations using English-Kinyarwanda OPUS-100 translation pairs; Stage 4 refines with 2,936 high-quality pairs filtered from KinyaCOMET at quality threshold 0.8. We evaluate on SemRel2024-rw and introduce Wiki-RW-STS, a new contamination-free Kinyarwanda STS benchmark of 300 pairs derived from Kinyarwanda Wikipedia. A seven-checkpoint ensemble (all5+23A*2, with the final stage double-weighted) achieves Spearman \r{ho}=0.7298 on SemRel2024-rw, surpassing mE5-large by 20.9% and OpenAI text-embedding-3-large by 41.0%. KinyaEmbed also achieves the best document clustering silhouette score (0.2146) across all evaluated models. All checkpoints, the KinyaCOMET filtered pairs, and the Wiki-RW-STS benchmark are publicly available.

## Metadata
- **Published**: 2026-08-27T10:42:48Z
- **Authors**: Ireddi Rakshitha, Devavarapu Yashwanth, Ntakirutimana Pierre
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26941v1)