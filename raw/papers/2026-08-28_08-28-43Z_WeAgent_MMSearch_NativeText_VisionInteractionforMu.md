---
title: WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents
published: 2026-08-28T08:28:43Z
authors: Zongkai Liu, Hui Zhang, Liqiang Niu, Zhen Cao, Han Li, Juntao Liu, Wenchao Chen, Chengduo Zhao, Chao Yu, Fandong Meng
url: http://arxiv.org/abs/2608.28062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WeAgent-MMSearch: Native Text-Vision Interaction for Multimodal Search Agents

## Abstract
Multimodal search agents extend parametric knowledge with newly emerging and long-tail evidence from the open web. Yet many existing agentic search environments often expose retrieved evidence only as text and omit tool-returned images from subsequent context, reducing visually grounded trajectories to text-only reasoning. Long-horizon interaction also compounds tool-call, response-length, timeout, and budget failures, which can discard salvageable trajectories, waste rollout computation, and disturb policy updates. To address these issues, we introduce WeAgent-Harness, a multimodal agentic harness that supports native text-vision interaction and runtime recovery. Retrieved images receive persistent disk references, allowing the model to inspect, process, and cite them throughout the trajectory. Based on this harness, we develop WeAgent-MMSearch, an integrated system spanning data construction, agentic post-training, and multimodal rollout. For data construction, a strong MLLM uses WeAgent-Harness to discover, synthesize, and verify MMSearch-style tasks and collect expert trajectories. During post-training, our Failure-Aware GSPO (FA-GSPO) recovers salvageable abnormal rollouts and filters invalid ones to improve bounded multimodal planning and search.We also introduce VisTarget-Bench, a 150-task human-verified benchmark that pairs each question with a held-out target image, distinguishing image-retrieval failures from visual-perception failures. Evaluation on VisTarget-Bench and seven public benchmarks shows that agentic post-training improves the average score by 19.22 points, enabling our model to outperform similarly sized open-source models and rival models with roughly ten times its parameter count.

## Metadata
- **Published**: 2026-08-28T08:28:43Z
- **Authors**: Zongkai Liu, Hui Zhang, Liqiang Niu, Zhen Cao, Han Li, Juntao Liu, Wenchao Chen, Chengduo Zhao, Chao Yu, Fandong Meng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28062v1)