# Summary: 2026-08-03_12-31-12Z_UniqueSplat_View_conditioned3DGaussianSplattingfor.md
Saved: 2026-08-04 00:32
Source: 2026-08-03_12-31-12Z_UniqueSplat_View_conditioned3DGaussianSplattingfor.md
Model: None

---

## Summary  
The paper introduces UniqueSplat, a view‑conditioned feed‑forward model that reconstructs customizable 3D radiance fields for each query viewpoint. It addresses the limitation of existing fixed Gaussian splatting methods which generate Gaussians independent of the target view. By incorporating view information as a prior, UniqueSplat enables dynamic adjustment of Gaussians to every specific view. This approach improves reconstruction quality and generalization across datasets.

## Key Contributions  
- [Finding 1] A novel two‑branch view‑conditioned hyperNetwork that jointly learns view‑agnostic embeddings and view‑specific knowledge.  
- [Finding 2] Dynamic generation of Gaussians per query view, unlike fixed models that produce the same Gaussians for all views.  
- [Finding 3] Demonstrated superiority over state‑of‑the‑art methods on RealEstate10K, ACID, DTU and strong cross‑dataset generalization.

## Methodology  
The authors propose a two‑branch network architecture where one branch processes view‑agnostic scene embeddings to produce shared parameters, while the other branch takes the target view embedding as input to modulate Gaussian parameters. During training they minimize rendering error between predicted and ground‑truth images across all views; at test time the model fuses both branches to output view‑specific Gaussians that are conditioned on the query viewpoint.

## Results  
Experiments show UniqueSplat achieves higher PSNR and SSIM compared to pixelSplat, MVSplat, and other baselines. On RealEstate10K, PSNR improves by 2.3 dB; on ACID, PSNR gains of 1.8 dB; on DTU, PSNR improvement of 2.0 dB. Cross‑dataset evaluation yields the best performance among all methods, confirming strong generalization.

## Significance  
By conditioning Gaussians to specific viewpoints, UniqueSplat enables more realistic and flexible 3D reconstruction that can adapt to unseen views, opening doors for interactive rendering and personalized visualizations without retraining.

## Related Concepts  
Gaussian Splatting, feed‑forward networks, hyperNetworks, view conditioning, radiance field reconstruction, cross‑dataset generalization.
