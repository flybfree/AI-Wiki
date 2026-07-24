# Summary: 2026-07-21_02-23-22Z_SpaghettiArchitect_AContamination_Resistant_By_Con.md
Saved: 2026-07-24 00:30
Source: 2026-07-21_02-23-22Z_SpaghettiArchitect_AContamination_Resistant_By_Con.md
Model: None

---

## Summary  
Spaghetti Architect addresses the lack of controlled, contamination‑resistant code datasets by generating multi‑language programs from a clean JSON intermediate representation. It ensures correctness via an anti‑optimization transpiler that maps the IR to deliberately redundant flattened code in five languages while checking each instance against a reference oracle. The tool also provides orthogonal difficulty labels (intrinsic vs incidental) and resists contamination through private seed variants.

## Key Contributions  
- [Finding 1] Controlled generation of multi‑language code from a known optimal reference IR, eliminating uncontrolled messiness.  
- [Finding 2] Orthogonal difficulty labeling that distinguishes intrinsic problem size from incidental presentation, enabling fine‑grained evaluation.  
- [Finding 3] Empirical evidence that dataset annotations improve model performance, especially for weaker models.

## Methodology  
The authors designed Spaghetti Architect as an anti‑optimization transpiler that takes a clean JSON IR, applies nested anti‑pattern profiles to create redundant code in Python, JavaScript, Go, Java, and C++, compiles each program, runs it, and validates the output against a reference oracle. Difficulty is dialed by adjusting profile depth; contamination is avoided by minting fresh variants from a private held‑out seed.

## Results  
Experiments on four open models show exact match scores increase with scale; the intrinsic knob collapses arithmetic‑aggregation accuracy to zero for strong models. Development‑set scores match freshly re‑minted held‑out counterparts within |Δ| ≤ 0.012 (comprehension) and ≤ 0.011 (refactoring). Refactoring equivalence improves from 0.73 to 0.99, scale‑invariant, while prediction collapses; annotation ablation lifts the weaker model by –0.173 versus –0.017 for the unannotated ladder.

## Significance  
By providing a reproducible, contamination‑free dataset with precise difficulty labels, Spaghetti Architect enables fair evaluation and mitigates overfitting to existing corpora; the orthogonal labeling helps researchers isolate intrinsic vs incidental complexity; annotation benefits are significant across model strengths.

## Related Concepts  
- JSON intermediate representation  
- Anti‑optimization transpiler  
- Orthogonal difficulty axes (intrinsic, incidental)  
- Contamination resistance via private seed  
- Refactoring equivalence  
- Ablation study  
- Open‑ladder benchmarking
