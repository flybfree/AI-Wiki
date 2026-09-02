---
title: Elite-Weighted Supervised Fine-tuning for Goal-Directed Molecular Optimization
published: 2026-08-31T18:10:51Z
authors: Shiyun Wa, Yifei Wang, Anna G. Green, Simone Sciabola, Ye Wang
url: http://arxiv.org/abs/2609.00189v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Elite-Weighted Supervised Fine-tuning for Goal-Directed Molecular Optimization

## Abstract
Goal-directed optimization is essential for steering molecular generators to propose candidates with desired properties. However, it is often implemented with policy-gradient reinforcement learning, which requires a generation-trajectory log-probability whose form depends on the model architecture and generation procedure. This makes an optimizer difficult to reuse across architectures and conditional generative designs. Supervised fine-tuning needs none of that machinery, but its update is driven by a fixed dataset, so the reward never enters the update. We introduce Elite-Weighted Supervised Fine-tuning (EW-SFT), which uses reward to guide elite selection of high-scoring molecules, and updates the model by its own pretraining loss on that set. Ablations show that reward information is passed primarily through elite selection, rather than through continuous weighting within the selected set. Because the update consumes only scored molecules and the model's native loss, the same rule applies across autoregressive, masked-diffusion, and discrete-flow generators, and across de novo, motif-extension, and linker-design tasks. Under a fixed budget of 3D shape alignment oracle calls on two kinase reference compounds, EW-SFT consistently outperforms the corresponding native optimizers. It further improves goal-directed optimization under a 2D similarity oracle on four held-out references and achieves comparable performance on a sample-efficiency benchmark without a trajectory-level RL formulation. These results demonstrate that EW-SFT is a unified and effective optimizer across molecular generators, design constraints, references, and oracles.

## Metadata
- **Published**: 2026-08-31T18:10:51Z
- **Authors**: Shiyun Wa, Yifei Wang, Anna G. Green, Simone Sciabola, Ye Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00189v1)