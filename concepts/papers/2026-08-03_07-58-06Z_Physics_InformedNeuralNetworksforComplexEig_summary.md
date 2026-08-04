# Summary: 2026-08-03_07-58-06Z_Physics_InformedNeuralNetworksforComplexEigenfrequ.md
Saved: 2026-08-04 00:28
Source: 2026-08-03_07-58-06Z_Physics_InformedNeuralNetworksforComplexEigenfrequ.md
Model: None

---

## Summary  
The paper proposes a physics‑informed neural network framework that jointly identifies the complex eigenfrequencies and reconstructs the two‑dimensional complex‑valued mode fields of a representative ground‑state ITG branch in high‑confinement tokamaks. This region is characterized by a steep‑gradient pedestal where localized high‑frequency oscillations couple strongly between real and imaginary parts, posing challenges for conventional PINN approaches. The authors introduce Fourier feature encoding, complex‑valued neural propagation, and a three‑stage training scheme to overcome these difficulties while respecting sparse observations and physical constraints. Their framework recovers the target eigenfrequency and mode field with high accuracy, outperforming baseline PINN methods.

## Key Contributions  
- [Finding 1] The model jointly solves for both the complex eigenfrequency and the spatial mode field, enabling a complete description of the drift‑wave branch.  
- [Finding 2] By encoding data in Fourier features and using three‑stage training, the network mitigates steep‑gradient pedestal effects and strong real–imaginary coupling.  
- [Finding 3] Experimental results demonstrate superior performance over representative PINN baselines for eigenfrequency identification and mode reconstruction.

## Methodology  
The authors formulate a physics‑informed loss that incorporates the governing drift‑wave equations and boundary conditions, then train a neural network with Fourier feature encoding to represent complex‑valued quantities. A three‑stage training procedure first learns low‑order statistics of the eigenfrequency, proceeds to reconstruct the mode field, and finally refines both simultaneously while enforcing physical constraints such as energy conservation and confinement limits.

## Results  
The proposed framework accurately recovers the target complex eigenfrequency and the corresponding two‑dimensional complex‑valued mode field, achieving reconstruction errors below 2 % compared with experimental data. It also outperforms standard PINN baselines in both speed of convergence and robustness to sparse observations. The solution serves as a foundation for analyzing higher‑order modes and multiple branches.

## Significance  
Accurately characterizing the ground‑state ITG branch is crucial for understanding plasma confinement, edge transport, and the physics behind the steep‑gradient pedestal that limits fusion performance. By providing a reliable computational tool for eigenfrequency and mode reconstruction, this work advances both theoretical insight and practical diagnostics in tokamak research.

## Related Concepts  
PINNs, Fourier feature encoding, complex‑valued neural networks, eigenfrequency reconstruction, ITG drift waves, ground‑state branch, steep‑gradient pedestal.
