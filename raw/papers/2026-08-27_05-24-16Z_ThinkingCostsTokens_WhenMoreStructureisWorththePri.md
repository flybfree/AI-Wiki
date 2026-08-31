---
title: Thinking Costs Tokens: When More Structure is Worth the Price
published: 2026-08-27T05:24:16Z
authors: Thomas Nolasque, John Grey, Calista Pham, Ankit Vani
url: http://arxiv.org/abs/2608.27506v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Thinking Costs Tokens: When More Structure is Worth the Price

## Abstract
Adding inference structure to a language model lets it search, verify, and revise, but these actions consume the very budget they are supposed to use well. In this paper, we investigate whether there exists a token-budget threshold, below which the overhead of planning and verification hurts performance and above which it helps. We evaluate two systems on FinQA and TAT-QA financial reasoning tasks, using GPT-5.4 mini across 14 budget tiers ranging from 250 to 42,000 output-equivalent tokens. The first system is a monolith, which is a single LLM call. The second is a verified search architecture that adds planning, label-blind checking, and repair capabilities. We run 1,000 cases for a total of 28,000 completed cells. Both systems score 0% at the two lowest tiers, where neither can fit a complete prompt. At 1,000 tokens, the monolith reaches 18% accuracy while verified search scores near 0%, since the planning overhead leaves no room for an answer. From 1,500 tokens onward, verified search surpasses the monolith and maintains a consistent advantage, reaching approximately 44% at the highest tiers while the monolith reaches approximately 40%. The crossover occurs between 1,000 and 1,500 output-equivalent tokens, confirmed by a strict intersection-union test ($p \le 0.001$ at both endpoints).

## Metadata
- **Published**: 2026-08-27T05:24:16Z
- **Authors**: Thomas Nolasque, John Grey, Calista Pham, Ankit Vani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27506v1)