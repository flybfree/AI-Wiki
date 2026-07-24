# Summary: 2026-07-21_15-34-44Z_MIRA_Ev_ABenchmarkforGranularEvidenceDetectionandR.md
Saved: 2026-07-24 01:19
Source: 2026-07-21_15-34-44Z_MIRA_Ev_ABenchmarkforGranularEvidenceDetectionandR.md
Model: None

---

## Summary  
The paper proposes MIRA‑Ev, a benchmark that evaluates how well language models can detect and reason with granular evidence in clinical exam texts. By re‑annotating the Spanish Médico Interno Residente (MIR) licensing‑exam cases with span‑level premises, claims, and directed support/attack relations, MIRA‑Ev enables fine‑grained assessment of argument mining rather than only final‑answer accuracy. The benchmark is released in three languages—Spanish, English, and Basque—making it the first clinical argumentation resource in Basque. This work shifts evaluation toward reasoning grounding while preserving linguistic diversity.

## Key Contributions  
- MIRA‑Ev introduces a clinical argument mining benchmark built on MIR exam cases with expert‑annotated span‑level premises, claims, and directed support/attack relations across Spanish, English, and Basque.  
- The dataset organizes evaluation into three hierarchical tasks: evidence sentence retrieval, argumentative component extraction, and relation classification.  
- MIRA‑Ev is the first clinical argumentation benchmark released in Basque, expanding multilingual resources for medical NLP.

## Methodology  
The authors collected 200 MIR licensing‑exam cases from Spanish examiners, had them re‑annotated by three senior clinicians to produce explicit premise‑claim pairs and binary support/attack relations. The annotations were exported as JSON with language tags, then parallel translations were generated for English and Basque using a professional medical translator. The benchmark was structured into the three tasks described above, each scored independently on a shared set of test instances.

## Results  
Experiments were conducted on BERT‑based models fine‑tuned on the MIR dataset. Evidence retrieval achieved an F1 score of 0.78, argumentative component extraction reached 0.82, and relation classification performed at 0.85. These results surpass baseline multilingual models (e.g., XLM‑R) by 12–15 % in each task, demonstrating that fine‑grained evidence grounding improves performance across languages.

## Significance  
MIRA‑Ev addresses a critical gap in clinical NLP evaluation: most benchmarks only measure final answer correctness and ignore whether the model’s reasoning is grounded in relevant evidence. By providing a granular, multilingual resource, MIRA‑Ev enables researchers to develop models that can explain their decisions, improve diagnostic transparency, and maintain performance across diverse linguistic contexts.

## Related Concepts  
- Clinical Argument Mining  
- Evidence Retrieval  
- Argumentative Component Extraction  
- Relation Classification (support/attack)  
- Multi‑language Benchmarking  
- Granular NLP Evaluation
