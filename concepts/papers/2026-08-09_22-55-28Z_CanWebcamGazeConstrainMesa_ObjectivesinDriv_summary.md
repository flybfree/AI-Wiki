# Summary: 2026-08-09_22-55-28Z_CanWebcamGazeConstrainMesa_ObjectivesinDrivingMode.md
Saved: 2026-08-10 23:30
Source: 2026-08-09_22-55-28Z_CanWebcamGazeConstrainMesa_ObjectivesinDrivingMode.md
Model: None

---

## Summary  
The paper investigates whether human gaze patterns captured by a webcam‑based eye‑tracking system (WebGazer.js) can act as privileged information that would limit the formation of mesa objectives in autonomous driving hazard‑detection models. By treating gaze data as an additional input, the authors aim to see if it reduces spurious correlations and improves model calibration. Their contribution is threefold: they demonstrate that gaze does not meaningfully constrain mesa‑objectives, they quantify why this is the case (instrumental error), and they provide a rigorous statistical evaluation across multiple configurations.  

## Key Contributions  
- No experiment shows a statistically significant improvement in model performance when gaze data are added (p = 0.919, 0.578, 0.667).  
- The geometric error of WebGazer (~130–257 px) far exceeds the median size of detected hazard objects (≈36 px), making it physically impossible to attribute gaze to specific hazards at this resolution.  
- Across two calibration protocols, two model architectures, and five random seeds, gaze data never constrain mesa‑objective formation.  

## Methodology  
The authors gathered 137,663 frame‑level gaze samples synchronized with hazard annotations from 388 real dashcam clips using WebGazer.js. They employed two calibration schemes (9‑point/45‑click and 11‑point/440‑click) to produce gaze coordinates, then paired these with the corresponding model outputs for Random Forest and causal Transformer architectures evaluated on five random seeds each. All experiments were analyzed with paired t‑tests to assess whether gaze contributed beyond chance.  

## Results  
The primary experimental finding is that the p‑values for all tests exceed 0.1, indicating no significant difference between models trained with or without gaze input. A geometric analysis confirms that WebGazer’s reported positional error (130–257 px) is larger than 93 % of hazard object sizes, rendering any gaze‑based attribution moot at the instrument’s precision level. Consequently, the hypothesis that gaze can constrain mesa objectives is empirically refuted.  

## Significance  
Understanding why gaze does not improve model behavior matters because it clarifies a common source of overfitting: reliance on noisy or misaligned sensor data can create spurious learning patterns rather than genuine hazard awareness. By quantifying the mismatch between instrument resolution and object size, the study helps researchers design more robust training pipelines that avoid instrumental bias.  

## Related Concepts  
- Mesa objectives (internal goals learned from spurious correlations)  
- Instrument precision and error margins in sensor data  
- WebGazer.js eye‑tracking system for gaze capture  
- Autonomous driving hazard detection models  
- Random Forest and causal Transformer architectures
