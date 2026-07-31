# Summary: 2026-07-30_11-49-28Z_TemporalPoisoning_Clean_LabelBackdoorsviaEventRedi.md
Saved: 2026-07-30 21:48
Source: 2026-07-30_11-49-28Z_TemporalPoisoning_Clean_LabelBackdoorsviaEventRedi.md
Model: None

---

## Summary  
The paper introduces a new class of backdoor attacks on spiking neural networks (SNNs) called temporal poisoning, which operates without relabeling any training samples. By applying a fixed timestamp transformation only to the target‑class streams, the attack preserves the per‑pixel and per‑polarity event counts while reshuffling the sequence that the SNN processes. This clean‑label approach yields an accuracy of 100 % in the most aggressive configurations across three neuromorphic datasets and both convolutional and transformer‑based SNNs. The work also provides a model‑free detector based on per‑step event mass, revealing how defenses collapse when they ignore temporal information.

## Key Contributions  
- [Finding 1] Temporal poisoning achieves perfect attack success (ASR = 1.00) by redistributing events across time without altering labels or event counts.  
- [Finding 2] The attack works uniformly on both convolutional and transformer‑based SNNs, demonstrating its robustness to network architecture differences.  
- [Finding 3] A model‑free detector that monitors per‑step event mass can identify the temporal transformation, exposing the limits of rate‑collapsed defenses.

## Methodology  
The authors first defined a clean‑label poisoning scheme where a timestamp shift is applied solely to target‑class training streams. They then measured the resulting event distribution and compared it with normal data using per‑pixel, per‑polarity event counts. Experiments were conducted on three neuromorphic datasets (e.g., MNIST‑SNN, CIFAR‑10‑SNN, and a custom video dataset) with both CNN and transformer SNN backbones. Poison‑budget and trigger‑shape ablations were performed to quantify the impact of the transformation. Defenses such as time‑axis collapse and feature‑space detectors were evaluated, followed by design of a detector that computes event mass per step.

## Results  
Across all experiments, the temporal poisoning attack achieved an ASR of 100 % in the strongest configurations, confirming its effectiveness. Ablation studies showed that reducing poison budget or altering trigger shape significantly degrades performance, while defenses that ignore temporal ordering remained blind. The model‑free detector identified the event redistribution with high precision, highlighting how rate‑collapsed methods cannot capture the attack’s stealth.

## Significance  
Temporal poisoning demonstrates that clean‑label backdoors can be as effective as traditional dirty‑label attacks on SNNs, challenging existing security assumptions for neuromorphic systems. It underscores the importance of preserving temporal structure in event data and motivates the development of detectors that respect time‑based information.

## Related Concepts  
- Clean‑label poisoning (no label changes)  
- Temporal aggregation / timestamp transformation  
- Event redistribution across per‑pixel, per‑polarity counts  
- ASR (Attack Success Rate)  
- Neuromorphic event data  
- Convolutional and transformer SNNs  
- Model‑free detector based on per‑step event mass  
- Feature‑space backdoor detection  
- Rate‑collapsed defenses
