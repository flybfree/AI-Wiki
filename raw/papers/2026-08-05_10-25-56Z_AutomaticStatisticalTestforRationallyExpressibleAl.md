---
title: Automatic Statistical Test for Rationally Expressible Algorithms by Selective Inference, with Applications to Feature Selection
published: 2026-08-05T10:25:56Z
authors: Teruyuki Katsuoka, Tomohiro Shiraishi, Shuichi Nishino, Ichiro Takeuchi
url: http://arxiv.org/abs/2608.04667v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Automatic Statistical Test for Rationally Expressible Algorithms by Selective Inference, with Applications to Feature Selection

## Abstract
Selective inference (SI) provides statistically valid $p$-values for hypotheses selected by applying an algorithm to the data, correcting for the bias that arises when the same data are used both to select and to test a hypothesis. Developing an SI procedure for a new algorithm, however, has required an expert to derive, and then implement, the selection event, i.e., the conditions under which the hypothesis is selected. Repeating this specialized effort for every new algorithm is why exact SI has so far been available for only a narrow class. We propose AutoSI, a framework that removes this barrier in two ways. First, AutoSI constructs the selection event automatically from the algorithm's individual operations, so the user only writes the algorithm as ordinary NumPy-like code and derives nothing by hand. Second, AutoSI broadens the class of selection events SI can handle: existing exact methods are limited to selection events characterized by linear or quadratic inequalities in the data, whereas AutoSI covers any algorithm expressible through rational functions of the data (ratios of polynomials). We prove that the $p$-values computed by AutoSI are exactly valid in finite samples. We demonstrate AutoSI on three feature-selection methods, each written in a few dozen lines of code. One of these methods, the lasso with its tuning parameter selected by cross-validated $R^2$, cannot be handled within existing exact SI frameworks and is made possible by AutoSI. Experiments on synthetic and real datasets show that the resulting $p$-values control the type I error rate (i.e., the false positive rate) at the nominal level while retaining high power.

## Metadata
- **Published**: 2026-08-05T10:25:56Z
- **Authors**: Teruyuki Katsuoka, Tomohiro Shiraishi, Shuichi Nishino, Ichiro Takeuchi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04667v1)