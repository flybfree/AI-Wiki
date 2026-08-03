# Summary: 2026-07-31_14-07-12Z_BeyondRetrieval_AnalyticMemoryforMultimodalAgents.md
Saved: 2026-08-03 10:12
Source: 2026-07-31_14-07-12Z_BeyondRetrieval_AnalyticMemoryforMultimodalAgents.md
Model: None

---

## Summary
This paper introduces a novel paradigm for long-term memory in multimodal agents, shifting the focus from traditional retrieval-based systems to "analytic memory." The authors argue that current systems primarily organize interaction histories through summaries and indexes to return relevant information, but they fail to support complex computations over accumulated observations. To address this limitation, the researchers propose AdaMM, a framework that jointly supports both retrieval and analytic memory capabilities. By extracting provenance-linked attribute-value observations from diverse inputs like dialogue and images, AdaMM enables agents to perform sophisticated operations such as filtering, aggregation, ranking, and temporal comparison on their historical data.

## Key Contributions
- **Formulation of Analytic Memory**: The authors formally define "analytic memory" as a complementary abstraction to retrieval memory, establishing it as a necessary component for agents that need to compute over recurring multimodal observations rather than just retrieving them.
- **Development of AdaMM Framework**: They present AdaMM, a system that automatically discovers recurring field structures from unstructured data without relying on application-defined schemas, allowing for the materialization of data into queryable analytical structures.
- **Enhanced Performance on Benchmarks**: The proposed framework demonstrates significant performance improvements on long-term multimodal memory benchmarks, specifically MemEye and MemGallery, proving its efficacy in handling complex, multi-turn interactions.

## Methodology
The authors approach the problem by designing a system that moves beyond simple indexing. Instead of relying on rigid, application-defined schemas, AdaMM dynamically extracts provenance-linked attribute-value observations from dialogue transcripts, images, and contextual metadata. The system employs algorithms to discover recurring field structures within this unstructured data and materializes them into analytical structures. At inference time, the framework utilizes a memory-aware planner that decomposes user queries into distinct retrieval and analytic operations. These operations are then routed to appropriate tools, allowing the agent to combine semantic search with structured data manipulation for more accurate and context-aware responses.

## Results
Experiments conducted on two established long-term multimodal memory benchmarks, MemEye and MemGallery, validate the effectiveness of the proposed approach. The results indicate that AdaMM improves performance by up to 11.3% on the MemEye benchmark and by 7.3% on the MemGallery benchmark compared to existing retrieval-only baselines. These gains highlight the advantage of integrating analytical capabilities into memory systems for complex reasoning tasks.

## Significance
This work is significant because it addresses a critical gap in multimodal agent architectures: the inability to perform logical computations over long-term memories. By enabling agents to analyze, aggregate, and compare historical data rather than just retrieving it, this research paves the way for more intelligent, context-aware, and reasoning-capable AI systems. It represents a fundamental shift from passive memory storage to active memory utilization.

## Related Concepts
- Multimodal Agents
- Long-term Memory Systems
- Analytic Memory vs. Retrieval Memory
- Schema-less Data Extraction
- Attribute-Value Observations
- Memory-Aware Planning
