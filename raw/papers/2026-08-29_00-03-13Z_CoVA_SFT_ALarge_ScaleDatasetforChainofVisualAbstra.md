---
title: CoVA-SFT: A Large-Scale Dataset for Chain of Visual Abstractions
published: 2026-08-29T00:03:13Z
authors: Tsung-Han Wu, Heekyung Lee, Anya Ji, Haoming Chen, Trevor Darrell, Joseph E. Gonzalez, David M. Chan
url: http://arxiv.org/abs/2608.28958v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoVA-SFT: A Large-Scale Dataset for Chain of Visual Abstractions

## Abstract
Chain-of-thought (CoT) reasoning has dramatically improved large language models (LLMs) by allowing them to decompose problems into intermediate steps. While CoT is widely effective for linguistic tasks, text-only CoT forces models to serialize visual problems into awkward prose. Although architectural solutions exist to process visual inputs, the community lacks a massive, multi-step, self-corrected dataset to teach models how to build and maintain internal visual workspaces when solving purely textual reasoning problems. To address this limitation, we introduce CoVA-SFT, a highly structured corpus of 51.9K samples containing over 222K multimodal reasoning steps across 5 distinct layout families and 17 complex tasks, and CoVA-Bench, a companion benchmark of 1,700 held-out test samples spanning the same tasks for reproducible evaluation. By providing explicit rationale formulations, agentic renderings, and verification loops, CoVA-SFT teaches multimodal language models to interleave text and visual abstractions. We validate the dataset by demonstrating that models fine-tuned on CoVA-SFT outperform all interleaved CoT baselines by more than 2x on average on CoVA-Bench, though they still fall short of strong text-only CoT baselines, highlighting open challenges for future work.

## Metadata
- **Published**: 2026-08-29T00:03:13Z
- **Authors**: Tsung-Han Wu, Heekyung Lee, Anya Ji, Haoming Chen, Trevor Darrell, Joseph E. Gonzalez, David M. Chan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28958v1)