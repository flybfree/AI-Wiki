---
title: Hallucinations on the Board: Tool-Augmented Evaluation of LLM Chess Commentary
published: 2026-08-04T21:31:01Z
authors: S. Ashwin Hebbar, Peiyao Sheng, Sewoong Oh, Pramod Viswanath
url: http://arxiv.org/abs/2608.04240v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hallucinations on the Board: Tool-Augmented Evaluation of LLM Chess Commentary

## Abstract
Superhuman game engines in domains like chess have made expert-level evaluations easily accessible, yet they communicate what is true without the natural-language explanations that make such expertise educationally useful to experts and non-experts alike. Large language models could, in principle, bridge this gap, but they frequently hallucinate due to limited domain-specific knowledge, and standard reference-based or LLM-as-a-judge frameworks cannot reliably detect these errors. In this work, we present ACT-Eval, an evaluation framework that decomposes chess commentary into atomic claims and routes them to engine-supported tools and expert-annotated gold references to assess factual correctness, conceptual coverage, and move-quality judgment. We release a benchmark of 325 position--move pairs spanning pedagogical, tournament, and critical positions, including 125 positions with expert-verified gold atoms and a five-class error taxonomy. Evaluating leading proprietary and open-weight models, we find that factual hallucinations remain pervasive in chess commentary: GPT-5.4 without tools produces incorrect sub-claims 22.0% of the time, while smaller open-weight models exceed 40%. Although tool augmentation substantially improves factual correctness and move-quality assessment, coverage of expert strategic and tactical ideas remains limited across all models. Human calibration shows that ACT-Eval's factual judgments fall within the observed range of inter-human agreement, while its coverage scores correlate strongly with human assessments of strategic completeness.

## Metadata
- **Published**: 2026-08-04T21:31:01Z
- **Authors**: S. Ashwin Hebbar, Peiyao Sheng, Sewoong Oh, Pramod Viswanath
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04240v1)