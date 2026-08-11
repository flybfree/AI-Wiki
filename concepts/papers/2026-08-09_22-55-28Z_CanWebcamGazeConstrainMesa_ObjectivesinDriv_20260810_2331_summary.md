# Summary: 2026-08-09_22-55-28Z_CanWebcamGazeConstrainMesa_ObjectivesinDrivingMode.md
Saved: 2026-08-10 23:31
Source: 2026-08-09_22-55-28Z_CanWebcamGazeConstrainMesa_ObjectivesinDrivingMode.md
Model: None

---

## Summary  
This paper asks whether human gaze patterns captured by webcam‑based eye tracking can serve as a privileged input that constrains mesa‑objectives in autonomous driving hazard models. By comparing the performance of models trained with and without gaze data across multiple experiments, the authors find no statistically significant benefit, attributing the failure to the coarse precision of the WebGazer instrument rather than any intrinsic value of gaze information.

## Key Contributions  
- No experiment yields a statistically significant improvement from adding gaze data (p = 0.919, 0.578, and 0.667).  
- A geometric analysis reveals that WebGazer’s reported error ranges from ~130 to ~257 px, which exceeds 93 % of the median hazard‑object size (≈36 px), making object‑level gaze attribution physically impossible.  
- The study demonstrates that instrument precision, not gaze patterns, is the limiting factor for using eye tracking in driving models.

## Methodology  
The authors collected 137,663 frame‑level gaze samples synchronized with hazard annotations from 388 real dashcam clips. They evaluated two calibration protocols (9‑point/45‑click and 11‑point/440‑click), two model architectures (Random Forest and causal Transformer), and five random seeds per experiment, using paired t‑tests to assess whether gaze data improved performance.

## Results  
Paired t‑tests across all configurations produced p‑values of 0.919, 0.578, and 0.667, none of which are below the conventional α = 0.05 threshold. The geometric analysis confirms that the spatial error introduced by WebGazer is far larger than typical hazard objects, rendering any gaze‑based constraint ineffective.

## Significance  
The findings caution against treating webcam gaze as a reliable source of privileged information in safety‑critical AI systems; instead, they underscore the need for higher‑resolution eye‑tracking hardware or alternative constraints. The work also highlights how instrument precision can dominate model performance when it is orders of magnitude worse than the target data scale.

## Related Concepts  
- Mesa objectives (spurious internal goals)  
- Instrument precision and measurement error  
- WebGazer.js eye‑tracking library  
- Calibration protocols for gaze capture  
- Causal Transformer architectures for driving models  
- Paired t‑tests for hypothesis testing in experimental design
