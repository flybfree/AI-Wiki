# Summary: 2026-07-23_23-10-38Z_DAGForge_AuditableCausalDAGAuthoringwithBiomedical.md
Saved: 2026-07-26 21:32
Source: 2026-07-23_23-10-38Z_DAGForge_AuditableCausalDAGAuthoringwithBiomedical.md
Model: None

---

## Summary  
Causal directed acyclic graphs (DAGs) are essential for interpreting biomedical research but are typically assembled manually without clear provenance, leading to potential errors and lack of auditability. DAGForge addresses this gap by providing a browser‑based platform that automatically generates evidence‑linked DAGs from free‑text study descriptions using an LLM reasoning module. The system produces a reproducible literature snapshot, pairwise causal judgments with confidence scores, and a constraint‑checked graph where every edge is traceable to original excerpts. By integrating provenance checks, the authors reduce manual curation effort while ensuring that assumptions remain verifiable for expert review.

## Key Contributions  
- [Finding 1] DAGForge automatically constructs causal DAGs from textual study descriptions using a large language model that extracts verbatim evidence to support each directed edge.  
- [Finding 2] The system generates confidence estimates and provenance metadata for every proposed causal relationship, enabling auditable review of the graph’s assumptions.  
- [Finding 3] Experimental results show high edge recall on literature‑derived benchmarks while preserving verifiable evidence trails that LLM‑only baselines lack.

## Methodology  
The authors began by defining a workflow where a user inputs a study concept, which triggers DAGForge to retrieve relevant biomedical literature via an internal knowledge base. An LLM is then prompted with the retrieved excerpts and the study’s hypothesis to produce structured pairwise judgments (e.g., “X causes Y because of evidence X → Y”). These judgments are validated against predefined constraints to ensure acyclicity, and the resulting edges are compiled into a DAG. The interface tracks progress, allows manual review or adjustment of edges, computes adjustment sets for alternative graphs, and exports both the graph and its provenance log.

## Results  
In evaluation on two benchmark datasets—one compact synthetic DAG and one literature‑derived reference DAG—the system achieved an edge recall of 92 % and a precision of 87 %, outperforming LLM‑only baselines that produced 65 % recall. The provenance logs demonstrated full traceability: each edge could be linked to the exact citation paragraph, and confidence scores correlated with the length and relevance of the supporting excerpt.

## Significance  
By automating DAG construction while maintaining rigorous audit trails, DAGForge lowers the cognitive load on researchers and clinicians who must manually verify causal claims. This supports transparent study design, reproducible analysis pipelines, and regulatory compliance in biomedical research where causal inference is critical.

## Related Concepts  
- Causal Directed Acyclic Graph (DAG)  
- Large Language Model (LLM) reasoning for evidence extraction  
- Provenance‑driven auditability  
- Adjustment set computation
