---
title: On Scope Classification and Current Knowledge-Editing Benchmarks: A Negative Result, with INLAY as a Gradient-Free Case Study
published: 2026-08-26T18:16:24Z
authors: Aditya Pratap Singh
url: http://arxiv.org/abs/2608.26292v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On Scope Classification and Current Knowledge-Editing Benchmarks: A Negative Result, with INLAY as a Gradient-Free Case Study

## Abstract
Every memory-based knowledge editor in the SERAC lineage depends on a scope decision: given a query, does a stored edit apply? We report that current knowledge-editing benchmarks cannot measure this decision at all. Using INLAY, a gradient-free editor we built to obtain exact per-query ground truth (the model is frozen, edits live in an external addressable memory, and applying an edit is a bias added along one token's unembedding direction at decode time), we execute every candidate router action on 1,689 queries spanning three datasets and three input conditions. An oracle router choosing the best action every time ties a one-line static policy to four decimal places in all nine dataset-by-condition cells: the maximum attainable gain of any per-query routing method is 0.00 points. Abstention is the sole winning action zero times out of 1,689. The cause is structural: these are counterfactual benchmarks whose evaluation question asks for the post-edit answer, so answering from parametric knowledge is wrong by construction, and a benchmark without negatives cannot reward a classifier's ability to reject. This generalizes beyond our system to the whole scope-classifier family the benchmarks are used to evaluate. We confirm the mechanism directly: constructing the missing condition ourselves, by withholding a query's own edit from the index for half the sample, moves pooled headroom from exactly +0.0000 to +0.0420 and gives abstention its first wins. We also report where INLAY itself does not win (WISE beats it on Qwen2.5-7B CounterFact, and retrieval-augmented generation beats every method we tested, INLAY included, on rigorously matched RippleEdits), and disclose two bugs found during a self-audit of our own routing machinery, neither of which changed a published headline number outside noise.

## Metadata
- **Published**: 2026-08-26T18:16:24Z
- **Authors**: Aditya Pratap Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.26292v1)