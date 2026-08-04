---
title: Averaging Bias: Human Faithfulness Annotations are not Locally Faithful
published: 2026-07-31T18:39:28Z
authors: Huajian Zhang, Yiyang Feng, Jiawei Zhou
url: http://arxiv.org/abs/2608.00205v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Averaging Bias: Human Faithfulness Annotations are not Locally Faithful

## Abstract
Evaluation of faithfulness of text summarization treats a model generated summary as faithful only if every of its sentences is supported by the source document: a strict conjunctive rule under which a single unsupported sentence makes the whole summary unfaithful. Yet most faithfulness benchmarks collect only one global human annotation label per summary. We ask whether such global human labels actually implement the conjunctive rule. We hypothesize that annotators may accept a summary as faithful when most sentences are faithful, not only when all are faithful. To test our hypothesis, we use five large language model (LLM) judges as per-sentence raters across four widely used faithfulness benchmarks. We find that global human labels correlate better with the average of per-sentence LLM judgments than with the implementation of the strict conjunctive rule. A manual review confirms that a substantial fraction of summaries labeled faithful by humans contain genuine local factual errors. We call this tendency Averaging Bias. Our results reveal that human labels on widely used faithfulness benchmarks contain measurable Averaging Bias, calling for carefully structured designs for trustworthy human annotations

## Metadata
- **Published**: 2026-07-31T18:39:28Z
- **Authors**: Huajian Zhang, Yiyang Feng, Jiawei Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00205v1)