---
title: When do machine-learned exchange-correlation improvements inherit into density-functional tight binding?
url: http://arxiv.org/abs/2608.14875v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_20-30-22Z_Whendomachine_learnedexchange_correlationimproveme.md
generated_at: 2026-08-17 21:42
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how improvements in machine‑learned exchange‑correlation functionals affect density‑functional tight binding parameterizations, finding that a better parent functional does not guarantee improved parameters. It uses the transfer ratio to quantify anti‑transfer effects across covalent semiconductors.

## Key Takeaways
- The transfer ratio shows anti‑transfer where coherent negative ratios across four covalent semiconductors move the gap in the wrong direction.
- Minimal‑basis overgap is dominated by on‑site convention rather than basis incompleteness; fixing it removes most of the error and a d‑polarization shell can close 16–40% more.
- Occupied‑manifold enhancements, ionic/closed‑shell repulsive potentials affect some gaps while elemental covalent networks inherit neither gaps nor repulsive potentials.

## Context
Machine‑learned functionals aim to mimic Kohn‑Sham exchange‑correlation at low cost, and tight binding seeks large‑scale parameterization; this study bridges the gap by quantifying how changes in one affect the other. The analysis highlights that parameterizations built on multiplicative potentials cannot exactly represent orbital‑dependent operators.

## Implications
For practitioners, the transfer ratio offers a cheap pre‑test that can guide which parent functionals to use before costly reparameterizations. In industry, it may reduce computational waste and improve accuracy of large‑scale simulations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14875v1)
