---
title: REACT: Representational Early Analysis and Control of Chain-of-Thought Trajectories
url: http://arxiv.org/abs/2610.32113v1
type: paper-summary
date: 2026-10-25
source_paper: 2026-10-23_03-28-34Z_REACT_RepresentationalEarlyAnalysisandControlofCha.md
generated_at: 2026-10-25 21:45
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
REACT introduces a conditional activation intervention that learns a safety direction from paired safe and unsafe chain-of-thought trajectories and applies it once to an early hidden state, leaving all model weights frozen and all subsequent tokens unedited. The paper's central finding is that the optimal timing for such interventions is not where risk is most readable but rather in a narrow two- to three-token early window, where intervention most effectively steers subsequent generation toward safe outputs.

## Key Takeaways
- REACT trains safety directions separately at each of the first five CoT positions and evaluates ungated edits with full post-edit regeneration across three distilled reasoning models and three generation seeds. The strongest safety gains concentrate in a two- to three-token early window, while on DeepSeek-R1-Distill-Llama-8B the effect falls to approximately zero at the fourth and fifth tokens, even though later hidden states can be more predictive of risk. This demonstrates a critical separation between risk readability and effective control: a hidden state that better encodes risk does not necessarily offer a better intervention point for steering generation.
- On the same 8B model, REACT raises the rate of fully safe CoT-answer outputs on the StrongREJECT-273 benchmark from 29.06% to 82.05%, while keeping benign refusal rates and response usefulness near baseline levels. This shows that a single early intervention can dramatically improve safety without degrading the model's helpfulness or its ability to refuse appropriately.
- The method requires no fine-tuning or weight modification; the model weights remain entirely frozen, and all tokens after the single edited hidden state are generated normally. This makes the approach lightweight and potentially deployable without retraining infrastructure.

## Context
As reasoning models increasingly rely on extended chain-of-thought generation, the question of how and when to intervene for safety becomes more urgent. Prior work has explored post-hoc filtering, output-level safety classifiers, and fine-tuning-based alignment, but relatively little attention has been given to intervening within the reasoning trajectory itself at the hidden-state level. REACT addresses this gap by treating early CoT hidden states as intervention points and systematically studying how timing affects downstream generation quality and safety.

## Implications
For practitioners deploying reasoning models in production, REACT suggests that safety interventions should target the earliest feasible window in the reasoning chain rather than waiting for more risk-informative later states, fundamentally changing how safety monitoring pipelines might be architected. For the broader field, the separation between risk readability and effective control challenges assumptions in interpretability research and points toward a need for intervention-effect evaluation rather than mere risk-detection accuracy when designing safety mechanisms for reasoning models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.32113v1)
