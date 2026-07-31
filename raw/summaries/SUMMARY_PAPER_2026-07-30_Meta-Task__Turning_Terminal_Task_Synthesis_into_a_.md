---
title: Meta-Task: Turning Terminal Task Synthesis into a Terminal Task for Scalable Agent Training
url: http://arxiv.org/abs/2607.27929v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_09-41-08Z_Meta_Task_TurningTerminalTaskSynthesisintoaTermina.md
generated_at: 2026-07-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Meta‑Task, a framework that treats terminal task synthesis as an executable Terminal‑Bench format task within a real container environment. By iteratively generating, executing, and verifying tasks inside the loop, the method produces reliable, diverse data streams. Experiments on Terminal‑Bench 2.0 show that fine‑tuning only 3,221 synthesized trajectories yields 22.5% and 31.8% Avg Pass@1 for Qwen3‑14B and Qwen3‑32B respectively, outperforming concurrent approaches with far less training data.

## Key Takeaways
- Weak reliability stems from the disconnect between task generation and real execution, which can produce tasks that fail when run.
- Limited diversity and scalability arise because existing synthesis relies on static repositories rather than generating new ones dynamically.
- LLM‑as‑Judge filtering is integrated to ensure only high‑quality, verifiable trajectories reach training.

## Context
Training large language agents at scale demands a massive supply of varied, executable terminal tasks. Current synthesis pipelines often fall short due to reliability issues and narrow data sources, limiting the effectiveness of fine‑tuning. Meta‑Task addresses these gaps by embedding verification directly into the generation pipeline.

## Implications
The approach enables practitioners to generate high‑quality training data without relying on external repositories, reducing costs and accelerating model development. By improving performance with minimal data, it offers a scalable solution for deploying advanced agents in real‑world settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27929v1)
