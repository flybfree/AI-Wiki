---
title: Quality Metrics for LLM-Generated Asset Administration Shells: A Perturbation-Based Evaluation Approach
published: 2026-09-07T10:00:47Z
authors: Janek Groß, Elena Zentgraf, Jens Heidrich
url: http://arxiv.org/abs/2609.07290v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Quality Metrics for LLM-Generated Asset Administration Shells: A Perturbation-Based Evaluation Approach

## Abstract
The rapid digital transformation of manufacturing, often referred to as Industry 4.0, relies on seamless interoperability between physical and software assets. A central enabler is the Asset Administration Shell (AAS), a standardized digital representation of such assets. Recent advances in large language models (LLMs) enable the generation of AAS submodels from unstructured sources such as product datasheets but raise challenges for quality assurance. In particular, unexpected errors, the lack of ground truth references, and the absence of standardized quality metrics hinder reliable adoption. In this work, we evaluate quality metrics for AI-generated AAS using a perturbation-based evaluation framework. By systematically degrading AAS generation along multiple dimensions, we assess how well different metrics reflect quality changes. Based on a dataset of 200 products from multiple manufacturers, we generate 6,400 AAS instances using GPT-4o-mini, Qwen3, and DeepSeek-R1. Our results show that metrics based on exact matching of property names and similarity-based soft matching of property values, in particular value-based recall and name-based F1 score, provide the most reliable indicators of quality degradation. Furthermore, we quantify the impact of different perturbation types and analyze differences across model families and product segments. These findings support the selection of suitable metrics, the tuning of LLM-based pipelines, and the integration of AI-generated AAS into industrial applications.

## Metadata
- **Published**: 2026-09-07T10:00:47Z
- **Authors**: Janek Groß, Elena Zentgraf, Jens Heidrich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07290v1)