---
title: MOF-Sleuth: Tool-Grounded Reward Alignment for Explainable Fine-Grained MOF CIF Auditing
url: http://arxiv.org/abs/2607.19935v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_09-05-43Z_MOF_Sleuth_Tool_GroundedRewardAlignmentforExplaina.md
generated_at: 2026-07-23 22:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
MOF‑Sleuth is a reinforcement‑guided CIF auditing agent that produces evidence‑grounded explanations for chemical and structural errors in metal‑organic framework databases. The system combines a deterministic Forensic Lab that extracts composition, geometry, connectivity, occupancy, coordination, and charge from the CIF with a Sleuth reasoning engine that generates diagnoses supported by specific evidence. Across four benchmarks it achieves state‑of‑the‑art detection rates while providing clear, chemically grounded attributions.

## Key Takeaways
- The Forensic Lab extracts multiple chemical attributes such as composition, geometry, connectivity, occupancy, coordination and charge from CIF records, turning hidden data into explicit evidence for explanation.  
- Reinforcement learning rewards both the final binary decision and the specific evidence cited, aligning tool outputs with chemically accurate diagnoses.  
- Chemically Grounded Diagnosis (Chem‑GD) measures how well a correct diagnosis is explained by factual CIF‑derived evidence, improving attribution beyond coarse labels.

## Context
Fine‑grained chemical reasoning in large language models remains limited because evidence is implicit across atom‑site records and requires complex geometric calculations. This paper addresses the gap by linking LLM explanations directly to measurable chemical properties, demonstrating that reinforcement learning can turn raw CIF data into reliable diagnostic support.

## Implications
For researchers, MOF‑Sleuth offers a framework to audit high‑volume crystallographic databases without manual inspection, reducing errors in downstream simulations and ML pipelines. Practitioners can rely on evidence‑backed diagnoses to trust model outputs, fostering reproducibility and confidence in computational chemistry workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19935v1)
