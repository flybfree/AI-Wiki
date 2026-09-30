---
title: Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling
published: 2026-09-28T14:57:53Z
authors: Mohamed Eltahir, Abobaker Ahmed, Nawaf Barebood, Hussain Bu Subayt, Tanveer Hussain, Naeemullah Khan
url: http://arxiv.org/abs/2609.37494v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Your Benchmark Is Not Saturated: Reviving Multiple-Choice Evaluation with Answer Pooling

## Abstract
Multiple-choice benchmarks are cheap to grade and are running out of room, and the standard remedy, writing harder items, is slow and repeated for every benchmark. A saturated benchmark still holds a harder task. Each question's wrong options are written for that question alone, so a model can score by eliminating a few options. We propose AnswerPool: take $N$ questions that share a context, pool all their options into one list, and ask the model to assign every question its answer. No item is written and no label changes. The chance of guessing a group right falls from $10^{-3}$ to $5\times10^{-7}$ for five four-option questions, and a model that recognizes its answers keeps its multiple-choice score, so the accuracy lost to pooling measures the credit the format gave for elimination. Deleting answers from the pool makes questions unanswerable with exact ground truth, so abstention is scored in the same pass. Across eight text, image, and video benchmarks and eighteen models, pooling is harder for every model, the elimination credit is largest for the weakest models, and seven of eight open-weight models answer 87 to 100% of unanswerable questions.

## Metadata
- **Published**: 2026-09-28T14:57:53Z
- **Authors**: Mohamed Eltahir, Abobaker Ahmed, Nawaf Barebood, Hussain Bu Subayt, Tanveer Hussain, Naeemullah Khan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37494v1)