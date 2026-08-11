---
title: An Agentic AI Framework Overcomes Fundamental Limitations of Large Language Models for Glaucoma Detection from Fundus Photography
published: 2026-08-07T17:33:12Z
authors: Jalil Jalili, Hossein Taghizad, Anuwat Jiravarnsirikul, Christopher Bowd, Akram Belghith, Raheleh Kafieh, Christopher A. Girkin, Sally L. Baxter, Robert N. Weinreb, Linda M. Zangwill, Mark Christopher
url: http://arxiv.org/abs/2608.07651v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Agentic AI Framework Overcomes Fundamental Limitations of Large Language Models for Glaucoma Detection from Fundus Photography

## Abstract
Large language models (LLMs) show promise in medical image interpretation but suffer from hallucination, limited accuracy, and run-to-run inconsistency. We developed and validated an agentic AI framework integrating LLMs with specialized deep learning tools for glaucoma detection from fundus photography. The workflow had three steps: (1) LLM initial assessment; (2) function calling to invoke specialized tools for image quality (QAModel, FundaQ-8), glaucoma classification (SwinV2-Tiny), and optic disc/cup segmentation (SegFormer-B0); and (3) LLM reflection integrating the initial impression with tool outputs. Two LLMs (Gemini 2.5 Flash, GPT-5.4 mini) were evaluated on two public datasets (ORIGA, n=100; RIM-ONE-v3, n=100) under uncropped and cropped fields of view; all images were independently graded by a masked fellowship-trained glaucoma specialist. The agentic workflow improved classification accuracy by 16 to 47 percentage points across all conditions, reaching within 6 points of the specialist; on RIM-ONE-v3 the best configurations matched the specialist accuracy of 88%. LLM-alone approaches failed in two ways: GPT-5.4 mini showed positive bias (sensitivity 95-100%, specificity 0-5%), while Gemini 2.5 Flash varied stochastically between runs; the agentic workflow corrected both. Cup-to-disc ratio error fell 15-50% (MAE 0.156-0.228 to 0.104-0.132), and correlation with specialist grading rose from weak (r=0.12-0.39) to moderate-strong (r=0.59-0.84). Run-to-run consistency rose from near-random (kappa as low as -0.01) to near-perfect (kappa up to 0.96). Integrating LLMs with specialized tools addressed key limitations of LLM-alone approaches, including over-diagnosis and run-to-run variability. Gains held for both LLMs, suggesting generalizability across backbones, and may signal a shift from monolithic models toward orchestrated multi-agent systems in medical AI.

## Metadata
- **Published**: 2026-08-07T17:33:12Z
- **Authors**: Jalil Jalili, Hossein Taghizad, Anuwat Jiravarnsirikul, Christopher Bowd, Akram Belghith, Raheleh Kafieh, Christopher A. Girkin, Sally L. Baxter, Robert N. Weinreb, Linda M. Zangwill, Mark Christopher
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07651v1)