# Summary: 2026-07-28_10-26-09Z_FromTrainingtoDeployment_Post_HocCausalFeatureIden.md
Saved: 2026-07-28 22:43
Source: 2026-07-28_10-26-09Z_FromTrainingtoDeployment_Post_HocCausalFeatureIden.md
Model: None

---

## Summary  
The paper proposes a post‑hoc diagnostic called the Normalised Sensitivity Ratio (NSR) that identifies which features drive a trained model causally versus spuriously when environments undergo structured shifts. It does so without requiring access to training data, operating under a regime where only spurious feature means shift while causal mechanisms stay constant. The NSR is defined as the squared coefficient of variation of per‑environment sensitivity across environments.

## Key Contributions  
- [Finding 1] Theorem 1 proves exact identification of causal features via NSR under a linear structural causal model with three or more non‑degenerate environments.  
- [Finding 2] The authors characterize failure modes: weak shifts leading to O(ε⁴) collapse, degenerate geometry causing O((1−α)⁴) proxy attenuation, and provide quantitative criteria for regime assessment.  
- [Finding 3] Finite‑sample rates are O_p(n⁻¹) under the null and O_p(n⁻¹²) under the alternative, demonstrating statistical efficiency.

## Methodology  
The authors treat each environment as a distribution where only spurious features shift. They compute model sensitivity (gradient magnitude) for every feature in each environment, then evaluate NSR as the ratio of variance to mean squared sensitivity across environments. Under the SCM assumptions, causal features produce constant sensitivity, so their contribution vanishes from NSR variance, leaving only spurious features that track shift and increase NSR.

## Results  
Theoretical analysis yields exact identification; experiments on synthetic data achieve AUROC = 1.0 when the structured‑shift regime holds. Five model families show consistent ranking (Kendall τ ≥ 0.529). On real bike‑sharing data, six of eight causal features are recovered with Precision@7 = 0.75 without retraining.

## Significance  
NSR offers a model‑agnostic, post‑hoc tool to diagnose feature importance in deployed systems where training provenance is unavailable, crucial for trustworthy AI across multi‑site clinical or genomics pipelines. Its theoretical guarantees and finite‑sample rates provide concrete performance metrics for practitioners.

## Related Concepts  
- Normalised Sensitivity Ratio (NSR)  
- Structured‑shift regime  
- Linear Structural Causal Model (SCM)  
- Post‑hoc causal feature identification  
- Coefficient of variation  
- Kendall τ ranking
