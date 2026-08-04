# Summary: 2026-08-03_06-10-33Z_TowardPlasticity_PreservingKLRegularizationforCapa.md
Saved: 2026-08-03 23:41
Source: 2026-08-03_06-10-33Z_TowardPlasticity_PreservingKLRegularizationforCapa.md
Model: None

---

## Summary  
This paper addresses a critical challenge in large language model (LLM) reinforcement learning: the trade-off between preserving existing capabilities and improving performance on new tasks through post-training optimization. Standard KL regularization methods often impose overly restrictive constraints that can degrade prior knowledge, leading to capability loss. The authors introduce CoKL—a conditional regularization framework—that selectively preserves correct responses while minimizing interference with exploration and task-specific learning. By narrowing the preservation constraint from full output distributions to correctness-conditioned ones, CoKL enables more efficient and effective post-training adaptation without sacrificing robustness.

## Key Contributions  
- [Finding 1] CoKL decouples the total probability assigned to correct responses from their conditional distribution, allowing regularization of relative probability allocation among reference-supported correct outputs without anchoring incorrect outputs or total correctness mass.  
- [Finding 2] The framework uses forward KL divergence with a finite-group training objective, providing a practical implementation for RL-based LLM post-training that avoids the strict optimal correctness gap limitation of full-policy regularization when the reference policy is imperfect.  
- [Finding 3] CoKL achieves superior balance between target-task improvement and prior-capability retention across multiple model scales in continual learning settings, outperforming both forward and reverse KL regularization.

## Methodology  
The authors propose a conditional regularization approach that focuses only on the distribution of correct responses under specific conditions, rather than constraining the entire policy output. By conditioning the KL constraint on correctness, CoKL allows the model to allocate probability mass freely among incorrect or uncertain outputs while still ensuring that correct responses remain appropriately prioritized relative to each other. The training objective is derived from forward KL divergence applied to these conditioned distributions, resulting in a finite-group formulation suitable for RL environments with discrete action spaces. This design enables the model to maintain exploration and adaptability while preserving core capabilities.

## Results  
Experiments conducted in controlled multi-solution environments and continual post-training settings across various LLM scales demonstrate that CoKL significantly outperforms existing regularization methods. Specifically, CoKL maintains higher retention of prior knowledge compared to full-policy forward and reverse KL regularization, which often induce an optimal correctness gap when the reference policy is imperfect. In tasks requiring both task adaptation and capability preservation, CoKL achieves higher cumulative reward without significant degradation in original performance. The results show that conditional constraints are more effective than unconditional ones for maintaining plasticity while ensuring correctness.

## Significance  
This work advances the field of LLM post-training by introducing a nuanced regularization strategy that respects both exploration and capability retention. By avoiding the pitfalls of overly restrictive KL methods, CoKL enables safer and more efficient adaptation in real-world applications where model stability is critical. The approach supports continual learning without catastrophic forgetting, making it valuable for deployment scenarios involving multiple task cycles.

## Related Concepts  
- Reinforcement Learning (RL)  
- Large Language Models (LLMs)  
- Post-training Optimization  
- KL Regularization  
- Forward and Reverse KL Divergence  
- Capability Retention  
- Plasticity-Preserving Methods  
- Conditional Distributions
