---
title: A Composable Evaluation System for Reproducible Omni-Modal Foundation Model Evaluation
published: 2026-09-01T14:37:57Z
authors: Hodong Lee, Sanghee Park, Dohoon Ryu, Jungwhan Kim, Junyeob Kim, Soyoon Kim, Geewook Kim
url: http://arxiv.org/abs/2609.01315v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Composable Evaluation System for Reproducible Omni-Modal Foundation Model Evaluation

## Abstract
Building an omni-modal foundation model means evaluating it across text, image, video, and audio. Excellent evaluation toolkits exist for each modality, but their inference engines, prompt conventions, and metric implementations are mutually incompatible, so practitioners end up maintaining separate environments for every toolchain and still struggle to compare results across them. OmniEvaluator grew out of this need in our own model development: rather than reimplementing benchmarks, it connects existing inference engines and curated evaluation libraries at a higher level, exposing four inference backends, four evaluation frameworks, and over a thousand benchmarks through a single interface. Every run is recorded as an artifact capturing the full configuration for exact reproduction, and results flow into a shared dashboard for cross-model comparison. A federated mode shares GPU inference servers across concurrent evaluations, and a built-in verifier, small enough to run on CPU, keeps its score stable across engines and prompts where rule-based scoring fluctuates under configuration mismatch, matching cost-efficient commercial LLM judges without their recurring API cost. The system, demo video, and dashboard are publicly available. (https://github.com/naver-ai/omni-evaluator)

## Metadata
- **Published**: 2026-09-01T14:37:57Z
- **Authors**: Hodong Lee, Sanghee Park, Dohoon Ryu, Jungwhan Kim, Junyeob Kim, Soyoon Kim, Geewook Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01315v1)