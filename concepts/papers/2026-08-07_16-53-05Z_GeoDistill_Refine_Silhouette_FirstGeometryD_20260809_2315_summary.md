# Summary: 2026-08-07_16-53-05Z_GeoDistill_Refine_Silhouette_FirstGeometryDistilla.md
Saved: 2026-08-09 23:15
Source: 2026-08-07_16-53-05Z_GeoDistill_Refine_Silhouette_FirstGeometryDistilla.md
Model: None

---

## Summary  
The paper proposes GeoDistill‑Refine, a two‑stage framework for annotation‑free spacecraft segmentation that improves upon naive pseudo‑label distillation by stabilizing teacher outputs and refining geometry using signed‑distance fields, skeletons, and area objectives. It achieves higher IoU and F1 scores than a baseline student trained only on SAM 3 pseudo‑masks. The method reduces reliance on unreliable prompts while maintaining a compact model size.

## Key Contributions  
- [Finding 1] GeoDistill‑Refine stabilizes teacher pseudo‑mask predictions across six fixed prompts using an unweighted vote, mitigating prompt‑induced geometric errors.  
- [Finding 2] The student learns a foreground silhouette first and then refines it with signed‑distance‑field, skeleton, and area objectives derived from the pseudo‑mask.  
- [Finding 3] A sample‑level gate based on valid‑prompt ratio and pseudo‑mask area plausibility suppresses influence of unreliable pseudo‑geometry.

## Methodology  
The authors approach the problem by decoupling segmentation into two stages: first generating a coarse silhouette via a lightweight network, then applying geometry refinement using auxiliary branches that compute signed‑distance fields, skeleton graphs, and area metrics. The teacher’s six prompts are fused to produce a robust pseudo‑mask; a gate evaluates prompt agreement and plausibility before allowing refined outputs to influence the student loss.

## Results  
On SpaceSense‑Bench HJM lockbox set, GeoDistill‑Refine raises Image IoU by 0.0456 and Boundary F1 by 0.1380 compared with a plain pseudo‑label student. External tests on SPEED+ Lightbox, Sunlamp, and TANGO show competitive regional overlap gains in boundary quality and foreground precision. The deployed TinyUNet contains 0.263 M parameters and runs at ~1.1 ms per image on an RTX 4090.

## Significance  
This work demonstrates that annotation‑free segmentation can be made robust to prompt variability by integrating geometry‑aware refinement, offering a practical path toward scalable spacecraft monitoring with minimal compute overhead.

## Related Concepts  
- SAM 3 pseudo‑masks  
- GeoDistill framework  
- Signed‑distance‑field (SDF)  
- Skeleton graph  
- Area objective  
- Sample‑level gate
