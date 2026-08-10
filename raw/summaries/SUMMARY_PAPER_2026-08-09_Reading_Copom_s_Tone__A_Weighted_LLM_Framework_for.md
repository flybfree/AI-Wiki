---
title: Reading Copom's Tone: A Weighted LLM Framework for Hawkish-Dovish Sentiment, Forward Guidance, and Uncertainty
url: http://arxiv.org/abs/2608.07251v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_14-08-31Z_ReadingCopom_sTone_AWeightedLLMFrameworkforHawkish.md
generated_at: 2026-08-09 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a natural‑language processing framework for quantifying the tone of Copom statements and linking it to forward guidance and uncertainty. It combines sentence‑level intensity weights with document‑wide scores, yielding an average score of +0.107 over 80 statements from 2016 to 2026.

## Key Takeaways
- The model assigns hawkish or dovish sentences a 0‑to‑1 intensity weight and aggregates them into a bounded document score ranging from –1 to 1, with the highest reading of +0.570 occurring in August 2021.
- It also measures forward guidance direction, explicitness, uncertainty level and change over time, producing separate full‑document metrics beyond the tone score.
- The latest statement (August 5 2026) scores +0.232 using eight hawkish, two dovish and nine neutral sentences, showing a nuanced structure with ambiguous guidance but higher uncertainty than before.

## Context
This work builds on iSent’s approach to central‑bank sentiment analysis, adapting it for the Copom system while introducing an LLM‑driven weighting scheme. It demonstrates how large language models can be used to decompose policy communication into interpretable components such as tone and guidance direction.

## Implications
The framework offers a transparent, auditable tool that separates rhetorical tone from actual policy guidance, useful for researchers and practitioners monitoring central‑bank messaging. By providing both descriptive scores and forward‑guidance metrics, it supports better understanding of market expectations without implying predictive power.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07251v1)
