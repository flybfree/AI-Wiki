---
title: When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning
url: http://arxiv.org/abs/2609.01455v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_15-59-32Z_WhenSafetyRoutingBreaks_UnderstandingAlignmentFrag.md
generated_at: 2026-09-01 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why benign fine‑tuning causes large language models to lose safety alignment, showing that refusal behavior collapses while general utility degrades little. It attributes this fragility to a low‑rank output routing mechanism that is reshaped during training and can be restored with few examples.

## Key Takeaways
- Safety Fisher is low‑rank, meaning the safety geometry becomes flat after fine‑tuning yet still contains an output‑routing pathway.
- The alignment process selectively re‑sharpens MLP modules on the output side, causing asymmetric fragility where safety collapses to high attack success rates while utility degrades mildly.
- Few safety examples can restore refusal behavior because internal safety representations are preserved despite the geometry flattening.

## Context
Benign fine‑tuning is a common technique for improving model performance without harmful data. Safety alignment research has traditionally focused on gradient conflicts, but this study reveals a geometric cause that affects how models route outputs and respond to attacks.

## Implications
Understanding this routing mechanism helps practitioners design training strategies that protect safety without sacrificing utility. It also suggests that fine‑tuning methods like LoRA or ASAM may need scaling adjustments to maintain protection as more examples are added.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01455v1)
