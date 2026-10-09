---
title: Could LLM Watermark Detection be Public?
published: 2026-10-08T15:05:58Z
authors: Georgios Milis, Tom Sander, Tomáš Souček, Heng Huang, Pierre Fernandez
url: http://arxiv.org/abs/2610.12106v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Could LLM Watermark Detection be Public?

## Abstract
Watermarking large language models is popular for tracing chatbot and agentic outputs, yet detectors remain unreleased since exposing them could let attackers do targeted edits with the detector's feedback. However, watermarks are already vulnerable to uninformed tampering attacks. We thus first quantify whether a public detector would be an additional liability in a deployment setting at varying levels of access, from token-level scores to a binary verdict. Second, we introduce a split-key public-private watermarking method that exposes one key through a public detector while keeping the other for full verification and forensics. An informed attacker can only move the public signal, creating an imbalance between public and private scores. We introduce a statistical test for this imbalance, and combine it with the full key verdict in a two-stage mechanism. Third, we evaluate the split-key method on a wide range of removal and forgery attacks, comparing the uninformed to detector-informed settings. Public detection improves removal only at small edit budgets, since plain rephrasing already strips the watermark at a lower quality cost, but it does enable forgery, which the private pipeline can identify. Overall, releasing half of the watermark enables transparency and interoperability, and tampering with the released half stays detectable. This bounds the provider's liability and questions the need to keep detectors fully private.

## Metadata
- **Published**: 2026-10-08T15:05:58Z
- **Authors**: Georgios Milis, Tom Sander, Tomáš Souček, Heng Huang, Pierre Fernandez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12106v1)