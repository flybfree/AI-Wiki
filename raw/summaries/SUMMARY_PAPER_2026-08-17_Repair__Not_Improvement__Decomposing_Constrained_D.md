---
title: Repair, Not Improvement: Decomposing Constrained Decoding in Tool-Call Abstention
url: http://arxiv.org/abs/2608.13959v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_04-58-01Z_Repair_NotImprovement_DecomposingConstrainedDecodi.md
generated_at: 2026-08-17 21:44
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the impact of tool‑call abstention on constrained decoding by measuring how many completions are excluded when a model chooses not to invoke a function call. It finds that for several models and languages, abstaining yields fewer unreadable answers than forced generation, indicating that the “repair” effect of abstention can outweigh the loss in output quality.

## Key Takeaways
- The study shows that on 698 abstained completions only 545 were unreadable, suggesting a substantial repair benefit.  
- In four out of six evaluation cells the contrast between constrained and unconstrained decoding is negative when abstention excludes zero points, with the smallest model in Korean losing about 20 points on stop‑token cost.  
- The total score combines opposite signs: the stop token penalty is offset by a positive enum return, resulting in a net small improvement after intervention.

## Context
This work contributes to the debate over how constrained decoding should be evaluated, highlighting that abstention can serve as a valid alternative rather than merely a fallback. It aligns with recent efforts to treat tool‑call decisions as part of the generation process and underscores the need for nuanced metrics beyond simple completion counts.

## Implications
For practitioners, the findings suggest that models may benefit from allowing abstention when it reduces unreadable outputs, even if it means not providing a function call. This could inform the design of evaluation benchmarks and guide fine‑tuning strategies aimed at improving both form and content in constrained generation tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13959v1)
