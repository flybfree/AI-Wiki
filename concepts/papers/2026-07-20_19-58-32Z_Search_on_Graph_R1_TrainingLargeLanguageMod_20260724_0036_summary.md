# Summary: 2026-07-20_19-58-32Z_Search_on_Graph_R1_TrainingLargeLanguageModelstoSe.md
Saved: 2026-07-24 00:36
Source: 2026-07-20_19-58-32Z_Search_on_Graph_R1_TrainingLargeLanguageModelstoSe.md
Model: None

---

## Summary  
The paper introduces Search‑on‑Graph‑R1 (Sogrone{}), a method that trains large language models to answer knowledge graph questions by internalizing navigation into an 8B model using supervised fine‑tuning and reinforcement learning. It achieves strong performance on benchmark datasets without requiring auxiliary modules or LLM judges at inference.

## Key Contributions  
- [Finding 1] Sogrone{} integrates a frontier teacher with each question’s gold SPARQL query, enabling the model to follow a known answer path via live Search tool calls.  
- [Finding 2] The approach achieves state‑of‑the‑art results on WebQSP, CWQ, and GrailQA, surpassing all frozen frontier‑LLM systems and setting new records on CWQ.  
- [Finding 3] Reinforcement learning reduces the number of Search calls needed to reach answers compared with its supervised initialization.

## Methodology  
The authors scaffold a large language model by fine‑tuning it on a dataset where each example includes the question, gold SPARQL query, and the teacher’s traversal path. During SFT, the model learns to generate queries that align with known paths; RL then optimizes for efficiency by rewarding fewer Search calls. At inference, the model uses only its own 8B parameters and a live Freebase Search tool without additional modules.

## Results  
On WebQSP, CWQ, and GrailQA, Sogrone{} outperforms all frozen frontier‑LLM baselines, with the strongest performance on CWQ among compared systems. Training experiments isolate gains: supervised fine‑tuning provides baseline improvement, while reinforcement learning adds further efficiency and accuracy. The method transfers across different model families and requires no auxiliary components at deployment.

## Significance  
By embedding graph navigation directly into a compact 8B model, Sogrone{} reduces reliance on costly frontier inference, enabling scalable deployment of knowledge‑aware LLMs. Its RL‑driven optimization demonstrates that reinforcement learning can enhance both efficiency and answer quality without external supervision.

## Related Concepts  
Knowledge Graph Question Answering (KGQA), SPARQL queries, reinforcement learning for model training, supervised fine‑tuning, Live Search tool integration, frontier LLM, 8B parameter model, Freebase server, trajectory grounding, query generation, path following.
