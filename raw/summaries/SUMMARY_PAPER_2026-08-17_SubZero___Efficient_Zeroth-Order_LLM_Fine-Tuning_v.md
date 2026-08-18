---
title: SubZero+: Efficient Zeroth-Order LLM Fine-Tuning via Large Learning Rates
url: http://arxiv.org/abs/2608.15665v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_10-13-25Z_SubZero__EfficientZeroth_OrderLLMFine_TuningviaLar.md
generated_at: 2026-08-17 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
SubZero+ addresses the instability of zeroth-order fine‑tuning by introducing a multi‑query gradient estimator that operates within low‑rank subspaces, an adaptive subspace Adam optimizer, and a sign correction for QR construction to guarantee Haar‑distributed projection matrices. The method stabilizes convergence across models from 1.3 B to 32 B parameters, expands the usable learning‑rate range, and narrows performance gaps with first‑order techniques while keeping memory overhead low.

## Key Takeaways
- Multi‑query gradient estimation within layer‑specific low‑rank subspaces reduces variance without triggering the multi‑query paradox.  
- The subspace Adam optimizer uses these in‑subspace statistics to perform adaptive updates, improving stability across varying learning rates.  
- A sign correction for QR‑based subspace construction ensures Haar‑distributed projection matrices, eliminating orientation ambiguity that previously caused implementation issues.

## Context
Zeroth‑order optimization promises backpropagation‑free fine‑tuning of massive language models, yet variance in gradient estimators hampers practical deployment. SubZero+ tackles this by combining low‑rank subspace analysis with adaptive optimisation and robust matrix construction, offering a viable alternative to full‑parameter or LoRA tuning.

## Implications
For practitioners, SubZero+ enables efficient fine‑tuning of large models without sacrificing stability, accelerating research cycles and reducing hardware costs. The framework’s scalability across model sizes suggests broader adoption in industry pipelines where rapid iteration is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15665v1)
