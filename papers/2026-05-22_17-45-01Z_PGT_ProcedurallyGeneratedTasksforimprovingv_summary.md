---
title: "Summary: 2026-05-22_17-45-01Z_PGT_ProcedurallyGeneratedTasksforimprovingvisualgr.md"
date: 2026-05-22
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-05-22_17-45-01Z_PGT_ProcedurallyGeneratedTasksforimprovingvisualgr.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-05-25 00:00
Source: 2026-05-22_17-45-01Z_PGT_ProcedurallyGeneratedTasksforimprovingvisualgr.md
Model: None

---


## Summary  
The paper introduces Procedurally Generated Tasks (PGT), a data‑driven framework to improve visual grounding in multimodal large language models (MLLMs). By overlaying unambiguous geometric primitives on images, PGT provides dense supervision that separates perception from semantic priors. Experiments show substantial gains across relational, quantitative and 3D benchmarks. The method also serves as a diagnostic tool for identifying the source of perception failures.

## Key Contributions  
- Finding 1: PGT yields up to +20 % improvement on What'sUp benchmark when instruction‑tuned MLLMs are augmented with PGT data.  
- Finding 2: Fine‑tuning state‑of‑the‑art MLLMs on PGT data boosts performance by up to +5.5 % on What'sUp and +8.3 % on CV‑Bench‑2D.  
- Finding 3: The framework disentangles visual grounding from semantic priors, indicating that many spatial deficits stem from inadequate supervision rather than inherent architectural or resolution limitations.

## Methodology  
The authors generate tasks procedurally by placing unambiguous geometric primitives (e.g., cubes, spheres) onto random images, creating a dense set of labeled pairs where the model must ground each primitive to its location. This creates supervision that is both fine‑grained and independent of high‑level semantics, allowing the model to learn precise spatial relationships without relying on textual descriptions.

## Results  
Across relational, quantitative, and 3D/depth tasks, PGT yields significant improvements: instruction tuning LLaVA‑v1.5‑Instruct with PGT data improves What'sUp by +20 % and CV‑Bench‑2D by +13.3 %, while fine‑tuning top models gives +5.5 % on What'sUp and +8.3 % on CV‑Bench‑2D. These gains are consistent across diverse architectures, confirming the framework’s effectiveness.

## Significance  
PGT addresses a critical bottleneck in MLLM performance by providing cheap, scalable supervision that directly targets visual grounding. By exposing models to structured spatial tasks, it uncovers latent weaknesses and enables targeted improvements without retraining from scratch, offering both a diagnostic tool and a path to better perception.

## Related Concepts  
- Visual grounding  
- Multimodal Large Language Models (MLLMs)  
- Procedural task generation  
- Dense supervision  
- Instruction tuning

[[PGT: Procedurally Generated Tasks for improving visual grounding in MLLMs]]