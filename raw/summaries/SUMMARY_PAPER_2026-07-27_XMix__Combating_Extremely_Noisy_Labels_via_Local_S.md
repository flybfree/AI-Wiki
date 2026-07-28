---
title: XMix: Combating Extremely Noisy Labels via Local Smoothness in Self-Supervised Feature Space
url: http://arxiv.org/abs/2607.23865v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_22-15-23Z_XMix_CombatingExtremelyNoisyLabelsviaLocalSmoothne.md
generated_at: 2026-07-27 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
XMix tackles the problem of extremely noisy labels in supervised deep learning by leveraging local smoothness within a self‑supervised feature space. The framework estimates noise rates from neighbor features, identifies clean samples across classes, and generates reliable pseudo‑labels during semi‑supervised training. Experiments show XMix outperforms existing methods both in extreme noise scenarios and on standard LNL benchmarks.

## Key Takeaways
- XMix uses maximum likelihood among self‑supervised feature neighbors to estimate the true noise rate without relying on corrupted labels, providing an objective measure of label quality.  
- The same neighbor set helps locate additional clean samples, ensuring balanced selection across classes and mitigating class imbalance issues.  
- During semi‑supervised learning, XMix employs neighboring pseudo‑labels to produce more reliable targets, thereby improving the overall training signal.

## Context
Self‑supervised feature spaces are increasingly used to obtain auxiliary supervision when labeled data are scarce or noisy. However, most approaches either ignore extreme noise levels or require manual tuning of noise parameters, limiting their robustness in real‑world applications where label errors can be severe and class distributions uneven.

## Implications
XMix offers a practical solution that can be integrated into existing semi‑supervised pipelines without additional hardware constraints, making it accessible to industry practitioners. By systematically enhancing sample selection through local smoothness, the method improves model generalization even when labels are severely corrupted, fostering more reliable AI systems in noisy environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23865v1)
