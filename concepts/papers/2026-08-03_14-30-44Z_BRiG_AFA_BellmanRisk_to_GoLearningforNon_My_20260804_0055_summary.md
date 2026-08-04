# Summary: 2026-08-03_14-30-44Z_BRiG_AFA_BellmanRisk_to_GoLearningforNon_MyopicAct.md
Saved: 2026-08-04 00:55
Source: 2026-08-03_14-30-44Z_BRiG_AFA_BellmanRisk_to_GoLearningforNon_MyopicAct.md
Model: None

---

## Summary  
The paper proposes BRiG‑AFA, a supervised active feature acquisition framework that learns candidate‑conditioned risk‑to‑go functions via Bellman regression to guide non‑myopic selections. By fitting these functions backward from the terminal classification risk, the method allows greedy inference that minimizes only observed risks while respecting remaining budget and masks. Experiments on Fashion‑MNIST demonstrate consistent accuracy gains across budgets, outperforming one‑step baselines by up to 10 percentage points at four acquisitions. The work establishes a reproducible mechanism‑level benchmark for Bellman risk regression in active learning.

## Key Contributions  
- [Learning candidate‑conditioned risk‑to‑go functions with Bellman targets enables non‑myopic feature selection.]  
- [Greedy inference using only observed values, mask, candidate identity, and budget yields the optimal next acquisition.]  
- [Empirical results show up to 10.2 pp accuracy improvement at four acquisitions on Fashion‑MNIST.]

## Methodology  
BRiG‑AFA constructs a separate risk‑to‑go model for each remaining budget, initializing them with the one‑step terminal classification loss. The models are updated iteratively by minimizing Bellman targets that incorporate the true next acquisition’s contribution to accuracy. During inference, the algorithm selects the candidate pixel whose learned risk is lowest, using only the observed mask and remaining budget—no conditional density or complex RL required.

## Results  
On Fashion‑MNIST with 20 candidate pixels, BRiG‑AFA improves test accuracy by an average of 3.5 pp across budgets {2,4,8,12,16}, reaching a peak gain of 10.2 ± 0.74 pp at four acquisitions. Five random seeds yield mean gains of 4.84 ± 2.17 pp and 4.39 ± 1.10 pp for budgets two and three, respectively. A MiniBooNE study shows positive gains at eight and sixteen acquisitions but mixed results at smaller budgets.

## Significance  
The work provides a deployable, supervised alternative to myopic greedy rules and to complex RL or generative active‑learning methods, offering a clear Bellman risk regression pipeline that can be directly integrated into existing pipelines. By demonstrating consistent performance gains across multiple datasets and acquisition depths, it validates the theoretical promise of risk‑to‑go learning for non‑myopic feature selection.

## Related Concepts  
- Active Feature Acquisition (AFA)  
- Risk‑to‑Go learning  
- Bellman backup  
- Greedy inference in active learning  
- Non‑myopic acquisition strategies  
- Candidate‑conditioned risk functions
