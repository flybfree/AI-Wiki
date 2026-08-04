---
title: MedUPS: Towards Diagnostic Assistance in Uncommon Medical Cases with Large Language Models
published: 2026-08-02T05:27:21Z
authors: Ofir Ben Shoham, Oriel Perets, Nir Grinberg, Nadav Rappoport
url: http://arxiv.org/abs/2608.01012v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedUPS: Towards Diagnostic Assistance in Uncommon Medical Cases with Large Language Models

## Abstract
Uncommon and off-guideline cases are difficult for clinical decision support, because physicians must make a series of management decisions under diagnostic uncertainty and rarely see the full case at once. Most large language model (LLM) benchmarks for medicine score only the final diagnosis, yet much of clinical care turns on the next appropriate action: the next test to order, the imaging study to obtain, the specialist to involve, or the differential to pursue. We introduce MedUPSQA, a dataset of 21,874 mid-stream clinical decision points built from 5,535 real case reports, and MedUPS, an alignment framework that supervises models on these intermediate decisions as they unfold along a patient's trajectory. We segment free-text case presentations into chronologically ordered, accumulating clinical chunks and align models to predict the next step with reinforcement learning (GRPO), using an external LLM-as-a-Judge reward. This objective mirrors how clinicians actually meet patients, reasoning forward from accumulating evidence toward the next decision, rather than committing to a final label. Across three backbones, mid-stream alignment raises next-step accuracy from 55.2 to 66.7 for Qwen3.6-27B, from 47.2 to 57.8 for Qwen3.5-9B, and from 37.8 to 44.4 for HuatuoGPT-3-8B, with 95% CI. In several model scales we test the objective improves accuracy more than scale, with smaller models surpassing larger, frontier models we evaluate. We further train supervised fine-tuning (SFT) baselines on the mid-stream task, SFT improves all backbones above base, indicating the target framwork carries signal independently of the optimizer. We release the dataset, code, and aligned checkpoints.

## Metadata
- **Published**: 2026-08-02T05:27:21Z
- **Authors**: Ofir Ben Shoham, Oriel Perets, Nir Grinberg, Nadav Rappoport
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01012v1)