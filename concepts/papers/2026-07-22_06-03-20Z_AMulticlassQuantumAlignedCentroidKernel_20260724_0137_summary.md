# Summary: 2026-07-22_06-03-20Z_AMulticlassQuantumAlignedCentroidKernel.md
Saved: 2026-07-24 01:37
Source: 2026-07-22_06-03-20Z_AMulticlassQuantumAlignedCentroidKernel.md
Model: None

---

## Summary  
The paper introduces **McQuack**, a trainable quantum kernel designed for multiclass classification that scales linearly with the number of training samples. It replaces the costly full‑Gram matrix with a trainable sample‑to‑class‑centroid fidelity matrix, thereby addressing three classic limitations of traditional kernels: quadratic scaling, non‑trainable fixed kernels, and an absence of an intrinsic multiclass formulation. The authors evaluate McQuack both in simulation and on real IBM quantum hardware (124 qubits) across a wide range of datasets. They also analyze the trainability of the model up to 13 qubits and demonstrate that barren plateaus can be avoided with proper initialization.

## Key Contributions  
- [Finding 1] A trainable quantum kernel that scales linearly in the number of training samples, eliminating the O(N²) cost of full‑Gram kernels.  
- [Finding 2] The use of a sample‑to‑(class‑centroid) fidelity matrix as a trainable replacement for the full Gram matrix.  
- [Finding 3] No evidence of barren plateaus up to 13 qubits, highlighting that parameter initialization is crucial for successful optimization.

## Methodology  
The authors propose **McQuack** as a quantum kernel method where each class is represented by a trainable circuit encoding centroid features. The kernel computes fidelity between training samples and these centroids using a trainable measurement, which avoids constructing the full Gram matrix. This approach enables linear‑time evaluation of the kernel. Implementation was carried out on IBM Q devices; optimization employed gradient descent with careful initialization to mitigate barren plateaus.

## Results  
In simulation, McQuack outperforms existing “pure” quantum baselines such as VQE kernels. On hardware inference (without training), its performance matches that of a radial‑basis‑function (RBF) kernel. Training experiments up to 13 qubits succeed when the model is initialized properly; no barren plateaus were observed, confirming the trainability claim.

## Significance  
McQuack bridges classical kernel methods with trainable quantum computing, offering a scalable framework for multiclass classification on near‑term NISQ devices. It provides a template for future research that aims to leverage quantum advantage while maintaining practical training dynamics and performance comparable to classical kernels.

## Related Concepts  
- Quantum kernel  
- Centroid representation  
- Fidelity matrix  
- Trainable circuits  
- Barren plateau avoidance  
- IBM Q hardware  
- Linear scaling in kernel methods
