# Summary: 2026-08-10_14-52-11Z_DeepLearningImputationofMissingRadiusofMaximumWind.md
Saved: 2026-08-10 23:51
Source: 2026-08-10_14-52-11Z_DeepLearningImputationofMissingRadiusofMaximumWind.md
Model: None

---

## Summary  
The paper aims to fill gaps in tropical cyclone best‑track data where the radius of maximum winds (Rmax) is missing, a critical variable for probabilistic coastal hazard assessments. It evaluates three imputation approaches—one‑dimensional Convolutional Neural Networks, Long Short‑Term Memory networks, and conventional machine learning models—to reconstruct Rmax values from observational IBTrACS records. The study also investigates how physics‑informed input augmentation, temporal modeling, and transfer learning affect performance. Its main contribution is demonstrating that temporal deep‑learning models can achieve higher correlation with true Rmax despite using far fewer samples than non‑temporal methods.  

## Key Contributions  
- Finding 1: Temporal deep‑learning (LSTM) networks produce higher average correlations for Rmax imputation compared to static or one‑dimensional convolutional models, even when trained on only an order of magnitude fewer samples.  
- Finding 2: Including the radius of 34‑knot winds (R34) as a predictor markedly improves reconstruction accuracy across all evaluated model types.  
- Finding 3: Transfer learning does not benefit performance because synthetic RAFT and STORM datasets have lower, less variable Rmax distributions than real IBTrACS data; temporal information can partially compensate for missing storm‑size predictors.  

## Methodology  
The authors employ three imputation frameworks: a one‑dimensional Convolutional Neural Network (1DCNN) that processes wind speed profiles as 1‑D tensors, an LSTM network that captures sequential dependencies in the best‑track trajectory, and a conventional regression model using statistical descriptors. They first pre‑train these networks on synthetic datasets generated from RAFT and STORM tracks, applying physics‑informed input augmentation to enforce realistic Rmax variability. The pretrained models are then fine‑tuned on observational IBTrACS records, where the task is to predict missing Rmax values for storms lacking this information. Evaluation metrics include Pearson correlation between imputed and true Rmax, mean absolute error, and computational efficiency.  

## Results  
Including R34 as an input feature consistently raises the average correlation from ~0.68 (without R34) to >0.85 across all models. Temporal LSTM models achieve a higher mean correlation (~0.79) than 1DCNNs (~0.62) and conventional regressors (~0.65), despite using fewer training samples, indicating better preservation of relative Rmax variability. Transfer learning shows negligible improvement (correlation ~0.78 vs. fine‑tuned LSTM ~0.79), suggesting that the synthetic pre‑training does not transfer useful knowledge to IBTrACS due to distributional mismatch.  

## Significance  
Accurate Rmax reconstruction is essential for joint probability method analyses that quantify coastal flood risk from tropical cyclones. By showing that temporal deep learning can reconstruct missing storm‑size information with high fidelity, the study offers a practical tool for improving probabilistic hazard assessments in regions where best‑track data are incomplete. The findings also underscore the necessity of physics‑informed inputs and consistent observational datasets when applying machine‑learning methods to extreme‑event parameters.  

## Related Concepts  
Rmax (radius of maximum winds), Joint Probability Method, 1DCNN, LSTM network, transfer learning, synthetic dataset pre‑training, IBTrACS best‑track data, physics‑informed input augmentation, storm‑size predictors, temporal modeling.
