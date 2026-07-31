# Summary: 2026-07-30_08-45-14Z_SearchasComputationAllocation.md
Saved: 2026-07-30 21:42
Source: 2026-07-30_08-45-14Z_SearchasComputationAllocation.md
Model: None

---

## Summary  
The paper formalizes a class of “terminal computation‑allocation” problems where costly internal computations generate observations that influence only the final decision loss, and it derives optimal allocation policies under various budget constraints. By linking the value of computation (VOC) to information theory, the authors show how mutual information equals myopic VOC under log loss while simple regret VOC corresponds to a knowledge‑gradient quantity. The work also demonstrates that maximizing approximate VOC recovers weighted A* with greedy best‑first search as a limiting case, revealing a shared decision problem without a single universal optimal rule.

## Key Contributions  
- [Finding 1] The theory formalizes terminal computation‑allocation problems and derives Bellman equations for optimal allocation under fixed budgets, priced computation, and exact certification.  
- [Finding 2] It establishes that VOC equals mutual information when the loss is log loss, whereas simple regret VOC is a knowledge‑gradient quantity; mutual information provides only an upper bound on VOC.  
- [Finding 3] Approximate VOC maximization recovers weighted A* with greedy best‑first search as a limiting case, showing how different heuristics correspond to computational frontiers.

## Methodology  
The authors model each computation step as a costly operation that produces observations and updates beliefs about a latent environment. They then apply dynamic programming via Bellman equations to compute optimal allocation policies for fixed budgets. To illustrate the model across different topologies, they simulate bandit pulls, tree expansions, and node simulations, comparing outcomes under exact certification versus approximate certification.

## Results  
Theoretical results: VOC equals mutual information under log loss; simple regret VOC is a knowledge‑gradient quantity; mutual information gives an upper bound on VOC. Experimental simulations confirm that maximizing approximate VOC yields weighted A* with greedy best‑first search as the limiting case, and that different computation topologies produce equivalent decision outcomes when aligned to this objective.

## Significance  
This work bridges computational cost and decision quality by providing a unified framework for evaluating costly actions in planning and learning. It moves beyond information gain toward a metric—VOC—that directly captures how much computation improves the final outcome, offering new insights into acquisition strategies that are both efficient and effective.

## Related Concepts  
- Terminal computation allocation  
- Bellman equations  
- Value of computation (VOC)  
- Mutual information  
- Knowledge gradient  
- Weighted A*  
- Greedy best‑first search
