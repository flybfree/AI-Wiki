# Summary: 2026-07-29_17-46-35Z_ImprovingItemDiscoverabilityine_CommerceSearchviaR.md
Saved: 2026-07-29 22:30
Source: 2026-07-29_17-46-35Z_ImprovingItemDiscoverabilityine_CommerceSearchviaR.md
Model: None

---

## Summary  
The paper aims to improve item discoverability in e‑commerce search by generating implicit user intents that expand recall while preserving relevance. It proposes a scalable discovery‑augmented search system that leverages intent‑conditioned retrieval. The approach uses a two‑stage hybrid architecture combining closed‑weight large language models and a fine‑tuned small language model to handle head and tail queries efficiently. Evaluation is performed using both human preference metrics and end‑to‑end purchase analysis.  

## Semantic links
- [[concepts/papers/2026-07-21_16-04-35Z_In_ContextTimeSeriesClassificationwithRando_summary.md|Summary: 2026-07-21_16-04-35Z_In_ContextTimeSeriesClassificationwithRandomConvol.md]] — 3 title terms overlap; 1 backlink; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 1 backlink; 6 summary/topic terms overlap
- [[concepts/papers/2026-08-03_15-03-35Z_KC_Agent_ADual_ProcessCognitiveArchitecture_20260804_0042_summary.md|Summary: 2026-08-03_15-03-35Z_KC_Agent_ADual_ProcessCognitiveArchitectureforEffi.md]] — 3 title terms overlap; 9 summary/topic terms overlap; semantic match 0.09

## Key Contributions  
- Closed‑weight LLMs significantly boost discoverability for head queries, extending coverage from about 60% to roughly 80% of query traffic.  
- A finetuned small language model trained via LoRA adapters and teacher‑student distillation reduces inference cost by around 30% while maintaining high quality.  
- The discovery‑augmented search framework can act as a marketplace‑balancing mechanism, giving long‑tail and emerging items exposure based on query conditions.  

## Methodology  
The authors address the precision‑recall tradeoff by first using closed‑weight LLMs to generate rich implicit intents for head queries, then extending those benefits to tail queries with a finetuned small language model. The SLM is trained through LoRA adapters and teacher‑student distillation, allowing it to inherit knowledge from the LLM while being lightweight. This two‑stage hybrid architecture balances quality and computational cost.  

## Results  
Experimental results show that intent generation quality improves across both head and tail queries, leading to higher downstream retrieval effectiveness. The system achieves a 20% absolute increase in recall (60%→80%) with only about one‑third the inference cost of the teacher model, demonstrating a favorable cost‑quality tradeoff.  

## Significance  
This work matters because it tackles the limitation of precision‑only search in grocery e‑commerce, where discoverability drives satisfaction and sales. By enabling broader recall at lower cost, the approach supports long‑tail products and emerging suppliers, potentially reshaping marketplace dynamics and improving overall system fairness.  

## Related Concepts  
Intent generation, recall expansion, closed‑weight LLMs, fine‑tuned small language model, LoRA adapters, teacher‑student distillation, discovery‑augmented search, cost‑quality tradeoff, dual evaluation framework.
