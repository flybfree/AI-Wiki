---
title: Fairness-Aware Test-Time Prompt Tuning
published: 2026-08-26T12:26:18Z
authors: Yoann Launay, Parameswaran Kamalaruban, Tom Kempton, Stuart Burrell, David Sutton
url: http://arxiv.org/abs/2608.25707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fairness-Aware Test-Time Prompt Tuning

## Abstract
Vision-language models have displayed remarkable capabilities in multi-modal understanding and are increasingly used in critical applications where economic and practical deployment constraints prohibit re-training or fine-tuning. However, these models can also exhibit systematic biases that disproportionately affect protected demographic groups and existing approaches to addressing these biases require extensive model retraining and access to demographic attributes. There is a clear need to develop test-time adaptation (TTA) approaches that improve the fairness characteristics of pretrained models under distributional shift. In this paper, we evaluate how episodic TTA affects fairness in CLIP classification under subpopulation shifts and develop FairTPT, a novel fairness-aware episodic TTA method that jointly minimizes target marginal entropy while maximizing spurious marginal entropy through soft-prompt tuning. We find that standard episodic TTA generally exacerbates disparities between majority and minority groups, that blinding a model to spurious attributes without degrading target performance is inherently challenging, and that excessive blinding can lead to catastrophic forgetting. This model collapse can be prevented by monitoring test-time changes in target loss within the linear regime, while still achieving fairness improvements on reactive data and preserving overall performance. FairTPT outperforms all state-of-the-art episodic test-time debiasing methods and establishes a foundation for robust TTA, which is essential for achieving fairness in practice.

## Metadata
- **Published**: 2026-08-26T12:26:18Z
- **Authors**: Yoann Launay, Parameswaran Kamalaruban, Tom Kempton, Stuart Burrell, David Sutton
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25707v1)