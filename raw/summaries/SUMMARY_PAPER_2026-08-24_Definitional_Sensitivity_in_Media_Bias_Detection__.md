---
title: Definitional Sensitivity in Media Bias Detection: A Multi-Definition Dataset and Benchmark
url: http://arxiv.org/abs/2608.23095v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_11-02-52Z_DefinitionalSensitivityinMediaBiasDetection_AMulti.md
generated_at: 2026-08-24 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how different definitions of media bias influence the way humans and large language models annotate news articles. By comparing ratings across four bias categories under varied conceptual framings, the authors reveal that definition choice dramatically shapes annotation outcomes, especially for LLMs. The study introduces MUDD, a dataset designed to expose definitional sensitivity in bias detection.

## Key Takeaways
- Conceptual framing of definitions causes significant shifts in human and LLM ratings, indicating that changing the core meaning of a term alters perceived bias.
- Construct‑preserving elaboration—adding descriptive details without altering the central concept—does not produce similar annotation changes across participants or models.
- The effect is stronger for LLMs than for humans, suggesting that model training may amplify sensitivity to definitional ambiguity.

## Context
Media bias detection is a core task in AI fairness research, yet prior work often assumes uniform definitions across datasets. This gap can lead to misleading comparisons of model performance and to the deployment of biased or inconsistent classifiers. The paper contributes by empirically demonstrating that definition matters, prompting a reevaluation of how bias labels are constructed.

## Implications
For practitioners, this highlights the need for explicit, shared definitions when creating annotation protocols and prompt templates. Ignoring definitional sensitivity may propagate errors into downstream classification systems, affecting both research reproducibility and real‑world media analysis tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23095v1)
