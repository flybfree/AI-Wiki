# Summary: 2026-07-28_16-47-59Z_Quasi_SVD_LearningaLie_constrainedmatrixfactorisat.md
Saved: 2026-07-28 23:00
Source: 2026-07-28_16-47-59Z_Quasi_SVD_LearningaLie_constrainedmatrixfactorisat.md
Model: None

---

## Summary  
The paper proposes Quasi‑SVD, a differentiable matrix factorisation that is fully parallelised on GPUs to achieve real‑time processing for medical imaging tasks. By enforcing exact orthogonality only on one Lie‑parameterised factor while using soft constraints for the remaining components, it avoids iterative singular‑vector optimisation and preserves reconstruction fidelity comparable to classical SVD. The framework accelerates computation by 3–20× relative to cuSOLVER and randomised SVD, delivering frame rates above 25 FPS on high‑dimensional ultrasound data and massive batch processing of small Mueller matrices. This asymmetric design makes structured matrix factorisation practical for live image‑guided clinical workflows where sequential solvers are infeasible.

## Key Contributions  
- [Finding 1] Quasi‑SVD replaces the full SVD with a Lie‑constrained, single exact orthogonal factor and soft constraints on the rest, enabling fully parallel GPU computation.  
- [Finding 2] The method achieves reconstruction fidelity (SSIM = 0.89–0.94) that is within the range of conventional SVD while reducing computational time by a factor of 3–20.  
- [Finding 3] It attains sustained throughput exceeding 25 FPS across two distinct medical imaging regimes, supporting real‑time clinical pipelines.

## Methodology  
Quasi‑SVD is built as a differentiable loss function that simultaneously optimises the Lie‑constrained factor and enforces soft orthogonality constraints on the remaining factors. The loss is computed element‑wise, allowing GPU kernels to process each matrix slice independently without iterative updates. This fully parallelised formulation eliminates the bottleneck of sequential SVD solvers such as cuSOLVER or randomised SVD, while still guaranteeing a valid factorisation through the exact Lie constraint.

## Results  
Experimental evaluation on spatio‑temporal background subtraction for ultrasound localisation microscopy (high‑dimensional matrix separation) and Mueller matrix polarimetry for neurosurgical tissue characterisation (massive batch processing of small matrices) shows SSIM values between 0.89 and 0.94, a speedup of 3–20× over baseline solvers, and frame rates above 25 FPS on both tasks. The framework exhibits robust domain transfer across multiple imaging instruments, confirming its applicability to diverse clinical settings.

## Significance  
Quasi‑SVD demonstrates that structured matrix factorisation can be deployed in real‑time medical imaging workflows where classical solvers cannot meet latency requirements. By prioritising reconstruction fidelity over exact spectral recovery and leveraging Lie algebra constraints, the method bridges the gap between theoretical optimality and practical clinical deployment.

## Related Concepts  
- Singular Value Decomposition (SVD)  
- Lie algebra constraints  
- Matrix factorization  
- GPU parallelisation  
- Real‑time imaging  
- Soft constraints  
- cuSOLVER
