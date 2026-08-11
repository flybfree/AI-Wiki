# Summary: 2026-08-10_06-09-50Z_FromInaudibleInputstoModelFailures_Low_FrequencySa.md
Saved: 2026-08-10 23:38
Source: 2026-08-10_06-09-50Z_FromInaudibleInputstoModelFailures_Low_FrequencySa.md
Model: None

---

## Summary  
The paper investigates a previously overlooked safety risk in large audio‑language models (LALMs) by demonstrating that low‑frequency signals, which are inaudible to humans, can cause substantial performance degradation. To address this issue, the authors introduce Intermittent Low‑Frequency Lockout (ILL), an inaudible red‑team test that evaluates model vulnerability using a universal waveform template in a black‑box setting. They also propose Distributional Requery Guard (DRG) as a mitigation strategy that detects distribution shifts and triggers a clean reacquisition to recover semantics. Across six LALMs and multiple tasks, ILL reduces accuracy by up to 67 % while receiving an average human audibility rating of 1.33, indicating near‑threshold inaudibility.

## Key Contributions  
- Finding 1: Low‑frequency inputs can cause a sharp drop in model accuracy, reaching as high as 67 % reduction.  
- Finding 2: The generated waveforms are barely audible (mean rating ≈ 1.33), confirming they are effectively inaudible to humans.  
- Finding 3: Applying DRG improves the attacked accuracy from 28.5 % back to 46.1 %, showing that clean reacquisition can substantially offset the loss.

## Methodology  
The authors first construct a low‑frequency waveform using Frequency Confusion Transfer, which aligns with variations in corpus spectral content while maintaining continuous phase. Sentence Attention Scale Estimation identifies active intervals where the model should be most vulnerable. ILL then feeds this waveform to LALMs in a black‑box red‑team scenario, measuring performance loss. DRG works by monitoring distributional shifts between clean and attacked data; when shifts are detected, it requests a second recording to restore the original distribution.

## Results  
Experimental results across six LALMs on diverse audio‑understanding tasks show that ILL consistently reduces accuracy by 30–67 % points. Human listeners rate the inaudible waveform at an average of 1.33, which is close to the threshold of 1.17 for clean audio, indicating near‑inaudibility. DRG mitigates this effect: after a clean reacquisition, attacked accuracy rises from 28.5 % to 46.1 %, demonstrating that the guard effectively restores model performance.

## Significance  
These findings reveal a critical safety gap in LALMs—low‑frequency, inaudible signals can trigger failures without any perceptible input to users. By quantifying this risk and providing DRG as a practical mitigation, the work lays a foundation for more robust audio understanding systems that can tolerate subtle, non‑perceptual perturbations.

## Related Concepts  
LALMs, low‑frequency inputs, inaudible waveforms, red teaming, Sentence Attention Scale Estimation, Frequency Confusion Transfer, Distributional Requery Guard, spectral variation, black‑box evaluation.
