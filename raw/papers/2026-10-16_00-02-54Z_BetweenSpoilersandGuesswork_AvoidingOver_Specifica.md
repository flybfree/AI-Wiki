---
title: Between Spoilers and Guesswork: Avoiding Over-Specification in Coding Benchmarks
published: 2026-10-16T00:02:54Z
authors: Yuanzhe Liu, Bastian Lipka, Avraham Shinnar, Jatin Ganhotra, Yao Ma, Martin Hirzel
url: http://arxiv.org/abs/2610.22760v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Between Spoilers and Guesswork: Avoiding Over-Specification in Coding Benchmarks

## Abstract
Benchmarks drive AI progress, but are hampered by task under-specification and over-specification. Task under-specification causes guesswork, where solutions have to make things up, or worse, resort to contamination or reward hacking. Task over-specification causes spoilers, where solutions can bypass some of the harder steps the benchmark was supposed to measure. Since future-looking benchmarks should be difficult, over-specification reduces a benchmark's shelflife of community adoption. Repository-level coding benchmarks have helped the field progress but experience unnecessary churn due to both over- and under-specification. For instance, SWE-bench Pro, FEA-bench, Doc2Feat-bench, and Multi-SWE-bench all tackle under-specification by augmenting task statements with hints derived from ground truth. We show that leaking ground-truth information into the task statement causes over-specification in some of these benchmarks. We experiment with various specification levels, trying to thread the needle between spoilers and guesswork. Based on these results, we recommend techniques for deriving parsimonious hints. We will release our hints so the community can obtain more reliable signals from popular benchmarks.

## Metadata
- **Published**: 2026-10-16T00:02:54Z
- **Authors**: Yuanzhe Liu, Bastian Lipka, Avraham Shinnar, Jatin Ganhotra, Yao Ma, Martin Hirzel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.22760v1)