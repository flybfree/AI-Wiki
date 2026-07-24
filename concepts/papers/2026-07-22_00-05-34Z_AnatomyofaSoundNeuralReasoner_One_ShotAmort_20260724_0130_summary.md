# Summary: 2026-07-22_00-05-34Z_AnatomyofaSoundNeuralReasoner_One_ShotAmortization.md
Saved: 2026-07-24 01:30
Source: 2026-07-22_00-05-34Z_AnatomyofaSoundNeuralReasoner_One_ShotAmortization.md
Model: None

---

## Summary  
The paper investigates why the Lattice Deduction Transformer (LDT) behaves like a one‑shot predictor rather than an iterative search solver in clue‑rich Sudoku completion, identifying three phenomena: first‑pass poisoning, search inertness, and over‑amortization. By analyzing forward passes, constraint‑graph attention, and positional tables, the authors show that the model commits to most cells after a single pass, rendering subsequent branching ineffective. The study also demonstrates that augmenting digit permutations and applying symmetry‑aware test‑time unions can restore near‑perfect performance without retraining. This work bridges theory and practice by diagnosing specific architectural weaknesses in neural solvers of constraint‑rich completion problems.

## Key Contributions  
- [Finding 1] First‑pass poisoning occurs when the initial forward pass assigns values to a large fraction (≈94–96 %) of blanks, causing hard‑slice failures before any search iteration begins.  
- [Finding 2] Adding learned branching, MRV, backtracking, value exclusion, and shared nogoods does not improve solvability but reduces repeated invalid derivations by a factor of ~1,497.  
- [Finding 3] On from‑scratch graph coloring tasks the one‑shot behavior disappears, indicating that LDT‑like systems are only one‑shot amortized predictors in clue‑rich settings.

## Methodology  
The authors trained LDT on both standard 6×6 and augmented 9×9 Sudoku instances using constraint‑graph attention and positional tables. They measured accuracy across three symmetry‑disjoint training seeds, compared the performance of attention‑only vs. full CoLT models, and evaluated test‑time strategies such as digit‑permutation augmentation and union over symmetry transforms. Additionally, they tested LDT on a graph‑coloring benchmark to contrast clue‑rich versus non‑clue‑rich behavior.

## Results  
- 9×9 accuracy rises from <1 % (random) to 96.5 ±0.3 after digit‑permutation augmentation across seeds.  
- Test‑time union over symmetry transforms converts hard‑slice checkpoints from 72.8–78.9 % to 100 % without retraining.  
- Full CoLT matches attention‑only accuracy, while positional tables recover only with longer training, highlighting sample‑efficiency gains.

## Significance  
Understanding LDT’s one‑shot amortization reveals a design flaw that wastes compute and data; fixing it through augmentation or symmetry handling can dramatically improve real‑world solver performance. The findings also suggest that many neural solvers are not genuine search procedures but calibrated predictors, prompting research into more robust iterative architectures.

## Related Concepts  
- One‑shot amortization: the model’s accuracy is set in a single forward pass rather than through repeated iterations.  
- First‑pass poisoning: early commitment to cell values leads to premature dead ends.  
- Search inertness: subsequent search steps fail because the initial state already encodes the solution.  
- Constraint‑graph attention: a mechanism for encoding and querying partial solutions.  
- Positional tables: learned lookup structures that aid in value exclusion.  
- Symmetry‑aware testing: leveraging board symmetries to boost test accuracy without retraining.
