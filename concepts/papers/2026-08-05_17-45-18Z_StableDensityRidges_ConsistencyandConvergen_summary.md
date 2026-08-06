# Summary: 2026-08-05_17-45-18Z_StableDensityRidges_ConsistencyandConvergenceofSub.md
Saved: 2026-08-05 22:34
Source: 2026-08-05_17-45-18Z_StableDensityRidges_ConsistencyandConvergenceofSub.md
Model: None

---

## Summary  
The Subspace Constrained Mean Shift (SCMS) algorithm is widely used to extract density ridges, yet the literature assumes that its trajectories converge to a static ridge defined solely by the Hessian of the data density. This paper disproves that assumption and introduces a “stable ridge” as the true limit of SCMS, showing that the classical definition ignores the continuous rotation of the trailing eigenspace induced by the algorithm’s vector field. The authors develop a generalized constant‑step‑size SCMS framework that guarantees uniform R‑linear convergence to this stable ridge and provides Hausdorff‑distance convergence rates for ridge estimation.  

## Key Contributions  
- [Finding 1] The static density ridge is not the correct limit of SCMS; instead, a stable ridge defined through the Jacobian of the projected density gradient is the true theoretical target.  
- [Finding 2] A generalized constant‑step‑size SCMS framework achieves uniform R‑linear convergence and topological surjectivity onto the stable ridge.  
- [Finding 3] The original SCMS suffers polynomial‑time complexity due to implicit coupling of step size with smoothing bandwidth, while the new approach is statistically consistent and more efficient.  

## Methodology  
The authors first analyze the underlying vector field of SCMS, demonstrating that the trailing eigenspace rotates as the algorithm progresses. They then define a stable ridge using the Jacobian of this projected density gradient, which captures both curvature and orientation changes. To obtain convergence guarantees, they replace the variable‑step Mean Shift operator with a constant step size, yielding a linearized dynamics problem whose fixed point is precisely the stable ridge. Convergence rates are derived analytically via perturbation theory, leading to an R‑linear bound on the Hausdorff distance between successive ridge approximations.  

## Results  
Theoretical analysis shows that under mild regularity assumptions (e.g., bounded Hessian eigenvalues and Lipschitz continuity of the density), the generalized SCMS converges with rate O(Rⁿ) where n is the dimension of the trailing eigenspace, and the Hausdorff distance between the k‑th approximation and the stable ridge satisfies ‖‖R_k – R*‖_H ≤ C·Rᵏ. Simulations on synthetic datasets confirm that the constant‑step version yields faster convergence than the original algorithm and reduces computational cost by a factor of two to three, while maintaining statistical consistency.  

## Significance  
By correcting the fundamental assumption about SCMS convergence, this work provides a mathematically rigorous target for ridge extraction and improves both theoretical guarantees and practical performance. The stable‑ridge concept bridges nonparametric density estimation with dynamical systems theory, offering a unified framework applicable to high‑dimensional data analysis and manifold learning.  

## Related Concepts  
Density ridges, Mean Shift, subspace constrained methods, Jacobian of projected gradients, Hausdorff distance convergence, R‑linear convergence, topological surjectivity.
