title: "Summary: 2026-06-25_17-51-59Z_MappingPolitical_EliteNetworksinEuropewithaMultili.md"
# Summary: 2026-06-25_17-51-59Z_MappingPolitical_EliteNetworksinEuropewithaMultili.md
Saved: 2026-06-25 22:01
Source: 2026-06-25_17-51-59Z_MappingPolitical_EliteNetworksinEuropewithaMultili.md
Model: None

---


## Summary  
The paper aims to map political‑elite networks across Europe using a multilingual joint entity‑relation extraction pipeline that produces scalable, signed knowledge graphs from unstructured news texts. It combines span‑based named‑entity recognition, a linking cascade to Wikidata identifiers, and an ontology‑constrained mixture‑of‑experts model for guided decoding of directed relationships. The approach achieves high textual correctness (68.2 % strict / 93.7 % lenient) on a gold standard and demonstrates success in two case studies: the full lifecycle reconstruction of an Austrian political party and the analysis of overlapping patronage networks in Poland. This work bridges raw multilingual text to structured relational data, offering a replicable foundation for cross‑national computational social science.

## Key Contributions  
- [Finding 1] The pipeline achieves high textual correctness with 68.2 % strict and 93.7 % lenient accuracy on a 3491‑relation gold standard.  
- [Finding 2] It reconstructs the complete lifecycle of an Austrian political party, tracing internal fractures, personnel shifts, and court convictions.  
- [Finding 3] In Poland it uncovers overlapping economic‑governance networks of state‑enterprise patronage and a balanced conflict network between Civic Platform (PO) and Law and Justice (PiS).

## Methodology  
The authors built a modular pipeline: first span‑based NER identifies entities; then a three‑stage linking cascade maps mentions to language‑independent Wikidata IDs using domain ontologies; finally a high‑throughput ontology‑constrained mixture‑of‑experts model performs guided decoding of directed, signed relationships.

## Results  
The pipeline was evaluated on the gold standard yielding 68.2 % strict and 93.7 % lenient textual correctness. Case studies in Austria and Poland validated reconstruction of party lifecycle and network analysis respectively.

## Significance  
This work provides a robust, replicable foundation for cross‑national computational social science by enabling large‑scale extraction of relational data from multilingual news corpora without proprietary APIs or manual coding.

## Related Concepts  
- Joint entity‑relation extraction  
- Named‑entity recognition (NER)  
- Wikidata linking cascade  
- Mixture‑of‑Experts (MoE) models  
- Ontology‑constrained decoding  
- Temporal knowledge graphs
