---
title: EviStreams: Human-in-the-Loop AI Data Extraction for Systematic Reviews in Medicine
url: http://arxiv.org/abs/2609.27418v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_06-35-07Z_EviStreams_Human_in_the_LoopAIDataExtractionforSys.md
generated_at: 2026-09-23 21:11
model: freedomaisvr/gemma-4-12b-it
---

## Summary
EviStreams is an open-source, no-code web platform designed to facilitate AI-assisted data extraction for systematic reviews in medicine while strictly adhering to established clinical protocols. The system addresses the significant labor bottleneck caused by manual review processes by providing a human-in-the-loop framework that allows domain experts to control three key stages: program design, field specification, and reviewer-blinded dual review with adjudication. Evaluation results show that the quality of data extraction is primarily driven by how fields are specified rather than which specific large language model is used.

## Key Takeaways
- The platform addresses the "expert-labor bottleneck" in systematic reviews by integrating AI into a protocolized workflow where two reviewers independently extract data and an adjudicator resolves discrepancies to ensure a fully auditable record of every value produced.
- EviStreams allows domain experts to define typed fields rather than raw prompts, ensuring that the extraction process follows a structured decomposition approved before any code runs, which helps maintain consistency across different studies.
- Empirical evaluations conducted across four clinical corpora and three frontier model families reveal that the quality of extracted data is shaped significantly more by the precision of the field specification than by the specific choice of large language model.

## Context
As large language models (LLMs) become increasingly capable of processing complex information, there is a growing need to integrate them into high-stakes fields like medicine where reliability and reproducibility are paramount. This paper addresses a critical gap in current AI applications by prioritizing human-in-the-loop control over "black box" automation, ensuring that the final output remains verifiable and compliant with clinical standards.

## Implications
For medical researchers and practitioners, EviStreams provides a pathway to significantly reduce the manual labor required for systematic reviews without compromising the integrity of the evidence used to form clinical guidelines. By demonstrating that field specification is more important than model choice, it suggests that organizations can achieve high-quality results by focusing on better data definitions and structured workflows rather than solely pursuing larger or more expensive models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.27418v1)
