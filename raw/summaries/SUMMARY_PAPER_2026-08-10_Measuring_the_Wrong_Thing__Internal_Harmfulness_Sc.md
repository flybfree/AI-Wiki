---
title: Measuring the Wrong Thing: Internal Harmfulness Scores Anti-Rank Successful Jailbreaks
url: http://arxiv.org/abs/2608.09624v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_14-05-32Z_MeasuringtheWrongThing_InternalHarmfulnessScoresAn.md
generated_at: 2026-08-10 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how internal harmful intent scores are misaligned with actual jailbreak outcomes by introducing Active Attention Probing to provide a fixed, content‑independent measurement coordinate. Experiments on Llama show that wrapping prompts increases harmful generation from 0.05 to 0.27 while the score’s AUROC drops from 0.936 to 0.803, indicating that the filter is judging the wrong quantity.

## Key Takeaways
- Wrapping a prompt can make it appear less harmful to an internal safety score yet actually increase the likelihood of successful jailbreaks.  
- The false positive budget of the score is wasted on attacks that would have failed without wrapping, lowering the AUROC for wrapped prompts (0.220).  
- Distribution shift caused by wrapping degrades calibration and threshold transfer across multiple target models, attack families, and judges.

## Context
AI safety systems rely on internal scoring mechanisms to pre‑filter harmful inputs before generation. Traditional methods use attention scores that depend on prompt location, which can be altered by simple wrapper tricks. This misalignment can lead to unsafe outputs being allowed while benign prompts are blocked, undermining the trustworthiness of automated moderation.

## Implications
Practitioners must recognize that internal safety scores are not reliable predictors of real‑world attack success and should incorporate content‑independent probes like Active Attention Probing. Failure to address this issue could result in widespread misuse of AI systems and erode user confidence in automated safety tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09624v1)
