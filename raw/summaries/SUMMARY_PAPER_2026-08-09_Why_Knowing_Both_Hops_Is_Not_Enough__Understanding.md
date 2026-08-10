---
title: Why Knowing Both Hops Is Not Enough: Understanding Two-Hop Generalization in Language Models
url: http://arxiv.org/abs/2608.07261v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_14-17-34Z_WhyKnowingBothHopsIsNotEnough_UnderstandingTwo_Hop.md
generated_at: 2026-08-09 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why large language models succeed on some two-hop reasoning tasks yet fail on others, finding that generalization depends on whether the second hop matches training distribution. It shows that when the second hop is out-of-distribution, lower layers build correct intermediate representations but upper layers cannot reason over them.

## Key Takeaways
- Models generalize reliably only when the second hop follows the training distribution because they can reuse consistent intermediate representations across contexts.
- Failures on out‑of‑distribution two‑hop queries arise from a mismatch between lower and upper layers: lower layers create correct representations while upper layers are trained to map facts directly rather than reason over them.
- A recurrent‑style training strategy that reuses reasoning circuitry improves generalization on such queries.

## Context
This work sheds light on the limited reasoning capabilities of transformer architectures, which often treat each token independently and cannot maintain coherent intermediate states. Understanding these limitations helps researchers design better prompting or architecture modifications to support multi‑step inference.

## Implications
For practitioners developing AI assistants that must answer complex questions, this research suggests that training should emphasize consistent internal representations rather than only surface patterns. It also points toward architectural changes like recurrent loops to enable true two‑hop generalization across diverse inputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07261v1)
