---
title: The Internal Anatomy of Strategic Choice in Large Language Models
url: http://arxiv.org/abs/2609.07478v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-07_13-34-30Z_TheInternalAnatomyofStrategicChoiceinLargeLanguage.md
generated_at: 2026-09-08 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how large language models make strategic choices in ordinal $2\times2$ games by tracing activations from prompt incentives to final decisions. It finds that dense and mixture‑of‑experts models behave differently, with some failing to translate incentive into choice while others do so effectively.

## Key Takeaways
- Dense models mirrored the unadjusted human decline observed as game complexity increased.  
- Incentive and choice were detectable in every model, yet they differed on whether the incentive actually reached the decision point.  
- Fixed decision cues could be distinguished internally but altered choices selectively depending on the model’s computation path.

## Context
Understanding the internal mechanics of strategic reasoning in LLMs is crucial for advancing research into alignment and explainability. This work highlights that behavior can persist while computational pathways diverge, a nuance central to future AI safety efforts.

## Implications
For practitioners, mapping incentive‑to‑choice pathways helps design models that better align with human preferences without sacrificing performance. It also informs industry approaches to model interpretability, enabling targeted interventions where internal computation misaligns with external behavior.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07478v1)
