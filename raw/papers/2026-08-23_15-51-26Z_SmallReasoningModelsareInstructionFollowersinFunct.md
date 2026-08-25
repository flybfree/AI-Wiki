---
title: Small Reasoning Models are Instruction Followers in Function Calling
published: 2026-08-23T15:51:26Z
authors: Yalda Taheri, Mohammad Hassan Heydari, Erfan Naaman, Afsaneh Fatemi
url: http://arxiv.org/abs/2608.22472v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Small Reasoning Models are Instruction Followers in Function Calling

## Abstract
Function calling represents the core capability of agentic large language models (LLMs). Existing research has focused on enhancing LLMs function-calling accuracy through fine-tuning, reinforcement learning (RL), and multi-agent frameworks, particularly for native function-calling LLMs. This work demonstrates that LLMs achieve superior accuracy in function calling in instruction-following contexts (i.e., standard user-assistant interactions) rather than a tool calling context. We introduce Instruction-Followed Function Calling (IFFC), a novel framework that decouples function-calling logic from the primary LLM and delegates it to a dedicated smaller model operating within the instruction-following paradigm. Our method consistently outperforms both native function calling (NFC) and prompt-based function calling (PFC) baselines, with particularly strong gains on reasoning-oriented LLMs. Furthermore, we demonstrate that IFFC maintains robust performance under aggressive quantization, enabling efficient on-device deployment without significant accuracy degradation. This work establishes a new paradigm for reliable, resource-efficient function calling in edge-computing scenarios.

## Metadata
- **Published**: 2026-08-23T15:51:26Z
- **Authors**: Yalda Taheri, Mohammad Hassan Heydari, Erfan Naaman, Afsaneh Fatemi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22472v1)