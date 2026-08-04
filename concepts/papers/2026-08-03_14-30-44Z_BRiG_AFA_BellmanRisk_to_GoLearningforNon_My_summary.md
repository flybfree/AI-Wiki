# Summary: 2026-08-03_14-30-44Z_BRiG_AFA_BellmanRisk_to_GoLearningforNon_MyopicAct.md
Saved: 2026-08-04 00:03
Source: 2026-08-03_14-30-44Z_BRiG_AFA_BellmanRisk_to_GoLearningforNon_MyopicAct.md
Model: None

---

## Summary  
The paper proposes BRiG‑AFA, a supervised active feature acquisition method that learns a candidate‑conditioned risk‑to‑go function for each remaining budget using Bellman targets, thereby avoiding the myopic bias of greedy rules. By fitting these functions backward from terminal classification risk and then greedily selecting the next measurement to minimize the learned risk, BRiG‑AFA achieves non‑myopic performance without requiring complex reinforcement‑learning or generative models. The authors demonstrate that this approach consistently improves test accuracy over one‑step baselines across a range of budgets on benchmark datasets.  

## Key Contributions  
- [Finding 1] A deployable, supervised risk‑to‑go learner that conditions on the candidate feature and remaining budget, eliminating the need for complex RL or density estimation.  
- [Finding 2] The use of Bellman targets to fit candidate‑conditioned risk functions, enabling a greedy selection that minimizes observed terminal risk.  
- [Finding 3] Empirical evidence that BRiG‑AFA yields measurable accuracy gains (e.g., +4.84 ± 2.17 pp at budget 2) compared to one‑step baselines on non‑myopic benchmarks.  

## Methodology  
BRiG‑AFA builds a separate risk‑to‑go model for each candidate feature and each possible remaining acquisition budget. The terminal classification risk is used as the base, and Bellman targets recursively propagate backward through the acquisition sequence. During inference, only observed values, the current mask of unobserved features, the selected candidate identity, and the remaining budget are available; the algorithm greedily picks the measurement that minimizes the learned terminal risk. This process repeats until the budget is exhausted, producing a non‑myopic acquisition plan.  

## Results  
On the controlled non‑myopic benchmark, BRiG‑AFA improves accuracy by 4.84 ± 2.17 percentage points at two acquisitions and by 4.39 ± 1.10 points at three acquisitions (mean ± SE over five seeds). Across Fashion‑MNIST with twenty candidate pixels, the method gains an average of 10.20 ± 0.74 points after four acquisitions, with a mean paired gain of 3.50 ± 0.37 points across budgets {2,4,8,12,16}. A three‑seed MiniBooNE study shows positive gains at eight and sixteen acquisitions, suggesting the method’s effectiveness grows with budget size.  

## Significance  
BRiG‑AFA provides a reproducible mechanism‑level case for direct Bellman risk regression in active learning, offering a simple yet powerful alternative to myopic greedy rules without resorting to costly reinforcement‑learning or generative models. By conditioning on candidate features and budgets, it addresses the limitation of one‑step baselines that ignore context‑dependent value, thereby enabling more accurate feature selection under real‑world acquisition constraints.  

## Related Concepts  
- Active Feature Acquisition (AFA)  
- Myopic vs. non‑myopic learning  
- Bellman backup in reinforcement learning  
- Risk‑to‑go functions  
- Candidate‑conditioned models
