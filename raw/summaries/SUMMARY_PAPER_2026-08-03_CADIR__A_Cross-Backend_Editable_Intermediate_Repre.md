---
title: CADIR: A Cross-Backend Editable Intermediate Representation for Agentic CAD Generation
url: http://arxiv.org/abs/2608.00891v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_23-07-08Z_CADIR_ACross_BackendEditableIntermediateRepresenta.md
generated_at: 2026-08-03 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CADIR, an editable intermediate representation that enables agents to generate and edit computer-aided design programs across different CAD systems. By representing modeling processes as a compositional construction graph with explicit parameter dependencies, CADIR preserves construction history and topological references. The authors demonstrate that CADIR improves geometric fidelity and cross‑backend reconstruction compared with existing methods.

## Key Takeaways
- CADIR uses an OCCT geometry kernel via OCP to create an explicit execution diagnostic system that records modeling operations, constraints, and topology selections in a graph.  
- Geometric Signature Matching allows adapters to reconstruct native editable feature histories in FreeCAD, SolidWorks, and Fusion 360 despite parameter changes or backend differences.  
- The construction‑graph retrieval method supports both full‑graph and subgraph queries, letting agents leverage complete models or specific modeling substructures.

## Context
Current CAD generation relies on backend‑specific scripts that hide dependencies, limiting traceability and editability. AI‑driven design tools need a representation that can survive translation between platforms while maintaining geometric accuracy. This work addresses those gaps by providing a language‑agnostic, graph‑based model that integrates seamlessly with large language models.

## Implications
CADIR opens the door to truly agentic CAD pipelines where natural‑language or image prompts directly drive editable designs across multiple environments. Practitioners can trust that modifications are reflected consistently in all downstream systems, fostering collaborative and iterative design workflows without manual re‑export.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00891v1)
