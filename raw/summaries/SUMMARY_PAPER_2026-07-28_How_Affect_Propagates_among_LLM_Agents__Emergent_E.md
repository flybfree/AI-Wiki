---
title: How Affect Propagates among LLM Agents: Emergent Emotional Contagion in Crowd Simulation
url: http://arxiv.org/abs/2607.25140v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_23-22-17Z_HowAffectPropagatesamongLLMAgents_EmergentEmotiona.md
generated_at: 2026-07-28 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how affect spreads among language model agents within a multi‑agent crowd simulation by examining the perception‑appraisal‑expression loop that drives emotional contagion. The results reveal that alarm and other emotions propagate with spatial, temporal, and personality‑dependent patterns in small groups, while the dynamics vary across different LLM backends.

## Key Takeaways
- Alarm spreads from seeded agents as a traveling front, reaching a stable nonzero plateau of alarmed individuals whose distribution depends on the prompted personality profiles.  
- The appraisal step is highly sensitive to prompt variants, sampling temperatures, and model backends, causing backend‑dependent differences in how ambiguous alarms are interpreted as panic or anger versus fear.  
- Spatial layout and scenario context (alarming, joyful, neutral) shape both the speed and final state of emotional contagion within sparse crowds.

## Context
Understanding affective propagation in AI agents is crucial for designing socially aware systems that can mimic human interaction patterns. This work bridges affective science with large language model behavior, offering a framework to study emergent social dynamics in digital environments.

## Implications
For developers building multi‑agent platforms, the findings suggest that backend selection and prompt engineering directly affect user experience and safety. Practitioners should consider these variables when deploying emotionally responsive AI systems to avoid unintended panic or misinterpretation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25140v1)
