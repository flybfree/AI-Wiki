---
title: Cloud and On-Premises Deployment of Uzbek Legal RAG via Targeted Retriever Fine-Tuning
published: 2026-08-29T14:07:39Z
authors: Tatul Danielyan, Mariam Avetisyan, Hrant Davtyan
url: http://arxiv.org/abs/2608.29284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cloud and On-Premises Deployment of Uzbek Legal RAG via Targeted Retriever Fine-Tuning

## Abstract
Deploying large language models for legal question answering raises challenges that general-purpose leaderboards do not capture, particularly for low-resource languages and under hard operational constraints. We report on building and operating a retrieval-augmented (RAG) legal assistant for Uzbek that must run in two regimes: a managed cloud service that maximizes answer quality within a per-token cost ceiling, and an on-premises deployment for clients whose legal data may not leave their infrastructure, restricting us to open-weight models on limited local hardware under latency constraints. Because no evaluation existed for this setting, we build two domain benchmarks: a retrieval benchmark of 178 expert-annotated legal queries with gold provision spans, and an end-to-end benchmark of 504 expert-curated question--answer pairs scored by an LLM judge whose ratings we validate against human judgments and against an independent-family judge. Applying these benchmarks under each regime, we find the open-versus-proprietary gap is small and cheaply closed by fine-tuning. Therefore, we train UTE-1, which is a state-of-the-art text embedder among open models for Uzbek. We also demonstrate that closing the performance gap via fine-tuning is both impractical due to the intensive hardware demands of long-context legal Q\&A and unnecessary, given that legal acts change frequently. We support this by reporting a negative result from a QLoRA experiment. We distill practical guidance for similar deployments, drawn from a system serving real users in production. We release our benchmarks, evaluation code and the fine-tuned embedder (UTE-1) \href{https://metric-ai-lab.github.io/Uzbek-Legal-RAG/}{at this https URL} to support future work on low-resource legal NLP.

## Metadata
- **Published**: 2026-08-29T14:07:39Z
- **Authors**: Tatul Danielyan, Mariam Avetisyan, Hrant Davtyan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29284v1)