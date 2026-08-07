---
title: Small Foundation Models of Human Cognition and Behaviour
url: http://arxiv.org/abs/2608.05224v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_11-34-20Z_SmallFoundationModelsofHumanCognitionandBehaviour.md
generated_at: 2026-08-06 21:36
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether small language models can replicate human cognitive performance across a wide range of tasks using behavioural data. It finds that models with 600M to 1B parameters match larger baselines on held-out participants, while scaling matters more for out-of-distribution tasks. The results show that models rely heavily on stimulus and feedback information.

## Key Takeaways
- Models trained from 600M to 1B parameters can achieve performance comparable to a 70B model on unseen participants, indicating a narrow effective capacity ceiling.
- Removing stimulus or outcome feedback eliminates most learned knowledge, showing that choice history alone is insufficient for task execution.
- Trial order matters: models are invariant when trials are independent but sensitive where response order influences later choices.

## Context
This work addresses the gap between massive language models and the need for compact cognitive proxies in psychology. By demonstrating that tiny models suffice for many experiments, it suggests a new approach to efficient AI‑driven behavioural research.

## Implications
Researchers can deploy lightweight models as cost-effective alternatives to large LLMs without sacrificing predictive power on standard datasets. Practitioners may integrate these models into experimental pipelines to reduce computational overhead while maintaining accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05224v1)
