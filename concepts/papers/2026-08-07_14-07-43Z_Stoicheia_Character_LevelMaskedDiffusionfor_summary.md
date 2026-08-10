# Summary: 2026-08-07_14-07-43Z_Stoicheia_Character_LevelMaskedDiffusionforAncient.md
Saved: 2026-08-09 22:58
Source: 2026-08-07_14-07-43Z_Stoicheia_Character_LevelMaskedDiffusionforAncient.md
Model: None

---

## Summary  
The paper introduces Stoicheia, a 405‑million‑parameter character‑level masked diffusion encoder designed to restore damaged Ancient Greek texts while simultaneously performing parsing and metrical scansion without any task‑specific retokenization. By treating the input as five independently maskable planes—letters, word/sentence boundaries, diacritics, capitalization, and punctuation—Stoicheia can fill lacunae, re‑segment, accentuate, and add punctuation directly from a single backbone. The model is pretrained on a 380 million‑word revision‑pinned corpus and evaluated across three tasks: inscription reconstruction, morphosyntactic tagging/dependency parsing, and macronization with scansion.

## Key Contributions  
- **Stoicheia architecture**: A 405M‑parameter character‑level masked diffusion model that operates on five aligned maskable planes (letters, boundaries, diacritics, capitalization, punctuation).  
- **Checkpoint diversity**: Eleven released checkpoints covering all literary passages with no overlap; one checkpoint has never seen documentary text.  
- **Quantitative gains**: 5.6 CER points on inscription reconstruction, 12.9 LAS on parsing, and 6.0 balanced‑accuracy points on macronization compared to prior baselines.

## Methodology  
The authors pretrain Stoicheia by randomly masking characters across the five planes within a diffusion framework trained on a revision‑pinned corpus of 380 million words. The model learns to reconstruct full text while respecting linguistic constraints such as word boundaries and diacritics. To ensure coverage and privacy, they release ten rotated folds that together span every literary passage, plus one fold with no documentary exposure. Experiments compare Stoicheia against prior state‑of‑the‑art systems on reconstruction error (CER), parsing loss (LAS), and macronization accuracy.

## Results  
- **Reconstruction**: 5.6 CER improvement; Ithaca test reduces character error from 24.6 to 15.5 and raises top‑1 accuracy from 63.0 to 74.5.  
- **Parsing**: LAS drops to 12.9, outperforming the 2025 Aeneas‑framework successor (≈23.5).  
- **Macronization**: Balanced accuracy rises by 6.0 points relative to earlier models.

## Significance  
Stoicheia demonstrates that a single character‑level diffusion pretraining can simultaneously address multiple downstream challenges in Ancient Greek textual analysis, eliminating the need for separate tokenizers or task‑specific fine‑tuning and thereby improving overall restoration quality across diverse challenges such as damaged inscriptions, parsing, and metrical scansion.

## Related Concepts  
- Masked diffusion models  
- Character‑level language modeling  
- Revision‑pinned corpora  
- Layered masking (letters, boundaries, diacritics, capitalization, punctuation)  
- Checkpoint diversity for privacy and coverage
