---
title: HOPPER: Learnable Hop Extraction for Linearized Graph Sequence Models
url: http://arxiv.org/abs/2608.09031v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_02-31-46Z_HOPPER_LearnableHopExtractionforLinearizedGraphSeq.md
generated_at: 2026-08-10 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
HOPPER is an end‑to‑end learnable extension of Linearized Graph Sequence Models that learns how to extract hop sequences before they are processed by a state‑space model, enabling flexible adaptation to graph structure and node features while preserving permutation equivariance. The framework demonstrates state‑of‑the‑art performance on the ECHO‑Synth benchmark and shows that adjusting the message backtracking window can further improve accuracy on long‑range physics benchmarks.

## Key Takeaways
- HOPPER learns a custom hop extraction process, allowing the model to adapt propagation depth to specific graph inputs rather than relying on fixed operators.  
- The framework supports feature‑conditioned and structure‑aware mechanisms that maintain permutation equivariance across different graph topologies.  
- Varying the maximum neighborhood size of message backtracking cancellation can optimize accuracy for long‑range dependencies, highlighting the importance of structural memory windows.

## Context
This work advances the field by decoupling information depth from processing depth in graph neural networks, a known challenge that limits deep architectures and causes over‑smoothing. By treating node propagation as a sequence and learning its extraction, HOPPER offers a principled way to handle long‑range dependencies without sacrificing scalability.

## Implications
For practitioners, HOPPER provides a modular toolkit that can be integrated into existing graph models with minimal architectural changes, facilitating research on diverse tasks such as physics simulation and knowledge graph reasoning. Industry applications could leverage this flexibility to build more accurate and efficient graph representations for real‑world data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09031v1)
