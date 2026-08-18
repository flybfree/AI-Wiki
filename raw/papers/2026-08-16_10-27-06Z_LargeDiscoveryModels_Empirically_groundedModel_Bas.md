---
title: Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search
published: 2026-08-16T10:27:06Z
authors: Zhongwei Yu, Yan Song, Xue Yan, Anjie Liu, Xingyu Lu, Yihang Chen, Huichi Zhou, Siyuan Guo, Luoyang Sun, Sihan Chen, Xiangning Yu, Jun Wang
url: http://arxiv.org/abs/2608.15669v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Large Discovery Models: Empirically-grounded Model-Based Open-Ended Search

## Abstract
Scientific discovery often involves optimising expensive-to-evaluate objectives over vast, structured, and open-ended hypothesis spaces, such as molecules, protein sequences, and computer programs. Generative models such as large language models (LLMs) provide expressive priors over such spaces, but their likelihoods and self-assessments are unreliable proxies for the objectives and calibrated epistemic uncertainty, especially for novel candidates outside the observed data distribution. We introduce the Large Discovery Model (LDM), an empirically grounded recurrent architecture that couples a generative model with a Bayesian non-parametric reward surrogate model. The generative model proposes and refines candidate designs, while the surrogate predicts their performance and quantifies uncertainty, yielding an uncertainty-aware value that guides candidate generation, refinement, and selection. The discovery memory and the surrogate model are continually updated as each new experimental observation arrives. We evaluate LDM on three scenarios spanning different design modalities and objectives, including neural-network training, antibody design, and molecular optimisation. Compared to LLM-only reflection or traditional statistical search across these domains, LDM achieves a $2.4\times$ greater reduction in validation BPB, an $18.2\%$ relative decrease in binding energy, and more than $60\%$ relative gains in molecular multi-objective performance. These results suggests that LDM could serve as a general-purpose discovery engine for effective search over open-ended hypothesis spaces.

## Metadata
- **Published**: 2026-08-16T10:27:06Z
- **Authors**: Zhongwei Yu, Yan Song, Xue Yan, Anjie Liu, Xingyu Lu, Yihang Chen, Huichi Zhou, Siyuan Guo, Luoyang Sun, Sihan Chen, Xiangning Yu, Jun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15669v1)