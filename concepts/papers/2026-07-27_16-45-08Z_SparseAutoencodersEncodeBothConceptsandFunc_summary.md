# Summary: 2026-07-27_16-45-08Z_SparseAutoencodersEncodeBothConceptsandFunctions_T.md
Saved: 2026-07-27 21:46
Source: 2026-07-27_16-45-08Z_SparseAutoencodersEncodeBothConceptsandFunctions_T.md
Model: None

---

## Summary  
The paper addresses a long‑standing inconsistency in the use of sparse autoencoders (SAEs) as interpretability tools: features that are easy to describe may not reliably steer model behavior, and activation‑based feature selection can miss important causal drivers. To bridge this gap, the authors introduce Feature‑Effect Geometry Analysis (FEGA), an unsupervised method that examines how logit changes propagate when a single SAE feature is held constant across diverse contexts. Their contribution is threefold: they reveal that most features produce multi‑directional effects rather than stable one‑dimensional directions; they distinguish two families of features—value‑like (static, factual) and pointer‑like (context‑dependent)—and show that each exhibits characteristic geometric patterns; finally, they demonstrate empirically that a feature can be both interpretable and causally relevant without providing a consistent steering direction.  

## Key Contributions  
- [Finding 1] Feature‑Effect Geometry Analysis (FEGA) uncovers that SAE features rarely generate one‑dimensional effects across contexts; most produce cloud‑like logit changes spanning multiple directions.  
- [Finding 2] Value‑like features—linked to static factual attributes—exhibit structured, low‑dimensional effect clouds, though these still span several orthogonal directions rather than a single axis.  
- [Finding 3] Pointer‑like features, tied to context‑dependent operations, produce diffuse, high‑variance logit changes that lack coherent directionality.  

## Methodology  
The authors adopt an unsupervised framework: for each SAE variant and dataset pair, they fix the activation of a chosen feature while varying all other inputs across a set of prompts or tasks. This generates a cloud of resulting logits. By computing geometric descriptors such as variance, covariance matrices, and principal component loadings on this cloud, FEGA quantifies how “directional” the effect is. The analysis is repeated for many features to identify patterns that persist across SAE architectures (e.g., variational autoencoders, denoising autoencoders).  

## Results  
Experiments on several downstream tasks show that only a minority of features exhibit one‑dimensional logit trends; the majority produce multi‑directional clouds. Value‑like features consistently yield lower variance and more aligned principal components, reflecting their role in encoding fixed information. Pointer‑like features, however, generate high‑variance, isotropic changes, indicating context‑driven influence. The FEGA framework thus quantifies the “downstream geometry of feature effects,” providing a quantitative complement to activation‑based interpretability.  

## Significance  
These findings explain why SAE interpretability tools often fail: features that are easy to describe may not reliably produce desired output changes, and their causal impact can be obscured by non‑linear, multi‑directional logit shifts. By focusing on the geometry of feature effects rather than activation patterns alone, FEGA offers a principled way to assess which SAE components truly steer model behavior, guiding more reliable downstream interventions and selection processes.  

## Related Concepts  
- Sparse Autoencoders (SAEs)  
- Feature Geometry / Feature‑Effect Geometry Analysis (FEGA)  
- Value‑like vs. pointer‑like features  
- Downstream geometry of feature effects  
- Logit changes and their causal interpretation  
- Interpretability in deep learning models
