---
title: Training-Free Universal Approximation by Prompting Random Transformers
url: http://arxiv.org/abs/2608.09558v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_12-57-22Z_Training_FreeUniversalApproximationbyPromptingRand.md
generated_at: 2026-08-10 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how expressive a transformer can be when pretraining is omitted, showing that random weights guided by soft prompts can approximate any Hölder function on a compact manifold. It constructs explicit soft prompts as solutions to linear systems that align attention logits with Gaussian kernel exponents, enabling the frozen network to emulate a Nadaraya‑Watson estimator and achieve universal approximation with minimax‑optimal rates.

## Key Takeaways
- A single‑layer transformer with untrained random weights can approximate any Hölder function when steered by an appropriate soft prompt.  
- The constructed prompts solve linear systems that match attention logits to Gaussian kernel exponents, linking the model to classical kernel regression.  
- Theoretical guarantees of optimal rates depend on the intrinsic dimension and hold under mild rank conditions satisfied almost surely with Gaussian initialization.

## Context
This work bridges approximation theory and transformer architecture by demonstrating that prompting can substitute pretraining for expressive power. It highlights a theoretical pathway where inference‑time prompts generate model behavior, reducing reliance on large pre‑training datasets.

## Implications
For practitioners, this suggests that task‑specific performance may be achieved with lightweight prompt engineering rather than costly weight updates. Industry adoption could lower the barrier to deploying transformer models in low‑resource settings while preserving strong approximation guarantees.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09558v1)
