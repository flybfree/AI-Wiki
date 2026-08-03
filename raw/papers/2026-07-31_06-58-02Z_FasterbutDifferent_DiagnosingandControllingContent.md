---
title: Faster but Different: Diagnosing and Controlling Content Drift in Accelerated Multimodal Diffusion Language Models
published: 2026-07-31T06:58:02Z
authors: Yaoxuan Dou, Yang Shu
url: http://arxiv.org/abs/2607.29079v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Faster but Different: Diagnosing and Controlling Content Drift in Accelerated Multimodal Diffusion Language Models

## Abstract
Training-free acceleration makes diffusion-based multimodal large language models (dMLLMs) more deployable, but it may silently change generated content. We study this serving-time consistency problem on 300 real images, comparing Fast-dLLM outputs with the same model's unaccelerated outputs. Across the mild parallelism induced in our long-form setting (1.05--1.25 committed tokens per step), confidence-threshold tuning changes decoding behavior but not baseline agreement. State-refresh ablations and an image-swap intervention instead identify stale visual and generated-text states as contributors to drift. For the tested Fast-dLLM implementation, shortening the KV-cache refresh interval yields a monotonic speed--agreement frontier and near-exact agreement at a measured 1.3x speedup. The initial diagnosis also appears with dLLM-Cache and LaViDa, although dLLM-Cache recovers agreement only after both caches are tightened, which removes its speed advantage. Independent prompts and images reproduce the threshold-insensitivity and refresh recovery. A targeted audit finds genuine content substitution in half of 50 low-agreement pairs. In a separate blinded two-annotator evaluation, the pooled accelerated-minus-baseline factual-error difference is 0.00 (95% CI [-0.17,+0.17]); this sample detects no difference but does not establish factual equivalence. Finally, none of the tested adaptive or smoothed-refresh variants beats the fixed interval at matched compute. Our contribution is a paired diagnostic and an implementation-scoped consistency control, not an accuracy or safety guarantee.

## Metadata
- **Published**: 2026-07-31T06:58:02Z
- **Authors**: Yaoxuan Dou, Yang Shu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29079v1)