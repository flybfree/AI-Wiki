# Summary: 2026-07-27_18-39-05Z_AutomaticKnowledgeGraphConstructionandQueryforEart.md
Saved: 2026-07-28 22:23
Source: 2026-07-27_18-39-05Z_AutomaticKnowledgeGraphConstructionandQueryforEart.md
Model: None

---

## Summary  
This paper proposes an automatic knowledge graph construction and query system for earthquake catalogs using GraphRAG, eliminating the need for manual structuring of raw tabular data. The approach builds structured graphs from event records across three independent catalogs without expert labeling. It enables precise, transferable queries with minimal cost and improved accuracy through carefully crafted prompting fixes.

## Key Contributions  
- First systematic application of GraphRAG to raw earthquake catalog data across multiple independent datasets.  
- Construction of fully queryable knowledge graphs that capture spatiotemporal relationships without manual structuring.  
- Identification of two main pitfalls in graph‑based retrieval and development of four seismology‑informed prompt fixes that eliminate fabrications.

## Methodology  
The authors applied GraphRAG, a retrieval‑augmented generation framework, directly to raw catalog records from three independent earthquake datasets: a reservoir adjacent swarm, the 2019 Ridgecrest tectonic sequence, and the 2021 Maduo Mw7.4 aftershock series. The pipeline ingests tabular events, creates node‑edge structures representing locations, magnitudes, times, and event types, and stores them in a graph database. GraphRAG then retrieves relevant subgraphs via vector similarity and generates answers by prompting the model with structured queries, applying four expert‑crafted fixes to correct hallucinations.

## Results  
Experimental evaluation shows that the generated graphs align with catalog‑derived ground truth on all three datasets, achieving >95% factual correctness after prompt fixes. The vector RAG baseline outperforms a simple graph‑only approach in summarization and temporal stage comparison, demonstrating clear benefits of layered retrieval. Retrieval latency remains low, confirming near‑zero cost operation.

## Significance  
This work provides a practical, transferable interface for seismic data analysis that reduces reliance on manual labeling and subjective windowing, enabling rapid insight generation across diverse catalogs. By integrating graph reasoning with prompt engineering, it bridges the gap between raw catalog output and actionable knowledge, supporting automated decision support in earthquake monitoring.

## Related Concepts  
- Knowledge Graph Construction  
- Retrieval‑Augmented Generation (GraphRAG)  
- Vector Similarity Search  
- Prompt Engineering for AI Models  
- Spatiotemporal Event Modeling
