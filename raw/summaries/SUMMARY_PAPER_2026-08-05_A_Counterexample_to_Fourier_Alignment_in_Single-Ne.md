---
title: A Counterexample to Fourier Alignment in Single-Neuron Modular Addition
url: http://arxiv.org/abs/2608.04451v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_04-56-53Z_ACounterexampletoFourierAlignmentinSingle_NeuronMo.md
generated_at: 2026-08-05 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper presents a counterexample to the Fourier alignment conjecture in single-neuron modular addition, showing that a neuron can become inactive while its Fourier energy remains uniformly spread across frequencies. This demonstrates that single-frequency alignment does not follow from training dynamics on this model.

## Key Takeaways
- An initially active ReLU neuron can become completely inactive within finite time and settle at a limit where the Fourier energy is equally distributed among all nonzero real frequency classes.
- The counterexample occurs for an open set of initial conditions, implying positive probability under Gaussian initialization.
- The failure extends to every Clarke trajectory from that open set, even with smooth dead‑zone ReLU approximations and fixed‑step full‑batch gradient descent.

## Context
This work challenges a longstanding belief in neural network training theory by revealing that Fourier alignment is not guaranteed for single neurons. It highlights the gap between idealized analysis and realistic training settings where numerical methods like finite steps can produce pathological outcomes.

## Implications
For practitioners, this suggests that relying on Fourier energy as a proxy for learning progress may be misleading. Researchers should consider more robust metrics or validate assumptions with empirical examples rather than theoretical guarantees alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04451v1)
