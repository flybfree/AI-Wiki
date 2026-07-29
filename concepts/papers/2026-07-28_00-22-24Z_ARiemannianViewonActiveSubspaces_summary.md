# Summary: 2026-07-28_00-22-24Z_ARiemannianViewonActiveSubspaces.md
Saved: 2026-07-28 22:27
Source: 2026-07-28_00-22-24Z_ARiemannianViewonActiveSubspaces.md
Model: None

---

## Summary  
The paper proposes a Riemannian perspective on active subspaces, extending the Euclidean eigenvalue‑ordered principle to manifolds via parallel transport. It contrasts an intrinsic local decomposition of scalar quantities with the extrinsic gradient average used in manifold learning, both restricted to mean‑centered geodesic balls. The framework explains how scalar fields change most rapidly under each approach and identifies where they coincide. Numerical experiments on the 2‑sphere demonstrate ridge recovery at a curvature‑limited quadratic rate.

## Key Contributions  
- Active subspaces can be defined intrinsically via parallel transport, providing an eigenvalue‑ordered explanation of activity.  
- On central tangent spaces eigenvalues match second order in geodesic radius while dominant eigenspaces align with the spectral gap; beyond this point the intrinsic and extrinsic methods diverge.  
- The method yields a quadratic ridge recovery rate on hyperspheres such as the 2‑sphere, useful for preshape analysis.

## Methodology  
The authors consider scalar fields defined over Riemannian manifolds and study their variation under active subspaces. They compute eigenvalue decompositions in each tangent space of a mean‑centered geodesic ball, then compare intrinsic parallel‑transported frames with extrinsic gradient averages. Computations are performed on the 2‑sphere using curvature‑limited quadratic approximations.

## Results  
Theoretical analysis shows second‑order agreement for eigenvalues near the center and spectral gap dependence; numerically ridge recovery is recovered quadratically in curvature. The framework reproduces known results and offers a unified view of activity on curved spaces.

## Significance  
This work bridges manifold learning with Riemannian geometry, offering a principled way to identify active subspaces without relying on embedding coordinates. It improves stability of ridge regression on curved spaces and enables intrinsic algorithms for shape analysis.

## Related Concepts  
Active subspace, eigenvalue‑ordered activity, parallel transport, geodesic balls, extrinsic vs intrinsic gradient averages, spectral gap, quadratic recovery rate, hypersphere, preshape space.
