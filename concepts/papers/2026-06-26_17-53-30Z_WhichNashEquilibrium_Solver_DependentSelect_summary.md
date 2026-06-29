# Summary: 2026-06-26_17-53-30Z_WhichNashEquilibrium_Solver_DependentSelectiononZe.md
Saved: 2026-06-28 22:00
Source: 2026-06-26_17-53-30Z_WhichNashEquilibrium_Solver_DependentSelectiononZe.md
Model: None

---


## Summary  
The paper investigates whether solvers choose different Nash equilibria within a zero‑sum game polytope based on the algorithm rather than on an arbitrary seed, suggesting that solver design determines which member of the convex set is selected. It proposes that regularized last‑iterate methods (R‑NaD, magnetic mirror descent) converge to the maximum‑entropy equilibrium—essentially the information projection of their uniform reference onto the Nash set—while regret‑averaging techniques drift toward lower‑entropy faces. The study uses a tabular, exactly solvable testbed of six games with analytically known Nash polytopes, including a two‑dimensional polytope and Kuhn poker, to empirically compare solver behaviors across an ensemble of 180 randomized games.

## Key Contributions  
- [Finding 1] Selection is determined by the algorithm, not the seed; families differ only on asymmetric Nash sets.  
- [Finding 2] Regularized last‑iterate methods (R‑NaD, magnetic mirror descent) select the maximum‑entropy member, matching the information projection of their uniform reference onto the Nash set, observed at >99.7 % max entropy in Kuhn and exactly on the 2‑D polytope.  
- [Finding 3] The selected equilibrium has downstream strategic advantages that depend on sequential/hidden‑information structure; R‑NaD yields a strictly better hedge than CFR+ in Kuhn.

## Methodology  
The authors constructed six analytically solvable zero‑sum games, each with a known Nash polytope. They implemented standard regret‑averaging solvers (CFR, CFR+, fictitious play) and regularized iterators (R‑NaD, magnetic mirror descent). The experiments were run on a randomized ensemble of 180 games to capture variability across seeds and parameter settings.

## Results  
R‑NaD attained the maximum‑entropy member in 100 % of converged games; CFR+ was below it in 94 % (paired Wilcoxon p < 10⁻²⁷). On matrix games, selected members differ without either dominating. Negative results: removing CFR’s positive‑orthant projection does not eliminate boundary drift; R‑NaD selection is anchor‑following rather than initialization‑independent.

## Significance  
The findings demonstrate that solver choice influences equilibrium selection, affecting strategic outcomes and supporting the conjecture of I‑projection as a max‑entropy selector. This insight informs algorithm design for robust convergence in zero‑sum games with complex Nash sets.

## Related Concepts  
Nash polytope, maximum entropy, information projection, regret averaging, convex hull of equilibria, sequential/hidden‑information structure, anchor‑following behavior.
