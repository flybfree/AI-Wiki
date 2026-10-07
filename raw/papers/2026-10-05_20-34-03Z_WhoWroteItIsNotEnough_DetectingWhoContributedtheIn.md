---
title: Who Wrote It Is Not Enough: Detecting Who Contributed the Insight
published: 2026-10-05T20:34:03Z
authors: Zhuoyang Zou, Abolfazl Ansari, Jiaxi Yang, Delvin Ce Zhang, Qian Chen, Dongwon Lee, Wenpeng Yin
url: http://arxiv.org/abs/2610.07365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Wrote It Is Not Enough: Detecting Who Contributed the Insight

## Abstract
As LLMs increasingly assist scientific writing and peer review, detecting who wrote the text is no longer sufficient: we need to determine who contributed the underlying insight. We introduce Insight Provenance, the task of identifying whether a review insight originates from a human, an LLM, or their hybrid contribution. We construct InsightProv-v0 from 4,057 scientific papers and 12,660 human reviews, simulating different levels of LLM involvement with GPT-4o, Gemini, and DeepSeek and annotating provenance at the sentence level. We show that strong performance on raw data can be misleading, as models exploit linguistic and textual-authorship shortcuts that degrade substantially under progressively debiased evaluation. We therefore propose a two-stage adversarial framework that suppresses shortcut signals while preserving provenance-relevant information. Beyond detection, extensive analyses reveal what makes intellectual authorship identifiable: paper grounding and neighboring review context provide complementary provenance signals, while human, hybrid, and AI insights systematically differ in their information sources and failure modes. Most strikingly, AI insights predominantly remain close to generic or paper-provided information, whereas human insights more often introduce external knowledge and independent judgment. These findings suggest that while wording can be rewritten by an LLM, the provenance of an idea leaves a deeper and more persistent signal.

## Metadata
- **Published**: 2026-10-05T20:34:03Z
- **Authors**: Zhuoyang Zou, Abolfazl Ansari, Jiaxi Yang, Delvin Ce Zhang, Qian Chen, Dongwon Lee, Wenpeng Yin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07365v1)