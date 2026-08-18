---
title: DA-RAC: Distance-Aware Calibration of LLM Judges for Trustworthy AI Auditing
published: 2026-08-15T00:29:25Z
authors: Cheng Wu, Vishal Anand, Jaya Krishna Mandivarapu, Xiya Liu, Rui Zhuang
url: http://arxiv.org/abs/2608.14950v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DA-RAC: Distance-Aware Calibration of LLM Judges for Trustworthy AI Auditing

## Abstract
Generative AI systems are increasingly producing real-world artifacts, however their efficacy and validity are often evaluated via context-free LLM-scoring. These judges can be miscalibrated by irrelevant in-context reference examples, creating false confidence and allowing low-quality or harmful outputs to pass evaluation. We study this failure mode as context-induced miscalibration and introduce DA-RAC, a distance-aware reference-anchored calibration method for LLM judges. DA-RAC retrieves semantically and structurally similar labeled anchors for each judgement scenario, weights them by distance, and exposes neighborhood difficulty as a calibration and triage signal. On multi-run LLM-judge evaluation benchmarks, it improves calibration and reduces false-pass risk relative to zero-shot, chain-of-thought evaluation, and static-anchor baselines. Mechanistic analysis shows that judge scores vary systematically with anchor distance, while static references can induce misleading decision boundaries. Thus LLM-judgement requires not only better models, but also calibrated, auditable reference selection, especially when automated evaluation is used to support high-impact AI generated artifacts. Judgments should be grounded in relevant, inspectable, and contestable interpretive artifacts.

## Metadata
- **Published**: 2026-08-15T00:29:25Z
- **Authors**: Cheng Wu, Vishal Anand, Jaya Krishna Mandivarapu, Xiya Liu, Rui Zhuang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14950v1)