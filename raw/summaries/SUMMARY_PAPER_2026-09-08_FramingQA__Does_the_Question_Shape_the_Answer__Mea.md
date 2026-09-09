---
title: FramingQA: Does the Question Shape the Answer? Measuring the Compositional Framing Effect
url: http://arxiv.org/abs/2609.07448v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_12-56-44Z_FramingQA_DoestheQuestionShapetheAnswer_Measuringt.md
generated_at: 2026-09-08 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FramingQA, a benchmark that evaluates how question framing influences model answers across law, medicine, finance, and robotics simulations. The study shows that large language models respond differently to subtle rephrasings even when the underlying facts remain unchanged, revealing a compositional framing effect.

## Key Takeaways
- Strong per‑variant accuracy does not guarantee robustness; models can produce divergent outputs for the same factual premise when framed differently.
- Framing bias is injected at three levels—root question phrasing, propositional premise injection, and global premise‑question pairing—to capture varying degrees of influence.
- The benchmark tests nine open LLMs (3.8B–70B) across four domains, highlighting that model performance varies with framing rather than just raw accuracy.

## Context
Understanding framing effects is crucial because real‑world queries often contain incomplete or misleading assumptions, and experts rely on accurate answers regardless of phrasing. This research contributes to the broader AI community’s focus on question understanding and mitigating bias in language models.

## Implications
For industry practitioners, this work underscores the need for robust QA systems that remain consistent across user phrasings, especially in high‑stakes domains where errors can have serious consequences. It also prompts developers to design evaluation benchmarks that specifically test framing resilience.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07448v1)
