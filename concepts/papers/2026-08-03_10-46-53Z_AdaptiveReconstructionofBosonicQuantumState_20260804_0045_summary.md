# Summary: 2026-08-03_10-46-53Z_AdaptiveReconstructionofBosonicQuantumStates.md
Saved: 2026-08-04 00:45
Source: 2026-08-03_10-46-53Z_AdaptiveReconstructionofBosonicQuantumStates.md
Model: None

---

## Summary  
The paper proposes an adaptive reconstruction technique that enables efficient estimation of the fidelity of bosonic quantum states across a family of states rather than against a single reference point. By reconstructing the underlying Wigner function from only a small number of measurements, the method reduces the measurement burden while preserving phase‑space information such as displacements and rotations. The authors combine a physics‑informed parametric model with Bayesian inference, bootstrap resampling, and active learning to iteratively choose the most informative sampling points in phase space. This approach has been implemented experimentally on circuit quantum electrodynamics platforms using Schrödinger cat states with amplitudes α∈[1,3].  

## Key Contributions  
- Adaptive reconstruction that estimates fidelity across a family of bosonic states rather than a single target.  
- Integration of Bayesian inference and active learning to select optimal measurement points in phase space.  
- Demonstrated experimental robustness on cat states with amplitudes 1–3, achieving reproducible results within minutes despite mismatched priors.  

## Methodology  
The authors model the Wigner function using a parametric representation that captures displacement and rotation degrees of freedom. Bayesian inference propagates prior knowledge while fitting measurement data, bootstrap resampling estimates uncertainty, and active learning selects points that maximize information gain at each iteration. The loop repeats until convergence or a predefined time limit is reached, allowing rapid reconstruction without exhaustive state tomography.  

## Results  
On cat states with amplitudes α=1–3 the adaptive method required only ~20‑30 measurements per state to achieve fidelity estimates within a few percent of ground truth, compared with >100 measurements for standard tomography. The reconstructed fidelities remained stable under large displacements and rotations even when the prior was mismatched. These fidelities were subsequently fed into a closed‑loop optimal control experiment, enabling real‑time adaptation of bosonic quantum states without full state reconstruction.  

## Significance  
This work reduces the measurement burden for bosonic state characterization, making it scalable for quantum information processing where phase‑space transformations are common. By providing fast, adaptive fidelity estimates, the method supports autonomous optimisation of quantum states, eliminating the need for costly and time‑consuming tomography procedures. The approach therefore opens a pathway to more efficient control loops in photonic and superconducting platforms.  

## Related Concepts  
Wigner function, bosonic Hilbert space, state tomography, active learning, Bayesian inference, circuit QED, cat states, phase‑space translation/rotation invariance, optimal control, parametric modelling.
