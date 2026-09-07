---
title: Train What You Deploy:Token-Faithful Post-Training of a Production Coding
published: 2026-09-04T03:11:09Z
authors: Cheng Li, Jiexiong Liu, Yixuan Chen, Chi Hong
url: http://arxiv.org/abs/2609.04678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Train What You Deploy:Token-Faithful Post-Training of a Production Coding

## Abstract
Existing post-training pipelines for coding and terminal agents suffer severe token and control fidelity errors: simplified training environments mismatch production deployments, and offline token reconstruction from agent logs distorts original prompts and conflates policy calls with background model operations. We present a fidelity-aware training coupling framework that retains trainer-side sampling over original prompts, eliminates spurious model calls via a negotiated training protocol, and restricts loss computation to verifiable token spans with closed-failure guarantees. We further propose Certified Divergence Proximal Policy Optimization (C-DPPO), which establishes tight two-sided TV certification bounds, adaptive-K rules, budget-aware sequence guarantees, and error-robust policy masking atop standard DPPO. Evaluated on matched Baize5B and Baize10B models with identical training and test protocols on TMax-100, C-DPPO yields a consistent +3.0-point performance gain over standard DPPO across model scales. Certificate audits validate the reliability and full operational coverage of our certified training pipeline.

## Metadata
- **Published**: 2026-09-04T03:11:09Z
- **Authors**: Cheng Li, Jiexiong Liu, Yixuan Chen, Chi Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04678v1)