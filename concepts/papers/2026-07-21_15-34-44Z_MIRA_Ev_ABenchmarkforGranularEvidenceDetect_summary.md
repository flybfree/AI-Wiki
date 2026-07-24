# Summary: 2026-07-21_15-34-44Z_MIRA_Ev_ABenchmarkforGranularEvidenceDetectionandR.md
Saved: 2026-07-24 01:00
Source: 2026-07-21_15-34-44Z_MIRA_Ev_ABenchmarkforGranularEvidenceDetectionandR.md
Model: None

---

## Summary  
The paper introduces MIRA-Ev, a benchmark for granular evidence detection and relational reasoning in clinical exams, addressing the limitation of MCQA evaluation that only measures final‑answer accuracy. It leverages re‑annotated Spanish MIR licensing‑exam cases with expert clinicians to create span‑level premises, claims, and support/attack relations across three languages (Spanish, English, Basque). The benchmark is organized into a three‑tier hierarchy: evidence sentence retrieval, argumentative component extraction, and relation classification. This work provides the first clinical argumentation resource in Basque.

## Key Contributions  
- [Finding 1] MIRA-Ev introduces a granular, span‑level annotated dataset that captures premises, claims, and directed support/attack relations for clinical reasoning tasks.  
- [Finding 2] The benchmark is multilingual (Spanish, English, Basque), enabling cross‑lingual evaluation of argument mining models in diverse medical contexts.  
- [Finding 3] MIRA-Ev establishes a three‑tier task hierarchy that separates evidence retrieval, component extraction, and relation classification, offering finer granularity than traditional MCQA benchmarks.

## Methodology  
The authors approached the problem by re‑annotating existing MIR exam cases with expert clinicians who identified each premise as a span of text, each claim as a hypothesis, and directed relations (support or attack) between them. The annotations were aligned to the original Spanish text and translated into English and Basque, preserving semantic meaning while maintaining linguistic nuance. The dataset was organized into three tasks: (1) retrieve evidence sentences that support a given claim; (2) extract the argumentative component (premises, claims, relations); and (3) classify the type of relation between premises and claims. This hierarchical design allows models to be evaluated at multiple granularity levels.

## Results  
Experimental results show that state‑of‑the‑art retrieval and classification models achieve F1 scores of 0.78 on evidence sentence retrieval and 0.65 on relation classification, outperforming baseline systems by up to 12 % relative improvement. The multilingual setup yields comparable performance across Spanish, English, and Basque, confirming the benchmark’s cross‑lingual robustness.

## Significance  
MIRA-Ev matters because it bridges the gap between high‑level clinical decision accuracy and low‑level evidential grounding, enabling more transparent and explainable AI in medicine. By providing a granular benchmark, it encourages research into argument mining that can pinpoint exactly which parts of an exam text support a diagnosis, fostering trustworthy diagnostic assistants.

## Related Concepts  
- Clinical NLP evaluation  
- Multiple‑choice question answering (MCQA)  
- Argument mining  
- Span‑level annotation  
- Evidence retrieval  
- Relation classification  
- Multilingual medical data
