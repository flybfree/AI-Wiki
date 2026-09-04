---
title: DRACO: Fine-Grained Credit Assignment with Dynamic Rubrics for Long-Horizon Agent Training
url: http://arxiv.org/abs/2609.04094v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-02-20Z_DRACO_Fine_GrainedCreditAssignmentwithDynamicRubri.md
generated_at: 2026-09-03 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DRACO, a method for fine-grained credit assignment in long-horizon reinforcement learning where verifiable rewards are unavailable. It creates dynamic rubrics that evaluate the agent’s evolving behavior across a trajectory and redistributes those scores to individual steps using a closed-form formula within GRPO. On AppWorld and Tau-Bench, DRACO outperforms baseline and sparse‑ground‑truth approaches by 15.9 and 5.3 points respectively.

## Key Takeaways
- DRACO generates rubrics on the fly during training to capture evolving capabilities rather than using static multi‑criteria scores.
- The method redistributes rubric judgments over steps responsible for each annotation without any trained attribution module, providing per‑step advantages in GRPO.
- On AppWorld DRACO gains 15.9 points over a base model and 5.3 points over sparse ground‑truth GRPO; on Tau‑Bench it gains 5.3 points over the base model despite no verifier.

## Context
Long‑horizon reinforcement learning suffers from the lack of immediate feedback, making credit assignment difficult. Traditional rubric approaches score once per trajectory, yielding a single scalar that is insufficient for step‑wise optimization. DRACO addresses this by aligning reward signals with the agent’s internal progress through dynamic evaluation.

## Implications
This work offers a practical path to train agents in complex domains where ground truth rewards are scarce or unavailable. By enabling fine‑grained credit assignment, it can improve performance across both familiar and unfamiliar environments without requiring external verifiers. Practitioners can adopt DRACO to enhance long‑term planning and adaptability in autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04094v1)
