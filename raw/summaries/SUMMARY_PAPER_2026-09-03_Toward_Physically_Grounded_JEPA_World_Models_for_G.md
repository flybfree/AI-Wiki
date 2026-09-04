---
title: Toward Physically Grounded JEPA World Models for Goal-Conditioned Robotic Planning
url: http://arxiv.org/abs/2609.03565v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_09-11-13Z_TowardPhysicallyGroundedJEPAWorldModelsforGoal_Con.md
generated_at: 2026-09-03 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an end-to-end action-conditioned JEPA world model that combines latent prediction with inverse dynamics and state alignment to improve robotic planning toward visual goals. Experiments on four benchmarks show the model achieves top success rates, outperforming baseline LeWorldModel in several tasks while maintaining comparable performance on Reacher.

## Key Takeaways
- Inverse dynamics is added to latent predictions to prevent collapse and make transitions informative of actions that produced them.
- State alignment aligns consecutive representations with physical configuration and motion, grounding the model in robotics.
- Adding state alignment consistently improves planning success across all four tasks compared to IDM alone.

## Context
This work addresses a gap in AI-driven robotic control where visual goal specification must be translated into safe, efficient motions. By integrating physics-based constraints directly into world modeling, the approach moves beyond pixel prediction toward more physically grounded representations that support reliable planning.

## Implications
For robotics engineers and developers, this model offers a framework to embed physical laws into deep learning models, enabling higher reliability in real-world applications. The findings suggest that combining inverse dynamics with state alignment can lead to more robust and efficient planning systems across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03565v1)
