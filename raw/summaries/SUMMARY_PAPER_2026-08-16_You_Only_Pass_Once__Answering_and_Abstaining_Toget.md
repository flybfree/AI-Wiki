---
title: You Only Pass Once: Answering and Abstaining Together in a Single Forward Pass of a Frozen Language Model
url: http://arxiv.org/abs/2608.14465v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_16-44-35Z_YouOnlyPassOnce_AnsweringandAbstainingTogetherinaS.md
generated_at: 2026-08-16 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces YOPO (You Only Pass Once), a method that combines answering, conditional steering, and sufficiency detection within a single forward pass of a frozen language model. The approach restores reasoning accuracy by rewriting the residual stream with a small network trained to reconstruct it from steered outputs while reading a zero‑shot sufficiency probe on the reconstruction.

## Key Takeaways
- YOPO merges two previously separate techniques — conditional steering and zero‑shot sufficiency — into one pass, eliminating the need for an extra inference step.  
- The method improves three‑way accuracy from 0.375 to 0.798 on a 1.5B alphaNLI model and beats all two‑pass baselines across ten backbones and six families.  
- A source‑side audit revealed that the benchmark’s surface artifact was leaking answers, so results are anchored on native‑label replications such as SQuAD2, RepLiQA, and MuSiQue.

## Context
The work addresses a longstanding challenge in frozen model reasoning: under‑utilizing internal evidence and generating confabulations when inputs lack sufficient information. By integrating steering and sufficiency checks without additional passes, YOPO offers a more efficient alternative to current two‑pass pipelines that double inference cost.

## Implications
YOPO demonstrates that abstention can be learned from the residual stream itself, suggesting a path toward truly adaptive, single‑pass reasoning systems. For industry practitioners, this means lower latency and reduced compute while maintaining high accuracy across diverse domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14465v1)
