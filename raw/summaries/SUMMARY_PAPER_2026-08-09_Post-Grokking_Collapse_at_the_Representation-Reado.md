---
title: Post-Grokking Collapse at the Representation-Readout Interface in Muon-Trained Transformers
url: http://arxiv.org/abs/2608.07436v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_17-21-49Z_Post_GrokkingCollapseattheRepresentation_ReadoutIn.md
generated_at: 2026-08-09 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why Muon-trained transformers fail after grokking on modular arithmetic tasks and identifies the representation-readout interface as the source of collapse. It shows that AdamW performs better while Muon’s gradient dynamics become unstable, leading to sub‑threshold performance across many configurations. The failure is not due to the training objective but to an invertible map at the readout stage that becomes unselectable.

## Key Takeaways
- Muon’s hidden matrices and AdamW embeddings produce solutions that work on the training set but generalize poorly, dropping below 27.59% across five seeds.
- The gradient magnitude drops to around 10⁻⁶ after grokking, causing optimizer step‑size elasticity of –0.03 for Muon versus +1.5 for AdamW and a speedup of eight times per parameter when the Muon group is active.
- Freezing either the embeddings or readout eliminates failure in all runs, indicating that removing the representation‑readout interface resolves the collapse.

## Context
This study highlights a hidden instability in modular neural architectures that appears only after extensive training, suggesting that representational dynamics can be more fragile than the model’s architecture. It underscores the importance of monitoring gradient behavior and optimizer sensitivity during long‑term learning.

## Implications
For practitioners, the findings warn against assuming that deeper or more complex models will automatically improve performance on modular tasks without checking downstream representation stability. Industry developers may need to incorporate early‑stopping criteria based on gradient magnitude or use regularization that preserves invertible readout structures to avoid abrupt collapses.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07436v1)
