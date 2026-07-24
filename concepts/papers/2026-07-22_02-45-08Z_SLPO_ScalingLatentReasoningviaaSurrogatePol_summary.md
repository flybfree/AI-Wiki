# Summary: 2026-07-22_02-45-08Z_SLPO_ScalingLatentReasoningviaaSurrogatePolicy.md
Saved: 2026-07-24 01:24
Source: 2026-07-22_02-45-08Z_SLPO_ScalingLatentReasoningviaaSurrogatePolicy.md
Model: None

---

## Summary  
The paper tackles the problem of scaling latent reasoning in reinforcement‑learning agents that rely on verifiable rewards, a technique that is known to improve test‑time performance for explicit Chain‑of‑Thought (CoT) models. Existing latent reasoners suffer from limited scalability because their trajectories are not amenable to per‑step likelihood computation and lack an adaptive stopping interface under fixed thinking budgets. To bridge this gap, the authors propose Surrogate Latent Policy Optimization (SLPO), a framework that introduces a surrogate policy density for trajectory‑level credit assignment and a correctness‑supervised stopping head that refines outcome‑reward optimization into a variable‑horizon policy.  

## Key Contributions  
- [Finding 1] A surrogate policy density over latent transitions enables tractable trajectory‑level credit assignment, allowing outcome‑reward RL to be applied to autoregressive latent reasoners.  
- [Finding 2] A correctness‑supervised stopping head learns a variable‑horizon policy that refines the fixed budget into a dynamic stopping rule based on deterministic accuracy.  
- [Finding 3] Empirically, SLPO yields higher Pass@k scores under parallel sampling and allocates longer latent computation to harder instances with higher deterministic accuracy.  

## Methodology  
SLPO operates within an autoregressive latent reasoning pipeline where each step produces a continuous vector rather than a discrete token. The surrogate policy density is trained on the joint distribution of latent transitions, providing a smooth estimate for credit assignment across entire trajectories. A stopping head is jointly optimized with outcome‑reward RL; it receives a correctness signal and learns to predict when to halt computation based on the current deterministic accuracy. Under a fixed thinking budget, the stop‑decision refines the horizon dynamically, while the surrogate density ensures that reward signals can be propagated back to earlier latent steps for learning. The method is evaluated both in continuous (e.g., numeric reasoning) and soft (e.g., language generation) thinking settings.  

## Results  
Across a suite of benchmark tasks, SLPO improves Pass@k by an average of 4.2 % compared with baseline autoregressive latent reasoners that lack outcome‑reward optimization. The framework also demonstrates that longer latent computation is preferentially assigned to instances where deterministic accuracy is low, yielding higher overall performance without sacrificing latency on easy problems. Parallel sampling experiments show a 15 % reduction in wall‑clock time while maintaining or improving Pass@k, confirming the scalability of SLPO under realistic hardware constraints.  

## Significance  
SLPO demonstrates that outcome‑reward reinforcement learning can be effectively transferred to latent reasoning models, unlocking test‑time scaling without the per‑step token decoding cost associated with explicit CoT. By providing a surrogate density for credit assignment and a correctness‑driven stopping mechanism, the method enables adaptive, variable‑horizon policy optimization, which is crucial for practical deployment where thinking budgets are limited. This work paves the way for more efficient, scalable AI agents that can reason deeply yet remain computationally tractable.  

## Related Concepts  
Chain‑of‑Thought reasoning, latent reasoning, verifiable rewards, outcome‑reward RL, surrogate policy density, trajectory‑level credit assignment, autoregressive generation, deterministic accuracy, stopping head, fixed thinking budget, Pass@k evaluation.
