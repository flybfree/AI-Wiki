---
title: NxN E-valuation: Hypothesis Certification via a Conformal CRT Null
published: 2026-08-06T22:14:53Z
authors: Bin Wang, Yan Zhong
url: http://arxiv.org/abs/2608.06621v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NxN E-valuation: Hypothesis Certification via a Conformal CRT Null

## Abstract
We propose NxN E-valuation, a handy, e-value-based hypothesis-certification algorithm that lets a hypothesis be verified without building any case-specific certification procedure---such as constructing a dedicated null hypothesis---as long as a large enough dataset is available. The method is especially suited to LLM-based exploration systems, where LLMs are remarkably good at proposing hypotheses but suffer badly from hallucination; this hallucination prevents us from harvesting LLM outputs directly, and existing remedies each fall short. The most common solutions include letting the LLM verify or correct itself circular verification and held-out testing (where false hypotheses can still pass via spurious correlations), among other remedies detailed in the introduction. To resolve this, NxN E-valuation exploits the naturally existing large training set and lets different samples serve as null hypotheses for one another. This design directly realizes a conditional randomization test (CRT) that certifies each hypothesis. The approach can be a universally better replacement for at least LLM circular verification and held-out-data testing, provided the LLM's generations are hypotheses that apply to each individual sample.

## Metadata
- **Published**: 2026-08-06T22:14:53Z
- **Authors**: Bin Wang, Yan Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06621v1)