# Summary: 2026-07-24_22-20-44Z_Discrepancy_RoundedFairBanditswithStaticandTime_Va.md
Saved: 2026-07-27 23:29
Source: 2026-07-24_22-20-44Z_Discrepancy_RoundedFairBanditswithStaticandTime_Va.md
Model: None

---

## Summary  
The paper tackles the challenge of satisfying minimum‑exposure constraints in stochastic bandits by viewing the problem as a rounding task whose error manifests as a discrepancy vector. It introduces a blockwise model with both static and time‑varying exposure floors, showing that an optimal schedule can be built from fractional fair allocations while guaranteeing deterministic compliance per block. The authors develop UCB‑based algorithms—BDQ‑UCB, MOSS residuals, and kl‑UCB$^{++}$—that achieve regret bounds of $O(\sqrt{KR\log(KT)})$ (or $O(\sqrt{KR})$ with a residual variant), matching a matching lower bound. Experiments on synthetic floors, the MovieLens‑100k genre exposure dataset, and deployment stress tests confirm exact feasibility without penalty tuning.

## Key Contributions  
- [Finding 1] A blockwise model with time‑varying exposure floors yields deterministic satisfaction of each floor’s mandatory exposure while keeping regret tied to a nonmandatory budget $R$, not the horizon $T$.  
- [Finding 2] BDQ‑UCB achieves high‑probability regret $O(\sqrt{KR\log(KT))}$; a MOSS residual variant improves this to $O(\sqrt{KR})$, and a matching lower bound proves $\Theta(\sqrt{KR})$ is optimal even with positive mandatory exposure.  
- [Finding 3] Per‑arm rounding can violate group constraints by $\Omega(s)$, whereas Beck–Fiala null‑space rounding respects all group floors within the block budget with violation bounded by arm degree $t$, and composes with UCB at the same $R$‑parametrized regret.

## Methodology  
The authors model a fractional fair schedule as an integral pull sequence, defining the exposure error vector as a discrepancy. They employ UCB‑based algorithms that add instance‑dependent residuals (MOSS, kl‑UCB$^{++}$) to preserve optimality under constraints. Feasibility is verified block by block: each block’s floor is met exactly by BDQ‑UCB, while residual rules handle any remaining slack. The analysis combines regret bounds with a lower bound argument that shows no algorithm can do better than $\Theta(\sqrt{KR})$ regret.

## Results  
Theoretically, the proposed algorithms achieve regret $O(\sqrt{KR\log(KT)})$, matching the lower bound up to logarithmic factors, and the MOSS variant reaches $O(\sqrt{KR})$. Experiments on synthetic exposure floors demonstrate exact floor satisfaction without penalty tuning. On MovieLens‑100k genre data, the same rules respect per‑genre exposure floors while keeping regret competitive with tuned Lagrangian baselines. Deployment stress tests confirm that the plan‑sampling rule remains pathwise feasible under an initial cover‑slack condition and attains a conditional $\widetilde O(\sqrt{KT})$ guarantee.

## Significance  
This work provides efficient, provably optimal algorithms for constrained recommendation and allocation problems where exposure floors must be met per period. By decoupling regret from the horizon and offering exact feasibility guarantees, it enables reliable compliance in regulated systems without costly penalty tuning, thereby advancing both theoretical fairness analysis and practical deployment.

## Related Concepts  
- Discrepancy rounding: fractional fair schedules realized as integral pulls with error measured by a discrepancy vector.  
- UCB (Upper Confidence Bound): standard bandit selection rule extended with residuals for constraint handling.  
- Blockwise scheduling: time‑segmented allocation that allows deterministic floor satisfaction per block.  
- Mandatory vs nonmandatory budget $R$: the latter governs regret, the former ensures minimum exposure.  
- Group floors and arm degree $t$: constraints on per‑group exposure and rounding violations.  
- Lower bound matching: proof that $\Theta(\sqrt{KR})$ is optimal for regret under these settings.
