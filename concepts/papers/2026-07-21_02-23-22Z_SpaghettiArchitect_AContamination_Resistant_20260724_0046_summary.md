# Summary: 2026-07-21_02-23-22Z_SpaghettiArchitect_AContamination_Resistant_By_Con.md
Saved: 2026-07-24 00:46
Source: 2026-07-21_02-23-22Z_SpaghettiArchitect_AContamination_Resistant_By_Con.md
Model: None

---

## Summary  
Spaghetti Architect is a tool that mints code datasets with guaranteed correctness (construct‑validity) and controllable difficulty, addressing the uncontrolled nature of existing mined corpora. It creates language‑agnostic JSON intermediate representations that are deliberately transformed into redundant programs in five languages via an anti‑optimization transpiler. The generated programs are validated against a reference oracle to ensure they are correct by construction. Difficulty is dialed using nested anti‑pattern profiles and labeled on two orthogonal axes, while contamination is avoided through private seed variants.  

## Key Contributions  
- A tool that mints code datasets with guaranteed correctness (construct‑validity) and controllable difficulty.  
- Two orthogonal difficulty axes (intrinsic problem size vs incidental presentation) and a labeling scheme that isolates intrinsic versus incidental factors.  
- Experimental evidence showing that annotated difficulties improve model performance, especially for weaker models.  

## Methodology  
The authors start with clean JSON IR, apply an anti‑optimization transpiler to flatten the code in five languages (Python, JavaScript, Go, Java, C++), compile and run each program, compare it against a reference oracle, and then generate variants using private seed data. Difficulty is controlled by nested anti‑pattern profiles; labeling is performed via intrinsic (problem size) and incidental axes to separate difficulty sources.  

## Results  
Construct‑validity metrics move with established complexity and readability scores. On four open models, exact match rises with scale; the intrinsic knob collapses arithmetic‑aggregation accuracy to zero. Development‑set scores match freshly re‑minted held‑out counterparts within Δ≤0.012 (comprehension) and ≤0.011 (refactoring). Refactoring equivalence improves from 0.73 to 0.99, scale‑invariant; prediction collapses. Ablation shows annotated ladder inflates the weakest model by –0.173 versus –0.017 for the strongest model: the annotated ladder resolves one of three adjacent pairs where the unannotated resolves all three.  

## Significance  
It provides a reliable benchmark for code‑generation models, enabling fair comparison and reducing overfitting to noisy corpora. The labeled difficulty axes allow researchers to isolate intrinsic versus incidental factors, improving interpretability of model behavior.  

## Related Concepts  
Construct‑validity, anti‑optimization transpiler, orthogonal difficulty axes, contamination resistance, self‑annotation ablation, reference oracle, model ladder.
