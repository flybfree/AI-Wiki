---
title: Beyond the Black Box: Interpretable Models of Human Randomisation Failures
url: http://arxiv.org/abs/2608.07220v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_13-36-55Z_BeyondtheBlackBox_InterpretableModelsofHumanRandom.md
generated_at: 2026-08-09 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether the predictive power of black‑box sequence models like LSTMs over human randomisation failures can be replicated with transparent, interpretable alternatives. Using a large dataset of card game decisions, it shows that simple, rule‑based explanations capture most of the signal while deep learning models provide only marginal gains.

## Key Takeaways
- The repeat or avoid patterns in players’ recent actions explain the majority of the interpretable and exploitable information, indicating that behavioural memory is a key driver.  
- Frequency tracking adds little value beyond what can be derived from basic action history analysis, suggesting limited benefit for out‑of‑sample performance.  
- Naive and behavioral models perform comparably to deep learning approaches when evaluated against LSTM predictions, highlighting the redundancy of complex architectures.

## Context
Understanding human randomisation is crucial for designing fair games and robust AI agents that do not exploit predictable behaviour. This work contributes to the broader effort to replace opaque black‑box systems with transparent models that preserve interpretability without sacrificing predictive accuracy.

## Implications
For game designers, these findings suggest focusing on simple behavioural rules rather than sophisticated neural networks to anticipate player choices. Practitioners in AI can adopt lightweight, explainable methods to achieve comparable results while maintaining transparency and trust.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07220v1)
