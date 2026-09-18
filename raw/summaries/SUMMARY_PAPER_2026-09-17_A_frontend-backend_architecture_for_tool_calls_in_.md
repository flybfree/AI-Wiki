---
title: A frontend-backend architecture for tool calls in full-duplex speech models
url: http://arxiv.org/abs/2609.19334v1
type: paper-summary
date: 2026-09-17
source_paper: 2026-09-16_19-01-15Z_Afrontend_backendarchitecturefortoolcallsinfull_du.md
generated_at: 2026-09-17 20:14
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper introduces a novel frontend-backend architecture designed to integrate external tool usage into full-duplex speech-to-speech (S2S) models without compromising low-latency conversational flow. By utilizing a delegation token system and a prefill-and-repeat mechanism, the authors demonstrate that complex agentic tasks can be performed while maintaining natural turn-taking and interruption handling.

## Key Takeaways
- The proposed architecture utilizes a specialized "delegation token" emitted by a duplex speech-to-text frontend, which allows the system to hand off complex reasoning and tool execution to a separate text-based LLM backend. This modularity ensures that the primary S2S model does not need to be heavily modified or retrained for every new tool added to the system's repertoire.
- To maintain the natural flow of conversation, the authors developed a lightweight prefill-and-repeat mechanism. This allows the output from the tool-calling backend to be seamlessly injected back into the frontend and then synthesized using streaming TTS, ensuring that the user experiences minimal latency and consistent turn-taking during complex interactions.
- Empirical evaluations show significant success in both accuracy and reliability, specifically achieving 92-97% tool-call recall and outperforming major models like GPT-realtime-mini on the EVA-Bench. These results demonstrate that backend delegation is a highly effective method for scaling agentic capabilities in voice interfaces while preserving human-like interaction qualities.

## Context
The field of AI is rapidly shifting from static text interactions to dynamic, full-duplex speech-to-speech (S2S) experiences. However, integrating "agentic" behaviors—such as the ability to query databases or trigger external APIs—into these models often compromises the low latency and natural turn-taking required for human-like interaction. This paper addresses this specific trade-off by proposing a structural architecture rather than just a training objective.

## Implications
This research provides a practical blueprint for building production-ready voice agents that can perform complex tasks without sacrificing conversational quality. For industry practitioners, it suggests that modularity is key: by decoupling the "voice" and "action" layers, developers can build more reliable systems that are easier to update and scale. This approach could significantly lower the barrier for creating high-performance, multi-turn voice assistants capable of real-world utility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.19334v1)
