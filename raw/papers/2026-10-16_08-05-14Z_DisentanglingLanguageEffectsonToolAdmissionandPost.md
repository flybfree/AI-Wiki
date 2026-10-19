---
title: Disentangling Language Effects on Tool Admission and Post-Retrieval Safety
published: 2026-10-16T08:05:14Z
authors: Aditya Nawal, Manit Baser, Mohan Gurusamy
url: http://arxiv.org/abs/2610.23093v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Disentangling Language Effects on Tool Admission and Post-Retrieval Safety

## Abstract
LLM agents increasingly use retrieval tools across languages, yet their safety evaluation remains English-centric. It remains unclear whether language affects tool admission, post-retrieval generation, or both. We independently vary request, retrieved-page, and required response languages in a controlled URL-retrieval setting across ten models and seven languages. We identify Safety Loss through Interlingual Processing (SLIP). Non-English harmful requests increase mean tool admission from 46.9% to 67.4%, with a positive mean change in every model. This pattern also persists in an autonomous retrieval setup across all four models tested in this setting. Requiring answers in the page language increases pooled harmfulness on matched tool calls from 50.3% to 57.4% across four closed-weight models, mainly in Chinese and Hindi. Translating pages alone produces no consistent harm increase in eight models with comparable inference settings. Automated audits show that a non-harmful response may be a genuine safety refusal, a deflection citing language difficulties, or an unusable answer. Harmfulness labels alone cannot distinguish these outcomes. Multilingual safety evaluations should therefore measure tool admission and response harmfulness separately and distinguish refusal from capability failure.

## Metadata
- **Published**: 2026-10-16T08:05:14Z
- **Authors**: Aditya Nawal, Manit Baser, Mohan Gurusamy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23093v1)