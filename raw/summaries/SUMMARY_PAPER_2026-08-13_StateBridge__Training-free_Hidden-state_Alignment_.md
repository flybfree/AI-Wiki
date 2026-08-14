---
title: StateBridge: Training-free Hidden-state Alignment for Latent Communication in LLM Multi-Agent Systems
url: http://arxiv.org/abs/2608.13317v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_14-40-59Z_StateBridge_Training_freeHidden_stateAlignmentforL.md
generated_at: 2026-08-13 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces StateBridge, a training-free method for aligning continuous hidden states between agents in multi‑agent LLM systems. By using an orthogonal transformation and lightweight calibration, the authors eliminate the need for trained projectors or working‑memory layers. Evaluations on 26 model‑task pairs show that StateBridge matches or exceeds the best baseline across most tasks.

## Key Takeaways
- The method aligns sender final‑layer hidden states to receiver input space via a closed‑form orthogonal transformation, preserving information that discrete tokens cannot capture.
- Lightweight norm calibration and vocabulary anchoring make the alignment compatible with pretrained token distributions without additional training.
- The aligned continuous prefix is prepended to the receiver’s input, enabling seamless latent communication across diverse model families.

## Context
Latent communication aims to transmit rich internal representations directly rather than through text tokens. Existing approaches often require custom layers or trained projectors, limiting portability and scalability in large‑scale multi‑agent environments.

## Implications
StateBridge offers a practical solution that can be deployed across existing LLM pipelines without retraining, reducing development time and cost. This could accelerate the integration of hidden‑state communication into commercial AI agents, fostering more efficient and expressive interactions between autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13317v1)
