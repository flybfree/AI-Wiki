---
title: The Model Plants the Trigger: Answer-Side Backdoor Attacks in Multi-Turn Large Language Models
url: http://arxiv.org/abs/2610.07723v1
type: paper-summary
date: 2026-10-06
source_paper: 2026-10-06_04-17-18Z_TheModelPlantstheTrigger_Answer_SideBackdoorAttack.md
generated_at: 2026-10-06 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces answer-side backdoor attacks in multi-turn large language models, where a benign first-turn prompt causes the model to generate a harmless word that later functions as a hidden trigger. The attack bypasses safety refusals on harmful follow-up queries without placing any explicit trigger in user input, achieving near-perfect attack success with low poisoning while preserving general utility and clean-input safety.

## Key Takeaways
- The attack shifts the backdoor trigger from the input space to the model’s own generated answer, using a benign first-turn prompt to induce a specific innocuous word that becomes embedded in the dialogue history.
- In later turns, the model recognizes its self-generated trigger and suppresses refusal behavior when a harmful query arrives, allowing malicious outputs while the user’s visible inputs remain clean and unlikely to be flagged by input sanitization.
- Experiments across four LLMs show near-perfect attack success rates, approaching 100% at only a 5% poisoning rate, while maintaining general utility and safety on clean inputs, and representation-level analysis indicates that the self-generated trigger consistently weakens the model’s refusal signal.

## Context
Modern LLM safety defenses often assume that backdoors are activated by explicit malicious tokens or patterns in user prompts, leading to input filtering, prompt sanitization, and guardrails focused on the input side. This work challenges that assumption by showing that multi-turn dialogue can create a persistent, model-generated trigger inside the conversation state, exposing a blind spot in defenses that monitor only user inputs rather than generated outputs and dialogue history.

## Implications
For practitioners, this suggests that LLM security must monitor not only user prompts but also model-generated content, dialogue state, and internal refusal representations across turns. Industry deployments should consider defenses such as output-trigger detection, conversation-state auditing, refusal-signal monitoring, and poisoning-resistant training, because input-centric guardrails alone may fail against attacks that plant triggers through benign-looking interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.07723v1)
