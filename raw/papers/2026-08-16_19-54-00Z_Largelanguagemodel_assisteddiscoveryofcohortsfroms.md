---
title: Large language model-assisted discovery of cohorts from scientific literature
published: 2026-08-16T19:54:00Z
authors: Moritz Sturm, Lisa M. Berg, Inken Berg, Harishny Sarma, Jasmin Hartmann, Denissa Girschik, Gemma Roig, Christine M. Freitag, Andreas G. Chiocchetti
url: http://arxiv.org/abs/2608.15909v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Large language model-assisted discovery of cohorts from scientific literature

## Abstract
Background: Planning multi-study analyses requires identifying cohorts with the relevant participants, phenotypes, and data modalities. This process commonly relies on prior knowledge, cohort catalogues, and manual literature searches. We developed a complementary question-driven framework that searches relevant scientific literature and extracts explicit cohort names. Methods: The framework first generates multiple PubMed queries from configurable vocabularies and templates and retrieves the resulting scientific literature automatically through the PubMed API. A large language model then screens the retrieved titles and abstracts and extracts explicit cohort names using a prompt tailored to the research question. The extracted names are deduplicated with human review. Configurable code, prompts, and example outputs are available at https://gitlab.rz.uni-frankfurt.de/cap_molgenlab/literature-cohort-discovery. Evaluation: As a use case, we applied the framework to youth aggression genetics. From 5,400 generated PubMed queries, the framework retrieved 5,254 unique records and identified 188 candidate cohorts. Manual screening using predefined criteria, including participant age and genetic-data availability, retained 44 eligible cohorts. Automated LLM-based name extraction was within the agreement range of human annotators. We also searched four established cohort catalogues using the same research question. Their combined results contained 27 of the 44 eligible cohorts, while 17 were not returned by any cohort catalogue search. Conclusion: The framework converts research-question-specific vocabulary into screenable cohort inventories via a large, automated literature search. It can be adapted across populations, phenotypes, data modalities, and study designs, and provides a literature-based complement to curated cohort catalogues.

## Metadata
- **Published**: 2026-08-16T19:54:00Z
- **Authors**: Moritz Sturm, Lisa M. Berg, Inken Berg, Harishny Sarma, Jasmin Hartmann, Denissa Girschik, Gemma Roig, Christine M. Freitag, Andreas G. Chiocchetti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15909v1)