# Summary: 2026-08-02_04-39-27Z_Model_AgnosticFDRControlviaGroupGaussianMirrorandP.md
Saved: 2026-08-03 23:58
Source: 2026-08-02_04-39-27Z_Model_AgnosticFDRControlviaGroupGaussianMirrorandP.md
Model: None

---

## Summary  
The paper addresses the limitation of existing FDR‑controlled feature selection methods that assume independent features and single weights, proposing a grouped‑feature framework for sequential or block‑structured models such as lags, recurrent states, or attention interactions. It introduces model‑agnostic block‑level mirror statistics for linear models and permutation SHAP derivatives combined with kernel dependence measures for neural sequential models. The framework provides FDR control without specifying the covariate distribution and reduces to Gaussian Mirror or Neural Gaussian Mirror when each block contains a single feature.

## Key Contributions  
- A grouped‑feature FDR control framework that treats each block of sub‑features as a single unit, enabling model‑agnostic selection across linear and neural architectures.  
- Construction of null‑symmetric block‑level mirror statistics using matrix perturbations for linear models and permutation SHAP derivatives combined with kernel‑based dependence measures for sequential models.  
- Theoretical proof of FDR control in low‑ and high‑dimensional grouped linear models plus asymptotic symmetry of smoothed Permutation SHAP derivatives under fixed nonlinear fits.

## Methodology  
The authors first define block‑level importance scores: for linear models they compute Gaussian Mirror statistics by applying symmetric matrix perturbations to each block, yielding mirror statistics that are null‑symmetric; for neural sequential models they derive permutation SHAP gradients and integrate them with a kernel dependence measure to capture the correlation structure of grouped features. Both approaches are model‑agnostic—no explicit covariate distribution is required—and reduce to familiar Gaussian Mirror when the block size equals one, allowing seamless integration into existing pipelines.

## Results  
Simulations on synthetic data with correlated grouped signals demonstrate that the proposed methods achieve controlled false discovery rates while maintaining high power compared with standard FDR procedures; real‑world experiments on time‑series and attention models confirm reliable control and improved performance. Theoretical analysis proves asymptotic symmetry of smoothed Permutation SHAP derivatives for fixed fitted nonlinear models, guaranteeing consistency as block size grows.

## Significance  
This work extends classical FDR control beyond coordinate‑wise assumptions, enabling robust feature selection in complex sequential or grouped models where features are interdependent; it provides a unified, model‑agnostic tool that reduces to familiar Gaussian Mirror when the block size is one, facilitating adoption across diverse machine‑learning pipelines.

## Related Concepts  
Grouped feature selection, FDR control, Gaussian Mirror statistics, Permutation SHAP, kernel dependence measures, block‑level importance scores, asymptotic symmetry of smoothed derivatives.
