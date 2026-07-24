# Summary: 2026-07-22_11-12-07Z_Zero_ShotHeartRateVariabilityForecastingfromConsum.md
Saved: 2026-07-24 01:47
Source: 2026-07-22_11-12-07Z_Zero_ShotHeartRateVariabilityForecastingfromConsum.md
Model: None

---

## Summary  
The paper aims to forecast short‑term heart rate variability (HRV) from fragmented wearable data using time series foundation models without fine‑tuning, introducing a variability‑preserving imputation method. It evaluates three TSFMs—TimesFM, Chronos, and MOIRAI—against traditional baselines on real‑world data collected from 49 healthy individuals. The results show that TSMFs achieve low MASE errors (0.81–0.87) across both 32‑step and 64‑step horizons, outperforming baseline methods. Up to a two‑hour forecast horizon, the study establishes a practical baseline for clinical deployment.

## Key Contributions  
- Introduces variability‑preserving imputation that augments linear interpolation with locally adaptive stochastic noise.  
- Demonstrates that three time series foundation models (TimesFM, Chronos, MOIRAI) can forecast HRV from wearable data without fine‑tuning, achieving MASE 0.81–0.87.  
- Shows up to a two‑hour horizon the TSFMs outperform traditional baselines, establishing a practical baseline for clinical use.

## Methodology  
The authors collected HRV signals from 49 healthy participants using consumer wearables, which are fragmented and contain artifacts. They apply their imputation method to fill gaps while preserving physiological dynamics. Forecasting is performed with three TSFMs (TimesFM, Chronos, MOIRAI) and three baselines (Mean, Exponential Smoothing, EWMA). Both 32‑step and 64‑step context lengths are evaluated.

## Results  
The TSMFs achieve an average MASE of 0.81–0.87 across all models and horizons, with Chronos and TimesFM as the top performers; MOIRAI shows limited gains over baselines. Traditional baselines have higher errors (MASE ~1.2). Forecast accuracy remains stable up to a two‑hour horizon.

## Significance  
By achieving low MASE without fine‑tuning, the study demonstrates that foundation models can provide clinically useful HRV forecasts from real‑world wearable data, enabling early detection of autonomic dysfunction and adverse cardiac events with lead time up to two hours. This reduces reliance on manual calibration and personalizes monitoring.

## Related Concepts  
- Heart Rate Variability (HRV)  
- Time Series Foundation Models  
- MASE (Mean Absolute Scaled Error)  
- Consumer wearables  
- Forecasting horizons
