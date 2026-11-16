---
title: Is Abliteration Getting Harder? Not Uniformly: Refusal Removal by Direction-Based Ablation and ARA in Heretic on the Qwen3.8, Gemma 4, Olmo 3.1 and Mistral Small 3.2 LLMs Versus Their Predecessors
url: http://arxiv.org/abs/2611.17846v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-13_07-29-43Z_IsAbliterationGettingHarder_NotUniformly_RefusalRe.md
generated_at: 2026-11-15 21:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper challenges the claim that direction-based abliteration (a fine-tuning-free weight-editing technique that removes refusal behavior from open-weight LLMs) is becoming uniformly harder on newer model generations. By systematically applying multiple direction-based methods and Arbitrary-Rank Ablation (ARA) across five model release pairs spanning Qwen, Gemma, Olmo, and Mistral families, the author finds that refusal-removal difficulty varies substantially by model pair, method, and search budget rather than increasing monotonically with model generation. The results demonstrate that single-pair or single-method audits can yield contradictory conclusions, undermining broad generalizations about abliteration's declining effectiveness.

## Key Takeaways
- Across five release pairs (Qwen2.5-32B to Qwen3.8-27B, Gemma-2-27B to Gemma-4-31B, OLMo-2-32B to Olmo-3.1-32B, Mistral-Small-2409 to Mistral-Small-3.2, and Qwen2.5-7B to Qwen3.5-4B), direction-based abliteration methods (difference-in-means, MPOA, SOM, J-space) produced heterogeneous outcomes: newer models retained between -1 and +37 percentage points more refusal, while ARA results ranged from -26 to +34 points, showing no uniform trend of increasing difficulty.
- ARA did not consistently outperform or underperform direction-based methods; it lost less effectiveness than direction-based approaches in Gemma and OLMo pairs but lost more in Qwen pairs, and these verdicts shifted depending on the divergence budget and variance model used, with between-pair heterogeneity ranging from high to low (I² 20–80%).
- The paper reveals methodological fragility: keyword-count metrics at the tool's window did not systematically undercount judged refusal on average but differed by a mean 7 points per model, and audits restricted to a single pair, method, or prompt source can reach opposite conclusions, highlighting the danger of drawing broad claims from narrow experimental setups.

## Context
Abliteration has emerged as a popular technique in the open-weight LLM community for stripping refusal behavior from models without costly fine-tuning, enabling researchers and practitioners to deploy models that respond to a wider range of prompts. The developer of ARA publicly claimed that direction-based abliteration is increasingly failing on newer model releases, a claim that could discourage adoption of these techniques for the latest open-weight models. This paper provides the first systematic multi-model, multi-method comparison across five major open-weight model families, directly testing that claim under controlled conditions with a shared evaluation harness of 972 held-out harmful prompts from multiple established benchmarks.

## Implications
For practitioners and researchers who rely on abliteration to customize open-weight models, this work demonstrates that the technique's effectiveness cannot be predicted from model generation alone; instead, success depends on the specific model pair, chosen method, and computational budget, meaning users should evaluate abliteration empirically on their target model rather than assuming newer models are inherently harder to edit. For the broader AI safety and alignment community, the finding that single audits can produce opposite conclusions underscores the need for standardized, multi-model evaluation protocols before declaring any refusal-removal technique obsolete or universally effective, and it cautions against premature generalizations that could misguide tool development and deployment decisions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17846v1)
