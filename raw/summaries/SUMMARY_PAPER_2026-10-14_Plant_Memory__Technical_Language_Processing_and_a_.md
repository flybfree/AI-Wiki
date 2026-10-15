---
title: Plant Memory: Technical Language Processing and a Verified Maintenance Ontology for Agent-Accessible Failure Knowledge from SAP PM Work Orders
url: http://arxiv.org/abs/2610.19131v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_20-02-31Z_PlantMemory_TechnicalLanguageProcessingandaVerifie.md
generated_at: 2026-10-14 21:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Plant Memory is a system that applies technical language processing to SAP Plant Maintenance work order exports to extract structured, verified failure knowledge from industrial maintenance records. The paper demonstrates that rule-first extraction combined with optional LLM-assisted review can achieve 96.2% component accuracy and 82.1% top-1 root-cause correctness on diagnostic questions, substantially outperforming raw SAP data columns. The resulting knowledge graph is made accessible to both human technicians via a web application and to AI agents via a Model Context Protocol server, with every answer traceable back to source work orders.

## Key Takeaways
- Maintenance work orders in industrial plants are largely unusable for analysis because they contain abbreviated, misspelled text, buried asset identities, contradictory work-type labels, and empty fields for symptom, root cause, and action taken. Plant Memory addresses this by building an ISO 14224-aligned maintenance ontology where every extracted statement is a reified fact with a confidence score, evidence trail, and verification state.
- The extraction pipeline is deliberately rule-first, with an optional LLM serving only as a secondary reader whose disagreements elevate a fact's review priority rather than overwriting the rule-based extraction. This design choice preserves auditability and prevents hallucinated knowledge from entering the ontology unchecked.
- Human-in-the-loop verification is central: technicians review extracted facts through a queue, answer targeted knowledge-gap questions where failures recur without recorded causes, and approve or reject ontology drift proposals when new terminology appears. On a synthetic 12-month dataset of 400 work orders from a parboiled-rice plant, the system achieves 100% root-cause precision at 62% coverage, and ranked root causes from the ontology are correct at top-1 in 82.1% of diagnostic queries versus 53.6% for the raw SAP root-cause column.

## Context
This paper sits at the intersection of industrial knowledge management, NLP for domain-specific text, and agentic AI infrastructure. The broader AI field has increasingly focused on grounding language models in verified, structured knowledge rather than relying on parametric memory, and Plant Memory contributes a concrete pipeline for converting messy operational records into a queryable ontology. Its use of the Model Context Protocol to serve the same verified graph to both humans and AI agents reflects the emerging standard for tool-augmented reasoning, making it relevant to the growing ecosystem of enterprise AI agents that must reason over domain-specific failure data.

## Implications
For industrial practitioners, this work offers a practical path to preventing the loss of diagnostic expertise when senior technicians retire or leave, converting tacit knowledge locked in free-text work orders into a durable, queryable asset. For the AI research community, the rule-first-then-LLM architecture and the reified-fact ontology with confidence scoring provide a template for building trustworthy knowledge graphs from noisy operational data, reducing the risk of hallucination in agentic systems that must make consequential decisions about equipment reliability and safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19131v1)
