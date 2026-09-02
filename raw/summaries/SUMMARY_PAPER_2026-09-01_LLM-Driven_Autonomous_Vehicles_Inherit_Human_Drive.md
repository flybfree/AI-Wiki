---
title: LLM-Driven Autonomous Vehicles Inherit Human Driver Biases in Pedestrian Yielding: Results and Implications From A New Benchmark
url: http://arxiv.org/abs/2609.00192v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_18-11-49Z_LLM_DrivenAutonomousVehiclesInheritHumanDriverBias.md
generated_at: 2026-09-01 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how Large Language Models and Visual‑Language Models make pedestrian yielding decisions, showing that these biases mirror human driver prejudices. The authors introduce two bias testing methods—“All Else Being Equal” and “Self‑Consistency”—and find that models discriminate across gender, ethnicity, religion, disability, age, skin tone, and socio‑economic status.

## Key Takeaways
- Both LLMs and VLMs yield lower yielding probabilities to Black pedestrians compared with white pedestrians, reflecting real‑world driver bias.  
- The biases vary by model but are consistently tied to demographic attributes such as gender, disability, and age.  
- The “common sense” paradigm used in AV research may propagate these unfair outcomes if not explicitly addressed.

## Context
Autonomous vehicle systems increasingly rely on general‑purpose language models to interpret visual scenes, yet the ethical consequences of hidden bias remain underexplored. This work adds a methodological layer that evaluates fairness directly within the decision‑making pipeline, highlighting a gap in current AV evaluation frameworks.

## Implications
For industry developers, detecting and mitigating these biases is essential to maintain public trust and regulatory compliance. Practitioners must integrate bias testing into model validation pipelines rather than assuming “common sense” models are inherently neutral.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00192v1)
