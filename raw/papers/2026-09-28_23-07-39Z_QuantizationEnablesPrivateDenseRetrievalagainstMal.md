---
title: Quantization Enables Private Dense Retrieval against Malicious Service Providers
published: 2026-09-28T23:07:39Z
authors: Louis Tremblay Thibault, Sofiane Azogagh, Marc-Olivier Killijian, Ulrich Aïvodji
url: http://arxiv.org/abs/2609.36376v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quantization Enables Private Dense Retrieval against Malicious Service Providers

## Abstract
Dense retrieval, the key component of Retrieval Augmented Generation (RAG), retrieves the most relevant documents by comparing dense vector representations of queries and passages from a large corpus. In privacy-sensitive applications, the server observes the query and controls which evidence is returned, creating both confidentiality and integrity risks. We formulate private dense retrieval as providing query privacy and retrieval integrity against a malicious server, and develop a two-round cryptographic protocol that provides both guarantees. Our protocol reduces private and verifiable retrieval to multiplication of a committed matrix by an encrypted vector and uses low-bit quantization to make this computation practical. We evaluate the resulting trade-off between cryptographic cost, retrieval quality, and downstream RAG accuracy across six embedding models, four language models, and corpora of up to 2.68 million passages. Our results show that, with a clipped quantizer, three-bit quantization largely preserves retrieval quality and downstream accuracy, while a private query over a corpus the size of a clinical reference requires one to three minutes of server time. These results suggest that private dense retrieval is already practical for moderately sized, privacy-sensitive corpora when minute-scale latency is acceptable.

## Metadata
- **Published**: 2026-09-28T23:07:39Z
- **Authors**: Louis Tremblay Thibault, Sofiane Azogagh, Marc-Olivier Killijian, Ulrich Aïvodji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36376v1)