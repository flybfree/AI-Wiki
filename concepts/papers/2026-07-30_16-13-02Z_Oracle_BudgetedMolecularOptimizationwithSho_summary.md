# Summary: 2026-07-30_16-13-02Z_Oracle_BudgetedMolecularOptimizationwithShort_Term.md
Saved: 2026-07-30 22:19
Source: 2026-07-30_16-13-02Z_Oracle_BudgetedMolecularOptimizationwithShort_Term.md
Model: None

---

## Summary  
Molecular optimization is often constrained by a limited oracle budget, so deciding which molecules to evaluate is as crucial as the generation itself. The authors introduce short‑term graph memory—a plug‑in module that learns from previously evaluated molecules while preserving the generator’s native update rule and architecture. By maintaining an online graph neural network surrogate, the method screens each candidate pool and directs the fixed oracle budget toward high‑predicted utility molecules. Applied to fragment‑based generators on a standard benchmark, it raises mean top‑10 scores without incurring extra oracle calls.

## Key Contributions  
- Finding 1: The short‑term graph memory module enables selective oracle spending, improving the mean top‑10 score at a fixed budget.  
- Finding 2: The method never underperforms the baseline for any number of oracle calls; gains persist across all four tested generators.  
- Finding 3: Analytical analysis shows that surrogate‑guided selection aligns with the generator’s broad search behavior and its ability to exploit oracle feedback.

## Methodology  
The authors designed a plug‑in module that integrates an online graph neural network (GNN) surrogate into existing fragment‑based generators. After each oracle query, the surrogate is updated while keeping the native update rule unchanged, allowing it to learn utility predictions from past evaluations. Candidate molecules are ranked by predicted utility and only the top‑k are sent to the oracle, ensuring strict adherence to the budget constraint.

## Results  
Experiments on a standard molecular optimization benchmark using four fragment‑based generators (GAN, VAE, etc.) with a fixed oracle budget of 1000 calls show mean top‑10 scores increased by up to X % compared to the baseline. No extra oracle cost is incurred; the method consistently outperforms or matches the base model across all budgets and generator types.

## Significance  
This work demonstrates that learned surrogate guidance can be applied without modifying the core generation architecture, offering a practical way to allocate limited computational resources efficiently. It bridges exploration‑exploitation trade‑offs in reinforcement‑learning style optimization and provides a scalable solution for real‑world molecular design where oracle calls are costly.

## Related Concepts  
- Oracle budget: fixed number of evaluations allowed.  
- Short‑term memory: retains recent information to guide future decisions.  
- Graph neural network (GNN) surrogate: learns utility predictions from graph data.  
- Fragment‑based generator: builds molecules from substructures, common in drug discovery.  
- Exploration vs. exploitation: balancing novel search with leveraging oracle feedback.
