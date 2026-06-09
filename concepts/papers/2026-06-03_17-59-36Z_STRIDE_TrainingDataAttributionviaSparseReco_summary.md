# Summary: 2026-06-03_17-59-36Z_STRIDE_TrainingDataAttributionviaSparseRecoveryfro.md
Saved: 2026-06-04 00:01
Source: 2026-06-03_17-59-36Z_STRIDE_TrainingDataAttributionviaSparseRecoveryfro.md
Model: None

---


## Summary  
The paper addresses training data attribution for large language models, which is computationally expensive using causal interventions. STRIDE proposes a sparse recovery approach in activation space using lightweight steering operators, enabling fast and accurate attribution without retraining. It achieves state‑of‑the‑art performance while being 13× faster than prior methods. This work bridges the gap between theoretical TDA and practical LLM deployment.  

## Key Contributions  
- The introduction of STRIDE as a sparse recovery framework for training data attribution.  
- The design of steering operators that approximate functional effects of data subsets in activation space.  
- Empirical demonstration that STRIDE outperforms previous TDA methods by orders of magnitude in speed and accuracy.  

## Methodology  
The authors treat TDA as a compressive sensing problem, learning low‑rank steering operators via regression on perturbed predictions. They apply these operators to test data perturbations from training subsets, then perform sparse linear decomposition to isolate contributions per example. Training is lightweight; inference uses dot products with the learned operators.  

## Results  
Experiments on LLM pre‑training show attribution accuracy comparable to causal methods while reducing runtime by 13×. Ablation studies confirm operator sparsity and robustness across domains. Downstream tasks like data selection and contamination detection benefit from the recovered influence scores.  

## Significance  
By enabling fast, scalable TDA for LLMs, STRIDE facilitates responsible AI practices such as data curation and bias mitigation without prohibitive computational cost. It also advances theoretical understanding of activation space dynamics.  

## Related Concepts  
Training Data Attribution (TDA), Causal Interventions, Sparse Recovery, Compressive Sensing, Activation Space Modeling, Steering Operators, Large Language Models (LLMs).

[[STRIDE: Training Data Attribution via Sparse Recovery from Subset Perturbations]]