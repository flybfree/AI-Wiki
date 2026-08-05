# Summary: 2026-07-27_18-08-33Z_Fast_accurate_anddifferentiable_aneural_networksur.md
Saved: 2026-07-28 22:22
Source: 2026-07-27_18-08-33Z_Fast_accurate_anddifferentiable_aneural_networksur.md
Model: None

---

## Summary  
The paper introduces a neural‑network surrogate for the NRSur7dq4 waveform model of precessing binary black hole mergers, aiming to deliver fast, accurate, and differentiable inference. It trains separate multilayer perceptrons (MLPs) for each constituent quantity so that the combined network reproduces the reference waveform with high fidelity across a wide parameter space. The surrogate is validated on 10 000 waveforms spanning q∈[1,4] and χ_{A,B}≤0.8, achieving median sky‑averaged frequency‑domain errors of 8×10⁻⁵ to 1.7×10⁻⁴ with 95th percentiles below 10⁻³. On an NVIDIA L40S GPU the end‑to‑end evaluation of a single waveform is about 1 ms, roughly ten times faster than the reference C implementation and sustaining ~140× higher batch throughput at size 64.

## Semantic links
- [[concepts/papers/2026-08-03_09-27-33Z_FAST_GS_FrequencyAwareSpace_timeGaussianSpl_20260804_0036_summary.md|Summary: 2026-08-03_09-27-33Z_FAST_GS_FrequencyAwareSpace_timeGaussianSplattingf.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.07
- [[concepts/papers/2026-08-03_09-27-33Z_FAST_GS_FrequencyAwareSpace_timeGaussianSpl_summary.md|Summary: 2026-08-03_09-27-33Z_FAST_GS_FrequencyAwareSpace_timeGaussianSplattingf.md]] — 4 title terms overlap; 11 summary/topic terms overlap; semantic match 0.07
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 4 title terms overlap; 11 summary/topic terms overlap; semantic match 0.04

## Key Contributions  
- [Finding 1] A fully differentiable neural‑network surrogate that reproduces NRSur7dq4 waveforms to median sky‑averaged frequency‑domain errors of 8 × 10⁻⁵–1.7 × 10⁻⁴, with 95th percentiles below 10⁻³.  
- [Finding 2] The surrogate is up to ten times faster than the LALSimulation C implementation and sustains about one hundred forty times higher throughput at batch size 64 on an NVIDIA L40S GPU.  
- [Finding 3] The pipeline combines validated waveform accuracy with a differentiable inference framework, enabling Fisher information matrices, GPU‑accelerated nested sampling, gradient‑based MCMC and importance sampling.

## Methodology  
The authors decompose the precessing binary black hole waveform into independent components such as inspiral phase, merger, and ringdown. Each component is trained separately using a multilayer perceptron whose weights are learned from the full NRSur7dq4 model evaluated on 10 000 waveforms covering q∈[1,4] and χ_{A,B}≤0.8 with total masses between 60 and 300 M⊙. The trained MLPs are then combined in a differentiable pipeline implemented in JAX, allowing the surrogate to be evaluated end‑to‑end on GPU hardware.

## Results  
Median sky‑averaged frequency‑domain mismatches range from 8.0 × 10⁻⁵ to 1.7 × 10⁻⁴ across the parameter space, with 95th percentiles below 10⁻³. On an NVIDIA L40S GPU a single waveform is evaluated in about one millisecond end‑to‑end, roughly ten times faster than the reference C implementation of NRSur7dq4, and the batch throughput reaches approximately one hundred forty times that of the reference at batch size 64.

## Significance  
This work bridges high‑fidelity numerical relativity waveforms with real‑time inference by delivering a surrogate that is both accurate and computationally efficient. Its differentiability opens new avenues for Bayesian parameter estimation, enabling gradient‑based samplers such as nested sampling, MCMC and importance sampling without sacrificing waveform fidelity.

## Related Concepts  
precessing binary black hole merger waveform model (NRSur7dq4), neural network surrogates, differentiable programming, JAX, GPU acceleration, Fisher information matrix, nested sampling, MCMC, importance sampling, LALSimulation.
