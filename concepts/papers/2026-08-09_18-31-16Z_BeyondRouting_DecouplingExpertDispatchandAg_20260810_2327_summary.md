# Summary: 2026-08-09_18-31-16Z_BeyondRouting_DecouplingExpertDispatchandAggregati.md
Saved: 2026-08-10 23:27
Source: 2026-08-09_18-31-16Z_BeyondRouting_DecouplingExpertDispatchandAggregati.md
Model: None

---

## Summary  
The paper investigates whether the two functions that MoE routers perform—dispatching which experts to activate and aggregating their outputs—should be treated as separate or coupled operations in sparse Mixture‑of‑Experts (MoE) systems. By keeping expert selection, computation budget, and total router mass constant while only varying aggregation, the authors train a lightweight post‑compute head that adapts the weighting of already computed expert results without altering the backbone model. This decoupling yields measurable gains on several benchmarks and reveals a fundamental architectural distinction between expert selection (dispatch) and expert commitment (aggregation).  

## Key Contributions  
- [Finding 1] Decoupling dispatch and aggregation allows independent optimization, leading to a 0.016 ± 0.004 improvement in full‑horizon cross‑entropy on pretrained OLMoE‑1B‑7B.  
- [Finding 2] The Fixed‑Dispatch Adaptive Aggregation (FDAA) head, with 301K parameters, improves the fresh WikiText‑103 test by ΔCE = –0.1523 ± 0.0031 across three seeds while freezing the backbone, router, and experts.  
- [Finding 3] Audits of deep‑seek‑v2‑lite show that best‑vertex headroom remains significant on WikiText and C4, yet router Top‑1 correctly identifies the optimal expert only 12.5 % (WikiText) and 16.7 % (C4), confirming that selection rarely aligns with true competence.  

## Methodology  
The authors adopt a “fixed‑dispatch” configuration: the router selects a fixed set of Top‑8 expert IDs, each expert’s output is computed once per token, and only the aggregation weights are varied. They introduce FDAA—a small post‑compute head that directly optimizes the language‑modeling objective (cross‑entropy) on these aggregated outputs while freezing all higher‑level components. This design isolates the aggregation step from dispatch, enabling systematic experiments across diverse datasets and domains.  

## Results  
Full‑horizon cross‑entropy gains of 0.016 ± 0.004 are observed when aggregating expert contributions adaptively. The FDAA head reduces WikiText‑103 CE by ΔCE = –0.1523, a statistically significant improvement across three random seeds. Audits reveal that the router’s best‑vertex headroom is robust on WikiText and C4, but Top‑1 expert identification succeeds only 12.5 % (WikiText) and 16.7 % (C4). In mixed‑domain training, FDAA yields locked gains on WikiText and PTB while showing no effect on C4. These findings support a cross‑architecture distinction between expert selection and commitment.  

## Significance  
By proving that dispatch and aggregation can be optimized independently, the work expands the design space for MoE systems, allowing hardware or software constraints to dictate one component without penalizing the other. The FDAA head demonstrates that lightweight post‑compute adaptation can boost model performance substantially while preserving computational efficiency, offering a practical path toward more scalable and flexible expert routing architectures.  

## Related Concepts  
- Mixture‑of‑Experts (MoE) routing  
- Expert dispatch vs. aggregation  
- Sparse activation strategies  
- Cross‑entropy loss optimization  
- Headroom analysis in router selection  
- Mixed‑domain training and evaluation
