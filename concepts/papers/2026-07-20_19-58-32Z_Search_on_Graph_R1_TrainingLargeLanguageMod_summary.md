# Summary: 2026-07-20_19-58-32Z_Search_on_Graph_R1_TrainingLargeLanguageModelstoSe.md
Saved: 2026-07-24 00:25
Source: 2026-07-20_19-58-32Z_Search_on_Graph_R1_TrainingLargeLanguageModelstoSe.md
Model: None

---

## Summary  
The paper tackles Knowledge Graph Question Answering (KGQA) by training a large language model to navigate graphs efficiently, eliminating the need for costly frontier‑scale inference. It introduces **Search‑on‑Graph‑R1** (\sogrone{}), an 8 billion‑parameter model that learns both supervised graph navigation and reinforcement strategies. The core contribution is a teacher‑guided RL pipeline that uses live SPARQL queries as scaffolds, producing trajectories grounded in the knowledge graph from the start. This approach yields state‑of‑the‑art performance on benchmark datasets while requiring no auxiliary inference modules at deployment.

## Key Contributions  
- **Compact 8B model via SFT + RL** – The authors embed navigation into a compact 8 billion‑parameter model through supervised fine‑tuning followed by reinforcement learning, achieving strong results without expanding to frontier‑scale inference.  
- **Teacher‑scaffolded live Search tool** – Each question is paired with its gold SPARQL query; the teacher traverses the known answer path using a live Freebase \texttt{Search} tool, guaranteeing that every retrieved node belongs to the graph.  
- **RL reduces Search calls** – Reinforcement learning refines the model’s policy so it reaches answers in fewer \texttt{Search} invocations than its SFT baseline, improving efficiency and accuracy.

## Methodology  
The authors adopt a two‑stage training pipeline. First, they perform supervised fine‑tuning (SFT) where each training example consists of a KG question, the corresponding gold SPARQL query, and the answer path that the teacher follows using the live Search tool. This creates a dataset of “grounded” trajectories. Second, they apply reinforcement learning (RL) to optimize the model’s decision‑making: the reward is derived from reaching the correct answer with minimal Search calls. The RL loop iteratively adjusts the model’s policy without any external LLM judge or auxiliary module at inference time.

## Results  
On three benchmark sets—WebQSP, CWQ, and GrailQA—the \sogrone{} 8 b model outperforms every frozen frontier‑LLM system in our comparison. It achieves the strongest performance on CWQ among all evaluated methods. Crucially, inference requires no auxiliary module; the model relies solely on its learned policy to invoke Search. Isolation studies reveal that SFT and RL contribute complementary gains: SFT provides a solid base, while RL further reduces the number of Search calls required to answer questions.

## Significance  
This work demonstrates that large language models can be trained to perform knowledge‑graph navigation efficiently, lowering deployment costs and improving accuracy for KGQA tasks. By integrating reinforcement learning with teacher‑guided supervision, \sogrone{} offers a scalable alternative to costly frontier inference, enabling broader accessibility of graph‑aware AI without sacrificing performance.

## Related Concepts  
- Knowledge Graph Question Answering (KGQA)  
- SPARQL queries and path traversal  
- Reinforcement learning for policy optimization  
- Supervised fine‑tuning (SFT) of LLMs  
- Frontier large language models  
- Live Search tool integration with Freebase  
- 8 billion‑parameter model compression
