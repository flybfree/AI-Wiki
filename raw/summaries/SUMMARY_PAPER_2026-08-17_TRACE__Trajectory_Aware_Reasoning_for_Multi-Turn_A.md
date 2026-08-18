---
title: TRACE: Trajectory Aware Reasoning for Multi-Turn Adversarial Conversation Evaluation
url: http://arxiv.org/abs/2608.15594v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_07-32-02Z_TRACE_TrajectoryAwareReasoningforMulti_TurnAdversa.md
generated_at: 2026-08-17 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Trace, a trajectory‑aware defense mechanism that detects evolving jailbreak patterns in multi‑turn adversarial conversations and decides whether to allow, caution, or decline responses. Experiments on seven benchmarks show Trace reduces attack success rates from 74.9% (undefended) to 14.5%, outperforming the strongest baseline at 31.4%. The system also improves safety without excessive over‑refusal, achieving a 93.3% compliance rate.

## Key Takeaways
- Trace employs structured reasoning that analyzes each turn’s trajectory to identify manipulation cues and assign a jailbreak score before responding.
- The model balances helpfulness on benign prompts with robustness against attacks, as demonstrated by the 14.5% average ASR versus higher rates for baselines.
- Evaluation includes diverse datasets: 4k adversarial dialogues, 2.4k benign dialogs, and 600 sensitive‑but‑benign conversations.

## Context
Multi‑turn jailbreak attacks exploit the sequential nature of user inputs to circumvent LLM guardrails, turning seemingly harmless exchanges into harmful outputs. Current defenses often lack reasoning abilities, leading to either over‑refusal that harms usability or insufficient protection that fails against sophisticated attacks. This work addresses these gaps by integrating trajectory analysis into a reinforcement learning framework.

## Implications
For developers and safety researchers, Trace provides a practical template for building models that can reason about conversation flow while maintaining user experience. The approach could be adapted to other domains where sequential manipulation is a concern, such as automated customer support or content moderation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15594v1)
