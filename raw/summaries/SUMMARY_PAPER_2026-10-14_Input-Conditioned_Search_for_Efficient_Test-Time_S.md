---
title: Input-Conditioned Search for Efficient Test-Time Scaling of Recursive Reasoners
url: http://arxiv.org/abs/2610.18547v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_15-25-26Z_Input_ConditionedSearchforEfficientTest_TimeScalin.md
generated_at: 2026-10-14 02:07
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Input-Conditioned Search (ICS), a novel test-time scaling method for recursive reasoners that explores diverse reasoning traces by applying different update maps to the same latent state, without requiring any additional training. The authors demonstrate that ICS achieves the highest mean accuracy across six reasoning tasks while requiring up to two orders of magnitude fewer model FLOPs than existing depth- and width-scaling baselines, and provide theoretical and numerical evidence that ICS can locally eliminate incorrect attracting fixed points in the reasoning dynamics.

## Key Takeaways
- Existing test-time scaling strategies for recursive reasoners—scaling depth by applying more updates or scaling width by perturbing latent states to generate additional trajectories—both risk converging to incorrect attractors, meaning the model gets "stuck" in a wrong reasoning trajectory and cannot recover, analogous to a person hitting a dead end in their thinking.
- ICS addresses this limitation by searching over input conditions to induce alternative update maps from the pretrained reasoner, effectively allowing the model to "step back and approach the problem from a fresh angle" without any additional training, fine-tuning, or architectural modification. This makes it a purely inference-time intervention.
- Across six reasoning tasks, ICS outperforms all evaluated scaling baselines in mean accuracy while using up to two orders of magnitude fewer model FLOPs, demonstrating that it is not only more effective but dramatically more efficient. Controlled experiments confirm ICS can redirect trajectories from the same latent state, and rigorous numerical verification confirms it can locally eliminate incorrect attracting fixed points, providing a theoretical grounding for why the method works.

## Context
Test-time scaling has become a major research frontier in AI, with methods like chain-of-thought prompting, tree-of-thought search, and recursive reasoning all attempting to improve model performance by allocating more computation at inference time. Recursive reasoners, which iteratively apply a learned update rule to latent states, represent a particularly structured and analyzable class of models where scaling behavior can be studied through dynamical systems theory. This paper matters because it identifies a fundamental failure mode—convergence to incorrect attractors—that plagues both depth and width scaling, and proposes a principled, training-free solution grounded in the mathematical structure of the reasoning dynamics.

## Implications
For practitioners deploying recursive reasoning models in production, ICS offers a dramatically cheaper path to improved accuracy, potentially reducing inference compute costs by up to 100× compared to naive depth or width scaling, which is critical for real-time or resource-constrained applications. For the research community, the finding that input-conditioned search can eliminate incorrect fixed points motivates new directions in shaping recursive reasoning both during training and at test time, suggesting that the geometry of update maps and their sensitivity to input conditions are rich, underexplored levers for controlling model behavior. This work also reinforces the broader insight that diverse exploration strategies need not require architectural changes or retraining, opening doors for plug-and-play inference-time enhancements across many model families.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18547v1)
