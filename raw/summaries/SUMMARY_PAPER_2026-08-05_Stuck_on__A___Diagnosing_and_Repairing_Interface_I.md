---
title: Stuck on "A": Diagnosing and Repairing Interface Injury in Attention-to-KDA Linearization of a 0.6B Language Model
url: http://arxiv.org/abs/2608.02689v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_08-54-18Z_Stuckon_A__DiagnosingandRepairingInterfaceInjuryin.md
generated_at: 2026-08-05 01:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates what happens when 21 full‑attention layers of a 0.6B language model are replaced by linear‑attention KDA layers on a single consumer GPU. Although hidden‑state alignment and KL distillation bring the student’s perplexity close to that of the teacher, multiple‑choice accuracy collapses to near random chance (≈25–29% vs. 50.6%). A diagnostic shows the model “sticks” to option labels regardless of content, indicating an interface injury invisible to standard metrics.

## Key Takeaways
- The conversion preserves hidden‑state alignment and KL distillation, achieving teacher‑like perplexity but not improved reasoning on multiple‑choice tasks.  
- The model consistently predicts label A (≈81% of the time) even when answer options are rotated, revealing a loss of content understanding.  
- A 1,000‑step format‑targeted completion‑only KL stage repairs the interface, boosting C‑Eval scores by +12.48 points and roughly halving label stickiness.

## Context
Attention linearization aims to reduce memory and compute demands for large models on limited hardware. This work demonstrates that such transformations can degrade model behavior in ways that standard distillation metrics fail to capture, highlighting the need for deeper diagnostics of interface integrity during layer conversion.

## Implications
For practitioners, this research underscores that hardware‑constrained training may introduce subtle bugs that affect downstream performance, requiring targeted repair stages beyond simple distillation. The findings also suggest that evaluation protocols must examine label consistency, not just perplexity, to gauge true model health.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02689v1)
