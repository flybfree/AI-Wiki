# Summary: 2026-08-05_01-14-58Z_Real_timeprobabilistictsunamiforecastingviagenerat.md
Saved: 2026-08-06 00:10
Source: 2026-08-05_01-14-58Z_Real_timeprobabilistictsunamiforecastingviagenerat.md
Model: None

---

## Summary  
The paper proposes a probabilistic ensemble model based on conditional diffusion models to forecast onshore tsunami inundation while quantifying prediction uncertainty, moving beyond the deterministic predictions of current machine‑learning systems. It seeks to reconcile high spatial accuracy with calibrated uncertainty for near‑field megathrust‑generated tsunamis. The authors validate their approach against the 2011 Tohoku earthquake data, showing that uncertainty diminishes over time and inundation depth is predicted correctly. This work demonstrates a shift from deterministic to probabilistic tsunami forecasting.

## Key Contributions  
- [Finding 1] A conditional diffusion model can generate realistic inundation maps while providing calibrated probability estimates for each location.  
- [Finding 2] An ensemble of multiple model outputs yields uncertainty that systematically decreases as the event progresses, improving calibration.  
- [Finding 3] The framework enables a probabilistic early‑warning system that reduces false safety perception and supports risk‑aware communication.

## Methodology  
The authors constructed a conditional diffusion generator trained on historical inundation data from the 2011 Tohoku earthquake. The model conditions on seismic source information, time since rupture, and depth to generate probability maps of inundation extent and depth. By sampling many forward passes, an ensemble is formed; each sample represents a plausible future state, and the spread among samples quantifies uncertainty. Uncertainty estimates are updated iteratively as new data (e.g., tide gauge readings) become available.

## Results  
Validation against ground‑truth inundation maps shows spatial root‑mean‑square error below 5 m for depth predictions and near‑perfect capture of the flooded area. Early forecasts exhibit higher variance that contracts to near zero within minutes, matching the expected decreasing uncertainty trend. The ensemble improves calibration by reducing false alarms, as the probability of exceeding a safety threshold aligns closely with observed risk.

## Significance  
By introducing uncertainty quantification into real‑time tsunami forecasting, the model allows authorities to communicate probabilistic safety margins rather than binary safe/unsafe boundaries. This reduces public panic and enables more informed evacuation decisions. The work showcases generative AI’s capacity to transform deterministic disaster warnings into a calibrated, actionable risk assessment.

## Related Concepts  
Conditional diffusion models, ensemble learning, probabilistic forecasting, onshore inundation mapping, megathrust earthquakes, early warning systems, uncertainty quantification, calibration, spatial‑temporal modeling.
