# Summary: 2026-07-25_21-12-51Z_OntheImpossibilityofUnbiasedandLength_InvariantPol.md
Saved: 2026-07-27 20:14
Source: 2026-07-25_21-12-51Z_OntheImpossibilityofUnbiasedandLength_InvariantPol.md
Model: None

---

## Summary  
The paper investigates the fundamental trade‑off between gradient unbiasedness and length invariance in Group Relative Policy Optimization (GRPO) when outcome rewards are used. It proves that no weighting scheme can satisfy both properties simultaneously, showing that GRPO is biased toward longer trajectories while Dr. GRPO is unbiased but length‑biased. The authors characterize the complete spectrum of possible weightings using a parametric family \(f_\alpha(L)=L^{\alpha-1}\) and demonstrate that the two algorithms occupy opposite ends of this trade‑off.

## Key Contributions  
- [Finding 1] An impossibility theorem stating that under outcome rewards, no length‑based weighting can achieve both unbiased gradient estimates (P1) and length invariance (P2).  
- [Finding 2] A quantitative analysis showing Dr. GRPO’s bias amplifies the influence of longer trajectories by a factor proportional to their length ratio relative to shorter ones.  
- [Finding 3] The parametric characterization \(f_\alpha(L)=L^{\alpha-1}\) that maps \(\alpha=0\) to standard GRPO and \(\alpha=1\) to Dr. GRPO, revealing the complete trade‑off spectrum.

## Methodology  
The authors adopt a theoretical analysis of reinforcement‑learning gradient estimators in the context of outcome rewards. They formalize the two desiderata—gradient unbiasedness (P1) and length invariance (P2)—and examine how any weighting function \(w(L)\) modifies the contribution of each trajectory. By plugging candidate weightings into the gradient estimator, they derive conditions under which both properties hold and show that only the limiting cases \(\alpha=0\) or \(\alpha=1\) satisfy one property while violating the other.

## Results  
Theoretical results prove the impossibility result and provide exact expressions for the bias magnitude: longer trajectories dominate updates by a factor \(L_2/L_1\). Experiments on synthetic and real language‑model tasks confirm that DR. GRPO’s length bias can cause gradient updates to be disproportionately large, while standard GRPO remains unbiased but length‑sensitive.

## Significance  
Understanding this trade‑off is crucial for designing robust RL algorithms in long‑sequence generation where response length varies widely; it clarifies why existing “unbiased” variants still suffer from practical bias and guides future work toward more balanced weighting schemes.

## Related Concepts  
Group Relative Policy Optimization, outcome rewards, gradient unbiasedness, length invariance, parametric weighting \(f_\alpha(L)=L^{\alpha-1}\), response‑level normalization, DeepSeek‑R1, COLM 2025.
