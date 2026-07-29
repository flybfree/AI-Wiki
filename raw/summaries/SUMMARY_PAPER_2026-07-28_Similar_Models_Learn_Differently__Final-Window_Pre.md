---
title: Similar Models Learn Differently: Final-Window Pretraining Shapes Post-Training Beyond SFT
url: http://arxiv.org/abs/2607.25063v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_20-46-29Z_SimilarModelsLearnDifferently_Final_WindowPretrain.md
generated_at: 2026-07-28 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how the final window of pretraining influences a model's behavior after supervised fine-tuning, showing that checkpoints with identical SFT performance differ in their responses to subsequent alignment training because they were trained on different last data sources. It demonstrates that safety text appearing late in pretraining protects against harmful refusals more effectively than earlier or other sources.

## Key Takeaways
- The same post-SFT checkpoint can lead to divergent outcomes after further training depending on the content of its final pretraining window, which is often overlooked when evaluating models.
- Models trained with safety text last exhibit stronger refusal behavior and retain it better during reinforcement learning compared to those trained earlier or without such data.
- Evaluation should consider not only post-SFT performance but also what the model was trained on in its last window, as this shapes alignment responses.

## Context
This research highlights a hidden bias in pretraining that affects downstream alignment strategies. By focusing solely on SFT results, practitioners may misjudge which checkpoint is more suitable for safety or capability enhancements. The findings align with growing concerns about the cumulative effects of data ordering and content in large language model training pipelines.

## Implications
For developers, reporting the last window’s source is essential to guide alignment decisions. It encourages a more holistic view of model readiness, reducing the risk of deploying models that lack robust safety behaviors despite good SFT scores. This could shift industry standards toward transparent pretraining audits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25063v1)
