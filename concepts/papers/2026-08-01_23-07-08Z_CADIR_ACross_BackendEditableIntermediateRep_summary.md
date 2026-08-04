# Summary: 2026-08-01_23-07-08Z_CADIR_ACross_BackendEditableIntermediateRepresenta.md
Saved: 2026-08-03 20:32
Source: 2026-08-01_23-07-08Z_CADIR_ACross_BackendEditableIntermediateRepresenta.md
Model: None

---

## Summary  
The paper introduces CADIR, a cross‑backend editable intermediate representation for agentic CAD generation that preserves construction history and enables reliable editing across FreeCAD, SolidWorks, and Fusion 360. It solves the problem of implicit dependencies in backend‑specific scripts by providing explicit modeling operations and geometric signature matching.

## Key Contributions  
- CADIR defines an executable intermediate representation built on OCCT geometry kernel with compositional modeling ops.  
- Geometric Signature Matching identifies corresponding edges/faces across parameter changes and backends, enabling adapter reconstruction.  
- Construction‑graph retrieval method supports full‑graph and subgraph queries for text/image prompts.

## Methodology  
The authors start from the need to generate CAD programs from language or image inputs while maintaining editable histories. They leverage OCCT geometry kernel via OCP to create a construction graph that records modeling ops, parameter dependencies, constraints, and topology selections. Geometric Signature Matching is implemented as an algorithm that aligns geometric primitives across backends by matching edge/face signatures irrespective of parameters. The retrieval method uses graph indexing to locate subgraphs corresponding to queries.

## Results  
Experiments show CADIR yields higher geometric fidelity and execution reliability than prior representations such as static geometry or backend scripts. Adding construction‑graph retrieval improves model generation quality, especially for complex prompts, by allowing agents to retrieve relevant substructures. Cross‑backend editing demonstrates reliable reconstruction in FreeCAD, SolidWorks, Fusion 360 with minimal loss of editable features.

## Significance  
This work bridges the gap between natural‑language and CAD generation by providing a stable, cross‑platform representation that supports both creation and post‑generation editing. It enables agents to produce models once and reuse them across different design tools without re‑encoding, fostering interoperability and reducing errors.

## Related Concepts  
- OCCT geometry kernel  
- OCP (Open Component Platform)  
- Construction graph  
- Geometric signature matching  
- Cross‑backend editing
