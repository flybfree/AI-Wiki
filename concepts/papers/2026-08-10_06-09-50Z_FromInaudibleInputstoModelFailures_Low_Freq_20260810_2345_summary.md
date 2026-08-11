# Summary: 2026-08-10_06-09-50Z_FromInaudibleInputstoModelFailures_Low_FrequencySa.md
Saved: 2026-08-10 23:45
Source: 2026-08-10_06-09-50Z_FromInaudibleInputstoModelFailures_Low_FrequencySa.md
Model: None

---

## Summary  
Large audio‑language models (LALMs) can process low‑frequency signals that are inaudible to humans yet may still affect model behavior, a risk that has not been systematically examined. This paper introduces Intermittent Low‑Frequency Lockout (ILL), a black‑box red‑team technique that generates such signals and evaluates their impact on LALM performance. The authors also propose Distributional Requery Guard (DRG) to detect distribution shifts and trigger clean reacquisition for semantic recovery. Experiments across six LALMs show that low‑frequency attacks can degrade accuracy by up to 67 % while remaining barely audible, highlighting a previously overlooked safety vulnerability.

## Key Contributions  
- [Finding 1] Low‑frequency inputs, though inaudible, can cause significant model failures in LALMs.  
- [Finding 2] The ILL framework reduces accuracy by up to 67 % using near‑inaudible waveforms generated via Sentence Attention Scale Estimation and Frequency Confusion Transfer.  
- [Finding 3] DRG recovers performance, raising attacked accuracy from 28.5 % to 46.1 % after clean reacquisition.

## Methodology  
The authors adopt a universal waveform template that encodes low‑frequency spectral variation while maintaining continuous phase. Sentence Attention Scale Estimation identifies active intervals where the model’s attention is most vulnerable, and Frequency Confusion Transfer merges these intervals into a single inaudible signal. ILL operates as a black‑box red‑team test: it feeds the generated waveform to LALMs without revealing its composition and measures performance degradation. DRG monitors distributional shifts between clean and attacked inputs; if a shift is detected, it prompts a second recording to restore semantic fidelity.

## Results  
Across six LALM models and multiple audio understanding tasks, ILL caused an average accuracy drop of 67 % relative to baseline. Human listeners rated the generated waveform as audibility 1.33 on a scale where clean audio scores ~1.17, indicating near‑inaudibility. DRG intervention restored attacked accuracy to 46.1 %, up from 28.5 % without reacquisition, demonstrating its effectiveness in mitigating low‑frequency attacks.

## Significance  
These findings reveal a critical safety risk for LALMs that could be exploited by adversarial audio inputs, prompting the need for robust detection and recovery mechanisms. The work establishes ILL as a universal evaluation protocol and DRG as a practical guardrail, laying groundwork for future research into resilient audio‑language systems.

## Related Concepts  
low‑frequency signals, inaudible inputs, red teaming, Sentence Attention Scale Estimation, Frequency Confusion Transfer, distributional requery guard, LALMs.
