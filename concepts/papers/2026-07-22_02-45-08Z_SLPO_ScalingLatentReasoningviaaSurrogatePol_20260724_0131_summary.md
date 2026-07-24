# Summary: 2026-07-22_02-45-08Z_SLPO_ScalingLatentReasoningviaaSurrogatePolicy.md
Saved: 2026-07-24 01:31
Source: 2026-07-22_02-45-08Z_SLPO_ScalingLatentReasoningviaaSurrogatePolicy.md
Model: None

---

## Summary  
The paper proposes Surrogate Latent Policy Optimization (SLPO) to enable outcome‑reward reinforcement learning on latent reasoning models, overcoming the computational bottleneck of decoding intermediate tokens. It demonstrates that latent reasoners can achieve test‑time scaling without token‑level decoding while still benefiting from outcome‑reward optimization.  

## Key Contributions  
- [Finding 1] Latent reasoners can achieve test‑time scaling without token‑level decoding, reducing the cost of scaling.  
- [Finding 2] A surrogate policy density over latent transitions enables trajectory‑level credit assignment for outcome‑reward optimization.  
- [Finding 3] A correctness‑supervised stopping head refines outcome‑reward optimization into a variable‑horizon policy that adapts to thinking budgets.  

## Methodology  
The authors adopt a two‑stage approach: first they learn a surrogate policy density that maps latent transitions to probability distributions, allowing trajectory‑level credit assignment; second, they introduce a correctness‑supervised stopping head that refines the reward signal into a variable‑horizon policy that can allocate thinking time dynamically. This design integrates outcome‑reward RL with autoregressive latent generation and provides an adaptive interface for fixed‑budget reasoning.  

## Results  
Experimental results show that SLPO improves Pass@k scores across both continuous and soft thinking tasks when sampled in parallel. Moreover, the method allocates longer latent computation to harder instances, yielding higher deterministic accuracy than baseline methods.  

## Significance  
This work matters because it reduces the cost of scaling reasoning models from per‑token decoding to efficient latent operations, enabling large‑scale deployment while preserving alignment with outcome rewards and supporting adaptive, variable‑horizon training schedules.  

## Related Concepts  
Latent reasoning, Chain-of-Thought prompting, verifiable reward functions, surrogate policy density, outcome‑reward RL, variable‑horizon policies, Pass@k evaluation metric.
