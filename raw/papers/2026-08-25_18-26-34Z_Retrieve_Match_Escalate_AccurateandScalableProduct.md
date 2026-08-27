---
title: Retrieve, Match, Escalate: Accurate and Scalable Product Linking with VLM-Distilled Cross-Encoders and Agentic VLMs
published: 2026-08-25T18:26:34Z
authors: Jian Wang, Steven Xu, Sanjyot Thete, Maryam Barouti, Tom Tang, Elaine Wu, Charu Sareen, Kyle MacDonald
url: http://arxiv.org/abs/2608.25037v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieve, Match, Escalate: Accurate and Scalable Product Linking with VLM-Distilled Cross-Encoders and Agentic VLMs

## Abstract
Product linking, the entity-resolution task of mapping merchant product records to canonical catalog products, consolidates fragmented listings so downstream search, recommendation, and advertising see one clean entry per product. At marketplace scale, billions of noisy, multi-category records must be resolved against tens of millions of canonical products, where scoring every candidate with a single model is either too weak for the hard cases or too costly for the easy ones. We present a production retrieve-then-match cascade that spends computation in proportion to difficulty: retrieval surfaces plausible matches, a lightweight text cross-encoder auto-resolves the high-confidence majority, and an agentic multimodal vision-language model settles the ambiguous remainder by inspecting product images and issuing web searches for evidence that is in neither record. The cross-encoder is distilled from millions of dual-VLM-consensus labels, retiring human annotation from the training set, and is calibrated to auto-accept links at a 98% precision bar validated against a smaller operator-certified audit. The agent is a self-hosted open-weight model that reaches a closed frontier VLM's precision at a four-point recall cost (88% versus 92%) for roughly one-seventh the per-pair cost, with no fine-tuning. Per-pair cost spans nearly five orders of magnitude from the cheap cross-encoder to the frontier VLM, so escalating only the hard tail to the agent raises end-to-end link coverage from the cheap stage's 68% to 77%.

## Metadata
- **Published**: 2026-08-25T18:26:34Z
- **Authors**: Jian Wang, Steven Xu, Sanjyot Thete, Maryam Barouti, Tom Tang, Elaine Wu, Charu Sareen, Kyle MacDonald
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25037v1)