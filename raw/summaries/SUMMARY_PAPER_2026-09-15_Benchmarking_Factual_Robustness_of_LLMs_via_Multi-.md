---
title: Benchmarking Factual Robustness of LLMs via Multi-conversation Persuasion
url: http://arxiv.org/abs/2609.16777v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-15_07-46-01Z_BenchmarkingFactualRobustnessofLLMsviaMulti_conver.md
generated_at: 2026-09-15 20:03
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper investigates the factual robustness of Large Language Models against persuasion attacks designed to inject misinformation or enforce counterfactual claims. The authors identify a critical evaluation flaw termed "Refusal Inertia," where models artificially sustain initial safety refusals across multi-turn dialogues for contextual consistency, thereby masking their true vulnerabilities. To address this gap, they introduce the SAST-IR framework, which enforces strict memory wipes on the target model while preserving the attacker's history, revealing that stateless defenses are highly susceptible to even simple adversarial strategies.

## Key Takeaways
- The authors identify "Refusal Inertia," a phenomenon where LLMs artificially maintain initial safety refusals across multi-turn conversations for contextual consistency, which significantly obscures their actual susceptibility to isolated persuasion attempts.
- The proposed SAST-IR framework enforces strict memory wipes on the target model while retaining the attacker's conversational history, creating a rigorous worst-case adversarial setting that exposes severe brittleness in current stateless defense mechanisms.
- Experiments using the CP-Agent and CounterFact-Strict dataset reveal a "Complexity Paradox," demonstrating that simple, diverse attack strategies achieve an 84.7% genuine persuasion rate, whereas complex iteratively refined attacks often trigger defensive compliance rather than actual model manipulation.

## Context
As LLMs increasingly function as primary knowledge retrieval interfaces and decision-support tools, ensuring their resilience against adversarial persuasion is critical for maintaining information integrity and user safety. Traditional red-teaming methodologies have largely overlooked the impact of persistent conversation history on safety alignment, leading to overly optimistic assessments of model robustness. This research bridges a significant methodological gap by isolating memory-dependent defenses from real-world interaction dynamics.

## Implications
The findings suggest that current LLM safety protocols may be fundamentally over-reliant on conversational context rather than intrinsic factual grounding, necessitating architectural or training adjustments for stateless deployment scenarios. Practitioners and developers must prioritize rigorous, memory-isolated red-teaming to uncover latent vulnerabilities before deploying models in open-ended or stateless environments. Furthermore, the identified complexity paradox highlights the need for adaptive defense mechanisms that can effectively distinguish between genuine persuasion and superficial compliance triggers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.16777v1)
