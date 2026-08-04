# Summary: 2026-08-03_10-30-56Z_Upper_ExpectileMulti_StepQ_LearningforOff_PolicyRe.md
Saved: 2026-08-04 00:45
Source: 2026-08-03_10-30-56Z_Upper_ExpectileMulti_StepQ_LearningforOff_PolicyRe.md
Model: None

---

## Summary  
Off‑policy reinforcement learning suffers from a pessimistic bias that grows with the planning horizon because multi‑step returns couple each decision to suboptimal logged actions. We introduce Expectile $n$‑step Q‑learning (ENQ), which replaces the symmetric $n$‑step temporal‑difference loss with an asymmetric expectile loss parameterized by a single hyperparameter $\tau$. The proposed operator is proven to be a $\gamma^{n}$‑contraction, guaranteeing that bias vanishes at the optimal action‑value function for covered‑in‑support pairs under deterministic dynamics. In stochastic settings we obtain horizon‑independent two‑sided bounds on the bias. Our method therefore offers a theoretically sound alternative to standard $n$‑step Q‑learning while preserving the speed of multi‑step returns.

## Key Contributions  
- [Finding 1] The Expectile $n$‑step Q‑learning (ENQ) operator provides a $\gamma^{n}$‑contraction, reducing bias with horizon.  
- [Finding 2] Under deterministic dynamics, the bias vanishes at the optimal action‑value function for covered‑in‑support pairs; the fixed point satisfies the separation‑$n$ instance and its multiples of the lower‑bound inequality used by Long‑Horizon Q‑learning (LQL).  
- [Finding 3] In stochastic settings, ENQ bias admits two‑sided bounds with horizon‑independent noise constants.

## Methodology  
The authors address the bias problem by swapping the conventional symmetric $n$‑step TD loss for an asymmetric expectile loss that depends only on $\tau$, leaving $n$ and the backup horizon unchanged. They first prove that the resulting ENQ operator is a $\gamma^{n}$‑contraction, which mathematically limits error propagation. To evaluate the method, they apply a single $\tau=0.8$ across 27 manipulation and navigation task instances with a fixed backup horizon, comparing performance to LQL. A ten‑critic ensemble is also tested in a controlled scaling experiment to assess robustness.

## Results  
ENQ achieves competitive aggregate performance on all 27 tasks, matching or slightly exceeding LQL’s results. Crucially, ENQ demonstrates higher measured training‑step throughput than LQL, indicating faster learning dynamics. In the ten‑critic ensemble experiment, ENQ benefits more from parallelism, showing a larger speedup relative to LQL. Theoretical analysis confirms that bias is bounded and vanishes at $τ=1$, while stochastic bounds remain horizon‑independent.

## Significance  
By decoupling the expectile level $\tau$ from the backup horizon, ENQ offers a principled way to mitigate the horizon‑growing bias of multi‑step Q‑learning without sacrificing its efficiency. The results suggest that off‑policy methods can be made both theoretically sound and practically faster, encouraging further research into asymmetric loss functions for reinforcement learning.

## Related Concepts  
- Multi‑step returns  
- Off‑policy reinforcement learning  
- Expectile loss  
- Temporal difference (TD) error  
- $\gamma^{n}$ contraction  
- Separation‑$n$ instance  
- Long‑Horizon Q‑learning (LQL)  
- Ensemble Q‑learning
