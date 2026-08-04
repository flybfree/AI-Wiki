---
title: Deferred Exposure of Future Trajectories for Verifiable Reasoning in Autonomous Driving VLMs
url: http://arxiv.org/abs/2608.01755v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_06-24-36Z_DeferredExposureofFutureTrajectoriesforVerifiableR.md
generated_at: 2026-08-03 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the problem of trajectory anchoring bias in chain-of-thought reasoning for autonomous driving vision-language models by showing that exposing ground-truth future trajectories to teachers leads to less causally faithful decisions and hallucinations. The authors propose Deferred Exposure of Future Trajectories for RLVR (DEFT-RLVR) which replaces pre-decision anchors with post-decision verification targets, improving reasoning while preserving visual capabilities. Their framework also introduces Autonomous-Driving Multiple-Choice Question (AD-MCQ) as a scalable way to cast planning as selection among explicit trajectory candidates.

## Key Takeaways
- Teacher models rationalize revealed ground-truth trajectories instead of inferring decisions from scene evidence, causing anchoring bias.
- Removing the GT trajectory reduces hallucinations but makes open-ended trajectory generation difficult for high-level decision-making and low-level dynamics.
- DEFT-RLVR transforms future trajectories into verification targets after decisions are made, improving reasoning without sacrificing visual performance.

## Context
Current VLA models rely on chain-of-thought supervision to guide autonomous driving agents, yet their annotation pipelines often leak the correct outcome, undermining causal learning. This work highlights a critical gap where verification of reasoning must be decoupled from trajectory synthesis to ensure robustness and interpretability.

## Implications
For practitioners developing verifiable AD systems, DEFT-RLVR offers a practical method to evaluate decisions without requiring full trajectory generation. The approach can be integrated into existing training loops, making it scalable for real-world deployment and research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01755v1)
