---
title: Depth Enables Local Entropy: Quadratic Depth Dependence in Deep Variation-Norm ReLU Regression
url: http://arxiv.org/abs/2608.17434v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_07-03-14Z_DepthEnablesLocalEntropy_QuadraticDepthDependencei.md
generated_at: 2026-08-18 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates Gaussian regression on an explicit vector‑valued Parhi–Nowak deep‑RBV² architecture characterized by depth L, width w, layer‑sum variation budget A and output bound B. It demonstrates that the minimax risk exhibits a quadratic dependence on depth up to logarithmic factors and is intrinsic under a sample‑size dependent radius condition.

## Key Takeaways
- Quadratic depth dependence is intrinsic: the minimax risk scales as L² w² log(w) R²/n, showing that deeper networks increase risk quadratically.  
- A local packing yields codewords in an O(λ)L² ball with pairwise Ω(λ)-separation, establishing a lower bound of order L² w² log(w) R²/n.  
- Representation‑limited behavior appears at smaller radius; the pseudodimension based finite net provides an upper bound of O~(L² w² R²/n).

## Context
Understanding depth versus width trade‑offs remains central to deep learning research, especially for regression tasks where representation capacity and sample efficiency interact. This work contributes a rigorous minimax analysis that clarifies when deeper architectures provide meaningful gains.

## Implications
For practitioners designing deep regression models, the quadratic scaling warns against unnecessary depth without sufficient data or variation budget. The findings guide efficient model selection and resource allocation in high‑dimensional AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17434v1)
