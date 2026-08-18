---
title: Solvable Sokoban Without a Solver via Diffusion
url: http://arxiv.org/abs/2608.15958v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_23-17-07Z_SolvableSokobanWithoutaSolverviaDiffusion.md
generated_at: 2026-08-17 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a transformer‑based discrete diffusion model that predicts whether a Sokoban puzzle is solvable without ever using a solver, reward signal or explicit solvability labels. Trained only to fill masked tiles, the model reaches a 77.4 % correct solvability rate and can make 94.5 % of unsolvable puzzles solvable by removing a single wall.

## Key Takeaways
- The model’s global solvability emerges from its local objective of completing tile placements, showing that a simple generation task can inherit a complex decision property.
- Masked diffusion differs from autoregressive factorization: it conditions on any subset of cells and can reveal them in arbitrary order, better matching the non‑local constraints of Sokoban.
- Puzzle difficulty stems from interactions across distant parts of the board; a generator that is not locked into a fixed sequence aligns more closely with how solvability is actually determined.

## Context
This work highlights how generative AI can capture high‑level properties such as solvability from low‑level data, bridging the gap between puzzle solving and generation. By training on tile completion alone, the model demonstrates that local objectives can encode global constraints, a concept relevant to many PSPACE‑complete problems.

## Implications
For researchers, this approach offers a pathway to automatic solvability assessment without expensive solvers. Practitioners could leverage it for game design tools, where generating puzzles with desired difficulty is possible without manual verification. The method may inspire similar techniques for other complex decision tasks in AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15958v1)
