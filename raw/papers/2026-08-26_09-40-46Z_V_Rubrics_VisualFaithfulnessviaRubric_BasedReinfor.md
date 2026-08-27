---
title: V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning
published: 2026-08-26T09:40:46Z
authors: Shulin Tian, Minglun Li, Yuhao Dong, Hao Ding, Jiarui Yao, Haiwen Diao, Jingkang Yang, Hongyuan Zhu, Ziwei Liu
url: http://arxiv.org/abs/2608.25580v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# V-Rubrics: Visual Faithfulness via Rubric-Based Reinforcement Learning

## Abstract
Vision-language models can produce fluent answers that are insufficiently grounded in the visual evidence: a single unsupported object, chart value, or intermediate inference can undermine an otherwise plausible response. We argue that this is a credit-assignment failure in multimodal post-training. Scalar outcome rewards indicate whether an answer is acceptable, but do not identify which visual facts are grounded, which reasoning steps are valid, or which instruction constraints are missed. We introduce Visual Rubrics-Based Reinforcement Learning, which decomposes reference responses into atomic propositions and scores generated answers along Visual Faithfulness (VF), Reasoning Consistency (RC), and Instruction Following (IF). The resulting rubric items provide structured partial credit and localize rubric credit when supporting evidence spans are available. We first obtain an SFT checkpoint by fine-tuning Qwen3-VL-8B-Instruct on the public OpenMMReasoner-SFT-874K corpus, adapting OpenMMReasoner's cold-start data recipe. We construct V-Rubrics 50K, a 50,248-example training set from 17 visually grounded sources, by applying rule-based filters before deriving example difficulty from rejection-sampling scores and then annotating every example with Gemini-3-Pro under the same structured prompt and protocol. We train our model based on the same SFT checkpoint using component-wise, prefix-localized rubric credit. Experiments show that our rubricbased GRPO improves over both the shared SFT baseline and answer-only GRPO, with the largest gains on knowledge-oriented and visually grounded reasoning benchmarks. The results show rubrics as a useful reward abstraction for visual post-training.

## Metadata
- **Published**: 2026-08-26T09:40:46Z
- **Authors**: Shulin Tian, Minglun Li, Yuhao Dong, Hao Ding, Jiarui Yao, Haiwen Diao, Jingkang Yang, Hongyuan Zhu, Ziwei Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25580v1)