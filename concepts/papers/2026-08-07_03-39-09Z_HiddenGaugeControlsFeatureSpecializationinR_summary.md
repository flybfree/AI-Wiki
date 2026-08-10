# Summary: 2026-08-07_03-39-09Z_HiddenGaugeControlsFeatureSpecializationinReLUNetw.md
Saved: 2026-08-09 22:39
Source: 2026-08-07_03-39-09Z_HiddenGaugeControlsFeatureSpecializationinReLUNetw.md
Model: None

---

## Summary  
The paper investigates how the ownership of a feature can be controlled in an overparameterized ReLU network by a hidden parameter that is invisible to the initial predictor, leading to one neuron acquiring a teacher‑learned feature while its functional contribution vanishes. By constructing a tractable Gaussian teacher‑student model where only a positive‑homogeneous scaling gauge varies, the authors demonstrate a sharp Θ(D²) separation in specialization time and prove global selection of the owner neuron under favorable gauges. The analysis attributes these dynamics to a reaction–transport decomposition that yields distinct mobilities for changing feature coefficients versus their direction. The results are validated through theoretical proofs and finite‑sample training experiments.

## Key Contributions  
- [Finding 1] Feature ownership in ReLU networks can be controlled by an invisible gauge parameter, enabling one neuron to become the sole owner of a teacher feature while others become redundant.  
- [Finding 2] The selection process is deterministic: assigning the favorable gauge to a specific neuron forces it to learn the feature and drives the remaining neurons’ functional contribution to zero, with a Θ(D²) specialization time that cannot be explained by global clock changes.  
- [Finding 3] A reaction‑transport decomposition explains the effect as different mobilities for altering a feature’s coefficient versus its direction, linking the dynamics to loss, alignment, pruning, and dissipation trajectories.

## Methodology  
The authors adopt a Gaussian teacher–student framework where the initial network function is fixed, and only a positive‑homogeneous scaling gauge is varied. This gauge changes the effective weight of each neuron without altering the observable output. Using an exact reaction‑transport decomposition, they compute how feature coefficients evolve over time, treating coefficient change and direction change as separate “mobilities.” The model is then extended to finite‑time selection under visible perturbations (e.g., small‑step full‑batch gradient descent) and to population‑level training dynamics.

## Results  
Theoretical analysis yields a Θ(D²) separation in specialization time, confirming that the initial predictor does not dictate when or which neuron learns a feature. Deterministic assignment of the favorable gauge selects a single neuron as owner and nullifies the functional contribution of others. Loss, alignment, pruning, and dissipation trajectories predicted by the reaction‑transport model match empirical results from finite‑sample training, validating both global selection and functional pruning.

## Significance  
This work reveals an intrinsic mechanism that governs feature specialization independent of the initial network state, challenging longstanding assumptions about learning dynamics. By providing a theoretical foundation for hidden gauge control, it opens avenues to design architectures where specific neurons are preferentially responsible for tasks, potentially improving efficiency and interpretability in deep networks.

## Related Concepts  
ReLU networks, overparameterization, teacher‑student models, Gaussian processes, gauge theory, reaction–diffusion equations, functional pruning, selection dynamics, mobility, dissipation.
