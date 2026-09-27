---
title: Beyond Average Safety: Chance-Constrained LLM Fine-tuning
url: http://arxiv.org/abs/2609.29960v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-24_15-17-58Z_BeyondAverageSafety_Chance_ConstrainedLLMFine_tuni.md
generated_at: 2026-09-27 16:17
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces a chance-constrained formulation for fine-tuning large language models that explicitly limits the fraction of examples where safety degradation relative to a reference model exceeds a prescribed threshold, addressing the limitation of average-risk methods that obscure rare but severe failures. By employing a differentiable majorization of the violation rate and a constraint-aware gradient descent update with a closed form, the method ensures tail-aware safety preservation while maintaining feasibility in parameter space. Extensive experiments demonstrate that this approach consistently outperforms existing baselines across multiple tasks and models, establishing safety preservation as a reliability-constrained optimization problem rather than simple regularization.

## Key Takeaways
- Existing safety-preserving fine-tuning techniques typically control average safety loss or use weighted auxiliary penalties, which can fail to prevent rare but critical safety regressions; the authors propose a chance-constrained approach that directly limits the proportion of examples where safety performance drops below a specified threshold relative to a reference model.
- To make the empirical chance constraint tractable despite its discontinuous indicator function, the work introduces a differentiable majorization of the violation rate, creating a conservative yet computationally

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.29960v1)
