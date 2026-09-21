---
title: NemotronLabs VoiceChat: An Open Full-duplex Speech-to-Speech Model with Tool Calling Capabilities
url: http://arxiv.org/abs/2609.21967v1
type: paper-summary
date: 2026-09-20
source_paper: 2026-09-18_16-27-22Z_NemotronLabsVoiceChat_AnOpenFull_duplexSpeech_to_S.md
generated_at: 2026-09-20 21:08
model: freedomaisvr/gemma-4-12b-it
---

## Summary
NemotronLabs VoiceChat introduces an open-weight, full-duplex speech-to-speech (S2S) model designed to facilitate natural, real-time conversations while simultaneously performing complex tasks like tool calling. The architecture integrates a streaming speech encoder and decoder with parallel output streams for both agent text and structured function calls, allowing the system to listen, reason, and speak concurrently. Evaluation shows it achieves state-of-the-art performance in handling user interruptions and backchannels compared to other open-weight systems while maintaining high scores in tool selection and general language capabilities.

## Key Takeaways
- The model utilizes a sophisticated architecture that combines a streaming speech encoder with a decoder-only language model, specifically designed to support parallel output streams for both agent text and structured function calls. This allows the system to execute external tools while maintaining a natural conversational flow without significant latency.
- A key innovation is the inclusion of an auxiliary RNN-T branch for incremental user transcription, which helps the model maintain context during live interactions. The architecture also incorporates a streaming TTS decoder to ensure low-latency speech generation, enabling the model to listen and speak simultaneously.
- Empirical evaluations on benchmarks like Full-Duplex-Bench demonstrate significant progress in conversational dynamics; specifically, the model achieves 100% takeover rates following user interruptions and resumes responses after backchannels in 93% of cases. Furthermore, it achieves an 82.5% tool-selection F1 score on FDB 3.0, demonstrating that complex reasoning and action-oriented tasks can be integrated into a real-time speech interface.

## Context
The development of full-duplex speech-to-speech models represents a significant step toward human-like AI interaction, moving beyond the "turn-based" limitations of previous systems. This research addresses the challenge of integrating complex reasoning and external tool usage into low-latency, real-time conversational frameworks. By providing an open-weight model that handles these tasks simultaneously, it advances the democratization of sophisticated AI agents capable of real-world utility.

## Implications
This work provides a blueprint for building more interactive and useful AI assistants that can perform actions—such as booking appointments or querying databases—without breaking the flow of natural conversation. For developers and researchers, it proves that high-quality speech recognition, generation, and tool use do not have to be traded off against real-time responsiveness. This paves the way for a new generation of voice-based agents capable of sophisticated, multi-turn interactions in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.21967v1)
