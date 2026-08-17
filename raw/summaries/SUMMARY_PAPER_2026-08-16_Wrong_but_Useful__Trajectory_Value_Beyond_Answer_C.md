---
title: Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages
url: http://arxiv.org/abs/2608.14375v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_15-16-57Z_WrongbutUseful_TrajectoryValueBeyondAnswerCorrectn.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces the Diverse Hypothesis Deliberation (DHD) protocol to measure how a message’s trajectory value influences downstream reasoning, independent of its correctness. Experiments across mathematics and science benchmarks show that wrong‑helpful messages often improve final answers in both gpt‑oss‑120b and gemma‑4‑31B‑it models. The study demonstrates that answer accuracy alone cannot predict whether a message should be kept.

## Key Takeaways
- Wrong‑answer messages can still provide useful reasoning components, indicating trajectory value is separate from correctness.  
- In every benchmark‑model pair, more than 40 % of wrong‑helpful changes improve the final solution despite being incorrect.  
- The complete message yields better outcomes than retaining only its answer or reasoning, suggesting full context matters.

## Context
Multi‑agent systems rely on filtering messages based on confidence scores, assuming correctness equals usefulness. Recent work shows this assumption can be misleading when partial insights are valuable even if the final answer is wrong. This paper adds a systematic measure of trajectory value to complement existing accuracy metrics.

## Implications
Practitioners should design retrieval or inclusion strategies that consider both answer quality and reasoning utility rather than relying solely on correctness. The reusable labels from DHD can guide agents in selecting which messages to surface, improving overall system performance across diverse domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14375v1)
