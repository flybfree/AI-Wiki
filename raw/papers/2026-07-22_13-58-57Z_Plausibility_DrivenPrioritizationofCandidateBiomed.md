---
title: Plausibility-Driven Prioritization of Candidate Biomedical Annotations
published: 2026-07-22T13:58:57Z
authors: Emanuele Cavalleri, Miad Alavinezhad, Dario Malchiodi, Marco Mesiti
url: http://arxiv.org/abs/2607.20163v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Plausibility-Driven Prioritization of Candidate Biomedical Annotations

## Abstract
The rapid growth of biomedical knowledge has made the validation of automatically generated biological annotations a major bottleneck in biomedical curation. While computational methods can rapidly produce large numbers of candidate annotations, determining which are biologically valid still requires costly expert review. Prioritizing these candidates before manual curation has therefore become a fundamental challenge. Machine learning techniques can support this process by exploiting biomedical knowledge graphs (bioKGs), which capture biological entities and their functional associations. In this work, we propose a framework that leverages bioKGs to estimate the plausibility of candidate annotations and guide expert curation. Starting from knowledge graph embeddings, we train relation-specific binary classifiers using a community-based negative sampling strategy to obtain reliable confidence estimates. We then introduce a family of plausibility measures that combine classifier confidence, classifier reliability, and the semantic context provided by alternative relationships involving the same pair of biological entities. Unlike conventional confidence estimation, the proposed approach explicitly accounts for multiple biologically meaningful relations that may coexist between the same entities. Experimental results on five large bioKGs demonstrate that the proposed negative sampling strategy consistently improves classifier robustness, increasing balanced accuracy by an average of 5.8%. Moreover, the plausibility measures outperform classifier confidence alone, enabling more effective prioritization of candidate annotations for expert review. Overall, our results show that the use of bioKGs improves the efficiency of AI-assisted biomedical curation while preserving expert control over the final annotation assessment.

## Metadata
- **Published**: 2026-07-22T13:58:57Z
- **Authors**: Emanuele Cavalleri, Miad Alavinezhad, Dario Malchiodi, Marco Mesiti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20163v1)