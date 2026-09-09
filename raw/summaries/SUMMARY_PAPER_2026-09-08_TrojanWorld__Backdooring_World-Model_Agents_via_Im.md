---
title: TrojanWorld: Backdooring World-Model Agents via Imagination Steering
url: http://arxiv.org/abs/2609.07051v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_05-14-10Z_TrojanWorld_BackdooringWorld_ModelAgentsviaImagina.md
generated_at: 2026-09-08 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TrojanWorld, a backdoor attack that manipulates world-model agents by steering their imagination through physical triggers. It achieves near-zero deviation in target-action selection while preserving clean performance, and the compromised behavior persists after trigger removal. Experiments on TD-MPC2, DreamerV3, and R2-Dreamer show up to 0.026 deviation with >98.8% clean accuracy.

## Key Takeaways
- The attack uses a physical object as a trigger that activates only during perception, allowing stealthy deployment without altering the observation stream.
- Decision‑Reflective Induction combined with decision feedback steers imagination toward attacker‑specified actions while keeping predictive fidelity high.
- Causal Propagation maintains the induced preference even after the trigger disappears, enabling persistent malicious behavior.

## Context
World models are central to model‑based reinforcement learning, allowing agents to simulate future dynamics. Their pretrained nature creates a supply chain where backdoors could silently corrupt downstream systems, a concern that has not been fully addressed in interactive settings.

## Implications
This work highlights the need for robust detection and mitigation strategies for backdoor attacks targeting world models in autonomous agents. Practitioners must consider how perception‑based triggers can compromise system integrity and plan safeguards accordingly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07051v1)
