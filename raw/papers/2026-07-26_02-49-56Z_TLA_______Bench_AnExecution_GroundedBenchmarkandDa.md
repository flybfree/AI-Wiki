---
title: TLA$^{+}$-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA+ Specification Generation
published: 2026-07-26T02:49:56Z
authors: Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari, Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad
url: http://arxiv.org/abs/2607.23425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TLA$^{+}$-Bench: An Execution-Grounded Benchmark and Dataset for Natural-Language to TLA+ Specification Generation

## Abstract
Large language models increasingly write TLA$^{+}$ formal specifications from natural-language descriptions, but progress is hard to measure: existing resources grade by resemblance to a reference or by whether the output parses, neither of which shows correctness. We present TLA$^{+}$-Bench, a dataset and benchmark that grades by execution. Every gold specification ships a configuration the TLA$^{+}$ model checker runs over the full reachable state space, deciding exactly whether the specification holds the properties that configuration names. The dataset holds 403 model-checked gold and 897 parse-only silver specifications from 13 public repositories, subsumes prior TLA$^{+}$ generation data, and carries four model-written descriptions in two styles from two providers, with difficulty and category labels. Our main finding is about measurement itself: an exact oracle gives not one correctness number but a range. Varying only the grading choices earlier benchmarks leave unstated, on one fixed set of model outputs, the correct rate moves sixfold, from 10.0\% to 1.7\%; adding the interface-supply choice, where the model is told the configuration's names, widens the range to elevenfold, from 18.7\% to 1.7\%. We call this range the correctness envelope and measure each of its bounds. The findings inside it are stable. Every model writes valid TLA$^{+}$ far more often than correct TLA$^{+}$: the strongest is correct 16\% of the time by default and 26\% when given the interface names, open models at most 1\%, and correctness falls sharply with difficulty.

## Metadata
- **Published**: 2026-07-26T02:49:56Z
- **Authors**: Arslan Bisharat, Eric Spencer, Brian Ortiz, Khushboo Bhadauria, Mujtaba Nazari, Beatriz Santos, Anisa Ramos, TaiNing Wang, George K. Thiruvathukal, Konstantin Läufer, Mohammed Abuhamad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23425v1)