---
title: IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems
published: 2026-07-25T18:28:44Z
authors: Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani
url: http://arxiv.org/abs/2607.23322v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IKS-Instruct: A 24,000-Example Multilingual Dataset for Teaching Language Models Indian Knowledge Systems

## Abstract
Instruction tuning has become the standard method for adapting large language models to follow human intent, yet existing instruction datasets are dominated by English-language general-knowledge tasks and lack coverage of specialized pedagogical domains. This paper presents IKS-Instruct, a dataset of 24,795 instruction-response pairs for teaching language models to deliver educational content grounded in Indian Knowledge Systems (IKS). The dataset spans seven languages (English, Hindi, Sanskrit, Tamil, Telugu, Kannada, and Malayalam), covers 41 pedagogical techniques from the Vedic oral and mathematical traditions, and is aligned with the Central Board of Secondary Education (CBSE) curriculum for classes 6 through 12. The pairs are derived from six source types: classical text corpora (Bhagavad Gita, Thirukkural, Sangam literature, Vedic texts), curriculum-aligned pedagogical templates, Vedic mathematical sutra demonstrations, bilingual instruction pairs, technique-grounded multi-turn dialogues, and cross-tradition comparative analyses. Quality is assessed through a multi-judge evaluation framework in which independent language models score responses on 12 dimensions including technique fidelity, pedagogical quality, factual accuracy, and IKS cultural depth. Under a uniform five-judge external panel (median aggregation over 1,201 stratified items), the strongest IKS-Instruct fine-tune of a compact 7B model reaches a median judge score of 6.39, within 0.15 of a strong general-purpose reference model (Nemotron-Nano at 6.54) at a fraction of its deployment cost, while the base model without IKS fine-tuning scores near zero on the IKS-specific dimensions. Model quality does not increase monotonically with data curation, a result we report together with the corresponding data-quality gains.

## Metadata
- **Published**: 2026-07-25T18:28:44Z
- **Authors**: Shwetha Singaravelu, Gayathri Muruganantham, Lakshmi Rajendran, Santhosh Sivasubramani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23322v1)