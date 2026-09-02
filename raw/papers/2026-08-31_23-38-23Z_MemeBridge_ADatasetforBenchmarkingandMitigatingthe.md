---
title: MemeBridge: A Dataset for Benchmarking and Mitigating the Bidirectional Cultural Gap in Meme Interpretation
published: 2026-08-31T23:38:23Z
authors: Hangxiao Zhu, Suliu Qin, Zhuoyan Li, Ming Jiang, Yu Zhang, Meng Xia
url: http://arxiv.org/abs/2609.00491v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemeBridge: A Dataset for Benchmarking and Mitigating the Bidirectional Cultural Gap in Meme Interpretation

## Abstract
Communicating across cultures is inherently challenging, especially through culturally dense and ambiguous formats like memes. While people expect large language models (LLMs) to hold promise for bridging such gaps, existing benchmark datasets often fail to capture the cultural context necessary for accurate interpretation. To address this, we introduce MemeBridge, a curated dataset centered on U.S.-originated memes, designed to capture two complementary perspectives: (1) how Chinese participants interpret these memes, and (2) how U.S. participants anticipate how people from other cultures might misunderstand them. Here, context refers to implicit cultural knowledge, including background beliefs, norms, and shared assumptions that shape meme comprehension. The dataset was constructed via a multi-stage crowdsourcing pipeline with rigorous validation, including human agreement checks and GPT-based classification verification. Each meme is annotated with sentiment, emotion, cultural significance, and knowledge type, providing rich supervision for downstream tasks. Notably, we observe that the anticipated misunderstandings from U.S. participants are often inaccurate, highlighting the asymmetries in cultural understanding and the challenges of adopting perspectives beyond one's own. This bidirectional framing, which focuses on both expression and perception, enables more nuanced benchmarking of cross-cultural comprehension. Our probing of multiple LLMs reveals that while models developed in different cultural contexts exhibit partial cross-cultural understanding, they often struggle with sophisticated interpretations. By contrast, fine-tuning with MemeBridge improves model performance, underscoring the value of culturally grounded resources for training and evaluating LLMs in globally diverse settings.

## Metadata
- **Published**: 2026-08-31T23:38:23Z
- **Authors**: Hangxiao Zhu, Suliu Qin, Zhuoyan Li, Ming Jiang, Yu Zhang, Meng Xia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00491v1)