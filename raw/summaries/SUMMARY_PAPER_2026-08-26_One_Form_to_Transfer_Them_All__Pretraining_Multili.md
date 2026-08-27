---
title: One Form to Transfer Them All: Pretraining Multilingual Language Models Beyond Native Orthography
url: http://arxiv.org/abs/2608.25904v1
type: paper-summary
date: 2026-08-26
source_paper: 2026-08-26_15-23-18Z_OneFormtoTransferThemAll_PretrainingMultilingualLa.md
generated_at: 2026-08-26 20:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how multilingual language models handle different writing systems by comparing orthographic text, IPA transcription, and romanization as pretraining inputs. It finds that romanized data provides the strongest cross‑lingual transfer, especially in larger models, and that fine‑tuning a text‑pretrained model on romanized data can hurt performance for languages already covered.

## Key Takeaways
- Romanization yields the strongest cross‑lingual transfer across all model sizes, outperforming both orthographic text and IPA transcription in downstream tasks on seen and unseen languages.  
- The advantage of romanization over text widens as model scale increases, indicating that larger models benefit more from script‑neutral representation.  
- Fine‑tuning a text‑pretrained model on romanized data can actually degrade performance for languages already present in the base model, though it offers marginal help when the model lacks any script coverage.

## Context
Multilingual language models often fail to transfer knowledge between scripts because they are trained on raw orthographic sequences that encode script differences. This systematic comparison provides a clear design guideline for handling typologically diverse datasets.

## Implications
For practitioners developing global AI systems, adopting romanization as a core pretraining strategy can improve performance across languages with different writing systems without requiring separate model architectures. It also reduces the need for costly script‑specific fine‑tuning pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.25904v1)
