---
title: Replacing Training with Memory: Listwise Selection for Text-to-SQL
published: 2026-09-01T07:35:00Z
authors: Yeonseok Jeong, Soyoung Yoon, Seongjun Lee, Seung-won Hwang
url: http://arxiv.org/abs/2609.00834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Replacing Training with Memory: Listwise Selection for Text-to-SQL

## Abstract
Modern Text-to-SQL systems often follow generate-execute-select pipelines, generating multiple candidate queries then selecting the best one. Listwise selection, by jointly comparing multiple candidates, has been widely adopted, but fine-tuning listwise selectors is costly. We thus propose a fine-tuning-free listwise selector. We replace two major fine-tuning objectives with inference-time strategies: (1) learning selection criteria as ordering and (2) mitigating positional bias. First, we build reusable structured memories instead of learning selection behavior as model parameters. Given a question, MaP-SQL retrieves memories distilled from training data that encode how natural language maps to schema elements, SQL operations, and expected outputs. These memories serve as explicit decision criteria for evaluating candidates in a listwise manner. Second, to mitigate ordering bias of listwise selectors, we aggregate rankings across multiple input permutations, with inference cost optimized by execution results and pointwise scoring. Our approach improves selection accuracy while maintaining efficiency and compatibility with existing large language models. Across Text-to-SQL benchmarks, it produces more stable selection without fine-tuning and fewer unnecessary comparisons than existing methods. On BIRD-dev, it outperforms the previous state-of-the-art selector-based method R^3-SQL by 2.02 execution accuracy points on average using the same candidate sets, with 2.92x fewer tokens.

## Metadata
- **Published**: 2026-09-01T07:35:00Z
- **Authors**: Yeonseok Jeong, Soyoung Yoon, Seongjun Lee, Seung-won Hwang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00834v1)