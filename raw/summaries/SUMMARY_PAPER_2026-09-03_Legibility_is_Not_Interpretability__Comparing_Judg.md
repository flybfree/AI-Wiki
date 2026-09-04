---
title: Legibility is Not Interpretability: Comparing Judged and Actual Importance in Chain-Of-Thought Reasoning
url: http://arxiv.org/abs/2609.04194v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_17-59-08Z_LegibilityisNotInterpretability_ComparingJudgedand.md
generated_at: 2026-09-03 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the legibility of chain-of-thought reasoning traces corresponds to their actual importance in influencing model performance. By defining step importance as the advantage a step provides, estimated through Monte Carlo rollouts, the authors show that large language models can identify high‑advantage steps but still struggle to capture the full range of important reasoning actions.

## Key Takeaways
- The paper defines step importance operationally as the change in expected reward caused by including or excluding a particular reasoning step, measured via Monte Carlo simulations.  
- LLM judges can reliably detect high‑advantage steps for incorrect responses but cannot consistently recognize steps that are crucial for correct answers, indicating partial recoverability of importance from trace text.  
- Fine‑tuning models as step‑level critics improves performance on error detection yet does not bring them close to the theoretical ceiling of identifying all important steps.

## Context
The study builds on a wave of work treating chain-of-thought traces as transparent windows into model reasoning, using judges and process reward models to diagnose errors. However, most approaches assume that textual cues fully encode functional importance, which this paper challenges by grounding importance in empirical advantage rather than textual description.

## Implications
For practitioners developing process‑reward modeling systems, the findings suggest that relying solely on legible traces may lead to incomplete or biased supervision for correct reasoning. This calls for more nuanced evaluation methods that consider both textual cues and actual performance impact of each step.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.04194v1)
