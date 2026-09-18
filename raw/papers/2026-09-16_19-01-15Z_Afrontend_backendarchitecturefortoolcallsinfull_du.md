---
title: A frontend-backend architecture for tool calls in full-duplex speech models
published: 2026-09-16T19:01:15Z
authors: Ke Hu, Slyne Deng, Chen Chen, Elena Rastorgueva, Edresson Casanova, Punit Kumar, Dharmendra Choudhary, Nikhil Srihari, Ameya Sunil Mahabaleshwarkar, Viet Anh Trinh, Slim Essid, Oluwatobi Olabiyi, Zhehuai Chen
url: http://arxiv.org/abs/2609.19334v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A frontend-backend architecture for tool calls in full-duplex speech models

## Abstract
Full-duplex speech-to-speech (S2S) models provide natural, low-latency conversational interaction and would benefit from the ability to use external tools and complete voice-agent tasks. We propose a frontend-backend architecture where a duplex speech-to-text frontend learns to emit a delegation token and forwards streaming ASR transcripts to a text-based backend LLM for tool calls. Tool-call results from the backend are injected back into the frontend through a lightweight prefill-and-repeat mechanism and then synthesized using streaming TTS to the user. Our approach largely preserves regular duplex turn-taking, interruption handling, and low-latency interaction as it requires minimal modifications to the frontend model. In a single-turn tool-call evaluation, our system achieves 92-97% tool-call recall, competitive tool-call prediction performance, and 81.2% accuracy in rejecting irrelevant calls. When equipped with a larger backend (e.g., Qwen3-235B-A22B), our system achieves competitive results on Full-Duplex-Bench-V3 compared to open and closed source models, and significantly outperforms GPT-realtime-mini and Qwen3-Omni-30B-A3B-Instruct on EVA-Bench. These results demonstrate that backend delegation is an effective and modular approach for combining natural duplex speech interaction with strong agentic tool-call capabilities.

## Metadata
- **Published**: 2026-09-16T19:01:15Z
- **Authors**: Ke Hu, Slyne Deng, Chen Chen, Elena Rastorgueva, Edresson Casanova, Punit Kumar, Dharmendra Choudhary, Nikhil Srihari, Ameya Sunil Mahabaleshwarkar, Viet Anh Trinh, Slim Essid, Oluwatobi Olabiyi, Zhehuai Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19334v1)