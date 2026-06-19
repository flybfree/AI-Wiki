---

title: "MSUE: Multi-Modal Soccer Understanding Expert"
url: http://arxiv.org/abs/2606.12106v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_14-00-55Z_MSUE_Multi_ModalSoccerUnderstandingExpert.md
generated_at: "2026-06-11 10:56"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces MSUE, a multi-expert question answering system for the 2026 SoccerNet VQA Challenge. It combines data synthesis with three specialized experts to achieve high accuracy on diverse soccer video queries. The model reaches 0.95 accuracy and secures third place in the competition.

## Key Takeaways
- A cost‑effective VLM pipeline transforms raw soccer footage into varied VQA samples, enabling both short answers and extended explanations.
- MSUE uses a Large Language Model to route questions among a text baseline (Gemini3‑Flash), a visual language model (Qwen3‑VL) and an external knowledge base for integrated reasoning.
- The architecture’s dynamic dispatch improves performance, delivering the highest accuracy reported in the challenge.

## Context
This work addresses the growing need for multimodal understanding in sports analytics where video, text and structured data must be interpreted together. By integrating LLM‑driven expert routing, it exemplifies a trend toward flexible, modular AI systems that can adapt to specific domain challenges.

## Implications
For developers, MSUE offers a template for building specialized QA pipelines without massive retraining. For the sports industry, such models could automate fan engagement and real‑time commentary generation, turning raw footage into actionable insights efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12106v1)
