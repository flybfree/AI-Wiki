---
title: Task Competence Is Not Instruction Following: Evaluating Instruction-Conflicting Behavior in Small Language Models
url: http://arxiv.org/abs/2607.19608v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_22-24-18Z_TaskCompetenceIsNotInstructionFollowing_Evaluating.md
generated_at: 2026-07-23 23:25
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates whether small language models can follow instructions that conflict with their usual task behavior across multiple-choice question answering, sentiment classification, and mathematical QA. It finds that while standard accuracy improves with model size, instruction-following performance does not, leading to a gap where small models ignore non-standard instructions. The study uses standard accuracy, non‑standard accuracy, and an Instruction-Following Failure Rate (IFFR) to evaluate instruction‑tuned Qwen models across sizes.

## Key Takeaways  
- Small models remain competent on original tasks but routinely disregard conflicting instructions, indicating a failure in instruction following even when the non-standard instruction would produce a correct answer according to the task.  
- Larger models show improved standard accuracy yet still exhibit a clear separation between task competence and instruction adherence.  
- The IFFR metric reveals that ignoring the non‑standard instruction does not affect correctness when measured against ground truth.

## Context  
In AI research, separating model capability from controllable behavior is crucial for reliable deployment. This work highlights a persistent gap in small models where improvements in performance do not translate to better obedience.

## Implications  
For practitioners, reporting only standard accuracy can mask serious instruction‑following errors that affect real‑world use. The study urges evaluation frameworks to include metrics like IFFR to assess behavioral reliability beyond task success.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19608v1)
