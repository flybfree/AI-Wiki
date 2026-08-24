---
title: Enhancing LLMs in Predictive Political QA with Semi-Structured Data
published: 2026-08-21T15:27:28Z
authors: Yinan Liu, Zihan Zhou, Zichun Jin, Xinyu Wang, Bin Wang, Xiaochun Yang
url: http://arxiv.org/abs/2608.21218v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing LLMs in Predictive Political QA with Semi-Structured Data

## Abstract
Predictive political question answering (QA), such as predicting how a political actor will vote, goes beyond factual lookup. External political resources offer rich historical evidence, but rarely contain the answer itself. Existing LLM augmentation methods, including actor-profile-based simulation and knowledge graph evidence injection, improve political reasoning but largely treat external resources as knowledge-based evidence, leaving prediction-relevant signals under-modeled. We identify two complementary signals for predictive political QA: actor stances that capture issue-specific preferences, and high-order structure signals that capture indirect dependencies among political actors. We propose PSL, a dual-view framework that converts semi-structured political records into inference-oriented evidence for LLMs. PSL extracts stance signals from question-relevant actor records in a semantic view, and learns structure-aware actor representations from an actor interaction graph in a vector view. Across three real-world datasets and multiple LLMs, PSL consistently outperforms baselines, with ablations confirming the complementary gains of stance and structure signals.

## Metadata
- **Published**: 2026-08-21T15:27:28Z
- **Authors**: Yinan Liu, Zihan Zhou, Zichun Jin, Xinyu Wang, Bin Wang, Xiaochun Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21218v1)