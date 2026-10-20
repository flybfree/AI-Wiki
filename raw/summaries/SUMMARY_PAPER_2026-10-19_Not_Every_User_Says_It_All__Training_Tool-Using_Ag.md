---
title: Not Every User Says It All: Training Tool-Using Agents Beyond Ideal Simulated Users
url: http://arxiv.org/abs/2610.24294v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-16_22-41-30Z_NotEveryUserSaysItAll_TrainingTool_UsingAgentsBeyo.md
generated_at: 2026-10-19 21:35
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the mismatch between training tool-using agents with idealized "strong" simulated users and the reality of "weak" users who omit details, and demonstrates that conventional reinforcement learning approaches fail to close this gap. The authors introduce StaGPO (State-Grouped Policy Optimization), a method that leverages explicit task-state tracking to assign step-level credit across rollouts reaching equivalent situations, enabling weak-user training to yield meaningful performance gains on benchmarks like ToolWOZ and tau2-bench.

## Key Takeaways
- Constructing weak users by masking sentences from a strong simulated user's replies while keeping the task and user knowledge fixed reveals that every agent policy's success drops under weak-user interaction, and that training with weak users through fixed masks, mixtures, or curricula does not produce policies that outperform strong-trained policies beyond run-to-run noise. Prompting agents to ask more clarifying questions also fails to compensate.
- StaGPO works by having the agent explicitly write what the task requires, what information is missing, and how gaps are being filled, then using GRPO to compare turns across different rollouts that converge to the same state, assigning fine-grained step-level credit rather than only episode-level rewards. This state-grouped comparison is the mechanism that makes weak-user training genuinely effective.
- On ToolWOZ, a Qwen3.5-2B policy trained with weak users via StaGPO reaches 76.8% success, surpassing GRPO by 4.8 points and the strongest baseline by 2.8 points, while also generalizing to unseen mask rates. When trained with strong users instead, StaGPO still serves weak users at least as well as GRPO trained with weak users, and on tau2-bench it achieves the highest weak-user scores for both Qwen3.5-2B and Qwen3.5-4B models.

## Context
Tool-using agents in the LLM agent ecosystem are overwhelmingly trained and evaluated against simulated users who articulate every requirement clearly, creating a training-evaluation distribution that diverges sharply from real-world user behavior where instructions are incomplete, ambiguous, or delivered incrementally. This paper directly confronts that distributional gap by formalizing weak users and showing that the standard RL recipe (SFT cold start followed by GRPO) cannot bridge it, which is a significant negative result for the field. The proposed StaGPO method extends the GRPO framework with state-aware credit assignment, representing a novel direction in agent RL that moves beyond outcome-only rewards toward process-aware optimization.

## Implications
For practitioners deploying tool-using agents in customer service, software assistance, or any interactive setting where users routinely under-specify their needs, this work signals that simply collecting noisier training data or prompting agents to ask more questions is insufficient; structured state-tracking and state-grouped credit assignment are necessary to build robust agents. For the broader RL-for-agents research community, StaGPO suggests that step-level credit assignment conditioned on task state is a more promising lever than curriculum or data-mixing strategies, potentially influencing how future agent training pipelines are designed. The finding that a small 2B-parameter model can outperform stronger baselines when trained with the right optimization signal also has practical implications for cost-efficient agent deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24294v1)
