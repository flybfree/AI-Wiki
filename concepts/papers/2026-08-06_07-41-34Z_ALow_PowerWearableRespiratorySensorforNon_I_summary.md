# Summary: 2026-08-06_07-41-34Z_ALow_PowerWearableRespiratorySensorforNon_Invasive.md
Saved: 2026-08-06 22:06
Source: 2026-08-06_07-41-34Z_ALow_PowerWearableRespiratorySensorforNon_Invasive.md
Model: None

---

## Summary  
The paper proposes a low‑power wearable respiratory sensor that captures small abdominal deformations using a force‑sensitive resistor (FSR) integrated into an abdominal belt and a custom Bluetooth Low Energy acquisition board, enabling real‑time non‑invasive monitoring of stress across everyday activities. The system combines a mechanical holder with the FSR to transfer breathing expansion directly to the sensor without analog amplification, allowing reliable signal extraction even when the user moves lightly.

## Key Contributions  
- A compact, low‑power wearable platform that detects respiratory changes through small body deformations without requiring analog amplification.  
- Demonstrated that the sensor maintains consistent amplitude variations and peak‑to‑peak timing of breathing signals under both stationary and light‑movement conditions.  
- Achieved 88.0 % test accuracy in distinguishing stress‑induction phases from relaxation phases using interpretable time‑domain features.

## Methodology  
The authors designed a force‑sensitive resistor embedded in an abdominal belt, coupled to a mechanical holder that translates the user’s abdominal expansion into electrical resistance changes. Data acquisition is performed by a custom Bluetooth Low Energy board, which streams raw signals to a processing pipeline. The pipeline extracts time‑domain features such as amplitude and peak timing from the respiratory waveform, then applies standard classifiers (e.g., SVM) to label each phase of a five‑phase stress‑induction protocol. Measurements were taken from 12 participants across multiple breathing patterns and body positions.

## Results  
In stationary conditions, the recorded signals exhibit clear amplitude changes and recurring peak‑to‑peak timing that are invariant across different breathing maneuvers. When light movement is introduced, baseline shifts are largely mitigated by the mechanical coupling, preserving signal integrity. The best‑performing model reached 88 % accuracy on a held‑out test set, confirming that the extracted respiratory features reliably separate stress‑induction phases from relaxation phases.

## Significance  
This work provides a practical solution for continuous, non‑invasive affective computing by offering a wearable sensor that can monitor respiration and infer emotional states in real time without intrusive measurements. The low power consumption and robustness to minor motion make it suitable for integration into everyday devices such as smart clothing or health monitors.

## Related Concepts  
- Respiratory signal as a physiological window into stress.  
- Force‑sensitive resistor (FSR) sensing of body deformation.  
- Bluetooth Low Energy wireless acquisition for wearable data streaming.  
- Mechanical coupling to translate physical expansion into electrical signals.  
- Time‑domain feature extraction and classification for affect recognition.  
- Wearable health technology and affective computing applications.
