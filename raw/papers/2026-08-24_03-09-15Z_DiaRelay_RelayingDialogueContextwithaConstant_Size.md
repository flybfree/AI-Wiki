---
title: DiaRelay: Relaying Dialogue Context with a Constant-Size Memory for Emotion Recognition in Conversation
published: 2026-08-24T03:09:15Z
authors: Zihao Zhou, Bin Yang, Jinghui Qin, Kebing Jin
url: http://arxiv.org/abs/2608.22745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DiaRelay: Relaying Dialogue Context with a Constant-Size Memory for Emotion Recognition in Conversation

## Abstract
Emotion Recognition in Conversation (ERC) requires models to identify subtle emotional cues that are often distributed across distant dialogue turns. Existing methods typically incorporate dialogue history through a fixed context window. However, short windows discard potentially useful long-range evidence, while enlarging the window repeatedly re-encodes overlapping utterances, increases computational and memory costs, and may introduce irrelevant context. Moreover, commonly used parameter-efficient adaptation methods, such as LoRA, mainly introduce fixed low-rank transformations in the feature space and do not explicitly maintain a dialogue-level state or condition their transformations on the evolving conversational context. To address these limitations, we propose a lightweight adapter, DiaRelay, to enable LLMs to explicitly maintain a dialogue-level memory for accurate ERC. Based on LoRA, DiaRelay introduces two extra tightly collaborative components, Selective Relay Memory Transition and Dual-axis Relay Memory Read. Selective Relay Memory Transition progressively aggregates useful historical evidence into a bounded relay memory and propagates it across successive utterance predictions. This allows earlier emotional cues to influence later predictions after they leave the local context window, without re-encoding the complete dialogue history or expanding the backbone context length. Dual-axis Relay Memory Read uses the propagated memory to dynamically modulate low-rank feature transformations, enabling context-dependent representation adaptation without test-time gradient updates. Extensive experiments show that DiaRelay can achieve SOTA weighted F1 and accuracy on MELD while obtaining competitive results on IEMOCAP with only an extra 7.1M trainable parameters, indicating the effectiveness and generalizability of our DiaRelay in enhancing LLM-based emotional understanding.

## Metadata
- **Published**: 2026-08-24T03:09:15Z
- **Authors**: Zihao Zhou, Bin Yang, Jinghui Qin, Kebing Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22745v1)