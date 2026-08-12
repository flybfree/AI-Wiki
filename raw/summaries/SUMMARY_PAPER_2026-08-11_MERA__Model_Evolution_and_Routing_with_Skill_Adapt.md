---
title: MERA: Model Evolution and Routing with Skill Adaptation for Agentic Systems at Scale
url: http://arxiv.org/abs/2608.10333v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_00-28-02Z_MERA_ModelEvolutionandRoutingwithSkillAdaptationfo.md
generated_at: 2026-08-11 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MERA, a framework for evolving small language models through skill‑adapted adaptation cycles. By replaying failed student invocations and distilling them into an iteratively updated SkillBook, MERA fine‑tunes a LoRA adapter to raise model performance on benchmark tasks.

## Key Takeaways
- MERA uses each failed student invocation as the unit of adaptation, turning isolated errors into verifiable teacher demonstrations.  
- The framework combines supervised learning with optional GRPO to refine a lightweight LoRA adapter that directly improves the small model’s reasoning ability.  
- Verifier‑backed fallback routing preserves high task quality at only 60.8% of Luna’s cost, showing adaptation can outperform static routing.

## Context
Current LLM agent pipelines rely on coarse‑grained routing that assigns tasks to models based on difficulty without enhancing the smaller model itself. This limits cost savings because the student’s capability remains fixed. MERA addresses this by embedding continual learning directly into the student model through skill‑specific adaptation cycles.

## Implications
The results demonstrate that multi‑cycle, verifier‑backed adaptation can boost small‑model performance beyond what routing alone achieves, offering a path to cheaper yet more capable agentic systems. Practitioners can adopt MERA’s SkillBook and LoRA pipeline to iteratively upgrade agents without scaling model size or inference budget.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10333v1)
