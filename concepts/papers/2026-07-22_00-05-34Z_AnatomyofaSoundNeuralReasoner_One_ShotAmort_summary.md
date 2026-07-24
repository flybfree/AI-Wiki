# Summary: 2026-07-22_00-05-34Z_AnatomyofaSoundNeuralReasoner_One_ShotAmortization.md
Saved: 2026-07-24 01:23
Source: 2026-07-22_00-05-34Z_AnatomyofaSoundNeuralReasoner_One_ShotAmortization.md
Model: None

---

## Summary  
The paper investigates why neural solvers for clue‑rich Sudoku become one‑shot predictors instead of full search algorithms, identifying first‑pass poisoning and search inertness as the core phenomena. It shows that learned branching, MRV, value exclusion, and shared nogoods do not affect which instances are solved but dramatically cut repeated invalid derivations (1,497×). The LDT model’s accuracy is driven by calibration and symmetry rather than raw capacity, while search merely removes computational waste.

## Key Contributions  
- **First‑pass poisoning:** the initial forward pass commits essentially every blank cell on standard 6×6 grids (≈94–96% of blanks) and a large fraction on augmented 9×9 grids, causing hard‑slice failures before any search begins.  
- **Search inertness:** learned branching, MRV, value exclusion, and CoLT do not change solving outcomes; they only reduce repeated invalid derivations by roughly 1,497 times.  
- **Calibration and symmetry dominate accuracy:** in clue‑rich completion the LDT’s performance is set by how well it calibrates predictions and exploits symmetry; search mainly trims computational cost.

## Methodology  
The authors analyze the Lattice Deduction Transformer (LDT) across three training seeds on both standard 6×6 Sudoku and augmented 9×9 grids. They compare full‑CoLT accuracy with constraint‑graph attention, which matches it at a frozen training budget while positional tables recover only after substantially longer training, suggesting an optimization advantage rather than capacity gap. To isolate the one‑shot effect, they test from‑scratch graph coloring where LDT behaves like a pure predictor and search improves accuracy. Digit‑permutation augmentation raises 9×9 accuracy to 96.5 ± 0.3 across seeds, and a test‑time union over symmetry‑transformed passes lifts hard‑slice checkpoint pass rates from 72.8–78.9 % to 100 % without retraining.

## Results  
Full‑CoLT achieves the same accuracy as constraint‑graph attention on frozen training; positional tables need longer training to recover performance, indicating an efficiency benefit rather than a fundamental limitation. Search components cut repeated invalid derivations by ~1,497×. Digit‑permutation augmentation boosts 9×9 accuracy to 96.5 ± 0.3 across three seeds on a symmetry‑disjoint split. Symmetry‑union test‑time passes raise all three hard‑slice checkpoints from 72.8–78.9 % to 100 %, confirming that search mainly eliminates waste rather than solving harder instances.

## Significance  
These findings reveal that neural solvers can be one‑shot amortized predictors in clue‑rich completion, offering substantial sample efficiency and reducing the need for extensive learning of complex search heuristics. The analysis challenges the assumption that learned search is essential for solving; instead it shows that calibration and symmetry are primary drivers of accuracy while search merely trims computational overhead.

## Related Concepts  
Neural solvers, lattice deduction transformer (LDT), first‑pass poisoning, search inertness, constraint‑graph attention, positional tables, symmetry‑augmented completion, graph coloring, calibration, sample efficiency.
