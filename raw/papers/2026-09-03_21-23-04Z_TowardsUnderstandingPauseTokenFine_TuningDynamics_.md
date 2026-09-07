---
title: Towards Understanding Pause Token Fine-Tuning Dynamics: A Mode Retention Perspective
published: 2026-09-03T21:23:04Z
authors: Jaehyeon Kim, Suhwan Kim, Nakyung Lee, Yeongoon Kim, Jimin Seo, Giho Lee, Jungwoo Lee
url: http://arxiv.org/abs/2609.04489v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Understanding Pause Token Fine-Tuning Dynamics: A Mode Retention Perspective

## Abstract
Pause-token methods improve LLM reasoning by inserting special tokens into sequences. Prior work explains these gains through computational expressivity. However, there is relatively little investigation into the training dynamics of pause tokens. We explore how pause tokens reshape the training dynamics of fine-tuning. Two controlled pilots expose distinct asymmetries. On a synthetic continual-learning task, masked pauses overwrite a previously-learned distribution roughly 4x less at matched final adaptation (H1, mode retention); on a synthetic math-reasoning probe, the boundary-adjacent token comes to encode substantially more downstream-step information (H2, non-myopic compression). We formalize a training rule consistent with both - Masked Boundary Pause (MBP), pause tokens placed at reasoning-step boundaries with their loss masked. Across 1B-8B Qwen and Llama models, MBP consistently improves reasoning, achieving gains of up to 6 points on math and 2.5 points on code, while preserving general language understanding abilities. We further demonstrate that this mode-preserving strategy extend gains to GRPO. These results recast pause tokens as a training-dynamics intervention on the retention-adaptation trade-off, rather than merely an inference-time computation device.

## Metadata
- **Published**: 2026-09-03T21:23:04Z
- **Authors**: Jaehyeon Kim, Suhwan Kim, Nakyung Lee, Yeongoon Kim, Jimin Seo, Giho Lee, Jungwoo Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04489v1)