---
title: Less Is More: Tuning Configurable Systems with Imperfect Fidelity
published: 2026-08-01T16:42:51Z
authors: Yulong Ye, Miqing Li, Tao Chen
url: http://arxiv.org/abs/2608.00759v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Less Is More: Tuning Configurable Systems with Imperfect Fidelity

## Abstract
Configuration tuning is essential for optimizing the performance of highly configurable systems, e.g., throughput or runtime, under a given environment. Yet, this is a challenging process as there can be many options to tune, and configuration measurement is often highly expensive. In this paper, we demonstrate the phenomenon of ``less can be more'': system configuration tuning can be greatly improved with much superior budget utilization by partially tuning under the imperfect-fidelity---an environment that is similar, but cheaper to measure, compared with the concerned perfect-fidelity of environment under which the system should be tuned. We codify a conceptual framework of fidelity for configurable systems, drawing on which allows us to propose MFTune, a tuner that proactively explores in the space of $>10^4$ possible imperfect-fidelity settings to approximate a useful one, which strikes for the wideness of tuning. This creates high-quality seeds for the perfect-fidelity, which in turn ensures the tuning depth. Experiment results against $10$ state-of-the-art tuners, obtained from running diverse real-world systems for $19$ months $24 \times 7$, show that MFTune performs considerably better on $83.33$\% cases with up to $19.34\%$ improvement while achieving hours of budget saving in general.

## Metadata
- **Published**: 2026-08-01T16:42:51Z
- **Authors**: Yulong Ye, Miqing Li, Tao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00759v1)