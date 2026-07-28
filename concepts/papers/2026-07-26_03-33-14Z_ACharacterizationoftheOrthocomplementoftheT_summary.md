# Summary: 2026-07-26_03-33-14Z_ACharacterizationoftheOrthocomplementoftheTangentS.md
Saved: 2026-07-27 23:52
Source: 2026-07-26_03-33-14Z_ACharacterizationoftheOrthocomplementoftheTangentS.md
Model: None

---

## Summary  
The paper aims to characterize the orthogonal complement of the tangent space associated with semiparametric Markov models that are not equivalent to DAG graphical models. It provides closed‑form expressions for this orthogonal complement and uses it to identify the full class of influence functions for target parameters, thereby enabling efficient semi‑parametric inference.

## Key Contributions  
- [Finding 1] Derivation of a general formula for the orthogonal complement of the tangent space in any semiparametric Markov model.  
- [Finding 2] Identification of the complete set of influence functions for the conditional mean parameter across several graphical models (undirected graphs, chain graphs, mixed graphs).  
- [Finding 3] Demonstration that this characterization resolves a longstanding gap in semi‑parametric theory for non‑DAG Markov models.

## Methodology  
The authors start from the definition of the tangent space at a point in the parameter space and compute its orthogonal complement using linear algebra on the model’s conditional independence structure. They then apply this complement to the influence function via the Rademacher representation, obtaining explicit formulas that depend only on the graph topology.

## Results  
Closed‑form expressions are derived for the orthogonal complement; they match known results for DAG models and extend them to undirected graphs, chain graphs, and mixed graphs. The corresponding classes of influence functions coincide with those obtained by standard semiparametric theory, confirming consistency.

## Significance  
By closing this gap, the paper enables efficient semi‑parametric inference in a wide range of non‑DAG Markov models that are common in social science data, improving computational tractability and statistical efficiency.

## Related Concepts  
tangent space, orthogonal complement, influence function, semiparametric estimation, graphical models (directed acyclic graphs, undirected graphs, chain graphs, mixed graphs), conditional independence, Rademacher representation.
