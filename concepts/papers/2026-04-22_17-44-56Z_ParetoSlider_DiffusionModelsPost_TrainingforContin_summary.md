# Summary: 2026-04-22_17-44-56Z_ParetoSlider_DiffusionModelsPost_TrainingforContin.md
Saved: 2026-05-08 03:23:12Z
Source: 2026-04-22_17-44-56Z_ParetoSlider_DiffusionModelsPost_TrainingforContin.md
Model: None
---
## Summary
ParetoSlider is a multi-objective RL post-training framework for diffusion models that aims to approximate an entire Pareto front rather than a single fixed reward trade-off. It conditions training on continuously varying preference weights, allowing inference-time control over competing objectives without retraining or maintaining multiple checkpoints.

## Key Takeaways
- Replaces early scalarization with continuously varying preference conditioning.
- Targets continuous control over conflicting rewards at inference time.
- Evaluated on SD3.5, FluxKontext, and LTX-2 flow-matching backbones.
- Matches or exceeds baselines trained for fixed trade-offs while enabling finer control.

## Context
The paper addresses RL post-training for generative alignment, where existing methods usually optimize a single scalar reward. This is limiting when objectives conflict, such as prompt adherence versus source fidelity in image editing.

## Implications
A single preference-conditioned diffusion model can support multiple quality trade-offs in one checkpoint, reducing the need for retraining and model proliferation while improving user control.

## Original Reference
- Title: ParetoSlider: Diffusion Models Post-Training for Continuous Reward Control
- Authors: Shelly Golan, Michael Finkelson, Ariel Bereslavsky, Yotam Nitzan, Or Patashnik
- URL: http://arxiv.org/abs/2604.20816v1
- Published: 2026-04-22T17:44:56Z

[[2026-04-22_17-44-56Z_ParetoSlider_DiffusionModelsPost_TrainingforContin.md]]