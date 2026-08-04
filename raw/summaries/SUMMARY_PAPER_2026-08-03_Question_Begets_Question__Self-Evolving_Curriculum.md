---
title: Question Begets Question: Self-Evolving Curriculum for Reinforcement Fine-Tuning on Competition Mathematics
url: http://arxiv.org/abs/2608.01522v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_22-19-01Z_QuestionBegetsQuestion_Self_EvolvingCurriculumforR.md
generated_at: 2026-08-03 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the limitations of training a language model on competition mathematics by introducing a self‑evolving curriculum that generates problem variants from already‑solved questions, thereby overcoming data scarcity and the lack of ground‑truth reasoning traces. The authors demonstrate that such a curriculum lifts pass@1 performance to 16.5 % after twenty rounds without plateauing, breaking the apparent ceiling observed with static training.

## Key Takeaways
- Question‑begets‑Question (QbQ) creates diverse problem variants from existing solutions, allowing the model to learn richer representations of the same underlying skill set.
- Reinforcement learning on only statements and answers eliminates the need for teacher reasoning traces while still enabling effective fine‑tuning despite data scarcity.
- The self‑evolving curriculum continuously adapts by selecting problems the model can mostly solve as seeds, preventing saturation and continuing to improve performance.

## Context
The study tackles a common challenge in AI research: limited labeled data and the difficulty of capturing reasoning traces for reinforcement learning. By focusing on competition math tasks like AIME, it highlights how curriculum design can mitigate these issues without relying on external oracles.

## Implications
For practitioners, this approach offers a scalable method to boost model performance on narrow domains where data is scarce. It suggests that adaptive curricula could be applied across various AI applications, from language translation to scientific reasoning, enhancing efficiency and scalability of fine‑tuning processes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01522v1)
