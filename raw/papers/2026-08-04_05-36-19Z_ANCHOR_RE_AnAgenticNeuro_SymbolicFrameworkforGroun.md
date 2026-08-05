---
title: ANCHOR-RE: An Agentic Neuro-Symbolic Framework for Grounded Biomedical Relation Extraction
published: 2026-08-04T05:36:19Z
authors: Shufan Ming, Yikun Han, Gibong Hong, Rui Zhang, Halil Kilicoglu
url: http://arxiv.org/abs/2608.03154v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ANCHOR-RE: An Agentic Neuro-Symbolic Framework for Grounded Biomedical Relation Extraction

## Abstract
Biomedical relation extraction (BioRE) extracts structured knowledge from biomedical literature for applications such as knowledge base construction and hypothesis generation. Traditional symbolic systems such as SemRep provide high precision but limited recall, while large language models (LLMs) offer stronger contextual reasoning but remain prone to false-positive predictions. We developed ANCHOR-RE, a framework that integrates ontology-guided reasoning, external knowledge grounding, and data-driven verification rules into LLM inference. We evaluated it on three BioRE benchmarks (SemRepGS, DDI, and ChemProt) using both proprietary and open-weight LLMs. To assess generalizability beyond benchmark datasets while reducing potential evaluation bias from LLM pretraining contamination, we conducted a temporal evaluation using 100 biomedical articles published in 2026. With the proprietary backbone, ANCHOR-RE outperformed direct LLM prompting, improving micro-F1 from 0.654 to 0.676 on SemRepGS, from 0.769 to 0.872 on DDI, and from 0.939 to 0.941 on ChemProt. On DDI and ChemProt, it also outperformed previously reported inference-only methods and approached fine-tuned or instruction-tuned systems without parameter updates. Similar performance gains observed with open-weight LLMs indicate that the benefits were not limited to the proprietary backbone. On the post-cutoff set, manual assessment of 500 randomly sampled predictions yielded a precision of 69%, maintaining consistent precision on previously unseen biomedical literature. Neuro-symbolic reasoning can improve the reliability of LLM-based BioRE without fine-tuning. Results across multiple benchmarks, model families, and post-cutoff literature support ANCHOR-RE as a practical training-free approach to biomedical literature mining.

## Metadata
- **Published**: 2026-08-04T05:36:19Z
- **Authors**: Shufan Ming, Yikun Han, Gibong Hong, Rui Zhang, Halil Kilicoglu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03154v1)