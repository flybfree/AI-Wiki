---
title: ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via Reliability-Guided Reasoning Chains
published: 2026-08-26T07:59:24Z
authors: Jinpu Jiang, Xuan Wu, Wenhao Song, Bo Yang, You Zhou, Hongwei Ge, Heow Pueh Lee, Yanchun Liang, Chunguo Wu
url: http://arxiv.org/abs/2608.25487v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReliableRAG: Combating Misinformation in Retrieval-Augmented Generation via Reliability-Guided Reasoning Chains

## Abstract
Retrieval-Augmented Generation (RAG) has emerged as a powerful architecture for Question Answering (QA) by integrating external information into Large Language Models (LLMs). However, false, inaccurate, and misleading information in news and social media poses a serious challenge to real-world RAG systems, especially in multi-hop QA, where complex multi-step reasoning can be misled by even a single deceptive misinformation segment in the retrieved documents. Existing approaches mainly rely on implicit alignment or explicit regulation, but their limited ability to assess fine-grained information reliability makes them vulnerable to deceptive misinformation that is semantically relevant to the question yet factually incorrect, leading to erroneous answers. To address this limitation, we propose ReliableRAG, which, to the best of our knowledge, is the first reliability-driven framework that mitigates deceptive misinformation in multi-hop QA through fine-grained evaluation of individual triples. ReliableRAG first extracts information segments from source documents and represents them as structured triples. It then quantifies triple reliability by combining query-triple semantic relevance with triple credibility, retaining only the top-$K$ reliable and non-redundant triples. Based on these refined triples, ReliableRAG autoregressively constructs robust reasoning chains to consolidate trustworthy evidence and filter deceptive misinformation, producing accurate answers faithful to reliable information. Experiments on three multi-hop QA datasets show that ReliableRAG outperforms existing methods, substantially improving the factual reliability and robustness of RAG systems under deceptive misinformation injection.

## Metadata
- **Published**: 2026-08-26T07:59:24Z
- **Authors**: Jinpu Jiang, Xuan Wu, Wenhao Song, Bo Yang, You Zhou, Hongwei Ge, Heow Pueh Lee, Yanchun Liang, Chunguo Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25487v1)