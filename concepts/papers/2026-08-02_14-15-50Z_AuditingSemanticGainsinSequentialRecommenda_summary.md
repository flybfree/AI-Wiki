# Summary: 2026-08-02_14-15-50Z_AuditingSemanticGainsinSequentialRecommendation_AL.md
Saved: 2026-08-03 23:27
Source: 2026-08-02_14-15-50Z_AuditingSemanticGainsinSequentialRecommendation_AL.md
Model: None

---

## Summary  
The paper addresses the attribution problem in sequential recommendation where improvements over ID‑only baselines could stem from various sources such as language‑model reasoning, semantic‑ID generation, or richer offline representations. It introduces LIME‑Rec, a lightweight and auditable recovery test that isolates these mechanisms without requiring serving‑time inference.

## Key Contributions  
- [Finding 1] LIME‑Rec achieves R@10 scores of 0.0996 on Amazon Beauty, 0.1105 on Toys, and 0.0593 on Sports, outperforming the strongest comparison baseline by 7.0%–12.0%.  
- [Finding 2] Three‑expert fusion without history calibration consistently beats calibrated SASRec, showing that calibration alone does not explain the recovery.  
- [Finding 3] Randomly permuting item‑text embeddings reduces R@10 by 13.6%–17.5%, indicating genuine item‑text correspondence is essential for gains.

## Methodology  
The authors construct LIME‑Rec by combining three independent experts: a SASRec sequential expert, an ItemCF co‑occurrence expert, and a semantic expert using frozen BAAI/bge‑base‑en‑v1.5 embeddings. Full‑catalog scores are normalized per user and fused at the score level with auditable gating; a bounded history calibration head is fitted solely on validation data to align expert contributions. The fusion gate and calibration head require no language‑model inference during serving, preserving transparency.

## Results  
On Amazon Beauty, Toys, and Sports, LIME‑Rec reaches R@10 scores of 0.0996, 0.1105, and 0.0593 respectively. These gains are consistent across datasets and exceed the best baseline by up to 12%. The ablation test of permuting embeddings shows a significant drop in performance, confirming that the improvement relies on real item‑text semantics rather than model capacity.

## Significance  
By providing an auditable recovery benchmark, LIME‑Rec clarifies whether reported gains are due to lightweight offline representations or more complex serving‑time mechanisms. This helps researchers and practitioners allocate effort where it matters most, avoiding over‑fitting to language models while preserving the benefits of richer item semantics.

## Related Concepts  
- Sequential recommendation  
- ID‑only baselines  
- Language‑model reasoning in recommender systems  
- Semantic‑ID generation  
- Offline item embeddings (e.g., BAAI/bge)  
- Auditable model fusion and calibration
