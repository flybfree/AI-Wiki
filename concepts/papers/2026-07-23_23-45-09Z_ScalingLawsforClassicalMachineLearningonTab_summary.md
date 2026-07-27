# Summary: 2026-07-23_23-45-09Z_ScalingLawsforClassicalMachineLearningonTabularDat.md
Saved: 2026-07-26 21:32
Source: 2026-07-23_23-45-09Z_ScalingLawsforClassicalMachineLearningonTabularDat.md
Model: None

---

## Summary  
The paper investigates whether classical machine‑learning models on tabular data obey universal scaling laws that hold across many datasets and model families, a question that has been explored only at small scale. By replicating the classic learning‑curve experiments in a distributed classroom setting with 127 students, the authors collect extensive data to test power‑law fits of error versus training size. Their study reveals that while power laws are often observed, they are not robust or dataset‑independent; instead, they emerge from specific experimental protocols and model families. The work therefore advances a nuanced view of scaling laws for classical ML on tabular data.

## Key Contributions  
- [Finding 1] Power laws fit (error = a N⁻ᵇ + c) to 77.7% of training runs with R² > 0.8, dominated by tree ensembles at full data but underperforming linear models on classification tasks.  
- [Finding 2] Across five out of six model families a single family‑level exponent predicts each dataset’s curve as well as per‑dataset exponents (R² gap < 0.011), indicating approximate shared behavior, though AIC prefers unconstrained fits and about 32–58% of points collapse within ±0.5 dex.  
- [Finding 3] Replicator‑implementation variance yields a mean CV(b) = 0.144 on the fitted exponent despite fixed random seeds, driven by variations in preprocessing, encoding, and missing‑value handling.

## Methodology  
The authors assembled 18 tabular classification/regression datasets and six model families (Boosting, Random Forest, SVM, Linear/Logistic, Ridge, Lasso). Each of 127 students executed a fixed protocol on three randomly assigned subsets, generating 36 runs per student. All runs recorded training size N, fitted power‑law parameters, and cross‑validation metrics; the aggregated curves and per‑cell fits were released for reproducibility.

## Results  
- Power‑law fitting succeeded in 77.7% of cells (R² > 0.8).  
- A single family exponent explained most cross‑dataset error within a 1 % R² gap, though curve collapse was partial.  
- Ridge models were unstable when leaving one dataset out, while Lasso never fit.  
- Replication variance in the fitted exponent averaged CV(b) = 0.144.

## Significance  
These findings challenge the notion of universal scaling laws for classical ML on tabular data, showing that observed power‑law behavior is context‑dependent and sensitive to experimental details. The study provides a benchmark dataset and practical guidance (a table of N needed for error = 0.15) that can inform future research on model capacity and learning dynamics.

## Related Concepts  
- Power law scaling laws in machine learning  
- Learning curves and error vs. training size  
- Tree ensemble dominance on tabular data  
- Approximate predictive compressibility  
- Cross‑dataset generalization of hyperparameters
