# Summary: 2026-08-03_07-03-51Z_ReFP_AD_RectifiedFlowPreconditioningforEnergy_Base.md
Saved: 2026-08-04 00:27
Source: 2026-08-03_07-03-51Z_ReFP_AD_RectifiedFlowPreconditioningforEnergy_Base.md
Model: None

---

## Summary  
The paper proposes ReFP‑AD, a method that uses geometric reparameterization via optimal transport to precondition energy‑based anomaly detection in high‑dimensional token embeddings. It enables stable finite‑step MCMC and accurate anomaly scoring without needing anomalous samples. By mapping embeddings into a well‑conditioned latent space, the approach improves AUROC on benchmark datasets. The unified protocol achieves state‑of‑the‑art performance across Image and Pixel tasks.

## Key Contributions  
- Geometric reparameterization using optimal transport rectified flow maps high‑dimensional token spaces to a well‑conditioned latent space.  
- Preconditioning enables stable persistent contrastive divergence and SGLD for energy‑based anomaly detection in full‑dimensional embeddings.  
- Gradient norm based anomaly scores provide accurate localization, achieving top AUROC improvements over prior unified EBM baselines.

## Methodology  
The authors address instability of Energy‑Based Models (EBMs) caused by anisotropy in high‑dimensional token spaces by learning a rectified flow that couples optimal transport to the embedding distribution. This flow acts as a preconditioner, transforming noisy embeddings into smoother latent variables. They then train an energy function using SGLD with persistent contrastive divergence on this preconditioned space and extract anomaly scores via gradient norms.

## Results  
On MVTec‑AD and VisA, ReFP‑AD achieves 98.6 %/97.9 % Image AUROC and 97.3 %/99.0 % Pixel AUROC respectively, surpassing prior unified EBM baselines by up to +10.8 % in Image AUROC. Ablation studies confirm the necessity of geometric reparameterization for stable MCMC and precise anomaly localization.

## Significance  
By resolving geometric challenges in high‑dimensional token spaces, ReFP‑AD makes energy‑based anomaly detection scalable and reliable without anomalous data, advancing unified modeling across heterogeneous datasets.

## Related Concepts  
- Energy‑Based Modeling (EBM)  
- Optimal Transport (OT)  
- Rectified Flow  
- Stochastic Gradient Langevin Dynamics (SGLD)  
- Persistent Contrastive Divergence  
- Anomaly Detection AUROC  
- Token Embeddings  
- Geometric Preconditioning
