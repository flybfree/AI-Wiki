# Summary: 2026-08-07_14-56-11Z_FromOptimalActionstoWorldModels_IdentifiabilityofT.md
Saved: 2026-08-09 23:06
Source: 2026-08-07_14-56-11Z_FromOptimalActionstoWorldModels_IdentifiabilityofT.md
Model: None

---

## Summary  
The paper investigates whether the transition probabilities of a discounted Markov decision process (MDP) can be uniquely recovered from optimal actions alone, when only the values of those actions are known for a class of rewards. It shows that many different transition kernels produce identical optimal actions across all reward types, demonstrating a severe identifiability problem; in contrast, certain reward structures—particularly those involving the next state—allow full recovery of the dynamics except in limited edge cases.

## Key Contributions  
- **Finding 1:** Two distinct transition kernels give the same optimal actions for every reward if they satisfy \( Q_{s,a} = (P_{s,a}+\tfrac1γ e_s^{\mathsf T}(L-I)) L^{-1} \) for an invertible matrix \(L\) with row sums equal to one; near kernels that have strictly positive entries, there exists an \((n(n-1))\)-dimensional family of such kernels.  
- **Finding 2:** For rewards that depend on the next state, i.e., \(r(s,a,s')\), every row at a state with at least two actions is fully determined by optimal actions; only rows where a single action exists may remain hidden because no alternative action can be distinguished.  
- **Finding 3:** State‑only rewards reveal less information: two kernels produce identical optimal actions exactly when every deterministic policy is optimal for the same set of rewards, indicating that state rewards cannot uniquely pin down the transition kernel.

## Methodology  
The authors start from the standard Q‑value representation under discount \(\gamma\) and introduce an invertible matrix \(L\) satisfying \(L\mathbf 1=\mathbf 1\). They show that kernels are indistinguishable via optimal actions precisely when they share this algebraic relationship. The analysis is then extended to three reward forms: (i) state rewards \(r(s)\), (ii) action‑dependent rewards \(r(s,a)\), and (iii) state‑action‑state rewards \(r(s,a,s')\). By comparing the conditions under which each form yields unique optimal actions, the authors map out when transition probabilities can be recovered versus when they remain ambiguous.

## Results  
The theoretical results are purely analytical: no simulation is required. The first finding establishes a broad non‑identifiability class of kernels; the second and third findings delineate precise regimes where partial or full recovery occurs depending on reward structure. These results clarify the limits of using optimal policies as a diagnostic tool for learning the underlying dynamics.

## Significance  
Understanding when optimal actions are sufficient to infer transition probabilities is crucial for model‑agnostic reinforcement learning, inverse RL, and any setting where only policy performance data is available. The paper warns that without additional information—such as state‑dependent rewards—the system may be underdetermined, potentially leading to multiple plausible world models.

## Related Concepts  
- Discounted Markov decision processes (MDPs)  
- Q‑function representation with discount \(\gamma\) and matrix \(L\)  
- Transition kernels and their identifiability  
- Letcher’s inverse problem for Q‑values  
- Optimal actions across reward classes  
- Deterministic policies and policy dominance
