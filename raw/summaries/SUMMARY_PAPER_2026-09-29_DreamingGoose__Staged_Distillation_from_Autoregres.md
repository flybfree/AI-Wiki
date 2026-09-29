---
title: DreamingGoose: Staged Distillation from Autoregressive Transformers to Bidirectional Recurrent Diffusion Language Models
url: http://arxiv.org/abs/2609.34253v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_03-57-11Z_DreamingGoose_StagedDistillationfromAutoregressive.md
generated_at: 2026-09-29 02:14
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates converting large pretrained autoregressive Transformers into attention-free, bidirectional recurrent diffusion models through a three-stage distillation pipeline. The authors demonstrate that while basic language modeling capabilities transfer partially within distribution, in-context retrieval fails completely without intervention and requires a dynamic curriculum to recover, revealing fundamental architectural coverage limits rather than simple memorization failures.

## Key Takeaways
- Converting Qwen3 teachers (1.7B and 8B) into bidirectional recurrent diffusion students shows that language modeling transfers only partially and in-distribution, while multi-query in-context retrieval drops to zero and cannot be restored by diffusion pretraining alone.
- A dynamic retrieval curriculum that advances the key-value query gap only when accuracy exceeds a threshold successfully restores recall across real text and scales to 8B models, whereas fixed-step schedules frequently truncate learning due to abrupt, seed-dependent capability emergence.
- Every model that achieves retrieval performance consistently scores zero on tokens never encountered during retrieval episodes, indicating the architecture suffers from a structural coverage limit rather than memorizing specific key-value bindings.

## Context
The massive computational investments in autoregressive Transformers have intensified interest in alternative architectures like recurrent and diffusion-based language models for improved parallelization and efficiency. This work addresses a critical gap in cross-architecture distillation by simultaneously transforming both the model structure and training objective, providing empirical evidence on which capabilities survive such drastic architectural shifts and why standard conversion methods fall short.

## Implications
Practitioners seeking to repurpose existing Transformer investments into more efficient recurrent or diffusion frameworks must anticipate severe retrieval degradation and implement adaptive, threshold-driven training curricula rather than relying on static distillation schedules. These findings suggest that future hybrid architectures should explicitly address coverage limitations in their design, potentially guiding the development of robust, compute-efficient language models that retain complex reasoning capabilities without prohibitive retraining costs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34253v1)
