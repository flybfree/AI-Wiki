# Summary: 2026-07-30_05-44-34Z_NMINE_NormalizedMutualInformationNeuralEstimation.md
Saved: 2026-07-30 21:39
Source: 2026-07-30_05-44-34Z_NMINE_NormalizedMutualInformationNeuralEstimation.md
Model: None

---

## Summary  
The paper proposes NMINE, a neural estimator for normalized mutual information (NMI) of continuous multidimensional variables, aiming to improve accuracy and stability over existing k‑nearest neighbor methods. It combines the Donsker–Varadhan representation for MI estimation with learned marginal entropy estimators inspired by MI‑NEE. The goal is to provide a scalable, differentiable alternative that handles high dimensions without sensitivity.

## Key Contributions  
- NMINE offers a fully neural estimator for NMI of continuous variables across 1–8 dimensions.  
- It integrates Donsker–Varadhan theory with learned marginal entropy approximations for unbiasedness and stability.  
- Experimental results show NMINE outperforms KSG baseline in Gaussian data, demonstrating improved accuracy.

## Methodology  
The authors formulate mutual information using the Donsker–Varadhan representation, which approximates MI via a sum of KL divergences between empirical CDFs and reference distributions. Marginal entropies are estimated by learning divergences to a uniform distribution via neural networks, recovering entropy from the divergence score. This yields a differentiable pipeline that can be trained end‑to‑end.

## Results  
Experiments on Gaussian data across 1–8 dimensions show NMINE achieves lower mean absolute error than KSG (k‑nearest neighbor based NMI) and converges faster during training. The improvement is statistically significant with p < 0.05, indicating neural estimation’s promise for continuous multidimensional dependency measurement.

## Significance  
By providing a stable, differentiable estimator that scales to high dimensions, NMINE addresses limitations of traditional NMI methods, enabling its use in fields like molecular dynamics and interpretable ML where NMI is valuable but problematic.

## Related Concepts  
Normalized Mutual Information (NMI), Donsker–Varadhan representation, mutual information, marginal entropy, K‑nearest neighbor estimation, MI‑NEE, KL divergence, neural network estimators.
