---
title: FACT: Failure-Aware Causal Training for World-Action Models
url: http://arxiv.org/abs/2608.10232v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_21-10-46Z_FACT_Failure_AwareCausalTrainingforWorld_ActionMod.md
generated_at: 2026-08-11 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FACT, a failure‑aware causal World‑Action Model that predicts future video and task progress directly from the executed action rather than only from successful demonstrations. By treating failed actions as valid targets for supervision, FACT enables the model to learn from both successes and failures, leading to improved performance on simulation and real‑world bimanual manipulation tasks.

## Key Takeaways
- FACT creates an action‑conditioned interface that predicts future video and progress, allowing failure rollouts to be used as training signals rather than being discarded.  
- The model’s progress predictor becomes aware of both successful and failed outcomes, which can optionally score sampled actions at inference time.  
- Experiments show that incorporating failure data improves performance and reduces success‑biased hallucinations when bad actions are executed.

## Context
World‑Action Models aim to align action generation with the consequences of those actions by leveraging future predictions from video models. Traditional approaches rely on demonstrations, which rarely include failures, limiting their ability to model real‑world dynamics where errors occur frequently.

## Implications
FACT demonstrates that failure data can be a valuable resource for training robust AI agents in physical tasks. Practitioners may integrate this approach to build systems that learn from mistakes, leading to safer and more reliable autonomous manipulation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10232v1)
