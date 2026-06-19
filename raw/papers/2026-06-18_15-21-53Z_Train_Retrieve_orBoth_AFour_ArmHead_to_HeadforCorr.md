---
title: Train, Retrieve, or Both? A Four-Arm Head-to-Head for Correct Statutory Citation on the Ontario Residential Tenancies Act
published: 2026-06-18T15:21:53Z
authors: Ali Asaria, Tony Salomone, Deep Gandhi
url: http://arxiv.org/abs/2606.20359v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Train, Retrieve, or Both? A Four-Arm Head-to-Head for Correct Statutory Citation on the Ontario Residential Tenancies Act

## Abstract
Self-represented tenants, landlords, and help-desk staff need to be pointed at the provision of law that actually governs a question, with a correct statutory citation. We study this task on the Ontario Residential Tenancies Act, 2006 (RTA) and its core regulation, asking the operator's question empirically: is fine-tuning enough, or is hybrid retrieval needed? We run a four-arm head-to-head on Qwen2.5-7B-Instruct (base zero-shot, LoRA SFT-only, RAG-only, and an SFT+RAG hybrid), scored on citation exact-match (section+subsection) over a small, human-verification-pending real eval set. The base model cannot cite the RTA and SFT-only mis-recalls sections; retrieval is essential and drives hallucination to zero by construction; and the SFT+RAG hybrid scores highest at 0.481 exact-match with zero hallucinated citations. Its edge comes from SFT making provision selection more robust to the higher-recall candidate sets that hurt zero-shot RAG. Notably, this cheap bge-small hybrid matches or beats a pipeline built on bigger, specialized retrieval models (a larger embedder and a cross-encoder reranker), and a larger/improved training set does not help either: strong statutory-citation performance here does not require specialized retrieval models or more data. The artifact zeroes hallucination and clears the lift-over-base bar but does not reach the aspirational 0.70 exact-match target. All results are on a small, human-verification-pending real eval set and are reported as preliminary.

## Metadata
- **Published**: 2026-06-18T15:21:53Z
- **Authors**: Ali Asaria, Tony Salomone, Deep Gandhi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.20359v1)