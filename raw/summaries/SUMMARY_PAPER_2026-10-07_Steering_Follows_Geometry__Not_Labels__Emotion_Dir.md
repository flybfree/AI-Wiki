---
title: Steering Follows Geometry, Not Labels: Emotion Directions in a Full-Duplex Speech Model
url: http://arxiv.org/abs/2610.08887v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-06_15-29-37Z_SteeringFollowsGeometry_NotLabels_EmotionDirection.md
generated_at: 2026-10-07 21:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether emotion can be controlled in a full-duplex speech language model (Moshi) through activation steering, a technique that adds directional vectors to the model's residual stream without any retraining. The authors find that while emotion is linearly decodable from Moshi's internal representations, steering is only partially and unevenly achievable, revealing that the geometry of emotion directions in the model does not align neatly with discrete emotional labels.

## Key Takeaways
- Emotion is linearly decodable from Moshi's residual stream, meaning that emotional states can be identified by projecting activations onto specific directions. However, the practical ability to steer the model toward a target emotion via mean-difference activation steering is only partially achievable and varies significantly across emotions, suggesting that linear decodability does not guarantee linear controllability.
- Happy, angry, and surprise emotions steer toward a shared directional component in the activation space, while sad is distinctly steerable along its own axis. This clustering implies that the model's internal geometry groups certain emotions together, making them harder to disentangle from one another during steering interventions.
- The shared component across happy, angry, and surprise cannot be simply projected away from all three emotions equally, indicating that naive orthogonalization strategies fail. This finding challenges the assumption that removing a common direction cleanly separates emotions and highlights the need for more nuanced, geometry-aware steering methods.

## Context
Emotion and delivery control in speech synthesis has been extensively studied for text-to-speech systems and turn-based dialogue models through prompt conditioning, reference-conditioned synthesis, and activation steering. Full-duplex voice agents, which listen and speak simultaneously, represent a newer frontier where affect modulation must happen in real time without discrete turn boundaries. Prior work such as PersonaPlex addressed identity control in duplex models but left affect control unexplored, making this study a first systematic examination of emotion steering in a fully open-source full-duplex speech language model.

## Implications
For practitioners building voice agents in customer service, emergency dispatch, or clinical communication, this work demonstrates that cheap, retraining-free activation steering can partially modulate emotion but cannot yet deliver precise, label-aligned control across all affective states. The uneven steerability and shared-direction geometry suggest that future systems will need geometry-aware or label-agnostic steering strategies rather than assuming each emotion maps to an independent, cleanly separable vector. This also raises caution for safety and reliability: deploying naive steering in production voice agents could produce unintended emotional blends, particularly when targeting happy, angry, or surprise simultaneously.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.08887v1)
