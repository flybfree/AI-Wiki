# Summary: 2026-07-31_14-07-12Z_BeyondRetrieval_AnalyticMemoryforMultimodalAgents.md
Saved: 2026-08-03 10:17
Source: 2026-07-31_14-07-12Z_BeyondRetrieval_AnalyticMemoryforMultimodalAgents.md
Model: None

---

## Summary
This paper introduces a novel paradigm for long-term memory in multimodal agents, moving beyond traditional retrieval-based systems to incorporate **analytic memory**. The authors argue that current systems primarily focus on retrieving relevant historical records but fail to support complex computations over accumulated observations, such as filtering, aggregation, and temporal comparison. To address this limitation, they propose **AdaMM**, a framework that jointly supports both retrieval and analytic memory capabilities. By extracting provenance-linked attribute-value observations from diverse inputs like dialogue and images, AdaMM organizes these into queryable structures that enable sophisticated analytical operations, significantly enhancing the agent's ability to reason over long-term interactions.

## Key Contributions
- **Definition of Analytic Memory**: The authors formally define "analytic memory" as a complementary abstraction to retrieval memory, enabling agents to perform computational operations (filtering, aggregation, ranking) on recurring multimodal observations rather than just retrieving static records.
- **Schema-Free Extraction Framework**: AdaMM introduces a method for automatically discovering recurring field structures and materializing them into analytical access points without relying on rigid, application-defined schemas, allowing for flexible handling of heterogeneous data sources.
- **Unified Planning Architecture**: The framework features a memory-aware planner that dynamically decomposes complex user queries into distinct retrieval and analytic operations, routing each to the appropriate specialized tools to optimize performance and accuracy.

## Methodology
The authors developed AdaMM, a framework designed to process multimodal inputs including dialogue transcripts, images, and contextual metadata. Instead of relying on predefined schemas, the system employs an automatic extraction mechanism to identify provenance-linked attribute-value observations from these diverse sources. It then discovers recurring field structures within this data and materializes them into a structured format that supports analytical queries. At inference time, a central memory-aware planner analyzes user requests, decomposing them into sub-tasks. These tasks are categorized as either retrieval-based (finding specific records) or analytic-based (performing computations across multiple records). The planner then routes each sub-task to the corresponding tool, ensuring that the agent leverages the most appropriate memory mechanism for each component of the query.

## Results
The researchers evaluated AdaMM on two established long-term multimodal memory benchmarks: **MemEye** and **MemGallery**. The experimental results demonstrated significant performance improvements over existing retrieval-only baselines. Specifically, AdaMM improved performance by up to **11.3%** on the MemEye benchmark and by **7.3%** on the MemGallery benchmark. These gains highlight the effectiveness of combining analytic capabilities with traditional retrieval methods in handling complex, long-term memory tasks.

## Significance
This work is significant because it addresses a critical gap in multimodal agent architectures: the inability to perform logical computations over time-series or aggregated data. By introducing analytic memory, the paper enables agents to answer complex questions that require synthesizing information across multiple interactions, such as comparing states over time or aggregating statistics from past events. This advancement moves multimodal agents closer to human-like reasoning capabilities, where memory is not just a storage unit but an active computational resource.

## Related Concepts
- Long-term Memory in AI Agents
- Multimodal Learning
- Retrieval-Augmented Generation (RAG)
- Analytic Memory vs. Retrieval Memory
- Schema-Free Information Extraction
- Memory-Aware Planning
