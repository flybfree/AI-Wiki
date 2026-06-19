---

title: "Summary: Vector Policy Optimization: Training for Diversity Improves Test-Time Search"
url: http://arxiv.org/abs/2605.22817v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-21_17-59-26Z_VectorPolicyOptimization_TrainingforDiversityImpro.md
generated_at: "2026-06-11 10:45"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces Vector Policy Optimization VPO, a method that replaces the standard GRPO advantage estimator with an approach that trains language models to generate diverse solution sets aligned with multiple vector-valued reward functions. Experiments across four tasks show VPO matches or exceeds scalar RL baselines on test‑time search metrics such as pass@k and best@k, especially when search budgets are large.

## Key Takeaways
- VPO explicitly optimizes for diversity by training the model to output a set of solutions that each specialize in different trade‑offs across vector reward dimensions.  
- The algorithm works as a drop‑in replacement for GRPO and improves test‑time performance, widening the gap between VPO and scalar RL baselines as search depth increases.  
- For evolutionary search tasks, VPO enables models to solve problems that GRPO cannot handle at all.

## Context
Current large language model post‑training optimizations focus on a single scalar reward, which often reduces output entropy and limits adaptability to diverse downstream tasks. Inference‑time search pipelines like AlphaEvolve rely on generating varied rollouts, making diversity a crucial design goal that is currently underserved by standard RL methods.

## Implications
Optimizing for vector‑valued rewards could become the default objective as AI systems are deployed in multi‑purpose applications where diverse solutions are needed. Practitioners may need to adopt VPO or similar techniques to ensure models produce task‑specific diversity without sacrificing overall performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.22817v1)
