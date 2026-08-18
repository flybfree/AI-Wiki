---
title: Toward Optimal Second-Order Path-Length Guarantee for Adversarial Multi-Armed Bandits
published: 2026-08-17T01:17:42Z
authors: Mengxiao Zhang
url: http://arxiv.org/abs/2608.15996v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Toward Optimal Second-Order Path-Length Guarantee for Adversarial Multi-Armed Bandits

## Abstract
We study second-order path-length regret in adversarial $K$-armed bandits against oblivious loss sequences. Bubeck et al. [2019] designed an algorithm that achieves $\widetilde{\mathcal{O}}(K+\sqrt{KQ_{\infty,1}})$ regret, where $Q_{\infty,1}$ is the first-order path length, and left open whether $\widetilde{\mathcal{O}}(\text{poly}(K)\sqrt{1+Q_{\infty,2}})$ regret is achievable under bandit feedback, where $Q_{\infty,2}$ is the second-order path length. Somewhat surprisingly, we resolve this question positively by showing that with a more involved analysis, the exact same algorithm of Bubeck et al. [2019] achieves $\mathcal{O}\left(K\log(KT)+\sqrt{K\log(KT)\bigl(1+Q_{\infty,2}\bigr)}\right)$ expected regret when $Q_{\infty,2}$ is known, where $T$ is the horizon. This matches the $Ω(\sqrt{KQ_{\infty,2}})$ lower bound up to logarithmic factors and additive terms. We further remove the knowledge of $Q_{\infty,2}$ using an adaptive restart scheme whose path-length estimator has uniformly bounded increments.

## Metadata
- **Published**: 2026-08-17T01:17:42Z
- **Authors**: Mengxiao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15996v1)