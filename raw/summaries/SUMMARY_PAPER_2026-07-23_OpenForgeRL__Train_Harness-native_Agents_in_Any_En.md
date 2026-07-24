---
title: OpenForgeRL: Train Harness-native Agents in Any Environment
url: http://arxiv.org/abs/2607.21557v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_17-38-30Z_OpenForgeRL_TrainHarness_nativeAgentsinAnyEnvironm.md
generated_at: 2026-07-23 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
OpenForgeRL is an open‑source framework that enables end‑to‑end training of agents built on harnesses such as Claude Code, Codex, and OpenClaw across any environment. By introducing a lightweight proxy that records harness calls for a standard RL codebase and a Kubernetes orchestrator that runs each rollout in isolated containers, the method decouples inference from training, allowing researchers to study and improve agents directly within their real‑world harnesses.

## Key Takeaways
- A lightweight proxy serves the harness's model calls while recording them as data for a conventional RL codebase like veRL.  
- A Kubernetes orchestrator executes each rollout in its own remote container, facilitating large‑scale training on any environment.  
- With only hundreds to a few thousand tasks, OpenForgeClaw achieves 31.7 pass³ and 55.9 pass@3 on ClawEval, matching or exceeding larger open baselines.

## Context
Training harness‑native agents remains challenging because the inference process is stateful and tightly coupled with the RL training loop. Existing approaches either require custom wrappers that limit flexibility or cannot be integrated into standard RL stacks. This paper tackles the problem by providing a generic infrastructure that abstracts away these couplings, making it possible to train diverse agents uniformly.

## Implications
The framework lowers the barrier for researchers and practitioners to experiment with different harnesses, accelerating progress in multi‑step reasoning and tool use. By exposing how harness choice influences learning dynamics, OpenForgeRL contributes valuable insights into agent reliability, self‑verification, and plan completion, which are critical for real‑world deployment of AI agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21557v1)
