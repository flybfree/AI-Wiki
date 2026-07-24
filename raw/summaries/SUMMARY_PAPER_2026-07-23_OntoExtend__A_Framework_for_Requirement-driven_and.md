---
title: OntoExtend: A Framework for Requirement-driven and Scalable Ontology Extension with LLMs
url: http://arxiv.org/abs/2607.17963v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_14-04-01Z_OntoExtend_AFrameworkforRequirement_drivenandScala.md
generated_at: 2026-07-23 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents OntoExtend, a requirements‑driven framework that uses large language models together with retrieval‑augmented generation to create ontology extensions grounded in competency questions. The system integrates relevant input ontologies and requirement statements, generating structured fragments that satisfy functional tests. Evaluation on 39 competency questions from public and industrial ontologies shows that the generated fragments have few structural issues and are rated as needing only minor revisions.

## Key Takeaways
- OntoExtend employs RAG to link competency questions directly to existing ontology knowledge, producing extensions that align with specific requirements.  
- The framework’s generated fragments consistently pass functional evaluation tests, indicating high relevance and correctness of the output.  
- Human ontology engineers find the drafts require only minor to moderate revisions before integration into larger ontologies.

## Context
The need for automated, requirement‑aware ontology extension is growing as domain knowledge evolves faster than manual curation can keep pace. While LLMs excel at generating ontologies from scratch, existing methods lack systematic ties to user requirements and robust evaluation protocols. OntoExtend addresses these gaps by embedding retrieval of relevant information into the generation pipeline.

## Implications
For researchers, OntoExtend offers a reproducible template for integrating LLMs with ontology engineering workflows, encouraging further work on requirement‑specific prompting. In industry, it can accelerate knowledge capture in large ontologies such as those used in EU projects and manufacturing systems, reducing development time and error risk. Practitioners should consider the specificity of competency questions when deploying the framework to ensure optimal utility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.17963v1)
