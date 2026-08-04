---
title: CraftAlign: Feature-Grounded Evaluation and Revision Guidance for AI Stories
published: 2026-08-02T16:57:05Z
authors: Yang Yang, Boyun Xu, Shaofeng Liang, Yun Han, Zining Zhong, Songning Lai, Kaishen Yuan, Yutao Yue
url: http://arxiv.org/abs/2608.01377v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CraftAlign: Feature-Grounded Evaluation and Revision Guidance for AI Stories

## Abstract
Large language models can now generate fluent and complete stories, yet many outputs still feel formulaic and unnatural because of cliches, over-explanation, linear causal progression, and stereotyped endings, an immediately recognizable AI flavor. Existing detection and evaluation methods often stop at source labels or holistic scores, while revision methods typically target predefined issues through localized edits, limiting their ability to support multiple plausible revision strategies or guide story-wide changes in information release, causal organization, and ending treatment. We introduce CraftAlign, a framework that aligns AI stories with the craft of human storytelling by both assessing Human/AI writing patterns and providing revision guidance. CraftAlign comprises two learned modules and an inference-time guidance pipeline. A feature estimator built on Qwen3.5-9B predicts 304 explicit writing features spanning style and narrative. A class-conditional energy model scores the resulting feature configuration against Human and AI writing patterns, conditioning on the original writing prompt when available. At inference time, CraftAlign applies schema-valid structured perturbations, selects changes that move the feature configuration toward the Human writing pattern, and converts them into natural-language guidance for a separate editor to rewrite the full story. Experiments show that CraftAlign accurately distinguishes Human and AI writing patterns and that its guidance outperforms revision baselines across editors and in a human study.

## Metadata
- **Published**: 2026-08-02T16:57:05Z
- **Authors**: Yang Yang, Boyun Xu, Shaofeng Liang, Yun Han, Zining Zhong, Songning Lai, Kaishen Yuan, Yutao Yue
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01377v1)