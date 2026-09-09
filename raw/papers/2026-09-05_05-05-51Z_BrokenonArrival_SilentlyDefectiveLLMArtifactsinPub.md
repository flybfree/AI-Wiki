---
title: Broken on Arrival: Silently Defective LLM Artifacts in Public Model Registries and How to Catch Them
published: 2026-09-05T05:05:51Z
authors: Aditi Patodiya
url: http://arxiv.org/abs/2609.05881v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Broken on Arrival: Silently Defective LLM Artifacts in Public Model Registries and How to Catch Them

## Abstract
Developers increasingly run large language models locally by pulling quantized GGUF artifacts from public registries, yet nothing in the distribution pipeline functionally tests these conversions before they reach users. We executed 327 quantized code-capable model artifacts: 305 from the official Ollama library, spanning 15 model lines at every eligible quantization level at or under 8 GB, and 22 from the most-downloaded community repositories on HuggingFace. Each ran a 15-task smoke suite calibrated so that healthy artifacts pass while a known-broken one fails; suspects then faced full 164-task evaluation, a second inference backend, an independent distributor's conversion of the same model and quantization as referee, and, for community files, re-testing under the artifact's own template. The official library carries five silently defective artifacts, a batch of four Qwen2.5-Coder-3B conversions and one phi3.5-mini conversion, that solve zero of 164 tasks and zero of the smoke suite on both backends while independent conversions of the same models work: 1.6% of official artifacts, 2 of 29 model-and-size conversion groups. The adjudication chain cleared small-model artifacts that a naive threshold would condemn as broken when they are merely collapsed by extreme quantization, and it exposed two older community conversions that degrade badly on CUDA yet pass on Metal: not defective files but backend-dependent failures, a third phenomenon no registry currently tests for. Two confirmed defects produce output whose surface statistics sit inside the healthy range, invisible to any low-noise heuristic short of execution. We release the audit dataset, the quantcheck acceptance-testing tool, and disclosure reports for every confirmed defect (https://github.com/aditi-p31/quantcheck), and argue that model registries need the acceptance gate that package registries already run.

## Metadata
- **Published**: 2026-09-05T05:05:51Z
- **Authors**: Aditi Patodiya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05881v1)