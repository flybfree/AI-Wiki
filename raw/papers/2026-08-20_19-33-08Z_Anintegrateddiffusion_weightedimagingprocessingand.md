---
title: An integrated diffusion-weighted imaging processing and interpretation platform for MR-guided radiotherapy
published: 2026-08-20T19:33:08Z
authors: Yunxiang Li, Yan Dai, Yen-Peng Liao, Jie Deng, Jill B De Vis, You Zhang
url: http://arxiv.org/abs/2608.20519v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An integrated diffusion-weighted imaging processing and interpretation platform for MR-guided radiotherapy

## Abstract
Background: Magnetic resonance imaging-guided linear accelerators (MR-Linacs) allow diffusion-weighted imaging (DWI) to be acquired at every treatment fraction, but converting these low-signal-to-noise-ratio acquisitions into clinical decisions requires both reliable quantitative processing and an interpretation that reconciles a scattered and often contradictory literature.   Purpose: To describe and evaluate an integrated, web-based platform that carries raw MR-Linac DWI to a structured, literature-grounded clinical interpretation, and to assess its retrieval-augmented generation (RAG) interpretation module by independent expert rating.   Methods: The platform couples a deep-learning processing pipeline, comprising distortion correction, denoising, and intravoxel incoherent motion (IVIM)/apparent diffusion coefficient (ADC) fitting, with longitudinal region-of-interest analysis and a RAG interpretation agent. The agent reasons over a two-layer knowledge base of curated publications (a structured catalog index plus line-indexed full text), delegates arithmetic to deterministic tools, and is designed to trace each statement to a source document, section, and line range. One medical physicist and one physician independently rated the agent's reports for nine longitudinal glioblastoma cases on a 1-5 scale across three metrics: clinical-reasoning soundness, literature-citation quality, and overall clinical utility.   Results: Across 54 ratings, the pooled mean was 4.65 +/- 0.80, with 93% of ratings >= 4; metric means were 4.6 (reasoning), 4.5 (citation), and 4.8 (utility), and raters agreed within one point on 85% of paired ratings.   Conclusions: A single platform can integrate MR-Linac DWI post-processing with traceable, expert-evaluated clinical interpretation, while highlighting the safeguards needed to verify LLM-generated reasoning in radiation oncology.

## Metadata
- **Published**: 2026-08-20T19:33:08Z
- **Authors**: Yunxiang Li, Yan Dai, Yen-Peng Liao, Jie Deng, Jill B De Vis, You Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20519v1)