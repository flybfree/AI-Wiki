---
title: "Summary: 2026-05-21_17-58-06Z_RemembertobeCurious_EpisodicContextandPersistentWo.md"
date: 2026-05-21
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-21_17-58-06Z_RemembertobeCurious_EpisodicContextandPersistentWo.md


**Source**: [Original Paper](http://arxiv.org/abs/2605.22814v1)
Saved: 2026-05-22 00:12
Source: 2026-05-21_17-58-06Z_RemembertobeCurious_EpisodicContextandPersistentWo.md
Model: None

---


## Summary  
The paper tackles the problem that curiosity‑driven reinforcement learning often fails in complex, photorealistic 3D environments because agents cannot maintain a stable model of the world and lack episodic context to explore beyond local loops. By introducing a persistent online 3D reconstruction as a world model and an agent policy parameterized as a sequence model over RGB observations, the authors create a system that can continuously update its knowledge while remembering past trajectories, thereby encouraging exploration toward novel regions. Their end‑to‑end design enables zero‑shot transfer to new worlds such as Gibson and AI‑generated scenes, outperforming conventional active‑mapping baselines.

## Key Contributions  
- [Finding 1] A persistent world model built from an online 3D reconstruction provides a stable intrinsic reward signal that does not reset when the agent revisits states.  
- [Finding 2] The agent maintains an episodic trajectory history, allowing it to remember previously visited regions and navigate toward unexplored areas.  
- [Finding 3] An end‑to‑end policy that combines sequence modeling over RGB frames generalizes zero‑shot to unseen worlds and achieves superior performance on downstream tasks like apple picking and image‑goal navigation.

## Methodology  
The authors adopt a curiosity‑based reinforcement learning framework where the intrinsic reward is derived from the prediction error between the agent’s 3D reconstruction model and sensory input. The world model is updated online using a depth camera, producing a continuous 3D representation that persists across episodes. Simultaneously, the policy is implemented as a sequence model (e.g., LSTM or Transformer) that consumes RGB frames, preserving an episodic memory of past observations to guide future actions. Training occurs on the HM3D dataset, which contains diverse indoor scenes with sparse rewards for picking apples and navigating to goals.

## Results  
Compared to RL‑based active mapping baselines (e.g., MAPF), the proposed system achieves higher cumulative reward during training and demonstrates zero‑shot transfer to Gibson and AI‑generated 3D worlds. In downstream tasks, the agent reaches apples with fewer steps than from‑scratch baselines and navigates goal locations without explicit retraining. Video demos illustrate smooth exploration and task completion.

## Significance  
This work resolves a longstanding limitation of curiosity learning in photorealistic 3D: the inability to sustain exploration due to transient world models and lack of episodic memory. By integrating persistent reconstruction with sequence‑based episodic policies, the authors provide a scalable architecture that can be deployed directly from RGB inputs, opening avenues for real‑world robotics and transferable AI agents.

## Related Concepts  
- Intrinsic reward / curiosity signal  
- Persistent world model (online 3D reconstruction)  
- Episodic memory in reinforcement learning  
- Sequence modeling over visual observations  
- Active mapping baselines  
- Zero‑shot generalization to new environments

[[Remember to be Curious: Episodic Context and Persistent Worlds for 3D Exploration]]