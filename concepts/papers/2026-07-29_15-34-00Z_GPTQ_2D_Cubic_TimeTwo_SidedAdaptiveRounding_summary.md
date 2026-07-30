# Summary: 2026-07-29_15-34-00Z_GPTQ_2D_Cubic_TimeTwo_SidedAdaptiveRounding.md
Saved: 2026-07-29 22:28
Source: 2026-07-29_15-34-00Z_GPTQ_2D_Cubic_TimeTwo_SidedAdaptiveRounding.md
Model: None

---

## Summary  
The paper tackles the two‑sided adaptive rounding problem, extending GPTQ to a matrix where both left and right basis matrices act on the residual, achieving cubic‑time rounding while preserving optimality. It shows that entries on each anti‑diagonal can be rounded independently in parallel, eliminating the quartic time of the naïve vectorized approach. The contribution is a new algorithm called GPTQ‑2D that produces identical rounded matrices to the original GPTQ method but with cubic complexity. This work bridges theoretical analysis and practical deployment for large‑scale matrix quantization.

## Key Contributions  
- Derives a quadratic‑metric formulation where the Gram matrix becomes a Kronecker product of two identity‑like bases, enabling a one‑dimensional optimization view.  
- Proposes an anti‑diagonal ordering that makes entries on each diagonal independent, allowing parallel rounding and reducing complexity to cubic time.  
- Provides a theoretical proof that GPTQ‑2D yields exactly the same rounded matrix as the original GPTQ algorithm.

## Methodology  
The authors vectorize the two‑sided residual minimization problem, converting it into a one‑dimensional quadratic program whose Gram matrix is the Kronecker product of the left and right basis matrices. They then exploit the symmetry of anti‑diagonals to parallelize rounding decisions: entries on the same anti‑diagonal are independent, so they can be processed simultaneously while a triangular feedback matrix updates only dependent entries. This construction replaces the O(N⁴) quartic cost with an O(N³) cubic algorithm.

## Results  
Theoretical analysis demonstrates that GPTQ‑2D runs in O(N³) time for an N×N matrix, matching the optimal bound known for quadratic optimization under this structure. Empirically, the algorithm matches GPTQ’s rounding error within machine epsilon across a suite of random and structured test matrices, confirming both correctness and speed.

## Significance  
This cubic‑time algorithm enables scalable quantization of large 2D tensors in deep learning models, cutting inference time and memory footprint without sacrificing accuracy. The result is especially valuable for edge devices where quartic algorithms are prohibitive, paving the way for faster, more efficient model deployment.

## Related Concepts  
- Adaptive rounding (GPTQ)  
- Babai’s nearest‑plane algorithm  
- Quadratic metric optimization  
- Kronecker product Gram matrix  
- Anti‑diagonal ordering  
- Triangular feedback matrices
