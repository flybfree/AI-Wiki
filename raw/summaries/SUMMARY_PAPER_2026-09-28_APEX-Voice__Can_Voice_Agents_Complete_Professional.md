---
title: APEX-Voice: Can Voice Agents Complete Professional Workflows Through Full-Duplex Interaction
url: http://arxiv.org/abs/2609.34973v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_11-53-07Z_APEX_Voice_CanVoiceAgentsCompleteProfessionalWorkf.md
generated_at: 2026-09-28 22:58
model: qwen3.6-35b-a3b
---

## Summary
APEX-Voice introduces a comprehensive benchmark designed to evaluate whether full-duplex voice agents can reliably execute complex professional workflows rather than just maintaining fluent conversation. The study assesses five leading real-time voice models across 120 interactive scenarios, revealing that current systems struggle significantly with end-to-end task completion, particularly in stateful coordination and knowledge retrieval tasks.

## Key Takeaways
- APEX-Voice comprises 120 workflows spanning ten professional archetypes such as form completion, corporate negotiation, and consulting, evaluated within a stateful Voice Workbench environment that enforces authorization constraints, typed tools, and gold-annotated artifacts to measure both artifact field accuracy and holistic workflow success.
- Evaluation of five frontier real-time voice agents shows severe limitations, with no model exceeding a 25% Pass@1 rate and the highest Reliable@3 score reaching only 10.8%, demonstrating that conversational fluency does not guarantee dependable execution of delegated professional tasks.
- Stateful coordination emerges as the dominant failure point across all tested systems, with performance degrading further in workflows demanding extensive knowledge retrieval and the ability to handle mid-speech corrections dynamically, highlighting critical gaps in long-horizon task management.

## Context
The rapid advancement of full-duplex voice AI has shifted focus from simple command execution to natural, interruptible dialogue; however, this benchmark highlights a critical gap where agents fail to translate conversational fluidity into structured professional outcomes. By introducing standardized workflows with strict success criteria, APEX-Voice addresses the need for rigorous evaluation beyond basic speech recognition or chat capabilities in enterprise settings.

## Implications
For practitioners and developers, these findings suggest that deploying voice agents for high-stakes professional tasks requires significant improvements in state management, tool usage reliability, and error recovery mechanisms rather than just optimizing

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34973v1)
