---
title: FailBench: How Reliable are VLMs at Judging Robot Task Success?
published: 2026-09-03T09:58:55Z
authors: Zaruhi Navasardyan, Tatul Danielyan, Hrant Davtyan
url: http://arxiv.org/abs/2609.03611v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FailBench: How Reliable are VLMs at Judging Robot Task Success?

## Abstract
Vision-Language Models (VLMs) are increasingly used to evaluate robot manipulation outcomes, but existing benchmarks offer limited evidence of cross-domain generalization. We introduce FailBench, a benchmark for robot failure detection comprising 2,197 manipulation attempts across 14 public sources (12 real-world, 2 simulated). In FailBench, 75% of failures occur naturally, and six real-world sources come from non-failure-detection datasets. Evaluating 13 VLM-based detectors, we find the best model achieves only 0.77 mean balanced accuracy. Notably, models fine-tuned for failure detection consistently underperform general-purpose VLMs and their own pretrained baselines. Performance depends heavily on required visual evidence: models approach saturation when outcomes depend on observable object motion, but degrade to near-chance (<0.60 balanced accuracy) on contact-intensive assembly tasks. Error analysis reveals a systematic bias toward predicting success under ambiguous evidence, which persists even with increased reasoning effort. Finally, we show that input-level intervention--spatially localizing and cropping outcome-relevant regions--improves the top detector by 2.4 percentage points without extra training.

## Metadata
- **Published**: 2026-09-03T09:58:55Z
- **Authors**: Zaruhi Navasardyan, Tatul Danielyan, Hrant Davtyan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03611v1)