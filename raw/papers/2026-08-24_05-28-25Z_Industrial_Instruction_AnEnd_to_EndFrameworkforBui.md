---
title: Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning and Benchmark Datasets from Industrial Technical Reports
published: 2026-08-24T05:28:25Z
authors: Parsa Bakhtiari, Hassan Bashiri, Alireza Khalilipour, Masoud Nasiripour, Moharram Challenger
url: http://arxiv.org/abs/2608.22817v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Industrial-Instruction: An End-to-End Framework for Building Instruction-Tuning and Benchmark Datasets from Industrial Technical Reports

## Abstract
Industrial technical reports contain high-value knowledge for maintenance, troubleshooting, and product engineering, but their heterogeneous structure (dense prose, specifications, tables) makes them difficult to index and reason over with standard retrieval and QA pipelines, and no public instruction-tuning or benchmark datasets are built from such documents. We address this gap with Industrial-Instruction, contributing (i) two open QA datasets built from real industrial technical reports and (ii) the end-to-end pipeline that produces them. Using 906 public Panasonic documents (7,525 pages), we apply layout-aware extraction, build a semantic retrieval index, and synthesize multiple-choice QA grounded in retrieved evidence under five query-document relationships (irrelevant retrieval, single-/multi-document support, single-/multi-document answer). After filtering an initial 23.9k generated samples, each dataset provides approximately 13.6k QA pairs with source documents and a held-out benchmark split. Fine-tuning small open LLMs (under 10B parameters) improves Set-Match Accuracy from 28.5% to 42.0% and F1 from 46.6% to 63.5% on the Panasonic benchmark. We release two parallel versions built by the same pipeline: one generated with the open-weight Qwen3-30B-A3B-Instruct model and one with the closed, API-based Claude-Opus-4.6 model, enabling a direct comparison of open- versus frontier-model data generation. The Claude-Opus-4.6 dataset yields a cleaner raw corpus and larger fine-tuning gains, at roughly two orders of magnitude higher cost. MMLU evaluation shows models trained on the Claude-Opus-4.6 data retain essentially all general knowledge, versus a small but measurable forgetting effect for the Qwen-generated data. Together, these datasets and pipeline offer a practical, reproducible path toward scalable industrial benchmarks and training data from real-world documentation.

## Metadata
- **Published**: 2026-08-24T05:28:25Z
- **Authors**: Parsa Bakhtiari, Hassan Bashiri, Alireza Khalilipour, Masoud Nasiripour, Moharram Challenger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22817v1)