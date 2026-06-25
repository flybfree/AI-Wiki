# Summary: 2026-06-24_17-52-57Z_Across_processweldingpenetrationstatuspredictional.md
Saved: 2026-06-24 22:02
Source: 2026-06-24_17-52-57Z_Across_processweldingpenetrationstatuspredictional.md
Model: None

---


## Summary  
The paper proposes an unsupervised domain adaptation framework combined with gradual source domain expansion to predict weld penetration status across laser and TIG welding processes, tackling the challenge of model transfer when physical mechanisms differ. It demonstrates that this approach outperforms supervised baselines both within‑process (TIGFH, LSPS) and between‑process (TIG→Laser, Laser→TIG). The method aligns feature distributions while preserving class discriminability, thereby reducing relabeling costs and enhancing monitoring versatility.  

## Key Contributions  
- [Finding 1] Achieves average accuracies of 90.65 % on TIGFH and 90.72 % on LSPS in same‑process transfer, surpassing a supervised baseline by roughly 35–38 %.  
- [Finding 2] In cross‑process scenarios (TIG→Laser and Laser→TIG) reaches 80.48 % and 81.13 %, improving over the baseline by about 43 % each.  
- [Finding 3] UMAP visualizations confirm that the model learns domain‑invariant features while maintaining clear class boundaries.  

## Methodology  
The authors employ unsupervised domain adaptation (UDA) to align the feature space between source welding processes and target processes without requiring labeled data on the target. They integrate gradual source domain expansion (GSDE), which iteratively augments the source dataset, enabling the neural network classifier to converge toward a shared representation that captures both process‑specific and universal characteristics.  

## Results  
Experiments on dedicated TIGFH and LSPS datasets report the reported accuracies; UMAP plots illustrate overlapping feature clusters across domains. The supervised baseline models achieve lower performance (≈50 % versus ≈90 %), highlighting the advantage of the proposed unsupervised approach.  

## Significance  
This method lowers the need for costly relabeling when transferring predictions to new welding processes, enabling robust, versatile monitoring systems that can be applied across different physical mechanisms without extensive retraining. It broadens the applicability of intelligent welding inspection tools and reduces operational risk in multi‑process environments.  

## Related Concepts  
Unsupervised domain adaptation, gradual source domain expansion, UMAP visualization, deep learning classification, cross‑process transfer learning, laser welding penetration prediction, TIG welding penetration prediction.
