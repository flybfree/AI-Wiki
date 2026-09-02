---
title: A Closed-Loop Evaluation of Capability Loss and Recovery in Compressed Driving Policies
url: http://arxiv.org/abs/2609.00718v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_04-50-17Z_AClosed_LoopEvaluationofCapabilityLossandRecoveryi.md
generated_at: 2026-09-01 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a closed-loop evaluation framework that tests how compressed driving policies degrade and recover during each stage of compression. By treating the driving task as a POMDP and training a belief-state policy with PPO, the authors systematically prune, distill, and quantize an actor network while monitoring its performance on five real-world curricula.

## Key Takeaways
- Structured pruning is identified as the first point where driving capability is lost, indicating that early compression stages have a more severe impact than later ones.  
- Knowledge distillation can partially restore some of the lost capability after pruning, but its effectiveness is limited by the quality and quantity of rehearsal data used for training.  
- Integer quantization further reduces the set of curricula that require the vehicle to stop and resume motion, showing that even the most aggressive compression step cannot preserve all driving tasks.

## Context
The rapid deployment of learned driving policies on resource‑constrained embedded systems raises concerns about safety when models are compressed. Existing evaluation methods rely on aggregate scores that do not capture real‑world performance nuances. This study bridges that gap by linking compression steps to observable driving outcomes, offering a more realistic benchmark for autonomous vehicle developers.

## Implications
For the field of AI in automotive applications, this work provides empirical evidence that compression strategies must be evaluated stage‑by‑stage and that safety‑critical tasks like stop‑and‑go maneuvers are especially vulnerable. Practitioners can use these findings to prioritize less aggressive compression or redesign distillation pipelines, ensuring that compressed policies remain reliable before field deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00718v1)
