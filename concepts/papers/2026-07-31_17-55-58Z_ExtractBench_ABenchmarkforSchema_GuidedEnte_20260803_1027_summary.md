# Summary: 2026-07-31_17-55-58Z_ExtractBench_ABenchmarkforSchema_GuidedEnterpriseD.md
Saved: 2026-08-03 10:27
Source: 2026-07-31_17-55-58Z_ExtractBench_ABenchmarkforSchema_GuidedEnterpriseD.md
Model: None

---

## Summary
This paper introduces ExtractBench, a comprehensive benchmark designed to evaluate the performance of agents in schema-guided enterprise document extraction tasks. The primary goal is to address the critical need for reliable information retrieval from complex business documents by providing a standardized evaluation framework that measures value accuracy, record completeness, grounding fidelity, and computational cost simultaneously. By aggregating data from diverse sources including real-world scans, synthetic lists, and human-verified forms, the authors create a robust dataset comprising 370 enterprise documents across eight distinct business domains. This benchmark serves as a critical tool for assessing how well large vision-language models and coding agents can adhere to user-defined schemas while maintaining source traceability in high-stakes enterprise workflows.

## Key Contributions
- **Comprehensive Multi-Metric Evaluation Framework**: ExtractBench is the first benchmark to simultaneously score value accuracy, record completeness at scale, grounding quality, and measured cost, offering a holistic view of agent performance beyond simple text extraction accuracy.
- **Diverse and Scalable Dataset Curation**: The authors developed a novel pipeline combining independent-system agreement for real documents, known values for synthetic lists, and human verification for forms, resulting in a dataset of 4,869 pages across 370 documents, 8 business domains, and 67 document types.
- **Performance Disparity Analysis**: The study reveals that while commercial Vision-Language Models (VLMs) excel on short documents, they frequently truncate record lists in longer contexts, whereas coding agents maintain higher accuracy but at significantly higher costs, highlighting a critical trade-off in enterprise deployment.

## Methodology
The authors constructed ExtractBench by curating a diverse set of 370 enterprise documents totaling 4,869 pages. The data collection strategy employed three distinct methods to ensure quality and diversity: independent-system agreement was used for real-world documents to establish ground truth, known values were utilized for synthetic lists to ensure precision, and human verification was applied to forms to capture nuanced extraction requirements. The evaluation system includes clear tags differentiating challenge scenarios across six document types. Metrics include order-insensitive value F1 for accuracy, word- and page-level F1 for grounding traceability, and cost measurements to assess economic efficiency.

## Results
Experimental results indicate that commercial VLMs perform well on short documents but struggle with long documents, often truncating record lists. Coding agents retain higher accuracy levels but incur much higher computational costs. Notably, LlamaExtract Agentic Plus ranked first across all three metrics, achieving accuracy comparable to coding agents at a fraction of the cost, demonstrating superior efficiency and reliability for enterprise applications.

## Significance
This work matters because it provides the first standardized, scalable benchmark for schema-guided extraction, enabling fair comparison of agent capabilities in real-world enterprise settings. It highlights the limitations of current VLMs in handling long-context record lists and offers a cost-effective alternative via LlamaExtract, guiding future development of efficient document processing agents.

## Related Concepts
Schema-Guided Extraction, Enterprise Document Processing, Vision-Language Models (VLMs), Grounding Metrics, Record Completeness, Cost-Efficient AI Agents, Benchmark Evaluation, Information Extraction, LlamaExtract, HuggingFace Datasets.
