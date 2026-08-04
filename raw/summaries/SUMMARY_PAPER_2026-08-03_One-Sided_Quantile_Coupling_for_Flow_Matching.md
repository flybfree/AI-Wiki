---
title: One-Sided Quantile Coupling for Flow Matching
url: http://arxiv.org/abs/2608.00978v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_04-03-59Z_One_SidedQuantileCouplingforFlowMatching.md
generated_at: 2026-08-03 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Quantile Coupling Flow Matching (QC-FM) a lightweight one‑sided coupling for continuous‑time flow matching that avoids costly batch transport. By projecting data ranks onto few random directions and mapping them to Gaussian quantiles, the method constructs source samples directly without pairwise cost matrices or assignments. Experiments on CIFAR‑10 CelebA FFHQ ImageNet‑64 show up to 12.9 % lower FID compared with baseline couplings.

## Key Takeaways
- QC-FM eliminates irreducible regression variance along each selected slice by making the ideal flow straight, while keeping the Gaussian prior unchanged.
- The coupling requires only one‑dimensional construction per slice, so there is no pairwise cost matrix and no assignment problem to solve.
- Training uses QC on an anchor subset and fills remaining slots with exact Gaussians, preserving QC bias yet retaining baseline signal.

## Context
Flow matching seeks to generate data distributions by learning velocity fields between a simple source and target. Traditional couplings rely on batch‑wise transport that scales quadratically, limiting scalability for large models. This work offers a simpler alternative that injects geometric bias without solving expensive assignment problems.

## Implications
For practitioners, QC-FM can be integrated into existing FM pipelines with minimal code changes, enabling faster training and higher sample quality. The method’s scalability supports deployment on massive image datasets where batch transport is prohibitive, potentially accelerating research in generative modeling and diffusion‑based synthesis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00978v1)
