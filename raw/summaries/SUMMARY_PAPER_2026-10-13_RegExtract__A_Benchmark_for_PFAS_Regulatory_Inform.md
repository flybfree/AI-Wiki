---
title: RegExtract: A Benchmark for PFAS Regulatory Information Extraction with LLMs
url: http://arxiv.org/abs/2610.15103v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_18-26-57Z_RegExtract_ABenchmarkforPFASRegulatoryInformationE.md
generated_at: 2026-10-13 20:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
RegExtract introduces a benchmark dataset designed to evaluate how well large language models can extract structured, traceable information from PFAS regulatory documents across US states. The benchmark comprises 488 human-annotated field instances spanning 20 state documents and 46 regulations, with each entry including both a value and a provenance reference. Through experiments with various prompting strategies, document condensing methods, and schema partitioning approaches, the authors find that document identification fields remain particularly challenging for LLMs, while field-specific few-shot examples significantly improve extraction performance.

## Key Takeaways
- The benchmark defines a typed, multi-field schema targeting critical regulatory elements such as material definitions, permitted uses, and product exemptions, and introduces provenance-aware evaluation metrics specifically tailored to regulatory text. This ensures that extracted facts can be traced back to their exact source in legally dense documents, which is essential for verification and compliance.
- The dataset spans 20 US state documents and 46 regulations, yielding 976 total entries (488 field instances each with a value and provenance entry). This breadth captures the significant variation in scope and product relevance across jurisdictions, reflecting the real-world complexity manufacturers and policymakers face when interpreting PFAS regulations.
- Experimental results across open- and closed-source LLMs reveal that document identification fields remain persistently difficult, but incorporating field-specific few-shot examples improves extraction accuracy. The study also evaluates document condensing methods and schema partitioning strategies, providing practical guidance for deploying LLMs in regulatory compliance workflows.

## Context
This paper sits at the intersection of NLP benchmarking, regulatory AI, and environmental policy. As PFAS regulations proliferate across US states with varying definitions and exemptions, manufacturers and policymakers struggle to interpret legally dense texts consistently. Existing information extraction benchmarks rarely address the provenance and traceability requirements unique to regulatory documents, making RegExtract a novel contribution that bridges legal text understanding with structured extraction evaluation.

## Implications
For industry practitioners, RegExtract provides a concrete evaluation framework for building AI tools that can automate hazardous substance identification, compliance monitoring, and regulatory question answering—tasks that currently demand significant manual legal review. For the AI research community, the findings highlight that document identification and provenance tracking remain unsolved challenges for current LLMs, guiding future work toward more reliable extraction systems. The open-source code and data at the IBM GitHub repository enable reproducible benchmarking and community-driven improvement of regulatory AI tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.15103v1)
