---
title: An Explicit Feedback Contract for Iterative ML-Agent Harnesses
url: http://arxiv.org/abs/2610.28798v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_18-24-29Z_AnExplicitFeedbackContractforIterativeML_AgentHarn.md
generated_at: 2026-10-21 21:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces an explicit feedback contract for iterative ML-agent harnesses that governs what an agent may observe during its model-development loop, when iteration should halt, and when the held-out test split may be accessed. The core mechanism releases a validation score only when a submission clears a noise threshold derived from the paired standard error, eliminating the need to tune arbitrary margins. Experiments across click-through-rate prediction, learning-to-rank, and a zero-signal control task demonstrate that the contract substantially reduces spurious gains, narrows the validation-test gap, and causes agents to stop iterating far earlier than under exact-score feedback.

## Key Takeaways
- The control task, where the true improvement is zero by construction, exposes the failure mode of exact feedback: an agent reading precise validation scores reported a fabricated gain of 0.0157, whereas the same agent operating under the noise-threshold contract reported only 0.0033, showing that unbounded feedback channels cause agents to chase noise as if it were signal.
- On both real-world tasks (CTR prediction and learning to rank), the contract narrows the gap between validation and test performance, and test scores are slightly higher rather than lower, indicating that restricting what the agent observes actually improves generalization rather than hindering it.
- The most dramatic behavioral difference is in stopping behavior: agents using exact feedback exhausted their full budget of thirty submissions on two of three tasks, including the one where nothing could be learned, while agents under the contract halted after four to twelve submissions. The authors reframe budget exhaustion not as diligence but as a diagnostic symptom of an unbounded feedback channel.

## Context
Iterative ML agents—systems that autonomously edit training code, run experiments, and select the next attempt based on validation metrics—are increasingly deployed in AutoML pipelines, Kaggle-style competitions, and internal model-development workflows. The adaptive-selection problem, where repeated querying of a validation split leaks information and inflates apparent performance, has been studied in classical statistics but has not been formally addressed within the agent-harness literature. This paper bridges that gap by treating the feedback channel itself as a design surface that must be constrained, rather than assuming agents will self-regulate their iteration behavior.

## Implications
For practitioners building or deploying ML-agent harnesses, the findings suggest that providing exact validation scores after every attempt is not a neutral convenience but an active source of overfitting and wasted compute. Adopting a noise-threshold release policy could reduce GPU-hours spent on fruitless iteration, tighten reported metrics, and make agent-generated model claims more trustworthy in production settings. For the broader field, the work reframes "exhausting the submission budget" from a sign of thoroughness into a red flag, potentially reshaping how benchmark harnesses and leaderboard systems are designed for autonomous agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28798v1)
