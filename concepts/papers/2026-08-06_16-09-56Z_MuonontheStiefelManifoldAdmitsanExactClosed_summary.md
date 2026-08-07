# Summary: 2026-08-06_16-09-56Z_MuonontheStiefelManifoldAdmitsanExactClosed_FormUp.md
Saved: 2026-08-06 22:20
Source: 2026-08-06_16-09-56Z_MuonontheStiefelManifoldAdmitsanExactClosed_FormUp.md
Model: None

---

## Summary  
The paper investigates the application of Muon, a matrix‑aware optimization method, to the Stiefel manifold—those matrices whose columns are orthonormal—and discovers that the corresponding update admits an exact closed‑form expression. This result enables the authors to introduce Skewon, a practical algorithm for orthogonality‑constrained optimization with an efficient implementation and provable first‑order convergence guarantees in smooth non‑convex settings.

## Key Contributions  
- [Finding 1] The exact closed‑form solution of the Muon update on the Stiefel manifold.  
- [Finding 2] A new algorithm, Skewon, that leverages this solution for efficient orthogonality‑constrained optimization.  
- [Finding 3] First‑order convergence analysis showing spectral norm decay under a constant step size.

## Methodology  
The authors start from the gradient flow on the Stiefel manifold, exploiting its geometric properties (orthogonal columns, unit‑norm constraints). By formulating the problem as minimizing a smooth objective with orthogonality constraints, they derive an analytical expression for the optimal step that preserves orthonormality. This derivation is then implemented in Skewon, which computes the update by solving a low‑rank correction to the current matrix. Theoretical convergence is established using Lipschitz continuity of the gradient and spectral norm bounds.

## Results  
Theoretically, Skewon guarantees that after each iteration the spectral norm of the gradient shrinks by at least a factor \(1-\eta\), where \(\eta\) is the step size, ensuring linear convergence in the smooth non‑convex regime. Experimentally, the algorithm matches or surpasses existing heuristic updates while requiring fewer matrix multiplications and lower memory overhead, demonstrating both theoretical and practical efficiency.

## Significance  
Providing an exact closed‑form update for Muon on the Stiefel manifold bridges a long gap between theory and practice in machine learning. It offers a reliable, low‑cost method for training models that enforce orthogonality constraints—such as random feature maps or low‑rank factorizations—without sacrificing speed or accuracy.

## Related Concepts  
Muon optimization, Stiefel manifold, orthogonality‑constrained optimization, gradient flow, first‑order convergence, spectral norm, matrix‑aware methods.
