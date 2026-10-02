---
title: Reason in Style: Discovering and Controlling Style in Language Models
published: 2026-09-30T21:15:45Z
authors: Ioana Marinescu, Eric Karl Oermann, Kyunghyun Cho
url: http://arxiv.org/abs/2610.00724v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reason in Style: Discovering and Controlling Style in Language Models

## Abstract
Language models learn content and style jointly, making stylistic variation in their outputs difficult to identify and control. We study whether recurring styles in model responses can be discovered without supervision and explicitly controlled. We design an algorithm that learns to separate representations of content and style from language models' outputs and validate its effectiveness on math questions in a controlled setting. By applying this method to over 100K verified traces from nine distinct teacher models, we discover six recurring yet imbalanced styles. We then fine-tune smaller student models to follow these styles when explicitly conditioned on them, using importance weighting to balance the contribution of the styles represented in the corpus. This approach improves Pass@$k$ over standard fine-tuning on the same data across six math reasoning benchmarks, demonstrating that we can diversify the style of answers effectively. We confirm that this also results in strong correspondence between requested and realized styles. We find that style affects correctness: the probability of solving a problem depends on the style we condition on, and different problems benefit from different styles. In summary, our results show that stylistic variation in model-generated data can be discovered in an unsupervised way, and made explicit, providing a source of both control and improved reasoning performance.

## Metadata
- **Published**: 2026-09-30T21:15:45Z
- **Authors**: Ioana Marinescu, Eric Karl Oermann, Kyunghyun Cho
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.00724v1)