---
title: Contextual Tamil Spelling and Grammar Correction Using Progressively Fine-Tuned Sequence-to-Sequence Transformers
published: 2026-09-03T02:02:39Z
authors: Karthikeyan A, Jaya Nirmala S, Sangeetha Sivanesan, Indhu R, Pranav Kumar, Bharat Jude Johnson, Vishnu Ram
url: http://arxiv.org/abs/2609.03273v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Contextual Tamil Spelling and Grammar Correction Using Progressively Fine-Tuned Sequence-to-Sequence Transformers

## Abstract
Tamil spell and grammar correction is challenging because Tamil is an agglutinative low-resource language with rich verbal morphology, complex sandhi (phonetic transformation) rules at word boundaries, and a script of 247 distinct letters. Prior work targets word-level surface errors with rule-based methods, statistical n-gram models, Minimum Edit Distance, or hybrid pipelines with a transformer re-ranker; such methods cannot reliably handle contextual errors - subject-verb agreement, tense consistency, or cross-word sandhi - which require sentence-level understanding. We propose an end-to-end sequence-to-sequence formulation and fine-tune mT5-small and mBART-50 on a synthetic corpus of up to 657,720 noisy-clean Tamil sentence pairs spanning ten error categories. Both backbones follow the same four-stage progressive schedule, each stage targeting one weakness: surface noise (v2), contextual grammar (v3), single-site sandhi (v4), and multi-site cross-word sandhi (v5). On a 1,000-sentence balanced diagnostic set verified disjoint from all training data, our best model, mBART-50 v5, reaches 69.3% top-1 exact-match accuracy, with 87.5% on sandhi and 43.5% on subject-verb agreement. The schedule is what produces these gains: subject-verb accuracy rises from 1.0% to 52.5% once contextual pairs are introduced, and sandhi from 0% to 87.5% once multi-site sandhi pairs are. We additionally quantify a precision-recall trade-off this literature has not reported: sandhi recall is paid for monotonically in identity accuracy. Finally, Tamil-LLaMA-7B-Instruct reaches 19.0% zero-shot and 24.7% with three demonstrations against a 20.0% copy baseline, showing that a Tamil-adapted instruction model does not transfer to specialised sentence-level correction without task-specific supervision.

## Metadata
- **Published**: 2026-09-03T02:02:39Z
- **Authors**: Karthikeyan A, Jaya Nirmala S, Sangeetha Sivanesan, Indhu R, Pranav Kumar, Bharat Jude Johnson, Vishnu Ram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03273v1)