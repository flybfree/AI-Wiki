---
title: Does This Action Still Explain the Task? Reverse Scoring for Diffusion Language Model Agents
published: 2026-09-29T20:54:04Z
authors: Jiacheng Qiu, Christopher E. Mower, Jan Peters, Haitham Bou-Ammar, Matthieu Zimmer
url: http://arxiv.org/abs/2609.38536v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does This Action Still Explain the Task? Reverse Scoring for Diffusion Language Model Agents

## Abstract
Diffusion-based large language models (dLLMs) promise to break the sequential latency bottleneck of autoregressive agents through parallel decoding, but recent evaluations show this efficiency does not transfer to embodied agentic competence: dLLM-backed agents repeatedly fall into retry loops, re-issuing an action long after it has failed. We give a mechanistic account of this failure and a training-free remedy. We trace the retry loop to the adaptivity of masked decoding: the sampler commits the positions it is most confident about and defers the uncertain ones, and at a failure state the context already offers a confident fill for the deferred decision, i.e. the failed action itself, so the retry is committed without the failure feedback ever being confronted. We model the resulting distortion of the action distribution as a task-blind corruption: contextually salient actions (e.g., the action just taken) receive inflated probability by a factor that depends on the state and the action but not on the task. Under this model, we analyse an invariance proposition: the task-blind factor cancels exactly from the reverse conditional, i.e. the likelihood of the task given the state and a candidate action, which coincides with the task posterior of an idealized uncorrupted model. Masked dLLMs evaluate the reverse conditional natively, unlike autoregressive models, by masking the task tokens and denoising, at the cost of a few parallel passes per candidate. We instantiate the rule as Reflect Reverse and evaluate it on four multi-turn embodied benchmarks, where it improves task success and progression rates over forward-scoring baselines.

## Metadata
- **Published**: 2026-09-29T20:54:04Z
- **Authors**: Jiacheng Qiu, Christopher E. Mower, Jan Peters, Haitham Bou-Ammar, Matthieu Zimmer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38536v1)