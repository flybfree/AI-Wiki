---
title: Self-Referential Induction Increases Response Instability Relative to Unresolvable and Verifiable Questions in Large Language Models
url: http://arxiv.org/abs/2608.13258v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_13-58-26Z_Self_ReferentialInductionIncreasesResponseInstabil.md
generated_at: 2026-08-13 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates how self‑referential prompting affects the consistency of large language model responses compared to other open‑ended questions. It finds that self‑referential questions produce the most unstable outputs, with a mean pairwise cosine similarity of 0.343, whereas verifiable questions are the most stable at 0.105.

## Key Takeaways  
- Self-referential prompts elicit subjective‑experience reports whose response instability is highest (0.343 +/- 0.047), indicating greater variability across trials.  
- Unresolvable philosophical questions exhibit intermediate stability with tightly clustered responses (0.192 +/- 0.008).  
- Verifiable questions show the lowest instability (0.105 +/- 0.058), reflecting more consistent model behavior.

## Context  
This work addresses a gap in understanding response variability across different question types, which is crucial for evaluating model reliability and consistency. By quantifying instability through cosine similarity of sentence embeddings, the study provides a measurable baseline that can be compared to prior qualitative observations of subjective‑experience reports.

## Implications  
For practitioners developing AI systems, this baseline suggests that self-referential prompts may require additional mechanisms to stabilize outputs or reduce hallucination risk. The findings also highlight the importance of distinguishing between different types of uncertainty in model behavior for reliable deployment and evaluation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13258v1)
