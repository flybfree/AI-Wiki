---
title: TacForcing: Streaming Action Generation with Execution-Time Tactile Feedback
url: http://arxiv.org/abs/2608.25798v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_13-48-52Z_TacForcing_StreamingActionGenerationwithExecution_.md
generated_at: 2026-08-26 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TacForcing, a streaming action-generation framework that integrates execution-time tactile feedback into vision-language-action models. By replacing the static action expert with a reactive streaming expert and using Execution-Aware Tactile Attention (EATA), TacForcing adapts to evolving contact states during manipulation. Across simulated and real tasks it achieves success rates of 65% and 69%, surpassing strong baselines.

## Key Takeaways
- TacForcing replaces the standard action expert with a streaming action expert that conditions actions on tactile observations acquired while execution is occurring.
- Execution-Aware Tactile Attention (EATA) limits tactile conditioning to actions near the end of the horizon, reducing temporal mismatch between feedback and action generation.
- The framework achieves higher success rates in both simulated UniVTAC tasks and real-world contact-rich manipulation tasks compared with existing reactive controllers.

## Context
Current vision-language-action systems generate whole action chunks from pre-execution observations, which cannot react to changes in tactile states during execution. This leads to suboptimal performance in tasks where contact evolves rapidly. TacForcing addresses this limitation by enabling continuous feedback integration within the generation pipeline.

## Implications
The results demonstrate that streaming reactive controllers can be embedded directly into existing VLA pipelines without major architectural overhauls, lowering development complexity. Practitioners can leverage this approach to build more responsive robotic manipulators for real-world applications such as assembly or medical procedures where tactile cues are critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25798v1)
