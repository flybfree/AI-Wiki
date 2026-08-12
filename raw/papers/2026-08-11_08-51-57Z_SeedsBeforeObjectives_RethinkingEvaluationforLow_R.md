---
title: Seeds Before Objectives: Rethinking Evaluation for Low-Resource Garhwali ASR
published: 2026-08-11T08:51:57Z
authors: Karamvir Singh Batra, Prathamjyot Singh, Ashima Sood, Jasmeet Singh, Sahil Sharma
url: http://arxiv.org/abs/2608.10670v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Seeds Before Objectives: Rethinking Evaluation for Low-Resource Garhwali ASR

## Abstract
At corpus sizes typical of low-resource dialects, single-run comparisons can yield gains that do not replicate. We show this for Garhwali, an under-resourced Indo-Aryan language of the central Himalaya, building the first reproducible multi-seed ASR benchmark on the official VAANI splits, with per-seed outputs and significance testing. Re-examining plausible gains, we find them fragile: neither Focal CTC nor a matra-weighted objective beats standard CTC under seed-level testing, the matra objective fails to cut even its targeted errors, and Hindi-to-Garhwali transfer gives no gain over direct fine-tuning. What holds up is mundane: w2v-BERT 2.0 with standard CTC reaches 47.0% WER over five seeds, beating the larger MMS-1B and comparable models; pretraining design, not parameter count, drives performance, and speed augmentation gives a small, largely consistent gain. Multi-seed evaluation on official splits separates real gains from seed noise.

## Metadata
- **Published**: 2026-08-11T08:51:57Z
- **Authors**: Karamvir Singh Batra, Prathamjyot Singh, Ashima Sood, Jasmeet Singh, Sahil Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10670v1)