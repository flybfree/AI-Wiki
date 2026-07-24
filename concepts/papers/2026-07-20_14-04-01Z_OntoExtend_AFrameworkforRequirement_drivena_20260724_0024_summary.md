# Summary: 2026-07-20_14-04-01Z_OntoExtend_AFrameworkforRequirement_drivenandScala.md
Saved: 2026-07-24 00:24
Source: 2026-07-20_14-04-01Z_OntoExtend_AFrameworkforRequirement_drivenandScala.md
Model: None

---

## Summary  
OntoExtend is a requirements‑driven framework that uses large language models (LLMs) together with retrieval‑augmented generation to create ontology extensions grounded in competency questions. The system retrieves relevant triples from source ontologies, formulates each requirement as a CQ, and lets the LLM generate extension fragments that are then evaluated for functional correctness. This bridges the gap between unstructured LLM‑generated ontologies and precise specification documents.  

## Key Contributions  
- OntoExtend provides a requirements‑driven, scalable ontology extension framework that integrates LLMs with retrieval‑augmented generation using competency questions.  
- The framework demonstrates that generated ontology fragments are structurally sound, functionally correct, and require only minor to moderate revision from ontology engineers.  
- It establishes a systematic evaluation methodology for LLM‑generated ontological extensions, highlighting sensitivity to CQ specificity and modelling profile.  

## Methodology  
The authors first translate each requirement into a competency question (CQ) that encodes the functional expectation of the extension. They then employ retrieval‑augmented generation (RAG): a retrieval system pulls pertinent triples from the input ontology, these are combined with the CQ and fed to an LLM, which outputs a draft fragment. The process is repeated iteratively across 39 CQs derived from two real‑world ontologies—Onto‑DESIDE (a public EU project) and Bosch’s industrial ontology—to produce a coherent set of extensions.  

## Results  
All generated fragments pass functional evaluation tests, confirming consistency with existing triples and adherence to the original requirements. Structural issues are rare; ontology engineers rate the needed revisions as minor to moderate. The framework scales to multiple CQs while preserving coherence across the extended ontology.  

## Significance  
This matters because ontology engineering is labor‑intensive and error‑prone; OntoExtend offers a practical drafting assistant that aligns LLM output directly with requirements, reducing manual effort and accelerating real‑world project implementation.  

## Related Concepts  
ontology extension, large language models (LLMs), retrieval‑augmented generation (RAG), competency questions, functional evaluation, ontology engineering, scalable frameworks.
