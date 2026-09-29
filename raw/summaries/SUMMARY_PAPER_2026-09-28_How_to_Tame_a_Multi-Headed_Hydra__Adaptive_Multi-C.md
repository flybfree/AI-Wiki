---
title: How to Tame a Multi-Headed Hydra? Adaptive Multi-Category Safety Steering for Large Language Models
url: http://arxiv.org/abs/2609.34514v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_07-53-31Z_HowtoTameaMulti_HeadedHydra_AdaptiveMulti_Category.md
generated_at: 2026-09-28 23:25
model: qwen3.6-35b-a3b
---

## Summary
The paper introduces CAM-Steer, a Category-Adaptive Multi-category Safety Steering framework designed to enhance the safety of Large Language Models during inference without modifying model parameters. By estimating risks associated with multiple harm categories within a single prompt using hidden state comparisons against prototypes, CAM-Steer dynamically combines safety directions and adjusts intervention strength while preserving the hidden-state norm. Experimental results demonstrate that this approach significantly outperforms existing baselines in defense success rates, particularly when multiple harm categories co-occur, all while maintaining negligible inference overhead.

## Key Takeaways
- CAM-Steer quantifies threat levels by comparing current hidden states against safe and unsafe prototypes for each harm category, enabling precise risk estimation that informs the steering process based on the specific dangers present in a prompt.
- The framework resolves the challenge of co-occurring harms by dynamically composing safety directions from different categories into a single steering vector and determining intervention strength via estimated risks, ensuring balanced protection without compromising performance on individual categories.
- CAM-Steer rotates hidden states along the composed direction with risk-determined angles while preserving norm, achieving superior defense

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34514v1)
