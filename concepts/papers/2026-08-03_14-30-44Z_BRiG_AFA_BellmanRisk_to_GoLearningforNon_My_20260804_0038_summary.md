# Summary: 2026-08-03_14-30-44Z_BRiG_AFA_BellmanRisk_to_GoLearningforNon_MyopicAct.md
Saved: 2026-08-04 00:38
Source: 2026-08-03_14-30-44Z_BRiG_AFA_BellmanRisk_to_GoLearningforNon_MyopicAct.md
Model: None

---

## Summary  
Active feature acquisition (AFA) seeks the optimal order of measurements for each test instance when a limited budget is available. While greedy rules are simple to implement, they often ignore features whose value emerges only after later acquisitions, leading to myopic performance. The authors propose **BRiG‑AFA**, a supervised method that learns a separate candidate‑conditioned risk‑to‑go function for every remaining budget and uses Bellman targets to fit these functions backward from the one‑step terminal classification risk. By minimizing this learned terminal risk greedily, BRiG‑AFA achieves non‑myopic acquisition without requiring reinforcement learning or conditional density estimation.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 6 summary/topic terms overlap
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 5 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 4 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Introduces a deployable supervised alternative that learns candidate‑conditioned risk‑to‑go functions for each remaining budget.  
- [Finding 2] Applies Bellman risk regression to compute terminal risk and performs greedy selection using only observed values, mask, candidate identity, and the remaining budget.  
- [Finding 3] Empirical results demonstrate that BRiG‑AFA improves accuracy over its one‑step ablation by 4.84 ± 2.17 percentage points at budget 2 and 4.39 ± 1.10 p.p. at budget 3; on Fashion‑MNIST with 20 candidate pixels it yields a mean paired gain of 3.50 ± 0.37 points across budgets {2,4,8,12,16}.

## Methodology  
The authors start from the one‑step terminal classification risk and iteratively update candidate‑conditioned risk functions using Bellman targets that incorporate the current mask, selected candidate, and remaining budget. The learned functions are then used to evaluate the expected future risk of each possible next measurement. During inference, BRiG‑AFA greedily selects the candidate that minimizes this terminal risk while respecting the observed data and the number of measurements left.

## Results  
In a controlled non‑myopic benchmark, BRiG‑AFA outperforms one‑step methods by 4.84 ± 2.17 p.p. at budget 2 and 4.39 ± 1.10 p.p. at budget 3 (mean ± SE over five seeds). On Fashion‑MNIST with twenty candidate pixels, the method improves accuracy at every reported nontrivial budget, achieving a mean paired gain of 3.50 ± 0.37 points across budgets {2,4,8,12,16}. A three‑seed MiniBooNE study shows mixed results at small budgets but positive gains at 8 and 16 acquisitions, suggesting that the improvement is not universal but emerges beyond a certain acquisition count.

## Significance  
BRiG‑AFA establishes a reproducible mechanism‑level case for direct Bellman risk regression in active feature acquisition, providing a supervised alternative to reinforcement‑learning or generative approaches. By demonstrating consistent non‑myopic gains across multiple datasets and budgets, the work clarifies when such methods are beneficial and guides future state‑of‑the‑art comparisons.

## Related Concepts  
Active feature acquisition (AFA), myopic versus non‑myopic strategies, greedy rules, reinforcement learning, generative active learning, Bellman risk‑to‑go learning, candidate‑conditioned functions, supervised risk regression, terminal risk, risk minimization.
