---
title: EpiBench: Can LLMs Understand Epitopes for Antibody Drug Discovery?
url: http://arxiv.org/abs/2608.06022v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_13-29-53Z_EpiBench_CanLLMsUnderstandEpitopesforAntibodyDrugD.md
generated_at: 2026-08-06 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents EpiBench, a benchmark designed to test whether large language models can reason about epitopes using only sequence information. The authors evaluate nine general‑purpose LLMs on five tasks that involve epitope discovery, functional assessment, and escape analysis. Results indicate that while the models capture some epitope signals, they still struggle with antibody‑specific grounding and long‑context residue localization.

## Key Takeaways
- EpiBench provides a closed‑book, sequence‑based benchmark with 1,609 curated samples linking structural contacts to functional assays and escape measurements.  
- The five tasks span the full antibody development workflow, enabling evaluation of epitope reasoning across discovery to clinical use.  
- Current LLMs show partial performance, limited by poor grounding in antibody sequences and inability to localize residues over long contexts.

## Context
Epitopes are critical for antibody‑drug interactions, yet most AI benchmarks focus on generic protein tasks or require structural inputs unavailable at the sequence level. This work bridges that gap by creating a purely textual benchmark that mirrors real‑world discovery pipelines.

## Implications
For researchers and industry practitioners, EpiBench offers a standardized way to measure LLM performance in epitope reasoning, guiding improvements in AI tools for antibody design. The findings highlight the need for better sequence grounding in biomedical LLMs to support reliable therapeutic development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06022v1)
