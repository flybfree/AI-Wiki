---
title: FairLMs: A Turnkey Library for Fairness in Language Models
published: 2026-09-18T04:11:40Z
authors: Jiale Zhang, Michael Larionov, Zichong Wang, Zhipeng Yin, Wenbin Zhang
url: http://arxiv.org/abs/2609.21296v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FairLMs: A Turnkey Library for Fairness in Language Models

## Abstract
Fairness research on language models involves measuring bias, applying mitigation methods, and examining the evidence on which an evaluation rests. Existing tools offer complementary functionality through different interfaces, so combining them requires reconciling model interfaces, evidence formats, access constraints, and result types before applicability can be checked or methods compared. We introduce \textbf{FairLMs}, a Python library that connects these activities through explicit declarations of model capabilities and input requirements. It provides 33 intrinsic and extrinsic metrics, 14 mitigation components spanning four intervention categories, 14 dataset and scoring-instrument diagnostics, adapters for the three Transformer architectures and supported hosted completion APIs, and benchmark loaders. Declarations are checked before execution and results carry the configuration under which they were obtained, so that compatible components can be combined, methods compared under a common protocol, and workflows extended to new models and datasets. The source code is available at: https://github.com/FairLMs/FairLMs.

## Metadata
- **Published**: 2026-09-18T04:11:40Z
- **Authors**: Jiale Zhang, Michael Larionov, Zichong Wang, Zhipeng Yin, Wenbin Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21296v1)