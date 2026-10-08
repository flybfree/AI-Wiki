---
title: RoboQuest: Generalist Physical Agents that Search, Inspect and Test
url: http://arxiv.org/abs/2610.10388v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_16-46-45Z_RoboQuest_GeneralistPhysicalAgentsthatSearch_Inspe.md
generated_at: 2026-10-07 22:11
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
RoboQuest introduces a benchmark designed to evaluate whether multimodal foundation models can function as generalist physical agents in unfamiliar environments by actively seeking task-relevant information through physical interaction. The benchmark comprises ten mobile manipulation tasks built around three forms of uncertainty—search, manipulation-based inspection, and interactive testing—and reveals that even the best frontier multimodal agent succeeds in only 23% of episodes, while a fine-tuned policy almost never succeeds. The core finding is that agents' primary weakness is not execution capability but rather premature commitment, where they stop exploring before gathering the evidence needed to complete a task.

## Key Takeaways
- The benchmark isolates three distinct forms of embodied uncertainty: agents must search for hidden objects, inspect properties that cannot be observed passively, and test the effects of unfamiliar tools through interaction. This decomposition reveals that current multimodal agents struggle not with individual motor skills but with the higher-level decision-making required to know when and where to gather information before acting.
- Evaluation of five frontier multimodal agents through a common visuomotor interface shows that execution skills are largely intact—when hidden information is supplied directly, agents can carry out most required actions. However, the best agent still fails in 77% of episodes, and a π_0.5 policy fine-tuned on full-episode demonstrations almost never succeeds, indicating that imitation learning alone cannot teach the exploratory reasoning these tasks demand.
- Failure analysis identifies two critical behavioral deficits: agents consistently stop exploring too early, committing to actions before observing the required evidence, and they rarely prevent or repair the disturbances their own exploration causes in the environment. Additionally, learning through trial and error remains difficult for most models, suggesting a fundamental gap in how current agents handle uncertainty and self-correction.

## Context
This paper sits at the intersection of embodied AI, multimodal foundation models, and benchmark design for physical agents. While prior benchmarks have focused on manipulation tasks where all necessary information is visible in the observation, RoboQuest targets the more realistic and harder scenario where agents must actively acquire information through interaction. This mirrors real-world deployment challenges where robots operate in novel, partially observable environments and must reason about what they do not yet know before committing to a course of action.

## Implications
For practitioners building embodied agents, the findings suggest that improving motor execution or scaling model size alone will not close the gap; instead, research must focus on teaching agents to reason about uncertainty, delay commitment until sufficient evidence is gathered, and handle the side effects of their own exploratory actions. For the broader AI community, the near-total failure of a fine-tuned policy on full demonstrations signals that imitation learning is insufficient for tasks requiring active information gathering, pointing toward the need for new training paradigms that explicitly reward exploration and evidence-based decision-making in physical environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10388v1)
