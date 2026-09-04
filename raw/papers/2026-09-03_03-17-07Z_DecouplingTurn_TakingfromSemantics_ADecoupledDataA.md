---
title: Decoupling Turn-Taking from Semantics: A Decoupled Data Approach for Finite-State-Machine-Based Full-Duplex Dialogue
published: 2026-09-03T03:17:07Z
authors: Yihang Li, Chenhui Chu
url: http://arxiv.org/abs/2609.03321v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Decoupling Turn-Taking from Semantics: A Decoupled Data Approach for Finite-State-Machine-Based Full-Duplex Dialogue

## Abstract
The Neural Finite State Machine (NFSM) framework offers a pragmatic path to full-duplex dialogue by serializing turn-taking control and response generation onto a single causal tape under the standard next-token prediction objective, thereby preserving semantic prowess at a low fine-tuning cost. However, its reliance on synthetic text data fundamentally limits turn-taking naturalness, as Large Language Models (LLMs) cannot faithfully simulate the fine-grained acoustic temporal dynamics of real human dialogues. In this work, we propose a decoupled data approach that learns turn-taking from real Human-Human (HH) spoken dialogues while shaping semantic behavior through configurable Human-Agent (HA) text dialogues. To operationalize this approach, we introduce a rule-based event-guided data transformation method that serializes HH spoken dialogues into FSM tapes by classifying turn-taking events and applying deterministic mapping rules, enabling scalable supervision without LLM-generated annotations. We further propose a Source-Aware Calibrated (SAC) Loss that jointly calibrates the long-tailed distribution of state transition tokens and channels each data source toward the capability it best supervises. Experiments show that our approach substantially improves turn-taking proficiency while recovering the foundation LLM's semantic capability. Our code and model are available at https://github.com/Liyht/def-fsm.

## Metadata
- **Published**: 2026-09-03T03:17:07Z
- **Authors**: Yihang Li, Chenhui Chu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03321v1)