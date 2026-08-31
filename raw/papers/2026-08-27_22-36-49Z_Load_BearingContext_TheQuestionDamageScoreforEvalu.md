---
title: Load-Bearing Context: The Question Damage Score for Evaluating Context Reliance in Linguistic Reasoning
published: 2026-08-27T22:36:49Z
authors: Neh Majmudar, Elena Filatova
url: http://arxiv.org/abs/2608.27756v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Load-Bearing Context: The Question Damage Score for Evaluating Context Reliance in Linguistic Reasoning

## Abstract
Determining whether large language models derive answers from context or prior knowledge remains a fundamental challenge. Self-contained linguistic olympiad puzzles provide a controlled setting where all answers derive solely from expert-designed context examples without external knowledge. Removing individual context examples can eliminate information needed for specific questions while leaving the rest of the puzzle unchanged. We leverage this to introduce a diagnostic framework for analyzing individual context examples. Using 53 UK Linguistics Olympiad puzzles, we generate two modified variants by deleting a single context example: (1) uniform random deletion, and (2) targeted deletion (inspired by error-correcting codes) to remove a structurally load-bearing example uniquely carrying necessary information. We formalize this impact using a Question Damage Score to classify puzzles as fragile or robust. Evaluating three frontier LLMs under instructions to abstain when information is insufficient, we find they rarely abstain, often continuing to produce correct answers after load-bearing context is removed. These findings motivate further investigation into context-based reasoning, prior knowledge, memorization, and linguistic inference. Beyond abstention, the framework enables fine-grained analyses of context reliance, including causal interventions, stopping-set analysis, targeted contamination studies, and mechanistic interpretability.

## Metadata
- **Published**: 2026-08-27T22:36:49Z
- **Authors**: Neh Majmudar, Elena Filatova
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27756v1)