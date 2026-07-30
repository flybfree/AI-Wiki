# Summary: 2026-07-29_11-29-45Z_StableandBudget_FeasibleCoalitionFormationforClust.md
Saved: 2026-07-29 22:23
Source: 2026-07-29_11-29-45Z_StableandBudget_FeasibleCoalitionFormationforClust.md
Model: None

---

## Summary  
The paper proposes a hedonic potential‑game framework for forming stable, budget‑feasible coalitions in clustered federated learning, separating the learning benefit, system cost, participant cost, and monetary transfers into a transferable surplus. It derives allocation rules that convert this surplus into individual preferences while guaranteeing nonnegative coordinator surplus and Nash stability. For symmetric pairwise allocations the induced game is an exact potential game, enabling convergence of better‑response processes and providing price‑of‑stability guarantees. The framework also approximates weighted maximum‑agreement correlation clustering with explicit constructions.

## Key Contributions  
- [Finding 1] Derives a transferable‑surplus model that separates learning benefit, system cost, participant cost, and monetary transfers; introduces an allocation rule converting surplus into hedonic preferences.  
- [Finding 2] Shows that for symmetric pairwise allocations the induced game is an exact potential game, guaranteeing Nash stability and convergence of better‑response processes.  
- [Finding 3] Provides polynomial‑time feasibility verification for bounded pair incentives under submodular retained slack, linking price‑of‑stability to additive/multiplicative guarantees.

## Methodology  
The authors model coalition formation as a hedonic potential game where surplus translates into participant utility. They formulate allocation rules that maximize individual preferences while respecting budget constraints, using submodular slack analysis and oracle queries for feasibility checks. Theoretical analysis proves the exactness of the potential structure, convergence properties, and welfare bounds.

## Results  
Theoretical results include existence of Nash‑stable partitions, exponential many budget constraints verified in polynomial time when slack is submodular, additive and multiplicative price‑of‑stability guarantees with asymptotic tightness. Empirically on a preregistered five‑seed CIFAR‑10 study the mechanism achieves certified optimal welfare on primary instances; equal‑surplus sharing fails Nash stability on three seeds; pairwise validation gain outperforms gradient alignment.

## Significance  
By linking coalition formation to potential games, the work ensures stable, cost‑effective federated learning that maximizes overall utility while respecting budgets. The price‑of‑stability analysis provides theoretical guarantees and practical insights for incentive design in distributed machine learning.

## Related Concepts  
Hedonic potential game, maximum‑agreement correlation clustering, submodular slack, price of stability, budget feasibility, coalition formation, federated learning, CIFAR‑10 experiments.
