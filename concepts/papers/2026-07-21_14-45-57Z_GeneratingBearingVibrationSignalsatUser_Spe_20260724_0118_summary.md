# Summary: 2026-07-21_14-45-57Z_GeneratingBearingVibrationSignalsatUser_SpecifiedF.md
Saved: 2026-07-24 01:18
Source: 2026-07-21_14-45-57Z_GeneratingBearingVibrationSignalsatUser_SpecifiedF.md
Model: None

---

## Summary  
The paper tackles the scarcity of intermediate fault‑probability samples in bearing‑vibration datasets, which are crucial for realistic maintenance‑decision studies. It proposes two methods to generate synthetic signals whose predicted fault probabilities match user‑specified targets (0.25, 0.50, 0.75). The first is a training‑based Probability‑Regularized GAN (PR‑GAN) that edits real signals via a residual generator while aligning the classifier output with the target probability; the second is a per‑sample counterfactual (CF) procedure that directly optimizes each input to achieve the target probability.  

## Key Contributions  
- The authors introduce PR‑GAN, a WGAN‑GP based framework that regularizes the GAN loss toward a user‑specified fault probability while preserving signal fidelity.  
- They develop a training‑free counterfactual (CF) method that optimizes each individual bearing vibration record to reach any target probability with minimal L1 change and 100 % success on retained samples.  
- Empirically, the CF approach achieves mean absolute error of 0.005–0.008 versus PR‑GAN’s 0.046–0.059, demonstrating superior probability alignment despite higher runtime.  

## Methodology  
The authors treat a heterogeneous ensemble classifier as a fixed probability oracle; they generate signals by either (i) training a GAN to push the classifier output toward a target probability using gradient‑penalty regularization and residual editing, or (ii) applying per‑sample counterfactual optimization that directly adjusts the input signal to satisfy the same constraint. Both methods evaluate mean absolute target‑probability error, total variation in time domain, and log‑PSD differences.  

## Results  
Experiments on CWRU and Paderborn bearing datasets show CF outperforms PR‑GAN: MAE 0.005–0.008 vs 0.046–0.059; success rates 1.000 % (CF) vs 0.501–0.680 % (PR‑GAN). CF also yields smaller average L1 changes, while PR‑GAN reports lower reported runtime in some cases.  

## Significance  
Providing synthetic bearing vibration data with intermediate fault probabilities enables more realistic evaluation of maintenance decision boundaries and reduces reliance on rare gray‑zone samples; the counterfactual method offers a practical, high‑accuracy solution without retraining models.  

## Related Concepts  
- Generative Adversarial Networks (GAN) and Wasserstein GAN‑GP regularization  
- Probability regularization in generative modeling  
- Counterfactual optimization for per‑sample signal adjustment  
- Fault probability estimation in vibration analysis
