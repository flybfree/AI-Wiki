---
title: RegExtract: A Benchmark for PFAS Regulatory Information Extraction with LLMs
published: 2026-10-10T18:26:57Z
authors: Defne Circi, Krystelle Lionti, Sarathkrishna Swaminathan, Daniel P. Sanders, L. Catherine Brinson, Bhuwan Dhingra, Basel Shbita, Mohab Elkaref, Sara Capponi, Tim Erdmann, Brandi Ransom
url: http://arxiv.org/abs/2610.15103v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RegExtract: A Benchmark for PFAS Regulatory Information Extraction with LLMs

## Abstract
Extracting structured information from regulatory documents is a critical but challenging task. Relevant facts are scattered across long, legally dense texts, and traceability of extracted facts to their source is essential for verification. With increasing awareness of the environmental and health impacts of per- and polyfluoroalkyl substances (PFAS), regulatory documents have expanded significantly, varying in scope and product relevance, making interpretation challenging for manufacturers and policymakers. We introduce RegExtract, a benchmark for structured information extraction from PFAS regulatory documents, comprising 488 human-annotated field instances across 20 US state documents and 46 regulations. Each field instance includes a value and a provenance entry, yielding 976 entries in total. We define a typed, multi-field schema targeting key elements such as material definitions, permitted uses, and product exemptions, and propose provenance-aware evaluation metrics tailored to regulatory text. Through experiments with open- and closed-source LLMs across prompting strategies, document condensing methods, and schema partitioning approaches, we find that document identification fields remain challenging, and that field-specific few-shot examples improve extraction. This work lays the groundwork for AI tools for hazardous substance identification, question answering, and compliance monitoring. The code and data are available at https://github.com/IBM/PFAS-regulations.

## Metadata
- **Published**: 2026-10-10T18:26:57Z
- **Authors**: Defne Circi, Krystelle Lionti, Sarathkrishna Swaminathan, Daniel P. Sanders, L. Catherine Brinson, Bhuwan Dhingra, Basel Shbita, Mohab Elkaref, Sara Capponi, Tim Erdmann, Brandi Ransom
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15103v1)