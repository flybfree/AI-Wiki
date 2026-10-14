---
title: Full-duplex Spoken Language Modeling with Discrete Diffusion
url: http://arxiv.org/abs/2610.17780v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_06-05-54Z_Full_duplexSpokenLanguageModelingwithDiscreteDiffu.md
generated_at: 2026-10-14 00:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Diffuplex is a full-duplex spoken language model built on discrete diffusion that decouples the timing of speech output from the content generation process, enabling simultaneous real-time dialogue tracking and parallel intelligent response generation. The model achieves 1872 tokens per second in thinking mode—substantially surpassing frontier autoregressive models in decoding speed—while also matching the first-audio latency of existing full-duplex systems without thinking, all while delivering markedly stronger linguistic intelligence.

## Key Takeaways
- Diffuplex introduces a fundamental architectural separation between "when to say" and "what to say" at the training level, rather than compressing both decisions into a single autoregressive timeline. During inference, an autoregressive interaction policy continuously tracks user speech for timing and turn-taking, while a parallel discrete diffusion process independently generates and refines response content. This decoupling means semantic computation is no longer bounded by the perception audio frame rate, allowing intelligence and responsiveness to improve simultaneously.
- In thinking mode, Diffuplex delivers 13.0 tokens per forward pass, reaching an average throughput of 1872 tokens per second, which substantially surpasses the decoding speed of frontier autoregressive models. This speed advantage stems from the parallel nature of discrete diffusion, which can generate multiple tokens simultaneously rather than sequentially.
- Even without thinking mode, Diffuplex matches the first-audio latency of existing full-duplex models while achieving markedly stronger linguistic intelligence, demonstrating that the discrete diffusion paradigm does not sacrifice responsiveness for quality. The model sustains real-time dialogue while devoting parallel computation to intelligent response generation, establishing a new paradigm for spoken agents.

## Context
This paper addresses a long-standing tension in spoken language modeling: autoregressive models must generate tokens sequentially, which inherently couples the speed of linguistic reasoning to the real-time constraints of audio perception and turn-taking. Prior full-duplex systems have struggled to improve both intelligence and responsiveness simultaneously because every additional reasoning step delays the next audio output. Diffuplex's use of discrete diffusion as a generative backbone represents a significant departure from the autoregressive paradigm that has dominated language modeling, offering a path toward spoken agents that can think deeply without falling behind in conversation.

## Implications
For practitioners building voice assistants, conversational AI agents, and real-time dialogue systems, Diffuplex suggests that discrete diffusion can serve as a viable alternative to autoregressive architectures for spoken language tasks, potentially enabling more capable and responsive agents in production deployments. The separation of timing policy from content generation opens new design space for spoken agents that can handle complex reasoning tasks—such as multi-step planning or knowledge retrieval—without introducing perceptible latency in dialogue. Broader industry adoption of diffusion-based spoken models could reshape how voice interfaces are engineered, moving away from the sequential token-by-token paradigm toward parallel, latency-tolerant generation pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17780v1)
