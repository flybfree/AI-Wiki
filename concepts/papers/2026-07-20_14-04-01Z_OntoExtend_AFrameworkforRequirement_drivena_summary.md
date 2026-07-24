# Summary: 2026-07-20_14-04-01Z_OntoExtend_AFrameworkforRequirement_drivenandScala.md
Saved: 2026-07-24 00:20
Source: 2026-07-20_14-04-01Z_OntoExtend_AFrameworkforRequirement_drivenandScala.md
Model: None

---

## Summary  
The paper introduces **OntoExtend**, a requirements‑driven framework that enables scalable ontology extension using large language models (LLMs) through retrieval‑augmented generation (RAG). By converting user requirements into competency questions, the system retrieves relevant knowledge from existing ontologies and feeds this context to an LLM to propose grounded extensions. The approach is designed to reduce the manual effort and error‑prone nature of ontology maintenance while providing a systematic evaluation pipeline for generated fragments.

## Key Contributions  
- OntoExtend provides a requirements‑driven framework for scalable ontology extension using LLMs with retrieval‑augmented generation.  
- The framework ties ontology generation explicitly to competency questions derived from user requirements, enabling grounded extensions.  
- Evaluation demonstrates that generated fragments have few structural issues, satisfy all functional tests, and receive minor‑to‑moderate revision ratings from ontology engineers.

## Methodology  
OntoExtend is built as a modular pipeline: first, competency questions are created to represent the target extension; second, relevant sections of input ontologies are retrieved via RAG; third, the retrieved context together with the question is sent to an LLM for fragment generation; fourth, generated fragments undergo structural checks and functional tests, followed by human rating. This design allows reuse of core models across different projects.

## Results  
The framework was applied to 39 competency questions drawn from two ontologies: the public EU‑project **Onto‑DESIDE** and a Bosch industrial ontology. The generated fragments exhibited low structural violations, passed all functional evaluation criteria, and were rated by ontology engineers as requiring only minor to moderate revisions before integration.

## Significance  
This work bridges the gap between LLM‑generated ontologies and practical requirement‑driven extension, offering a scalable, systematic approach that reduces manual effort and error risk. It provides a reusable framework for integrating LLMs into large‑scale ontology maintenance pipelines where incremental extensions are needed.

## Related Concepts  
- Ontology extension: the process of enriching an existing ontology.  
- Retrieval‑Augmented Generation (RAG): combining information retrieval with LLM generation.  
- Competency questions: requirement‑driven queries that specify desired extensions.  
- Structural evaluation: checking syntactic and semantic consistency of generated fragments.  
- Functional evaluation: verifying that generated content satisfies the intended purpose.
