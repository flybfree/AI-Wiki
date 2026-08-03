# Summary: 2026-07-31_17-55-58Z_ExtractBench_ABenchmarkforSchema_GuidedEnterpriseD.md
Saved: 2026-08-03 10:17
Source: 2026-07-31_17-55-58Z_ExtractBench_ABenchmarkforSchema_GuidedEnterpriseD.md
Model: None

---

## Summary
This paper introduces ExtractBench, a comprehensive benchmark designed to evaluate the performance of artificial intelligence agents in schema-guided enterprise document extraction. The primary goal is to address the growing need for reliable automated processing of complex business documents by providing a rigorous testing framework that measures not only accuracy but also grounding, completeness, and computational cost. By aggregating data from 370 diverse enterprise documents across eight distinct business domains, the authors establish a standardized environment for comparing various extraction methodologies. The study highlights significant disparities in performance between different model architectures, particularly regarding their ability to handle long documents and maintain source traceability.

## Key Contributions
- **Multi-Metric Evaluation Framework:** ExtractBench is presented as the first benchmark to simultaneously score value accuracy, record completeness at scale, grounding quality, and measured cost, offering a holistic view of agent performance rather than relying on single-dimensional metrics.
- **Scalable Curation Pipeline:** The authors developed a novel data curation strategy that combines independent-system agreement for real-world documents, known values for synthetic lists, and rigorous human verification for forms, ensuring high-quality ground truth across 4,869 pages.
- **Performance Disparity Analysis:** The study reveals that while commercial Vision Language Models (VLMs) excel on short documents, they frequently fail to truncate record lists correctly in long documents, whereas coding agents maintain higher accuracy but at a significantly higher financial and computational cost.

## Methodology
The authors constructed ExtractBench using a scalable schema and ground-truth curation pipeline. This involved collecting 4,869 pages from 370 enterprise documents spanning 67 document types and 8 business domains. To ensure data integrity, they employed independent-system agreement for real documents, utilized known values for synthetic lists, and incorporated human verification specifically for forms. The evaluation system uses clear tags to differentiate challenge scenarios and measures performance using order-insensitive value F1 for accuracy. Additionally, two grounding metrics—word-level and page-level F1—are used to assess source traceability, ensuring that extracted data can be faithfully linked to its original context.

## Results
Experimental results indicate that commercial VLMs perform well on shorter documents but struggle with long-form inputs, often truncating necessary record lists. In contrast, coding agents demonstrate higher accuracy retention over longer contexts but incur substantially higher costs. Notably, LlamaExtract Agentic Plus emerged as the top performer, ranking first across all three evaluated metrics. It achieved accuracy levels comparable to coding agents while operating at a fraction of the cost, demonstrating superior efficiency and effectiveness in schema-guided extraction tasks.

## Significance
This research is significant because it provides the first standardized, large-scale benchmark for schema-guided extraction, addressing a critical gap in enterprise AI evaluation. By highlighting the trade-offs between accuracy, grounding, and cost, ExtractBench enables developers to make informed decisions about model selection for real-world applications. The availability of the dataset and code promotes reproducibility and further innovation in automated document processing technologies.

## Related Concepts
- Schema-Guided Extraction
- Enterprise Document Processing
- Vision Language Models (VLMs)
- Grounding Metrics
- Record Completeness
- Automated Data Curation
- LlamaExtract Agentic Plus
