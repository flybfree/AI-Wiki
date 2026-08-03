# Summary: 2026-07-31_17-55-58Z_ExtractBench_ABenchmarkforSchema_GuidedEnterpriseD.md
Saved: 2026-08-03 10:17
Source: 2026-07-31_17-55-58Z_ExtractBench_ABenchmarkforSchema_GuidedEnterpriseD.md
Model: None

---

## Summary
The paper introduces ExtractBench, a comprehensive benchmark designed to evaluate the performance of AI agents in schema-guided enterprise document extraction. This task requires agents to accurately parse complex documents according to user-defined schemas while providing source evidence for every extracted value. The authors address critical gaps in existing evaluation methods by simultaneously measuring value accuracy, record completeness, grounding fidelity, and computational cost across a diverse dataset of real-world enterprise documents. By establishing a standardized evaluation framework, this work aims to facilitate the development of more reliable and efficient document processing systems for business applications.

## Key Contributions
- The introduction of ExtractBench, the first large-scale benchmark that jointly evaluates value accuracy, record completeness, grounding metrics, and cost efficiency for schema-guided extraction tasks.
- The development of a scalable curation pipeline that combines independent-system agreement for real documents, known values for synthetic lists, and rigorous human verification to ensure high-quality ground truth data.
- A comprehensive comparative analysis of various AI models, revealing distinct performance trade-offs between commercial Vision Language Models (VLMs) and coding agents, while identifying LlamaExtract Agentic Plus as the top-performing model across all key metrics.

## Methodology
The authors constructed a robust dataset comprising 4,869 pages from 370 enterprise documents spanning 8 business domains and 67 document types. To ensure data quality and diversity, they employed a multi-stage curation pipeline: independent-system agreement was used for real-world documents, known values were utilized for synthetic lists, and human verification was applied to forms. The evaluation system utilizes clear tags to differentiate challenge scenarios and measures performance using order-insensitive value F1 for accuracy, alongside word- and page-level F1 scores for grounding traceability. This methodology allows for a nuanced assessment of how well models adhere to schemas and provide verifiable evidence.

## Results
Experimental results indicate that commercial VLMs perform adequately on short documents but frequently truncate record lists when processing longer, more complex documents. In contrast, coding agents maintain higher accuracy levels but incur significantly higher computational costs. Notably, LlamaExtract Agentic Plus achieved the highest rankings across all three primary metrics—accuracy, completeness, and grounding—while delivering performance comparable to coding agents at a fraction of the cost. This highlights a significant efficiency advantage for agentic approaches in enterprise settings where cost and reliability are paramount.

## Significance
This research provides a critical tool for advancing AI-driven document processing by establishing a rigorous standard for evaluating schema-guided extraction. By highlighting the limitations of current VLMs with long documents and demonstrating the cost-effectiveness of specialized agentic models, it guides future development toward more scalable and accurate solutions. The open-source release of the dataset and code fosters reproducibility and encourages further innovation in enterprise AI workflows.

## Related Concepts
- Schema-Guided Extraction
- Enterprise Document Processing
- Vision Language Models (VLMs)
- Grounding Metrics
- Agentic AI
- Benchmark Evaluation
- Source Traceability
