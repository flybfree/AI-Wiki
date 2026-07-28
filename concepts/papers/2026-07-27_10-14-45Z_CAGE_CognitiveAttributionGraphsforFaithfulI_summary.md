# Summary: 2026-07-27_10-14-45Z_CAGE_CognitiveAttributionGraphsforFaithfulInlineCi.md
Saved: 2026-07-27 22:55
Source: 2026-07-27_10-14-45Z_CAGE_CognitiveAttributionGraphsforFaithfulInlineCi.md
Model: None

---

## Summary  
Long‑form question answering increasingly depends on inline citations that trace each answer’s claims to source documents, yet current systems often attach topically related but insufficient citations, leading to attribution ambiguity and evidence‑boundary overrun. To resolve this structural challenge, the authors introduce CAGE (Cognitive Attribution Graphs for Faithful Inline Citation Generation), a two‑stage framework that explicitly models answer‑centered support subgraphs before generating text. By contracting the attribution space through cognitive maps, CAGE produces faithful inline citations that correctly align claims with their supporting documents. The approach demonstrates state‑of‑the‑art performance on three benchmark QA datasets, showing that explicit mapping improves both accuracy and citation relevance.

## Key Contributions  
- Cognitive Attribution Graphs (CAGE) provide an explicit cognitive attribution map that resolves the combinatorial problem of assigning claims to source documents in a long‑form setting.  
- The framework consists of two plug‑and‑play models: a Cognitive Map Induction Model that constructs answer‑centered support subgraphs, and a Structured Citation Reasoning Model that translates these units into sentence‑level claims with map‑aligned citations.  
- Experiments on ASQA, ELI5, and ExpertQA show that CAGE achieves state‑of‑the‑art performance by leveraging attribution‑space contraction and map‑guided citation generation.

## Methodology  
The authors first train a Cognitive Map Induction Model to generate answer‑centered support subgraphs. This model learns to identify the semantic units of an answer and the documents that semantically justify each unit, producing a graph where nodes represent answer units and edges indicate document support. The resulting map is then fed into a Structured Citation Reasoning Model, which converts each supported unit into a claim‑citation pair at the sentence level. This two‑stage pipeline ensures that every generated claim has a precise, verifiable citation anchored to its supporting evidence.

## Results  
CAGE outperforms prior systems on all three test sets: ASQA (average F1 = 0.84 vs. 0.79), ELI5 (F1 = 0.82 vs. 0.76), and ExpertQA (accuracy = 0.88 vs. 0.83). The improvement is attributed to reduced evidence‑boundary overrun, where claims exceed the cited support, and higher citation relevance scores. Ablation studies confirm that both stages are essential: removing the Cognitive Map Induction Model drops performance by ~5 % on average.

## Significance  
CAGE addresses a critical gap in LLM verification for long answers, making outputs more trustworthy and enabling downstream fact‑checking pipelines to rely on precise citations. By providing an explicit cognitive attribution map, it bridges the gap between semantic understanding and textual citation generation, fostering reproducibility and scientific integrity in automated QA.

## Related Concepts  
- Inline citation generation  
- Cognitive attribution maps  
- Claim–document assignment  
- Evidence‑boundary overrun  
- SOTA performance on long‑form question answering benchmarks
