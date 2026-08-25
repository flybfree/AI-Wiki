---
title: Anchoring Bias: A Persistent Fairness Backdoor Attack against MLLMs under Continual Learning
url: http://arxiv.org/abs/2608.21577v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-21_19-28-37Z_AnchoringBias_APersistentFairnessBackdoorAttackaga.md
generated_at: 2026-08-24 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a persistent fairness backdoor attack for multimodal large language models that survives continual learning updates. It shows that the attack can embed group‑specific discrimination into the model’s latent space and keep it stable as the model is retrained on new data. Experiments reveal that the bias remains severe across multiple CL rounds, evading typical defenses.

## Key Takeaways
- The Latent Space Fairness Reinforcement technique anchors privileged‑group features while repelling targeted‑group features, creating a geometry that sustains discrimination even after updates.
- The Continual Learning Simulation iteratively adjusts the trigger to counteract simulated parameter drift, ensuring the backdoor remains functional throughout CL rounds.
- PFBA produces measurable fairness disparities that persist across continual learning cycles, demonstrating that fairness violations can be robust and long‑lasting.

## Context
Multimodal LLMs are deployed in safety‑critical applications where fairness is a core requirement. Continual learning enables models to adapt over time but also introduces parameter drift that can erode previously inserted attacks. Understanding how backdoor biases survive such updates is essential for reliable model behavior.

## Implications
This work highlights the need for fairness safeguards that account for continual learning, as existing defenses may fail against persistent attacks. Practitioners must design models with mechanisms to detect and mitigate bias that persists across training cycles, ensuring equitable outcomes in real‑world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21577v1)
