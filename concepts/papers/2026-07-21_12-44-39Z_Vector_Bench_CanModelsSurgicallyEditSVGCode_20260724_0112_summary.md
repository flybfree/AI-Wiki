# Summary: 2026-07-21_12-44-39Z_Vector_Bench_CanModelsSurgicallyEditSVGCode.md
Saved: 2026-07-24 01:12
Source: 2026-07-21_12-44-39Z_Vector_Bench_CanModelsSurgicallyEditSVGCode.md
Model: None

---

## Summary  
Vector‑Bench is a new benchmark that tests whether large language models can perform *surgical* edits on SVG code while preserving the rest of the document. The authors create 40 paired tasks where each task supplies a corrupted program, a visual instruction, and a hidden target, then score model outputs against a strict binary specification reward that requires both correctness and no unintended changes. Their experiments evaluate 34 different model endpoints across 1 360 requests, revealing a large gap between visible repair progress and faithful specification adherence.

## Key Contributions  
- **Finding 1:** Mean repair progress (≈43.7%) does not translate into high full‑specification success rates.  
- **Finding 2:** The strongest endpoint achieves only ~15 % of the required binary specification, despite the high average progress.  
- **Finding 3:** Unintended Change Rate (UCR) and validity‑gated repair progress together explain much of the partial outcomes.

## Methodology  
Vector‑Bench constructs a compact benchmark with 40 SVG repair tasks. Each task contains a corrupted program, an author‑written visual instruction that describes only visible defects without exposing element identifiers or path data, a hidden target program, and five annotated repairs on average. The binary specification reward uses attribute‑aware perceptual tolerances to verify that requested changes are applied while leaving all other structure unchanged; canonical equality and source fidelity serve as diagnostics. Validity‑gated repair progress (a near‑complete tier) and the Unintended Change Rate (UCR) are computed to capture partial outcomes.

## Results  
We evaluated 34 model endpoints—25 open‑weight, 5 inexpensive controls, and 4 frontier closed models—over 1 360 requests. The average repair progress across all tasks is 43.7 %, but the best endpoint’s full specification success rate is merely 15.0 %. Partial successes are largely accounted for by validity‑gated progress (≈38 %) and UCR (≈22 %). These findings demonstrate that visual‑level improvements do not guarantee precise, specification‑faithful SVG edits.

## Significance  
Vector‑Bench exposes a critical mismatch between the intuitive notion of “repair” and the rigorous binary requirement for correct, non‑intrusive editing. By quantifying both visible progress and strict specification adherence, it highlights the need for more robust evaluation metrics in instruction‑based vector editing beyond raster‑image judgments.

## Related Concepts  
- SVG (Scalable Vector Graphics)  
- Vector editing / surgical edit of code  
- Instruction‑based editing  
- Binary specification reward  
- Perceptual tolerances  
- Unintended Change Rate (UCR)  
- Validity‑gated repair progress
