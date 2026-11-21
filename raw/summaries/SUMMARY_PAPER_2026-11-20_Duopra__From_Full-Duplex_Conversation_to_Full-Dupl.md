---
title: Duopra: From Full-Duplex Conversation to Full-Duplex Agency
url: http://arxiv.org/abs/2611.25773v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-19_09-09-23Z_Duopra_FromFull_DuplexConversationtoFull_DuplexAge.md
generated_at: 2026-11-20 21:54
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Duopra is a full-duplex interaction model that integrates task execution capability directly into conversational control, addressing a critical gap where existing full-duplex models excel at natural turn-taking and interruptions but fail at timely tool invocation and argument revision. By treating the backend as a callable tool and training a unified action interface through a three-stage pipeline (protocol SFT, full-duplex RL, and projector-only repair), Duopra dramatically improves task completion rates—raising Pass@1 from 4.7% to 44.7% on Full-Duplex-Bench v3—while preserving the conversational agency that makes full-duplex interaction natural and low-latency.

## Key Takeaways
- Frontend-backend agent architectures in full-duplex systems create a fundamental failure mode: the frontend decides whether and what to request, while the backend determines how to execute. Most failures in Realtime-Venus-Audio + Harness on FDB v3 occur before a domain tool even executes, meaning unsent or incomplete requests prevent execution entirely or misdirect the backend toward incorrect actions.
- Duopra's three-stage training combines protocol supervised fine-tuning, full-duplex reinforcement learning that rewards timely and complete execution, and a projector-only repair stage that restores talker conditioning after thinker updates. This architecture allows direct tool calls and backend delegation to share a unified action interface with shared requirements for faithful initiation and correct execution.
- Quantitative results demonstrate substantial gains: Pass@1 improves from 4.7% to 44.7% with the same backend, Duopra achieves 47.7% direct tool calling (up from 26.0% after SFT alone), and reaches 49.3% with a DeepSeek backend. It also improves three FDB v1.0 takeover rates over the base model, confirming that task agency and conversational agency can coexist without degradation.

## Context
Full-duplex speech interaction models represent a frontier in human-AI communication, enabling simultaneous listening and speaking with natural backchannels, interruptions, and low-latency turn-taking. However, the field has largely treated conversational fluency and task execution as separate problems, delegating tool use to external harnesses or backend agents. This paper sits at the intersection of real-time speech modeling and agentic tool use, addressing a practical bottleneck where conversational models cannot reliably trigger or revise tool calls during live interaction. The work builds on benchmarks like Full-Duplex-Bench v3 and extends the architectural paradigm from pure dialogue systems toward integrated conversational agents.

## Implications
For practitioners building voice assistants, customer-service agents, or embodied AI systems, Duopra demonstrates that task execution does not need to be bolted onto a conversational model as a separate pipeline; it can be learned jointly, reducing latency and failure modes caused by miscommunication between frontend and backend components. For the broader AI research community, the finding that task agency can coexist with conversational agency challenges the prevailing assumption that full-duplex models must sacrifice tool-use reliability to maintain natural interaction, suggesting a unified training paradigm that could inform next-generation multimodal and agentic systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.25773v1)
