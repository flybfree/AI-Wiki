---
title: Beyond Success and Failure: Length-Aware Contrastive Learning for GUI Agents
url: http://arxiv.org/abs/2608.21830v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_08-01-47Z_BeyondSuccessandFailure_Length_AwareContrastiveLea.md
generated_at: 2026-08-24 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Length-Aware Contrastive Learning for GUI Agents (LACL-GUI), a contrastive reinforcement learning framework that uses trajectory-level quality signals to improve policy optimization in graphical user interface agents. Experiments show LACL-GUI yields more effective learning signals and consistently outperforms prior methods.  

## Key Takeaways  
- LACL-GUI incorporates structured preferences within both successful and failed trajectories, encouraging concise successful executions while differentiating failure quality based on divergence from successful trajectories.  
- The framework leverages trajectory-level supervision rather than outcome-only labels to generate stronger contrastive signals for policy optimization.  
- Experiments demonstrate that LACL-GUI provides more effective learning signals and consistently improves agent performance over prior methods.  

## Context  
In multimodal reinforcement learning, reward gradient misalignment remains a challenge for GUI automation. Contrastive RLVR methods have addressed stability but lack fine-grained trajectory supervision. This work bridges the gap by introducing detailed trajectory quality cues into contrastive training.  

## Implications  
This approach shows that detailed trajectory information can enhance RL agents' efficiency and reliability in UI environments, offering a scalable method for industry deployment and future research on trajectory-aware learning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21830v1)
