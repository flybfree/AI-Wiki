---
title: Auditing MCQA Benchmarks through Probability Landscapes
published: 2026-08-31T07:28:31Z
authors: Minsoo Song, Chanjun Park
url: http://arxiv.org/abs/2608.30372v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Auditing MCQA Benchmarks through Probability Landscapes

## Abstract
As Large Language Models rapidly advance, performance on standard multiple-choice question answering (MCQA) benchmarks is reaching saturation. While the community has responded by developing increasingly difficult datasets, validating question quality and filtering flawed items remains a labor-intensive process. To provide a scalable diagnostic approach, we propose a two-component probabilistic framework for auditing MCQA benchmarks using model output distributions. First, for benchmark-level analysis, we characterize the probability landscape using the top prediction probability ($P_{top1}$) and normalized residual entropy ($H_{norm}$), summarized globally by Mean Pairwise Distance (MPD). Second, for item-level diagnostics, we introduce noise injection to reduce meaningful distractor competition, enabling us to flag candidate items for targeted human review and categorize residual failure patterns. Across four MCQA benchmarks, our landscape analysis reveals benchmark-level differences in model confidence and residual option competition. Concurrently, our noise-injection method flags potentially actionable item-level issues, showing alignment with expert error annotations from MMLU-Redux. These results suggest that our probability-based framework provides a lightweight audit lens for comparing macro-level benchmark structure and prioritizing individual items for targeted human review.

## Metadata
- **Published**: 2026-08-31T07:28:31Z
- **Authors**: Minsoo Song, Chanjun Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30372v1)