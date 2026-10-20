---
title: VISAGENT: An Agent-Based End-to-End Voice Interaction System
url: http://arxiv.org/abs/2610.26168v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-19_10-59-45Z_VISAGENT_AnAgent_BasedEnd_to_EndVoiceInteractionSy.md
generated_at: 2026-10-19 23:49
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
VISAGENT is an agent-based end-to-end voice interaction system designed for large-scale public services, replacing rigid menu-driven workflows with natural speech interaction and a two-level routing paradigm that dispatches user requests to either a general conversational model or specialized domain agents. Validated through real-world deployment in China's 114 hotline across multiple service domains, the system demonstrates low-latency full-duplex interaction, robust routing scalability across hundreds of agents, and competitive speech naturalness, advocating a shift from isolated voice assistants toward agent-centric conversational infrastructures.

## Key Takeaways
- VISAGENT introduces a two-level routing paradigm that achieves sub-second intent-to-agent selection across hundreds of specialized agents, dynamically dispatching user requests to either a general conversational model or domain-specific agents. This hierarchical agent routing replaces the rigid menu-driven interaction patterns that constrain current public service voice systems, enabling natural speech-based workflows that scale to large operational environments.
- The system incorporates a user memory mechanism that informs preference-aware agent selection and supplies relevant preferences and context to selected agents, supporting personalized task execution. This reduces the need for users to repeat previously provided information across interactions, addressing a critical usability gap in fragmented vertical service systems where context is typically lost between calls.
- A voice-agent registration mechanism converts task agents into conversational entities, enabling dynamic onboarding and ecosystem-level extensibility through a scalable voice-agent marketplace. This architecture transforms the system from a fixed set of services into an extensible platform where new domain agents can be added without redesigning the core interaction pipeline, providing a general blueprint for building extensible voice-agent systems beyond public services.

## Context
This work sits at the intersection of large language model agents, speech interaction systems, and public infrastructure modernization, addressing a long-standing gap between conversational AI capabilities and the operational constraints of government and public service hotlines. As voice assistants have proliferated in consumer settings, public service systems have remained largely stuck in hierarchical menu trees and siloed vertical services, making VISAGENT's agent-centric architecture a significant departure from existing paradigms in the field.

## Implications
For public sector practitioners and system integrators, VISAGENT offers a deployable blueprint for replacing legacy IVR and menu-driven hotlines with extensible, agent-based conversational infrastructure that can onboard new services dynamically without architectural overhaul. For the broader AI research community, the paper signals a maturation of agent orchestration techniques toward production-grade, low-latency, multi-agent routing at scale, pushing the field from single-assistant prototypes toward composable, marketplace-driven conversational ecosystems applicable to healthcare, transportation, and other critical public domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26168v1)
