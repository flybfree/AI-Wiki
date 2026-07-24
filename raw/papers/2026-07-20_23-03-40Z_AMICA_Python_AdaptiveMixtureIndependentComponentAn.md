---
title: AMICA-Python: Adaptive Mixture Independent Component Analysis with Anderson Acceleration
published: 2026-07-20T23:03:40Z
authors: Scott Huberty, Christian O'Reilly
url: http://arxiv.org/abs/2607.18568v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AMICA-Python: Adaptive Mixture Independent Component Analysis with Anderson Acceleration

## Abstract
Adaptive Mixture Independent Component Analysis (AMICA) is widely used in EEG research and has long been associated with strong empirical performance for blind source separation. Despite its impact, practical use has historically depended on a single Fortran implementation, accessed via the EEGLAB toolbox for MATLAB, limiting its accessibility for analytical pipelines not designed within the MATLAB ecosystem. Here we present AMICA-Python, a Python implementation of the AMICA algorithm, with a scikit-learn-conformant API designed for integration with existing scientific Python pipelines. The implementation follows the reference algorithm closely while adopting modern software engineering practices and an interface familiar to Python users. Additionally, we introduce an optional Anderson acceleration scheme that can dramatically reduce the time to convergence for this relatively slow algorithm. To evaluate numerical agreement and practical performance, we benchmarked AMICA-Python against the reference Fortran implementation on 14 open EEG recordings. After averaging 3 runs of each implementation on all 14 recordings, AMICA-Python closely matched the reference, with a median final normalized log-likelihoods of 11.572 for both the Fortran and Python implementations, and a negligible median relative absolute difference of only $1.07\times10^{-8}$ when normalized by the absolute Fortran value. Runtime was also competitive. Relative to the reference implementation, AMICA-Python was 17.7\% faster, while the Anderson-accelerated variant was 34.1\% faster. AMICA-Python reproduces the reference implementation to high numerical precision with competitive runtime, while making AMICA available through a more accessible and extensible Python interface.

## Metadata
- **Published**: 2026-07-20T23:03:40Z
- **Authors**: Scott Huberty, Christian O'Reilly
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18568v1)