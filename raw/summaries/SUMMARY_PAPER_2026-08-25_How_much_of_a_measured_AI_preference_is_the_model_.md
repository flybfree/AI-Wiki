---
title: How much of a measured AI preference is the model, and how much is the instrument?
url: http://arxiv.org/abs/2608.23641v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_02-23-11Z_HowmuchofameasuredAIpreferenceisthemodel_andhowmuc.md
generated_at: 2026-08-25 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how much of a model’s reported preference is due to the model itself versus the instrument used to elicit it, using eight models and fifteen welfare outcomes across five prompt formats. It finds that preferences are generally consistent across instruments (generalisability coefficient 0.348) but vary significantly when any one instrument or model is removed.

## Key Takeaways
- The generalisability coefficient of 0.348 indicates limited cross‑instrument agreement, requiring about 38 instruments to reach a reliable estimate.
- Removing any single instrument, model, or the four probability‑based outcomes still leaves the preference estimate between 0.777 and 0.934, well above the null threshold of 0.365.
- The high confidence (87.6 %) persists even after eliminating all instruments that vary on non‑intensity scales.

## Context
This work addresses a persistent problem in AI welfare research where different elicitation methods produce divergent results, undermining trust in preference measurements. By isolating the instrument variable while keeping outcomes and models constant, the study provides a more reliable estimate of model preferences.

## Implications
Practitioners should treat preference scores as noisy signals rather than definitive measures, designing robust evaluation pipelines that account for methodological variability. The findings suggest that improving instrument consistency is crucial before drawing conclusions about model welfare.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23641v1)
