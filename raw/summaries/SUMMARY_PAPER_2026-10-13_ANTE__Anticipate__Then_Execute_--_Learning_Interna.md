---
title: ANTE: Anticipate, Then Execute -- Learning Internal World Models for Coding Agents from Verified Beliefs
url: http://arxiv.org/abs/2610.15368v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-11_05-46-07Z_ANTE_Anticipate_ThenExecute__LearningInternalWorld.md
generated_at: 2026-10-13 21:51
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ANTE (Anticipate, Then Execute) is an agentic reinforcement learning framework that equips coding agents with an internal world model by having the policy state a belief about the consequences of its next action before executing it, then verifying that belief against real execution results. By anchoring per-step credit assignment on the agent's own verified forecasts through Belief-Anchored Policy Optimization (BAPO), ANTE raises Qwen3-32B from 25.0% to 57.2% pass@1 on SWE-bench Verified, outperforming a matched GRPO baseline by 6.2 percentage points and demonstrating that learned foresight transfers across different harnesses and out-of-distribution domains.

## Key Takeaways
- ANTE introduces a belief-anchored credit assignment mechanism (BAPO) that converts the agent's own pre-action predictions into per-step advantages, solving the long-standing problem in coding-agent RL where terminal rewards fail to attribute blame to specific earlier steps that irreversibly corrupted repository state. The agent states an internal belief before each action, and the framework verifies it against actual execution results, turning settled predictions into actionable training signal.
- The framework includes ANTE-TTO (test-time optimization), which leverages the trained internal world model to select among candidate actions at inference time without requiring an external scorer, enabling effective test-time scaling. This means the agent's learned foresight directly improves action selection during deployment, not just during training.
- Empirical results show the world model's prediction accuracy climbing from 44% to 69% during RL training, and the resulting foresight capability generalizes across different agent harnesses and out-of-distribution domains, suggesting the learned internal model captures transferable causal structure about code execution rather than overfitting to a specific environment.

## Context
This paper addresses a critical gap in the rapidly growing field of LLM-based software engineering agents. Existing coding agents operate reactively: they observe tool outputs and execution results but never anticipate consequences, making them vulnerable to irreversible errors from ill-judged edits. Prior code world models either freeze their predictions before RL fine-tuning or reduce world modeling to a trivial next-token loss, limiting their utility. ANTE bridges this gap by co-training the world model and policy within the RL loop, aligning with broader trends toward model-based reinforcement learning and test-time scaling in agentic systems.

## Implications
For practitioners building autonomous coding agents, ANTE demonstrates that equipping agents with verified internal foresight yields substantial performance gains on real-world software engineering benchmarks without requiring external reward models or human feedback at inference time. The transferability of learned foresight across harnesses and domains suggests a path toward more robust, general-purpose coding agents that can anticipate consequences in unfamiliar environments. For the broader AI research community, the belief-anchored credit assignment approach offers a principled solution to the sparse-reward and credit-assignment challenges that plague agentic RL, potentially applicable beyond coding to any sequential decision-making task with verifiable outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15368v1)
