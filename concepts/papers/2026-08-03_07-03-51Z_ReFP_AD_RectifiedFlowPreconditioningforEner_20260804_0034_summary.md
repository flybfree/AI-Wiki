# Summary: 2026-08-03_07-03-51Z_ReFP_AD_RectifiedFlowPreconditioningforEnergy_Base.md
Saved: 2026-08-04 00:34
Source: 2026-08-03_07-03-51Z_ReFP_AD_RectifiedFlowPreconditioningforEnergy_Base.md
Model: None

---

## Summary  
The paper introduces ReFP‑AD, a geometric reparameterization technique that maps high‑dimensional token embeddings into a well‑conditioned latent space to enable stable energy‑based anomaly detection. By coupling an optimal transport rectified flow with contrastive divergence and preconditioning stochastic gradient Langevin dynamics, the authors achieve reliable finite‑step MCMC sampling in full‑dimensional spaces. The method yields unified anomaly scores derived from learned gradient norms and outperforms prior EBM baselines on standard datasets. This work bridges representation learning and density estimation for heterogeneous normal data without requiring anomalous samples.

## Key Contributions  
- [Finding 1] ReFP‑AD discovers a rectified flow that acts as a geometric preconditioner, converting anisotropic token embeddings into a near‑isotropic latent manifold.  
- [Finding 2] The preconditioned SGLD sampler converges to the true posterior of the energy landscape with finite steps, eliminating the instability caused by high‑dimensional anisotropy.  
- [Finding 3] Anomaly scores are computed from gradient norms in the learned energy surface, providing a unified metric compatible with contrastive learning objectives.

## Methodology  
The authors start with foundation models such as DINOv2 that produce token embeddings for both normal and anomalous images. They formulate an EBM whose energy depends on these embeddings but suffers from strong cross‑dimensional correlations. To remedy this, they define a rectified flow \(F_t\) parameterized by time \(t\) that is coupled to the optimal transport cost between the original embedding distribution and its shifted version under the anomaly prior. The flow’s Jacobian provides a preconditioner for SGLD updates: \(\theta_{k+1} = \theta_k - \eta \, J_F(t)^{-1}(V(\theta_k) + \nabla V(\theta_k)^\top)\). This geometric reparameterization is trained jointly with contrastive loss, ensuring the latent space remains well‑conditioned. Anomaly scores are then extracted as \(\| \nabla V(\theta) \|^2\) evaluated at each token embedding.

## Results  
On MVTec‑AD and VisA, ReFP‑AD attains AUROC of 98.6 %/97.9 % for images and 97.3 %/99.0 % for pixels respectively, surpassing prior unified EBM baselines by up to +10.8 percentage points in Image AUROC. Ablation studies confirm that removing the rectified flow or conditioning step degrades performance, underscoring its necessity for stable MCMC and accurate localization.

## Significance  
By resolving geometric instability in high‑dimensional token spaces, ReFP‑AD makes energy‑based anomaly detection scalable to foundation‑model representations without sacrificing accuracy. The preconditioned SGLD framework offers a principled way to handle anisotropy, opening the door to robust, unified detectors that can be applied across diverse modalities.

## Related Concepts  
- Energy‑Based Models (EBM)  
- Optimal Transport (OT) and rectified flow  
- Stochastic Gradient Langevin Dynamics (SGLD)  
- Contrastive Divergence  
- Anomaly scores via gradient norms
