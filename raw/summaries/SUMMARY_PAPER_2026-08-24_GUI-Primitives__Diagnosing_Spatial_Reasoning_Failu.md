---
title: GUI-Primitives: Diagnosing Spatial Reasoning Failures in Vision-Language GUI Grounding
url: http://arxiv.org/abs/2608.21832v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_08-04-59Z_GUI_Primitives_DiagnosingSpatialReasoningFailuresi.md
generated_at: 2026-08-24 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GUI-Primitives, a benchmark that tests whether vision-language models correctly bind relational language to specific interface elements. The results show that most models fail to select the right element even when they fall inside the correct candidate region, indicating problems with spatial reasoning rather than simple mis‑labeling.

## Key Takeaways
- Models emit unconstrained coordinates and often lie outside both designated candidates on 60–92 % of items.  
- Conditional on being within a candidate region, selection accuracy is high (0.82–0.90) for horizontal/vertical position, proximity, and list ordinal but drops to 0.50 for containment and occlusion.  
- The benchmark correlates with ScreenSpot‑Pro accuracy (Spearman ρ = +0.74), suggesting a link between existing grounding methods and the new task.

## Context
Vision-language models are increasingly used to interact with graphical user interfaces, yet they often struggle to understand spatial relationships expressed in natural language. Existing benchmarks either lack fine‑grained relational control or do not isolate whether failures stem from element localization or relation comprehension. This work fills that gap by systematically varying the relational phrase while keeping the screenshot and anchor fixed.

## Implications
The findings highlight a critical limitation of current GUI grounding systems: they cannot reliably translate spatial language into correct screen coordinates, which could hinder real‑world applications like automated form filling or robot assistance. Providing an oracle diagnostic such as marking candidates may guide future model design but does not yet offer a deployable solution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21832v1)
