---
title: XMix: Combating Extremely Noisy Labels via Local Smoothness in Self-Supervised Feature Space
published: 2026-07-26T22:15:23Z
authors: Chengqi Li, Yangdi Lu, Zhihao Shi, Wenbo He, Chamseddine Talhi, Nadjia Kara
url: http://arxiv.org/abs/2607.23865v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# XMix: Combating Extremely Noisy Labels via Local Smoothness in Self-Supervised Feature Space

## Abstract
Supervised deep learning models rely on large, accurately labeled datasets, yet noisy annotations are often unavoidable and can severely degrade performance under high noise levels. Recent state-of-the-art methods tackle this by using sample selection strategies that exploit the memorization effect to filter out clean data for semi-supervised learning. However, these methods struggle with extreme noise, class imbalance, and require careful tuning or prior noise knowledge. To address these limitations, we propose XMix, a novel framework that leverages local smoothness in the self-supervised feature space to systematically enhance all stages of the sample selection process, without dependence on potentially corrupted labels. First, XMix estimates the noise rate using maximum likelihood among self-supervised feature neighbors. Second, these neighbors then help identify additional clean samples and ensure balanced selection across classes during sample selection. Finally, in the semi-supervised learning phase, XMix uses neighboring samples to generate more reliable pseudo-labels. Our empirical results show that XMix substantially outperforms existing methods in extremely noisy environments and maintains superior performance in standard LNL benchmarks.

## Metadata
- **Published**: 2026-07-26T22:15:23Z
- **Authors**: Chengqi Li, Yangdi Lu, Zhihao Shi, Wenbo He, Chamseddine Talhi, Nadjia Kara
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23865v1)