---
title: GraphThink: Graph-Enhanced LLM Thinking for Long-Horizon Embodied Task Planning
published: 2026-08-08T04:05:05Z
authors: Chen Li, Sijie Cheng, Yuelin Zhang, Junxi Li, Maozhi Huang, Yang Liu, Wenbing Huang
url: http://arxiv.org/abs/2608.07905v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GraphThink: Graph-Enhanced LLM Thinking for Long-Horizon Embodied Task Planning

## Abstract
Embodied agents using LLM-based planners often struggle with physical hallucinations, poor generalization to long-horizon tasks, and lack of environmental awareness. We propose GraphThink, a novel framework that integrates a task graph to provide structured knowledge for robust planning and a scene graph to maintain environmental memory for event-driven replanning. Specifically, the task graph guides LLM thinking through contextual prompting and iterative refinement, effectively mitigating planning hallucinations. Furthermore, within the GRPO framework, the task graph offers delicate reward design to train the LLM planner, enhancing long-horizon planning capabilities and improving generalization. Finally, an event-driven replanning module, powered by the scene graph, enables closed-loop environment awareness and error correction. GraphThink achieves state-of-the-art performance on the ALFRED benchmark. In particular, our high-level planner surpasses leading API-based LLMs on both the validation set and held-out long-horizon tasks, underscoring its robust zero-shot and few-shot capabilities. Additional evaluations further demonstrate strong out-of-distribution generalization to novel tasks and environments.

## Metadata
- **Published**: 2026-08-08T04:05:05Z
- **Authors**: Chen Li, Sijie Cheng, Yuelin Zhang, Junxi Li, Maozhi Huang, Yang Liu, Wenbing Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07905v1)