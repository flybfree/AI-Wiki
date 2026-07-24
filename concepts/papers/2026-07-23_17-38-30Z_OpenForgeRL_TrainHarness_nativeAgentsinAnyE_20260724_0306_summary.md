# Summary: 2026-07-23_17-38-30Z_OpenForgeRL_TrainHarness_nativeAgentsinAnyEnvironm.md
Saved: 2026-07-24 03:06
Source: 2026-07-23_17-38-30Z_OpenForgeRL_TrainHarness_nativeAgentsinAnyEnvironm.md
Model: None

---

## Summary  
OpenForgeRL introduces a framework that enables end‑to‑end training of agents built around complex inference harnesses such as Claude Code, Codex, and OpenClaw. The core idea is to replace the native multi‑process inference pipeline with a lightweight proxy that records every model call as data for a standard reinforcement‑learning (RL) codebase while running each rollout in an isolated Kubernetes container. This decoupling lets researchers train agents directly on the harnesses and environments they will later deploy, without needing to modify the underlying RL stack. The approach is validated across diverse harness types and benchmarks, demonstrating superior performance over open baselines.

## Key Contributions  
- **OpenForgeRL framework**: A lightweight proxy plus a Kubernetes orchestrator that decouples training from inference for any harness‑based agent.  
- **High benchmark scores**: OpenForgeClaw reaches 31.7 pass³ and 55.9 pass@3 on ClawEval, while OpenForgeGUI attains 72.3 on WebVoyager—outperforming comparable open baselines.  
- **Harness‑RL analysis**: Empirical study showing that some harnesses (e.g., ZeroClaw) are harder to learn and that RL improves reliability such as self‑verification, tool coverage, and multi‑step planning.

## Methodology  
The authors built a proxy service that intercepts model calls from the harness, stores them in a structured format, and serves them to a standard RL agent (e.g., veRL). Each rollout is executed inside its own remote container orchestrated by Kubernetes, ensuring isolation and scalability. The recorded call‑history becomes the training data for the RL loop, allowing the same RL codebase to be reused across environments. This design avoids the need for custom stateful inference stacks that are difficult to integrate with open SFT/RL pipelines.

## Results  
Across tool/claw agents (OpenForgeClaw) and multimodal GUI browser‑computer use agents (OpenForgeGUI), OpenForgeRL consistently outperforms open baselines of similar size. In benchmark suites, it scores 31.7 pass³, 55.9 pass@3 on ClawEval, 33.7 on QwenClawBench; for GUI tasks it reaches 37.7 (OSWorld‑Verified), 63.0 (Online‑Mind2Web) and 72.3 (WebVoyager). The framework also enables rapid iteration: changing the harness or RL hyperparameters only requires updating the proxy configuration, not the training code.

## Significance  
OpenForgeRL matters because it removes a major bottleneck in deploying harness‑driven agents: the inability to train them end‑to‑end on open infrastructure. By abstracting away the complex multi‑process inference pipeline, researchers can focus on model and RL design while still benefiting from the full power of specialized harnesses. This opens the door for systematic study of how different harnesses affect learning dynamics and reliability.

## Related Concepts  
- **Harness inference**: Complex pipelines that orchestrate multiple models and tools during agent execution.  
- **Reinforcement Learning (RL)**: The standard RL codebase (veRL) used to train agents from the proxy‑generated data.  
- **Proxy service**: Lightweight component that records model calls for training without altering the harness.  
- **Kubernetes orchestrator**: Manages isolated containers per rollout, enabling scalable and reproducible training runs.  
- **Multi‑process stateful inference**: The original challenge OpenForgeRL addresses by decoupling it from RL.
