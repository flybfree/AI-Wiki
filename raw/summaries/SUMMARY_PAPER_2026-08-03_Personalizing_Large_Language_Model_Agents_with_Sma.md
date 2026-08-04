---
title: Personalizing Large Language Model Agents with Small Policy Models
url: http://arxiv.org/abs/2608.00215v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_18-56-30Z_PersonalizingLargeLanguageModelAgentswithSmallPoli.md
generated_at: 2026-08-03 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FABLE, a lightweight policy layer that personalizes frozen LLM agents using online learning from scalar feedback, enabling per‑user execution decisions without fine‑tuning the model. It achieves this by factorizing memory, information acquisition, and response choices, applying Bayesian contextual Thompson sampling to learn residual preferences, and providing regret bounds under a linear residual reward model.

## Key Takeaways
- FABLE learns user‑specific residual preferences relative to a fixed default score using Bayesian contextual Thompson sampling from scalar feedback alone. 
- The policy factorizes memory, information acquisition, and response decisions, allowing feedback to update each component separately while respecting feasible action sets. 
- Under linear residual reward assumptions the calibrated variant inherits an expected‑regret bound against the best feasible action.

## Context
Personalizing AI agents is a key challenge as deploying separate models per user is costly; existing methods rely on prompts or memory that expose data rather than adapt execution policies. FABLE addresses this by treating personalization as online bandit learning, fitting within the broader trend of lightweight adaptation for large language systems.

## Implications
This work enables scalable, privacy‑preserving personalization for proprietary LLM services, reducing reliance on costly fine‑tuning while improving user satisfaction through tailored responses and tool use. Practitioners can integrate FABLE as a modular layer to enhance agent behavior without compromising model performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00215v1)
