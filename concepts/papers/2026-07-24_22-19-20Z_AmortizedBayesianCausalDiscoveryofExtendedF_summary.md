# Summary: 2026-07-24_22-19-20Z_AmortizedBayesianCausalDiscoveryofExtendedFactorGr.md
Saved: 2026-07-27 23:29
Source: 2026-07-24_22-19-20Z_AmortizedBayesianCausalDiscoveryofExtendedFactorGr.md
Model: None

---

## Summary  
The paper proposes Amortized Bayesian Causal Discovery of Extended Factor Graphs (ABCDEFG), a framework for learning large‑scale causal graphs from interventional data while guaranteeing exact acyclicity and handling interventions whose targets are unknown. By integrating an amortization scheme into the inference of extended factor graphs, ABCDEFG produces a posterior distribution whose maximum a posteriori estimate identifies the true graph up to an equivalence class. The method scales to thousands of nodes, estimates uncertainty, and provides provable identifiability—addressing key shortcomings of existing score‑based or approximate Bayesian approaches.

## Key Contributions  
- [Finding 1] Exact acyclicity is guaranteed for all generated graphs, ensuring the learned structure remains a valid causal model.  
- [Finding 2] The algorithm scales to thousands of nodes through amortized inference updates that keep computational cost linear in the number of interventions.  
- [Finding 3] Interventions can be applied even when their target variables are unknown, and the posterior distribution quantifies uncertainty while yielding an identifiable MPE.

## Methodology  
ABCDEFG builds on extended factor graphs to represent both observed and latent variables, allowing causal edges to be represented as conditional probability distributions. The amortization technique separates the cost of updating the graph structure from the cost of re‑evaluating the likelihood under new interventions, enabling efficient incremental learning. A Bayesian inference pipeline computes a posterior over all possible extended factor graphs consistent with the interventional data, using variational techniques that are optimized via the amortized framework.

## Results  
On simulated datasets containing thousands of nodes, ABCDEFG achieves state‑of‑the‑art accuracy in graph reconstruction and produces well‑calibrated posterior estimates. The method outperforms both score‑based optimization and approximate Bayesian inference baselines. When applied to large‑scale single‑cell perturbation data from molecular biology experiments, ABCDEFG identifies previously unrecognized gene targets of growth factors with high confidence.

## Significance  
This work advances the field of causal discovery by delivering a scalable, uncertainty‑aware, and provably correct algorithm that can be deployed on real biological datasets. By handling unknown intervention targets and guaranteeing acyclicity, ABCDEFG enables more reliable inference in complex systems where traditional methods fail.

## Related Concepts  
- Bayesian Causal Discovery  
- Factor Graphs (extended)  
- Amortized Inference  
- Interventional Data  
- Identifiability Guarantees  
- Posterior Distribution Estimation
