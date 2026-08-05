---
title: Diversity is Not Ambiguity: Toward Accurate and Efficient Ambiguity Detection for Open-Domain QA
published: 2026-08-04T06:13:41Z
authors: Jiwon Lee, Yong-chan Park, Jungin Hong, U Kang
url: http://arxiv.org/abs/2608.03177v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diversity is Not Ambiguity: Toward Accurate and Efficient Ambiguity Detection for Open-Domain QA

## Abstract
How can question answering (QA) systems determine whether a query is ambiguous? Ambiguity detection is essential in open-domain QA, as misclassification leads to answering the wrong interpretation or unnecessary clarification. However, existing methods conflate answer diversity with ambiguity, leading to inaccurate predictions. They also process queries uniformly, resulting in wasteful computation. We propose ARCHIVE (Ambiguity Recognition via Cascaded Hypothesis Inspection and Conflict Verification), an accurate and efficient framework that detects ambiguity via logical conflict: a query is ambiguous when its valid answers cannot all be true under a single interpretation. ARCHIVE combines a lightweight early-exit encoder for surface-detectable cases with a conflict reasoning module that models logical relations among answers, reinforced by an invariance objective for robustness to noisy answer sets. We present QuireQA, a 4,703-query benchmark spanning factoid, non-factoid, and ill-formed queries. Experiments show ARCHIVE outperforms competitors, improving F1-amb by up to 10.4% and F1-unamb by up to 21.6%, while operating 16$\times$ faster than the best competitor.

## Metadata
- **Published**: 2026-08-04T06:13:41Z
- **Authors**: Jiwon Lee, Yong-chan Park, Jungin Hong, U Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03177v1)