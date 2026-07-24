---
title: OpenLanguageModel: Readable and Composable Small-Language-Model Pretraining for Education and Research
published: 2026-07-18T06:55:18Z
authors: Tavish Mankash, Vardhaman Kalloli, Keshava Prasad, Deepan Muthirayan
url: http://arxiv.org/abs/2607.16669v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OpenLanguageModel: Readable and Composable Small-Language-Model Pretraining for Education and Research

## Abstract
OpenLanguageModel (OLM) is an open-source PyTorch library for building and pretraining small language models while keeping their machinery visible. In OLM, model code reads like the architecture: components are ordinary modules, while Block, Residual, Repeat, and Parallel describe how they are wired. The resulting model can move unchanged from a teaching notebook to a complete pretraining run or a research ablation. OLM connects this readable model layer to tokenizers, local and streaming datasets, optimization, mixed precision, callbacks, checkpoints, and hardware-aware CPU, single-GPU, and single-node multi-GPU execution. We demonstrate the full path by tracing GPT-2 from diagram to code, launching a FineWeb-Edu training script, replacing one attention component, and letting AutoTrainer configure the available machine. The package includes 27 presets across nine familiar model families and documentation that progresses from LM fundamentals to architecture research. Validation shows close agreement with independent reference implementations, 90.6% four-GPU weak-scaling efficiency for a 348M-parameter workload, compact architecture edits, and positive early usability results. OLM is MIT-licensed and available through PyPI, GitHub, and its documentation site.

## Metadata
- **Published**: 2026-07-18T06:55:18Z
- **Authors**: Tavish Mankash, Vardhaman Kalloli, Keshava Prasad, Deepan Muthirayan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.16669v1)