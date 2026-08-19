---
title: VLCP: Vision Language Control Policy Closed-Loop Code Replanning for Robot Manipulation
url: http://arxiv.org/abs/2608.16978v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-17_17-28-38Z_VLCP_VisionLanguageControlPolicyClosed_LoopCodeRep.md
generated_at: 2026-08-18 20:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces VLCP, a closed‑loop control system that integrates a vision‑language model without fine‑tuning or demonstrations. By rewriting the robot’s control function from fresh observations every few steps, VLCP catches and corrects failures before they accumulate, achieving a tenfold improvement in success rate over open‑loop baselines.

## Key Takeaways
- The VLM remains frozen while generating Python code that directly controls the robot, eliminating the need for fine‑tuning or new demonstrations.  
- Every K steps the system re‑observes RGB views, proprioceptive state and a state delta to produce an updated control function, allowing immediate recovery from errors such as failed grasps.  
- The method requires only about ten compact queries per episode, with 84% of tokens cached, keeping computational cost low while preserving a skill library across episodes.

## Context
The integration of large vision‑language models into robotics has been limited by the need for costly fine‑tuning and demonstration data. This work shows that closed‑loop code rewriting can leverage existing model capabilities without retraining, opening a path toward more efficient and scalable robotic control pipelines.

## Implications
VLCP demonstrates that AI reasoning can be operationalized directly in robot behavior, reducing reliance on large labeled datasets. Practitioners may adopt this approach to build adaptive controllers quickly, lowering development time and enabling continuous improvement across diverse manipulation tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16978v1)
