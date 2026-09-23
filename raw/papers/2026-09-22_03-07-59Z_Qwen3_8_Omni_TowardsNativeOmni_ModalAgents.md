---
title: Qwen3.8-Omni: Towards Native Omni-Modal Agents
published: 2026-09-22T03:07:59Z
authors:  Qwen Team
url: http://arxiv.org/abs/2609.25611v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Qwen3.8-Omni: Towards Native Omni-Modal Agents

## Abstract
We introduce Qwen3.8-Omni-Flash, a natively multimodal agentic model for real-world multimodal productivity. Compared with previous omni models, which primarily emphasized perception and interaction, Qwen3.8-Omni-Flash substantially improves multimodal understanding and reasoning, as well as performance on long-horizon agentic tasks. These capabilities are supported by a native multimodal co-training strategy that preserves strong text-domain capabilities while facilitating the transfer of agentic capabilities from text to audio and video tasks. The model inherits the sparse mixture-of-experts (MoE) architecture of Qwen3.8-Next and extends the context window to one million tokens, supporting long-context multimodal reasoning and long-horizon planning. These advances enable integration into production workflows as a primary agent or a specialized sub-agent, supporting video editing, long-form audio and video translation, music-conditioned music video or movie generation, and video-based note or omni-skill creation. To address the lack of native audio and video support in existing agent harnesses, we release Qwen-MM-Plugins, a lightweight open-source plugin framework for multimodal productivity. We further frame real-time multimodal interaction as a system-level challenge requiring orchestration of context and memory management, tool use, and sub-agent delegation. Accordingly, we release Qwen-Live-Harness, an open-source framework for building responsive, real-time multimodal agents based on Qwen3.8-Omni-Flash. Extensive evaluations demonstrate that Qwen3.8-Omni-Flash achieves strong performance across multimodal understanding, reasoning, long-horizon agentic execution, and video productivity tasks. These results and the accompanying open-source tools support Qwen3.8-Omni-Flash as a practical foundation for deploying natively multimodal agents in research and production.

## Metadata
- **Published**: 2026-09-22T03:07:59Z
- **Authors**:  Qwen Team
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25611v1)