---
title: FinExam-10K: When Retrieval Helps Financial Reasoning?
published: 2026-08-28T10:16:14Z
authors: Yan Lin, Jingyu Sun, Zhongliang Guo, Qing Li, Zhuohan Xie, Yuxia Wang
url: http://arxiv.org/abs/2608.28155v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FinExam-10K: When Retrieval Helps Financial Reasoning?

## Abstract
Professional financial examinations require models to combine domain knowledge, calculation, and judgment, yet no benchmark covers the full CFA and FRM structure under one protocol. We introduce FinExam-10K, to our knowledge the largest reported English benchmark for this setting, with 10,198 expert-reannotated questions spanning CFA Levels I-III and FRM Parts I-II. We release 5,110 questions and sequester 5,088 for a quarterly maintained leaderboard. To separate coverage from local answerability, we report a 10,198-item Full-Coverage Track and a 7,625-item Context-Complete Reasoning Track, which is the primary basis for claims about reasoning from the supplied record. Across 17 models, the best accuracy is 85.29% overall. On the frozen Hard band, the best score is 34.68% on the Full-Coverage Track and 54.57% on the 372 context-complete items. All 17 models share 47 context-complete failures. Function-RAG and FunctionGraph-RAG rescue hundreds of errors but also overturn many correct answers, producing little or negative net gain. A gate trained only on public data decides from the question and initial response when FunctionGraph-RAG should run. On the 5,088 held-out items, the gate invokes FunctionGraph-RAG for 7.9% of questions and improves accuracy from 70.83% to 71.23% (p = .0446).

## Metadata
- **Published**: 2026-08-28T10:16:14Z
- **Authors**: Yan Lin, Jingyu Sun, Zhongliang Guo, Qing Li, Zhuohan Xie, Yuxia Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28155v1)