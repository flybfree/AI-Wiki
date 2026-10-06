---
title: ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience
published: 2026-10-04T15:27:20Z
authors: Haodong Lu, Dong Gong
url: http://arxiv.org/abs/2610.05303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ASCENT: Online Test-Time Training of Long-Horizon Agents via Self-Distillation of Verified Experience

## Abstract
A large language model (LLM) agent solves long-horizon tasks through many reasoning-action turns, with one verification signal at termination. Deployed agents face streams of related tasks, making their trajectories a natural resource for improvement. In-context adaptation agents store reflections, memories, or skills as text, so reuse depends on retrieving the right experience and on a frozen policy executing it. We study Online Agentic Test-Time Training (OaTTT), which trains the LLM's weights on its own execution trajectories during deployment. The agent executes each task once, in one pass over the stream, and the executed trajectory with its verification result is the only learning signal for weight updates that persist across tasks. Directly imitating or reinforcing the generated tokens of this single attempt destabilizes the policy. We introduce ASCENT (Agentic Self-distillation for Cross-task EvolutioN at Test-time), which instead self-distills verified experience. A stable version of the LLM, its frozen initial copy, receives the verified trajectory as privileged information and predicts next-token distributions along it with this hindsight. Distilling them into persistent LoRA fast weights updates the agent for later tasks, without an external reference solution or stronger teacher. By further removing invalid-action turns, ASCENT distills enhanced privileged experience for more efficient execution. We characterize its population target and the limits of sparse outcome selection. Across ALFWorld, WebShop, and AppWorld at varied model scales, ASCENT improves task success and interaction efficiency as experience accumulates, outperforms online adaptation methods, and transfers to held-out scenes, showing that an agent can consolidate verified experience into its weights without a separate training phase or memory retrieval. Project page: https://artificer-ai-lab.github.io/ASCENT

## Metadata
- **Published**: 2026-10-04T15:27:20Z
- **Authors**: Haodong Lu, Dong Gong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05303v1)