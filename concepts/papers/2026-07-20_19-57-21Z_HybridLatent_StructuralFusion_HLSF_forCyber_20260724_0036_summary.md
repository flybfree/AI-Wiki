# Summary: 2026-07-20_19-57-21Z_HybridLatent_StructuralFusion_HLSF_forCyberAnomaly.md
Saved: 2026-07-24 00:36
Source: 2026-07-20_19-57-21Z_HybridLatent_StructuralFusion_HLSF_forCyberAnomaly.md
Model: None

---

## Summary  
The paper proposes Hybrid Latent‑Structural Fusion (HLSF) to improve unsupervised anomaly detection in cyber security by combining CP‑APR structural scores with normalizing flow latent density scores. It aims to fuse these complementary representations into a single anomaly score for compromised user credentials. Experiments on LANL red‑team data show HLSF outperforms each method alone, achieving higher precision and recall while reducing false positives. The contribution is a new fusion framework that leverages both statistical tensor analysis and probabilistic modeling.

## Key Contributions  
- Integration of CP‑APR structural anomaly scores with normalizing flow latent density scores into a unified model.  
- Demonstration that the fused scores improve detection performance (precision ≈ 94%, recall ≈ 88%) on real compromised credentials compared to each method alone.  
- Validation that the hybrid approach reduces false positives by roughly 30% while preserving high sensitivity.

## Methodology  
The authors first apply CP‑APR to extract a low‑dimensional structural representation of user activity logs, generating anomaly scores based on deviation from expected tensor factorization. Simultaneously, they train normalizing flows on the same data to learn a latent density distribution and compute likelihood‑based density scores for each sample. HLSF then fuses these two scores using a weighted sum; weights are either set equal or learned via cross‑validation to balance structural and probabilistic contributions.

## Results  
On the LANL dataset (≈10 k compromised credentials), HLSF achieves 94% precision and 88% recall, versus CP‑APR alone at 72%/65% and normalizing flows at 78%/70%. The fused model reduces false positives by about 30% while maintaining a high detection rate. Ablation studies confirm that each component contributes significantly to the overall performance.

## Significance  
By merging statistical structural analysis with probabilistic density modeling, HLSF offers a more robust unsupervised detector for complex cyber threats where both pattern deviation and distribution shift matter. This reduces reliance on labeled data and could improve early detection in large enterprise networks, making security systems more reliable and less prone to false alarms.

## Related Concepts  
CP‑APR (Canonical Tensor Decomposition), Normalizing Flows, Latent Space Fusion, Anomaly Scoring, Red‑Team Data, Unsupervised Learning.
