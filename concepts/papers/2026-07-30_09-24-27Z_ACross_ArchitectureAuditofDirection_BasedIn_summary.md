# Summary: 2026-07-30_09-24-27Z_ACross_ArchitectureAuditofDirection_BasedInference.md
Saved: 2026-07-30 21:42
Source: 2026-07-30_09-24-27Z_ACross_ArchitectureAuditofDirection_BasedInference.md
Model: None

---

## Summary  
The paper audits five direction‑based inference‑time defenses across a wide range of vision‑language models to determine which candidates best balance refusal recovery and utility preservation while remaining architecture‑agnostic. It finds that no single defence dominates universally, but the image‑conditioning shift is the only one that retains utility at the noise floor on LLaVA 1.5 and Pixtral 12B, albeit with strong non‑transferability across families. The CMRM direction shows a high cosine alignment (mean 0.35) with this shift, indicating partial geometry overlap between two recipes. Finally, the authors demonstrate that direction‑based attacks are largely architecture‑specific and not interchangeable, even within the only comparable pair of models.

## Semantic links
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 4 title terms overlap; 2 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-08-03_14-21-21Z_NANQ_Noise_Floor_AwareMixed_PrecisionNon_Un_summary.md|Summary: 2026-08-03_14-21-21Z_NANQ_Noise_Floor_AwareMixed_PrecisionNon_UniformQu.md]] — 4 title terms overlap; 12 summary/topic terms overlap; semantic match 0.08
- [[concepts/papers/2026-07-28_15-38-27Z_A2TTA_Anchored_and_AgileTest_TimeAdaptation_summary.md|Summary: 2026-07-28_15-38-27Z_A2TTA_Anchored_and_AgileTest_TimeAdaptationforEvol.md]] — 4 title terms overlap; 8 summary/topic terms overlap; semantic match 0.03

## Key Contributions  
- [Finding 1] No single defence dominates on both refusal recovery and utility preservation across all model families; the image‑conditioning shift is best for LLaVA 1.5 and Pixtral 12B with minimal utility loss, but it is architecture‑specific.  
- [Finding 2] The CMRM direction exhibits a strong positive cosine alignment (0.35 mean) with the image‑conditioning shift in every cell, revealing partial geometry overlap between two recipes.  
- [Finding 3] Direction‑based defences are non‑transferable across architectures; only the comparable LLaVA 1.5 13B and Pixtral 12B pair shows similar behaviour, while a prompt instruction can dominate on Qwen2.5 VL.

## Methodology  
The authors compare five defence candidates—mean image conditioning shift, CMRM refusal direction, ShiftDC residual attack, prompt instruction to ignore the image, and random control—across 15 model‑and‑layer cells from four architectural families (LLaVA, Pixtral, Qwen2.5 VL, Qwen2 VL 2B). They employ a magnitude‑controlled protocol that matches the intervention size for each prompt and pairs every direction with a random control vector of identical norm to isolate effect.

## Results  
The image‑conditioning shift achieved the lowest utility loss (at measurement noise floor) on LLaVA 1.5 and Pixtral 12B, while other candidates varied: CMRM led on Qwen2 VL 2B, ShiftDC on Qwen2 VL 2B, and a prompt instruction on Qwen2.5 VL. The CMRM direction aligns with the image‑conditioning shift in all 15 cells (cosine mean 0.35, range 0.17–0.65), indicating they recover overlapping geometry. Direction‑specificity is observed in 13 of 15 cells; the only compatible pair (LLaVA 1.5 13B ↔ Pixtral 12B) shows similar behaviour, underscoring non‑transferability.

## Significance  
These findings highlight that direction‑based inference‑time defences cannot be treated as generic solutions; they must be calibrated per language decoder family and often fail to transfer across architectures. The observed geometry overlap suggests shared underlying mechanisms but also reveals the limits of cross‑model applicability, guiding future research on robust, architecture‑aware jailbreak mitigations.

## Related Concepts  
- Inference‑time defences, vision‑language models, residual stream attacks, direction‑based jailbreaks, utility preservation, cosine alignment, architecture specificity, modality refusal geometry.
