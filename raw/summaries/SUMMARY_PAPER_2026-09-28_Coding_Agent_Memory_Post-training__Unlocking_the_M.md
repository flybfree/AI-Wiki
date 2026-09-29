---
title: Coding Agent Memory Post-training: Unlocking the Memory Potential of Pre-trained File Operations for Long-Horizon Tasks via Reinforcement Learning
url: http://arxiv.org/abs/2609.34422v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_06-40-28Z_CodingAgentMemoryPost_training_UnlockingtheMemoryP.md
generated_at: 2026-09-28 22:55
model: qwen3.6-35b-a3b
---

## Summary
The paper addresses the challenge of long-horizon tasks where interaction histories exceed model context limits by introducing Coding Agent Memory Gym (CAMG) and CAMG-RL. By leveraging pre-trained file operations within persistent workspaces across diverse environments, the approach enables agents to learn effective memory management via reinforcement learning without relying on environment-specific interfaces. The resulting models achieve performance competitive with significantly larger counterparts on benchmarks like SWE-bench Verified and MLE-bench Lite.

## Key Takeaways
- CAMG provides long-horizon agentic-RL environments (Shop, Coding, DeepResearch, AutoResearch) equipped with executable shell access and episode-persistent workspaces, allowing agents to utilize file creation, revision, search, and reuse as a natural memory mechanism grounded in pre-training capabilities.
- CAMG-RL employs fully asynchronous PPO to train a single policy jointly across all four environments, learning file-based memory behavior directly from downstream task rewards rather than predefined memory tools, thereby decoupling learned behaviors from specific environment interfaces.
- Trained models CAMG-RL-4B and CAM

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34422v1)
