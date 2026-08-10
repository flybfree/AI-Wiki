# Summary: 2026-07-30_11-51-29Z_Onajointsimultaneouslearningofrelevantfeaturesubse.md
Saved: 2026-07-30 21:49
Source: 2026-07-30_11-51-29Z_Onajointsimultaneouslearningofrelevantfeaturesubse.md
Model: None

---

## Summary  
The paper proposes Entropy‑Optimal Manifold Regression (EOMR), an extension of Entropy‑Optimal Manifold Clustering that jointly discovers relevant feature subsets and low‑dimensional subspaces for regression‑like problems. By integrating entropy‑driven manifold learning with subspace extraction, EOMR achieves linear‑scaling iteration and memory complexities while delivering state‑of‑the‑art prediction on highly nonlinear benchmark datasets such as the Lorenz‑96 chaotic system and Hasegawa‑Wakatani plasma dynamics. The authors demonstrate that their method outperforms popular AI tools—gradient boosted random forests, deep neural networks, and transformer‑based TabPFN—by orders of magnitude in root mean squared error and model complexity. This work thus advances simultaneous feature‑subset and subspace learning for nonstationary, nonlinear regression tasks.

## Semantic links
- [[concepts/2026-07-27_FoundationModelsStateOfTheArt.md|Foundation Models State of the Art — 2026-07-27]] — 4 title terms overlap; 3 backlinks; 4 summary/topic terms overlap
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 4 title terms overlap; 3 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-08-01_08-41-29Z_S__4_R_SelectiveSampling_Subspaces_andSpars_summary.md|Summary: 2026-08-01_08-41-29Z_S__4_R_SelectiveSampling_Subspaces_andSparseRecons.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.07

## Key Contributions  
- [Finding 1] A unified framework (EOMR) that simultaneously learns relevant feature subsets and low‑dimensional subspaces with linear scaling.  
- [Finding 2] Empirical superiority over state‑of‑the‑art AI/ML models on two benchmark problems: Lorenz‑96 dynamics at strong and very‑strongly chaotic regimes, and Hasegawa‑Wakatani plasma edge data.  
- [Finding 3] A compact, entropy‑optimal description of the dominant dynamics (e.g., a linear autoregressive process with eight parameters) that captures the essential manifold structure.

## Methodology  
The authors start from an EOMC clustering algorithm that partitions high‑dimensional data into entropy‑optimal manifolds. They then augment this by performing subspace extraction via low‑rank factorization of the learned manifold representation, guided by a regularized regression loss. The joint optimization is performed iteratively with linear‑time updates and memory proportional to the number of features, enabling scalable computation on large datasets.

## Results  
On the Lorenz‑96 system (F = 8, 12) EOMR reduces RMSE by up to 70 % compared with gradient boosted random forests and deep nets while using a fraction of the parameters. For Hasegawa‑Wakatani plasma data, EOMR achieves an RMSE that is orders of magnitude lower than TabPFN v.03 and other transformers, and it distills the leading Essential Orthogonal Function (EOF) into a simple 8‑parameter autoregressive model. Model complexity metrics such as parameter count and training time are also markedly reduced.

## Significance  
EOMR bridges the gap between unsupervised clustering and supervised regression for real‑world problems where data lie on low‑dimensional, nonstationary manifolds. By jointly selecting useful features and extracting their subspace structure, it enables interpretable, efficient models that outperform black‑box deep learning approaches in both accuracy and computational cost.

## Related Concepts  
- Entropy‑Optimal Manifold Clustering (EOMC) – a clustering method based on entropy minimization.  
- Essential Orthogonal Functions (EOF) – low‑dimensional basis for signal decomposition.  
- Low‑rank factorization – technique for extracting compact subspace representations.  
- Nonstationary regression – problems where the underlying relationship evolves over time.
