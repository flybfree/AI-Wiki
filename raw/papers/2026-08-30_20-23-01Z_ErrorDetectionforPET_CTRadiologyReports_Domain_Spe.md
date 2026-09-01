---
title: Error Detection for PET/CT Radiology Reports: Domain-Specific vs Large Language Models
published: 2026-08-30T20:23:01Z
authors: Hermione Warr, Harry Anthony, Lilli J Freischem, Yasin Ibrahim, Daniel R McGowan, Konstantinos Kamnitsas
url: http://arxiv.org/abs/2608.30021v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Error Detection for PET/CT Radiology Reports: Domain-Specific vs Large Language Models

## Abstract
Errors in radiology reports can adversely affect patient treatment, yet automated report quality assurance remains challenging because errors are often subtle and require domain expertise to detect. Although large language models (LLMs) have recently been proposed for radiology report verification, their ability to detect clinically meaningful errors beyond chest X-ray datasets remains under-explored. To this end, we present the first systematic evaluation of language models for PET/CT report error detection, comparing compact domain-specific models with SOTA open-weight LLMs. We collected 30,633 oncology FDG PET/CT reports from 23 radiologists over 10 years. We trained domain-specific BERT models to detect clinically motivated synthetic reporting errors and evaluated alongside zero-/few-shot Qwen3-32B, Gemma-3-27B and Llama-3.3-70B on a held-out benchmark of 11,500 reports. A 15M-parameter model achieved 94.4% balanced accuracy with a 5.8% false-positive rate, compared with 84.0% for the strongest prompted LLM. Task-specific adaptation of Llama-3.3-70B closed this performance gap (94.4%) but retained substantially greater computational requirements. Our results suggest that domain-specific training matters more than model scale for PET/CT report error detection, supporting compact models as an accurate and computationally efficient approach to automated radiology report quality assurance.

## Metadata
- **Published**: 2026-08-30T20:23:01Z
- **Authors**: Hermione Warr, Harry Anthony, Lilli J Freischem, Yasin Ibrahim, Daniel R McGowan, Konstantinos Kamnitsas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30021v1)