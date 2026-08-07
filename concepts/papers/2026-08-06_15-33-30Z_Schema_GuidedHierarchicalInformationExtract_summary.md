# Summary: 2026-08-06_15-33-30Z_Schema_GuidedHierarchicalInformationExtractionandS.md
Saved: 2026-08-06 22:18
Source: 2026-08-06_15-33-30Z_Schema_GuidedHierarchicalInformationExtractionandS.md
Model: None

---

## Summary  
This paper introduces a schema‑guided framework that leverages generative AI to extract complex, hierarchical information from unstructured text documents in a single zero‑shot call and then evaluates the extracted results against a gold standard using a path‑based semantic matching algorithm. The core contribution is a unified model that encodes domain knowledge as a schema with attributes of variable cardinality, enabling both extraction and automated semantic evaluation without explicit programming for each attribute type. By applying this framework to NICE health‑technology‑assessment documents, the authors achieve high accuracy and dramatically reduced processing time compared with human experts.

## Key Contributions  
- **Single‑call zero‑shot hierarchical extraction**: The schema enables a single generative AI call (e.g., Claude Opus 3) to extract 12 out of 14 nested attributes from NICE documents, handling variable cardinalities automatically.  
- **Path‑based semantic matching with rubric**: A custom algorithm aligns extracted attribute values with gold standards and classifies the comparison as exact, semantically useful, or non‑match based on domain rules.  
- **Performance demonstration**: The system extracts 12/14 attributes with an F1 > 90 % while being ~30 times faster than a human expert, showing strong generalisation across generative models and HTA organisations/languages.

## Methodology  
The authors first design a schema that represents the domain’s knowledge structure: each attribute is defined with its hierarchy level, possible values, and cardinality constraints. The schema serves as an information model that guides the generative AI to produce structured output directly. Extraction occurs via one prompt‑response cycle, bypassing explicit rule‑based pipelines. For evaluation, a path‑based algorithm traverses the hierarchical schema, matching each extracted node to its gold standard counterpart; the rubric then evaluates the match quality (exact, useful, or non‑match) according to domain‑specific criteria.

## Results  
Experimental results on NICE HTA documents show that 12 attributes are correctly identified with an F1 score exceeding 90 %. The extraction time is approximately 30 times shorter than manual processing by a human expert. Moreover, the framework maintains comparable performance when transferred to other generative AI models and across different health‑technology‑assessment bodies in multiple languages, underscoring its robustness.

## Significance  
This work bridges the gap between unstructured text and reliable structured data, offering an automated pipeline that reduces labor costs and improves consistency. By integrating schema design with generative AI and a semantic evaluation rubric, it enables scalable extraction and assessment across diverse domains, paving the way for trustworthy AI‑driven information processing in regulated fields such as health technology.

## Related Concepts  
- Schema‑based information extraction  
- Generative AI (e.g., Claude Opus)  
- Hierarchical attribute representation with variable cardinality  
- Zero‑shot learning and prompting  
- Path‑based semantic matching algorithm  
- Rubric classification for evaluation outcomes  
- F1 score as a metric of extraction accuracy
