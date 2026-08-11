# Summary: 2026-08-10_09-06-03Z_CoRE_ConsensusRewardsviaEquilibriumforTest_TimeRei.md
Saved: 2026-08-10 23:43
Source: 2026-08-10_09-06-03Z_CoRE_ConsensusRewardsviaEquilibriumforTest_TimeRei.md
Model: None

---

## Summary  
The paper proposes CoRE (Consensus Rewards via Equilibrium) as a test‑time reinforcement learning reward function that replaces the simple majority vote over N roll‑out answers with a consensus mechanism based on graph‑theoretic equilibria. By modeling the N roll‑outs as nodes connected by edges representing answer agreement, reasoning similarity, and generation confidence, CoRE extracts a dominant set of roll‑outs via replicator dynamics, producing refined pseudo‑labels, graded rewards, and a cohesiveness gate. This approach generalizes majority voting, offering calibrated rewards that adapt to minority correct answers while penalizing noisy majorities. The method is self‑supervised, requiring no extra roll‑out cost.  

## Key Contributions  
- [Finding 1] CoRE replaces the brittle majority vote with a consensus reward derived from replicator dynamics on a graph of N roll‑outs.  
- [Finding 2] A block‑value analysis shows that consensus can recover correct minority answers when they outperform wrong plurality by up to +7.5 points, with confidence calibration lowering the threshold multiplicatively.  
- [Finding 3] Experiments across seven backbones and five benchmarks demonstrate CoRE improves untrained base by +21.7 points vs +20.4 for majority‑vote TTRL, achieving voting baseline accuracy in fewer steps.  

## Methodology  
The authors construct a graph where each node corresponds to one roll‑out of an answer set, with edges weighted by pairwise agreement on the correct answer (binary), similarity of reasoning traces (continuous), and model confidence scores (probabilistic). Replicator dynamics compute the stationary distribution that maximizes expected reward, yielding a dominant subset of nodes. The consensus pseudo‑label is derived from this subset, while graded rewards are assigned based on node weight in the equilibrium. A cohesiveness gate filters out low‑confidence or divergent roll‑outs before feeding them into RL.  

## Results  
Across 42 model‑benchmark cells (3 seeds each), CoRE outperforms majority‑vote TTRL by an average of +21.7 points, matching voting baseline accuracy in 54–70 % fewer steps. The consensus mechanism recovers correct minority answers when the margin exceeds the vote’s wrong plurality, and confidence calibration reduces the required margin multiplicatively.  

## Significance  
CoRE transforms a simple, often inaccurate majority vote into a calibrated, graded reward that respects both agreement and confidence, enabling more reliable test‑time RL without extra roll‑outs. This shift from voting to equilibrium improves robustness in noisy environments and accelerates convergence toward optimal policy.  

## Related Concepts  
- Replicator dynamics  
- Consensus learning  
- Graph‑based reward calibration  
- Test‑time reinforcement learning (TTRL)  
- Majority vote  
- Block‑value analysis
