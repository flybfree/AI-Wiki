---
title: Copy Less, Ground More: Overcoming Repetitive Copying in Long-Context Reasoning via Evidence-Aware Reinforcement Learning
url: http://arxiv.org/abs/2607.19345v1
type: paper-summary
date: 2026-07-21
source_paper: 2026-07-21_17-59-21Z_CopyLess_GroundMore_OvercomingRepetitiveCopyinginL.md
generated_at: 2026-07-21 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates repetitive copying in long-context reasoning, where large language models mistakenly reproduce prompt text instead of generating useful solutions. By separating key evidence from distractors and applying a grounding‑aware reward scheme called GEAR, the authors achieve up to four point gains over standard reinforcement learning while reducing copy artifacts.

## Key Takeaways
- The failure mode is pervasive across frontier long-context LLMs and worsens with longer contexts because models lack sufficient grounding in relevant evidence.  
- Grounding rewards that favor overlap with key evidence and penalize overlap with irrelevant context improve accuracy and cut down on repetitive copying.  
- An automated pipeline creates evidence‑annotated training data from any document, enabling the reinforcement learning method to be applied without manual annotation.

## Context
Long‑context evaluation is shifting from simple retrieval tasks to complex reasoning, yet current models often ignore the importance of focusing on pertinent information. This gap limits their usefulness in real‑world applications that require nuanced understanding across extended inputs.

## Implications
Practitioners can adopt grounding‑aware reward design to make long‑context LLMs more reliable and efficient, reducing hallucinations caused by copying. Companies developing automated reasoning systems will benefit from higher accuracy and shorter thinking traces, leading to cost savings and better user experiences.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19345v1)
