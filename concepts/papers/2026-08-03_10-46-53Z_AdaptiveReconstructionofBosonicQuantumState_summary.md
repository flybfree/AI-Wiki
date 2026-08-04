# Summary: 2026-08-03_10-46-53Z_AdaptiveReconstructionofBosonicQuantumStates.md
Saved: 2026-08-03 23:52
Source: 2026-08-03_10-46-53Z_AdaptiveReconstructionofBosonicQuantumStates.md
Model: None

---

## Summary  
The paper introduces an adaptive reconstruction technique for bosonic quantum states that estimates the fidelity of a state against a whole family of physically equivalent states while reconstructing its Wigner function from only a few measurements. By integrating a physics‑informed parametric model, Bayesian inference, bootstrap resampling and active learning, the method iteratively selects the most informative phase‑space sampling points to minimise measurement cost. The approach is demonstrated on a circuit quantum electrodynamics (CQED) platform for Schrödinger cat states with amplitudes α∈[1,3], yielding fast, reproducible fidelity estimates that remain robust to displacements and rotations despite using a mismatched prior.

## Key Contributions  
- Adaptive reconstruction framework that minimizes the number of measurements required to estimate fidelity across a family of bosonic states.  
- Experimental validation on a CQED platform showing stable fidelity within minutes, robustness to phase‑space translations/rotations, and sensitivity to subtle state imperfections.  
- Integration of the reconstructed fidelity into a closed‑loop quantum optimal control experiment, enabling autonomous optimisation of bosonic quantum states.

## Methodology  
The authors employ a parametric model of the Wigner function that is informed by underlying physics. Bayesian inference with bootstrap resampling provides posterior estimates of the state parameters. Active learning then selects measurement points that maximise information gain about the target state family, iteratively refining the reconstruction. This combination reduces the required shot count compared to uniform sampling protocols.

## Results  
Reconstruction yields fidelity estimates that are reproducible within a few minutes and remain accurate despite large displacements or rotations in phase space. The method is sensitive to small imperfections, which can be exploited for error detection. Compared with existing Wigner‑function sampling techniques, the adaptive strategy achieves higher measurement efficiency for cat states with amplitudes α∈[1,3]. Moreover, the reconstructed fidelity drives a closed‑loop optimal control loop, demonstrating autonomous state optimisation.

## Significance  
The work provides an efficient, scalable technique for characterizing bosonic quantum systems beyond single‑target tomography, enabling real‑time feedback and autonomous optimisation. By dramatically reducing measurement overhead while preserving robustness to phase‑space transformations, the method opens pathways for practical quantum information processing on platforms such as CQED.

## Related Concepts  
Wigner function, phase‑space translation/rotation invariance, Bayesian inference, active learning, circuit QED, Schrödinger cat state, fidelity estimation, optimal control, closed‑loop quantum systems.
