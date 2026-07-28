---
title: BettiSplit: Topology-Guided Privacy-Aware Split Learning Against Feature Inversion and Gradient Leakage
published: 2026-07-27T15:29:49Z
authors: Akarsh K. Nair, Muhammad Arifur Rahman, David Brown, Mufti Mahmud
url: http://arxiv.org/abs/2607.24556v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BettiSplit: Topology-Guided Privacy-Aware Split Learning Against Feature Inversion and Gradient Leakage

## Abstract
Split learning enables collaborative model training by partitioning neural networks across clients and servers. However, improper split placement can lead to severe privacy leakage through intermediate representations. In this work, we propose a topology-guided framework for privacy-aware split learning based on the persistent Betti complexity of smashed activations. Through comprehensive layer-wise analysis, we show that privacy risk in split learning is highly non-uniform across layers and exhibits sharp transition regions that are not captured by architectural depth alone. In particular, feature inversion fidelity increases from negligible reconstruction to as high as 0.98 SSIM at deeper, privacy-critical split points. We further demonstrate that Betti complexity consistently identifies representation regimes associated with elevated feature-space privacy leakage across architectures and datasets. Leveraging this observation, we introduce BettiSafe, a topology-guided split selection strategy that identifies privacy-sensitive layers without requiring explicit attack execution. BettiSafe improves resistance to feature inversion by 2 to 5 times compared to depth-based heuristics while preserving classification accuracy. In addition, Betti-based regularisation increases inversion difficulty by nearly 5 x without degrading model utility, enabling a favourable privacy utility tradeoff. Overall, our results highlight topological complexity as a promising structural descriptor for secure, adaptive, and representation-aware split learning in real-world collaborative systems

## Metadata
- **Published**: 2026-07-27T15:29:49Z
- **Authors**: Akarsh K. Nair, Muhammad Arifur Rahman, David Brown, Mufti Mahmud
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24556v1)