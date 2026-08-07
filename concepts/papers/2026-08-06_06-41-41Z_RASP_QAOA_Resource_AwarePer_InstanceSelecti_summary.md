# Summary: 2026-08-06_06-41-41Z_RASP_QAOA_Resource_AwarePer_InstanceSelectionforEx.md
Saved: 2026-08-06 22:05
Source: 2026-08-06_06-41-41Z_RASP_QAOA_Resource_AwarePer_InstanceSelectionforEx.md
Model: None

---

## Summary  
[The paper aims to develop a resource‑aware per‑instance selector for exact QAOA simulation that chooses among ten possible backend actions, discarding infeasible ones and ordering the rest by instance features while using analytical estimates for unsupported cases.] [It evaluates this selector on a content‑disjoint 60‑request H200 test set, succeeding on all 31 requests with at least one admissible action.] [The method achieves 27/31 top‑1 and 31/31 top‑2 selection with a geometric‑mean regret of 1.051.]  

## Key Contributions  
- [RASP‑QAOA succeeds on all 31 requests that have at least one admissible action, reaching 27/31 top‑1 and 31/31 top‑2 selection with a geometric‑mean regret of 1.051.]  
- [Its failure‑penalized PAR10 score is 0.0396 times that of the development‑selected CUAOA, yielding a high confidence interval (0.0085–0.1644).]  
- [A depth‑1 stump matches gradient boosting performance, and graph structure changes affect 16 decisions while improving the paired penalized score.]  

## Methodology  
[The authors construct RASP‑QAOA as a per‑instance selector that first eliminates actions incompatible with the requested QAOA semantics or execution constraints, then ranks the remaining actions by instance features such as graph size, circuit depth, precision mode, and memory policy; unsupported actions are handled via analytical work estimates.]  

## Results  
[On a content‑disjoint 60‑request H200 evaluation, RASP‑QAOA succeeds on all 31 requests with at least one admissible action, achieving 27/31 top‑1 and 31/31 top‑2 selection and a geometric‑mean regret of 1.051; its failure‑penalized PAR10 score is 0.0396 times that of CUAOA (95% CI: 0.0085–0.1644); a depth‑1 stump matches gradient boosting, and graph structure changes affect 16 decisions while improving the paired penalized score.]  

## Significance  
[This work demonstrates that resource‑aware representation selection can dramatically improve QAOA simulation efficiency up to n ≤ 35 qubits and p ≤ 5 repetitions, with gains driven primarily by representation features rather than classifier complexity; it also provides a benchmark (failure‑penalized PAR10) for evaluating selector performance.]  

## Related Concepts  
[QAOA exact simulation, backend selection, per‑instance selector, instance features, memory policy, geometric mean regret, PAR10 score, gradient boosting, stump learning.]
