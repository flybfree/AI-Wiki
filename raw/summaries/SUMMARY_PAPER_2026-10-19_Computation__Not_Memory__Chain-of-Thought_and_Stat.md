---
title: Computation, Not Memory: Chain-of-Thought and State Tracking in LLM Agents
url: http://arxiv.org/abs/2610.25760v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_04-18-24Z_Computation_NotMemory_Chain_of_ThoughtandStateTrac.md
generated_at: 2026-10-19 21:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how chain-of-thought reasoning influences the actions of language-model agents in tasks that require tracking a changing internal state, specifically a file-locking scenario. The authors find that the primary benefit of reasoning for rule-following comes from generating fresh reasoning at each action step, rather than from retaining or replaying earlier reasoning in the prompt. They further demonstrate that state information decodable from model activations without reasoning is a poor predictor of how interventions on reasoning text actually alter agent behavior.

## Key Takeaways
- Generating reasoning at the moment of action is the dominant mechanism for reducing rule violations: most of the improvement in avoiding lock-violating commands comes from reasoning written just before the action, while retaining earlier reasoning in the prompt adds little to rule-following, though it may help one model complete the task overall.
- The content of reasoning matters critically: filler text, reasoning written for a different history, and even an accurate table of the current state fail to reproduce the benefit of genuine reasoning. Moreover, when the agent is given reasoning written for a history that differs in one lock value, it acts on that external reasoning even when it contradicts its own observed history, showing that reasoning text can override the agent's own state tracking.
- State recoverability does not equal behavioral influence: linear probes can recover the current state from model activations about as well as a text classifier recovers it from the transcript, yet this decoding accuracy does not predict which reasoning interventions will actually change the agent's actions, indicating a gap between what is internally represented and what drives behavior.

## Context
This work sits at the intersection of chain-of-thought prompting, agent evaluation, and mechanistic interpretability. As LLM agents are increasingly deployed in tool-use and multi-step planning tasks, understanding whether reasoning serves as a genuine computational scaffold or merely as a superficial prompt artifact is a central open question. The paper contributes a controlled experimental framework that separates the generation of reasoning from its retention, and contrasts behavioral effects with internal-state decodability, offering a methodological template for future agent-evaluation studies.

## Implications
For practitioners building agentic systems, the findings suggest that investing in per-step reasoning generation is far more impactful than architectures that accumulate or replay prior reasoning chains, and that simply providing a correct state table does not substitute for the computational act of reasoning. For the broader field, the disconnect between decodable internal state and behavioral sensitivity to reasoning text warns against using probing accuracy as a proxy for understanding agent decision-making, urging more behaviorally grounded evaluation methods for reasoning-augmented agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25760v1)
