# Summary: 2026-08-06_19-24-01Z_KNOWPLAN_Knowledge_DrivenAIAgentsforSmartDegreePat.md
Saved: 2026-08-09 22:24
Source: 2026-08-06_19-24-01Z_KNOWPLAN_Knowledge_DrivenAIAgentsforSmartDegreePat.md
Model: None

---

## Summary  
The paper tackles the dual challenge of reconstructing a university’s curriculum from fragmented, schema‑less sources and then generating a personalized degree pathway that respects prerequisite and resource constraints. It introduces **KNOWPLAN**, a knowledge‑driven AI agent pipeline that first extracts all necessary facts (CatalogBrowse) before any student‑specific optimization is performed (DegreeMap). By enforcing an extraction‑first boundary, the system measures the interface between stages rather than assuming it, producing provable certificates for each phase. The approach reduces source crawling dramatically while delivering high recall, full feasibility guarantees, and measurable utility gains over existing baselines.

## Key Contributions  
- **Finding 1:** CatalogBrowse extracts curriculum information with a confidence‑based marginal‑gain scoring mechanism, deterministic parsing via platform adapters and a span‑constrained clause‑to‑AST fallback, and terminates on a closure certificate that guarantees completeness of index, schema, provenance, and reference coverage.  
- **Finding 2:** DegreeMap consumes the three provenance‑linked JSON documents to build a typed requirement hypergraph and optimizes it lexicographically under CP‑SAT constraints (feasibility, horizon, load, risk, personalized utility, option value), ensuring each optimization respects the previous stage’s proven optimum.  
- **Finding 3:** The full pipeline achieves 96.2 % inventory recall and 88.7 % masked‑source recovery at 47 % fewer source accesses than an exhaustive crawler; it attains 100 % hard feasibility while improving personalized utility by +0.066 over the strongest baseline, and certifies 99.5 % of requests with a utility gap of only 0.015 to the privileged gold graph.

## Methodology  
KNOWPLAN adopts an extraction‑first paradigm: CatalogBrowse operates without any user profile, exploring official university catalogs, departmental pages, JSON endpoints, and PDFs using a confidence‑driven marginal‑gain scorer. Actions are parsed deterministically through platform adapters that employ a span‑constrained clause‑to‑AST model as a fallback; the process stops when a closure certificate confirms full coverage of index, schema, provenance, and reference completeness. The output is a three‑document JSON contract linking provenance to each extracted fact. DegreeMap then ingests these documents, constructs a typed requirement hypergraph, and solves it lexicographically with CP‑SAT, optimizing for hard feasibility, completion horizon, load, risk, personalized utility, and option value while staying within the solver budget.

## Results  
Across a 100‑university broad track and a six‑school dense track, CatalogBrowse reaches 96.2 % inventory recall and 88.7 % masked‑source recovery with 47 % less source access than an exhaustive crawler. DegreeMap guarantees 100 % hard feasibility while boosting personalized utility by +0.066 relative to the strongest baseline. The complete pipeline certifies 99.5 % of user requests, and the utility gap between its solution and the privileged gold graph is only 0.015.

## Significance  
KNOWPLAN demonstrates that knowledge‑driven AI agents can replace costly, blind crawling with a principled extraction phase, delivering provable completeness and personalization at a fraction of the data cost. This reduces operational overhead for universities, improves student outcomes through accurate pathway recommendations, and establishes a certification framework that ensures each optimization step is bounded and auditable.

## Related Concepts  
knowledge‑driven AI agents, curriculum reconstruction from heterogeneous sources, hypergraph representation of requirements, CP‑SAT optimization, provenance‑linked JSON contracts, closure certificates, marginal‑gain scoring, attribute‑based learning, smart degree pathway planning.
