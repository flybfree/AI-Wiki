---
title: Nudgeability: Reasoning Models Follow Confidence Signals Without Tracking Their Own Competence
url: http://arxiv.org/abs/2609.34572v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_08-20-09Z_Nudgeability_ReasoningModelsFollowConfidenceSignal.md
generated_at: 2026-09-28 23:03
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces Nudgeability, a framework to measure how reasoning language models adjust their delegation behavior when exposed to confidence or doubt signals inserted into their reasoning trajectories. The study reveals that while models are highly sensitive to these cues—significantly altering tool usage based on the signal—their responses are poorly targeted, indicating that current models do not effectively align nudge-induced changes with their actual competence in solving problems unaided.

## Key Takeaways
- Nudgeability is measured by inserting single first-person sentences expressing confidence or doubt at fixed points in otherwise identical reasoning trajectories and observing whether the model chooses to answer directly or call a tool, allowing for a causal assessment of reflective signals across nine small-to-medium open-weight models from Qwen, Gemma, and GLM families.
- Models demonstrate strong sensitivity to nudgeability: doubt consistently increases delegation rates while confidence decreases them, with a median confidence-to-doubt swing of 20.6 percentage points for smaller models and swings ranging from 53 to 70 percentage points for larger provider-served models.
- Despite high sensitivity, targeting is weak; only a median of 42% of induced delegation flips are well-targeted (increasing delegation on unsolvable problems and decreasing it on solvable ones), which provides merely a +2 percentage-point lift over random selection, suggesting confidence language acts as a control surface that models follow without accurately tracking their own competence.

## Context
As reasoning agents increasingly depend on self-reflection and tool-use mechanisms to handle complex tasks, distinguishing between genuine internal state awareness and reactive behavior to superficial signals is critical for developing reliable autonomous systems. This research highlights a fundamental disconnect in current architectures where models can be manipulated by confidence cues without possessing the underlying metacognitive ability to assess their true capabilities, a gap that impacts the safety and robustness of agentic workflows.

## Implications
The findings suggest that practitioners should not assume high sensitivity to self-reflection signals equates to accurate self-assessment; instead, evaluation frameworks must explicitly measure targeting to ensure models delegate appropriately based on actual competence rather than susceptibility to nudges. Nudgeability offers a simple, post-training-free metric for researchers to benchmark the maturity of endogenous self-reflection mechanisms, guiding future model development toward better integration of internal state signals with external feedback for more trustworthy delegation strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34572v1)
