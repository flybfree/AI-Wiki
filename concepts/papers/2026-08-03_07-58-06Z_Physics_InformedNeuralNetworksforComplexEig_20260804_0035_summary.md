# Summary: 2026-08-03_07-58-06Z_Physics_InformedNeuralNetworksforComplexEigenfrequ.md
Saved: 2026-08-04 00:35
Source: 2026-08-03_07-58-06Z_Physics_InformedNeuralNetworksforComplexEigenfrequ.md
Model: None

---

## Summary  
This paper proposes a physics‑informed neural network (PINN) framework to simultaneously identify complex eigenfrequencies and reconstruct two‑dimensional complex‑valued mode fields for the ground‑state ion‑temperature‑gradient (ITG) drift wave branch in high‑confinement tokamaks. The steep‑gradient pedestal of the ITG branch is known to be sensitive to edge transport, which further complicates accurate reconstruction. By encoding Fourier features and using complex‑valued propagation, the framework jointly optimizes a neural network that outputs both quantities under physical constraints. Experiments demonstrate accurate recovery of target eigenfrequencies and mode fields, outperforming baseline PINN approaches. The method also learns a smooth phase evolution consistent with physical drift‑wave theory.

## Key Contributions  
- Joint identification of complex eigenfrequency and two‑dimensional complex‑valued mode field.  
- Fourier feature encoding with complex‑valued propagation to handle steep gradients.  
- Three‑stage training under physical constraints for sparse data.  

## Methodology  
The authors construct a PINN that incorporates Fourier features as input, propagates complex‑valued outputs through a neural network layer, and enforces the governing drift‑wave equations via residual loss. Training proceeds in three stages: (1) initializing the network with random parameters, (2) minimizing the combined physical residual and data fitting loss to recover eigenfrequency and mode field, and (3) fine‑tuning using gradient descent while respecting constraints on frequency magnitude and field smoothness.

## Results  
Experimental results show that the proposed framework recovers the target complex eigenfrequency within 0.5 % of the measured value and reconstructs the two‑dimensional mode field with RMS error below 1 %. These performances surpass representative PINN baselines that treat eigenfrequency and mode field separately or use real‑valued networks, indicating superior joint optimization. Additionally, the network learns a smooth phase evolution consistent with physical drift‑wave theory.

## Significance  
This work provides a robust computational tool for analyzing drift‑wave dynamics in high‑confinement plasmas where precise eigenfrequency and mode structure are critical for confinement improvement. By enabling rapid reconstruction of complex modes from sparse data, it supports design of advanced tokamak configurations and informs higher‑order mode studies.

## Related Concepts  
- Physics‑informed neural networks (PINNs) – Complex eigenfrequencies – Two‑dimensional complex‑valued mode fields – Fourier feature encoding – Drift‑wave physics
