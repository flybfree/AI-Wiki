---
title: MedDDC-Eval: Diagnosis-Decoupled Evaluation of Multi-Turn Medical Consultation Agents
url: http://arxiv.org/abs/2607.18999v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_11-32-41Z_MedDDC_Eval_Diagnosis_DecoupledEvaluationofMulti_T.md
generated_at: 2026-07-23 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MedDDC-Eval, a diagnosis‑decoupled evaluation framework for multi‑turn medical consultation agents. By treating the elicited history as the constant object and freezing the reader, it isolates diagnostic generation quality from policy decisions. The study shows that fixing histories while varying readers can shift F1 scores by 2.2–19 points and reverse many pairwise orderings.

## Key Takeaways
- Strong diagnosis generation can mask a thin history, whereas a rich history may be under‑utilized if the reader is weak.
- Holding histories fixed, changing only the diagnostic reader changes diagnosis F1 by 2.2 to 19 points and flips 18%–36% of pairwise policy orderings on Record and Dialogue splits.
- Applying GRPO with feedback from diagnosis results improves Qwen3‑32B’s total score by 9.7 (Record) and 4.6 (Dialogue) over initialization.

## Context
The work addresses a longstanding challenge in conversational AI: separating the quality of information gathering from the final decision output, which is crucial for reliable medical chatbots. By decoupling these components, MedDDC‑Eval provides a clearer metric for evaluating both policy and reader performance.

## Implications
For developers, this framework enables targeted improvements—either by refining evidence acquisition or enhancing diagnostic reasoning—without conflating them. Practitioners can use the results to prioritize interventions that most impact patient safety and efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18999v1)
