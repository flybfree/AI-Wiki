# Summary: 2026-07-30_06-40-05Z_AStructuredKnowledgeInfrastructureforDomain_Specif.md
Saved: 2026-07-30 20:27
Source: 2026-07-30_06-40-05Z_AStructuredKnowledgeInfrastructureforDomain_Specif.md
Model: None

---

## Summary  
The paper proposes a structured knowledge infrastructure to solve two failures in enterprise data analytics: generic RAG retrieves the wrong asset and provides no usage knowledge, leading to metric misinterpretation. It introduces a two‑layer solution with a three‑tier dual‑purpose knowledge base and a closed‑loop refresh pipeline that enables fast, accurate retrieval for 14 domains within an advertising data warehouse.

## Key Contributions  
- The system achieves Hit@10 from 19.1% to 96.6% on two benchmarks, a gain of 77.5 percentage points.  
- It reduces token usage by 71.6× via Graph‑Guided Retriever using a 2,859‑node knowledge graph for intent routing.  
- Knowledge coverage improves from 56% to 77%, with negative knowledge contributing 25 percentage points of the improvement.  

## Methodology  
The authors designed a three‑tier dual‑purpose knowledge base (179 documents, eight‑section annotation template) that serves both retrieval and generation. A closed‑loop refresh pipeline updates day‑level freshness via one yes/no approval with 30‑second hot reload. Retrieval is performed by Graph‑Guided Retriever (GGR) which routes queries through a knowledge graph; ranking is done by Scene‑Aware Ranker (SAR) that performs 19‑class entity recognition and scenario annotations.

## Results  
On two 100‑question benchmarks, latency remains 4.84–5.33 seconds end‑to‑end. The GGR reduces token count dramatically; the SAR adds negative knowledge for better ranking. Overall Hit@10 rises sharply while coverage improves from 56% to 77%.

## Significance  
By integrating a structured, domain‑specific knowledge base with real‑time refresh and graph‑guided retrieval, enterprises can eliminate asset misidentification and metric distortion, leading to reliable analytics and faster decision making.

## Related Concepts  
Retrieval Augmentation Generation (RAG), Knowledge Graphs, Entity Recognition, Scenario Annotation, Closed‑Loop Refresh Pipelines, Hit@10 Metric, Schema Drift, Asset‑Usage Gap.
