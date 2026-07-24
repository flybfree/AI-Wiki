# Summary: 2026-07-21_12-44-39Z_Vector_Bench_CanModelsSurgicallyEditSVGCode.md
Saved: 2026-07-24 00:46
Source: 2026-07-21_12-44-39Z_Vector_Bench_CanModelsSurgicallyEditSVGCode.md
Model: None

---

## Summary  
Vector‑Bench is a compact benchmark that tests whether language models can perform *surgical* edits on SVG code while preserving the visual appearance and structural integrity of the document. The authors create 40 tasks where each corrupted program is paired with a human‑written visual instruction, a hidden target program, and multiple annotated repairs, all scored by a binary specification reward that demands attribute‑aware perceptual tolerances. Their evaluation across 34 model endpoints shows that models can achieve modest repair progress but rarely meet the full specification, highlighting a persistent gap between visible output and precise code editing.

## Key Contributions  
- [Finding 1] The benchmark reveals that apparent repair progress (≈ 43.7% mean) does not translate into high‑level specification success, indicating that models often produce visually acceptable but semantically incorrect edits.  
- [Finding 2] Vector‑Bench provides a deterministic binary reward scheme and diagnostic metrics (validity‑gated repair progress, Unintended Change Rate) to separate visual correctness from precise attribute preservation.  
- [Finding 3] Even the strongest model endpoints achieve only ~15 % full specification success over 1360 requests, underscoring that current models lack robust attribute‑aware editing capabilities.

## Methodology  
The authors assembled a dataset of 40 SVG repair tasks. For each task they supplied: (i) a corrupted SVG program, (ii) an author‑written visual instruction describing the defect without exposing element identifiers or path data, (iii) a hidden target program that is the exact desired output, and (iv) five annotated repairs with average 60.55 protected objects per task. Scoring uses a binary specification reward: edits must respect attribute‑aware perceptual tolerances, keep rendering‑relevant structure unchanged, produce valid SVG, and maintain canonical target equality or stricter source fidelity as diagnostics.

## Results  
Over 1360 model requests evaluated across 34 endpoints (25 open‑weight, 5 inexpensive controls, 4 frontier closed), the best endpoint achieved 15.0 % full specification success. Mean repair progress was 43.7 %, and a validity‑gated tier captured most repairs as “good” but still many produced Unintended Change Rates (UCR) that violated protected objects or introduced new structural changes.

## Significance  
Vector‑Bench demonstrates that visual perception alone is insufficient for precise vector editing; models must be evaluated on attribute‑level fidelity. The benchmark and its metrics guide research toward more robust, specification‑faithful editors, which could enable reliable automated SVG manipulation in design, web graphics, and accessibility tools.

## Related Concepts  
SVG (Scalable Vector Graphics), vector editing, instruction‑based editing, perceptual tolerances, binary specification reward, Unintended Change Rate (UCR), validity‑gated repair progress, canonical target equality, semantic unchanged structure.
