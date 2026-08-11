# Summary: 2026-07-27_19-11-50Z_Shape_BasedInductiveBiasforGliomaGradingfromTumorC.md
Saved: 2026-07-29 22:11
Source: 2026-07-27_19-11-50Z_Shape_BasedInductiveBiasforGliomaGradingfromTumorC.md
Model: None

---

## Summary  
The paper proposes a shape‑based inductive bias to improve glioma grading from tumor contours by focusing on geometric structure rather than pixel intensities. By aligning closed tumor outlines with a functional shape‑alignment framework, the authors separate global deformation from residual Fourier components and encode them as frequency‑ordered tokens for an MLP classifier. This approach reduces model complexity while preserving diagnostic information. The method achieves higher performance in cross‑validation compared to standard convolutional networks.

## Semantic links
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 12 summary/topic terms overlap
- [[concepts/papers/2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningw_20260804_0021_summary.md|Summary: 2026-08-02_18-15-49Z_Cluster_AwareOver_the_AirFederatedLearningwithEner.md]] — 3 title terms overlap; 8 backlinks; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A compact multilayer perceptron (MLP) trained on frequency‑ordered shape tokens outperforms ResNet‑18 and ViT‑Tiny on BraTS 2020 tumor contours, reaching a mean balanced accuracy of 71.5%.  
- [Finding 2] The model uses far fewer parameters (2.9k–117.3k) than pixel baselines, representing at least 46× reduction in dimensionality.  
- [Finding 3] In noise‑free simulations the shape‑biased MLP consistently scores higher balanced accuracy (56.3–71.5%) while pixel models remain near 50%, demonstrating robustness to added noise.

## Methodology  
The authors first treat tumor contours as closed curves, then apply a functional shape‑alignment algorithm that computes a global deformation and a residual Fourier representation of the contour. These two components are flattened into ordered tokens representing low‑frequency and high‑frequency shape variations, which serve as input features for an MLP classifier. Model selection is performed via grouped inner validation to respect patient‑disjoint folds.

## Results  
On five‑fold patient‑disjoint cross‑validation with grouped inner validation, the proposed MLP achieves a mean balanced accuracy of 71.5%, pooled out‑of‑fold balanced accuracy of 72.4% (95 % CI: 66.4–77.8), and mean low‑grade glioma F1 of 54.9%. Compared to ResNet‑18 (65.9%) and ViT‑Tiny (63.3%), the shape‑based model is superior. In a controlled noise‑free simulation, balanced accuracy ranges from 56.3% to 71.5% for the MLP versus 50.0–52.5% for pixel models.

## Significance  
By embedding geometric information directly into the representation layer, the approach improves interpretability and scalability of glioma grading pipelines. The substantial reduction in parameters enables deployment on limited hardware while maintaining diagnostic accuracy, offering a pathway to more efficient clinical decision support systems.

## Related Concepts  
- Shape‑based inductive bias  
- Functional shape alignment  
- Fourier decomposition of curves  
- Multilayer perceptron (MLP) classification  
- Balanced accuracy metric for imbalanced class data  
- Grouped inner validation for patient‑disjoint cross‑validation
