# Summary: 2026-07-25_06-47-46Z_SearchArt_TrainingLong_HorizonSearchAgentwithScala.md
Saved: 2026-07-28 20:17
Source: 2026-07-25_06-47-46Z_SearchArt_TrainingLong_HorizonSearchAgentwithScala.md
Model: None

---

## Summary  
The paper introduces SearchArt, a framework for training long‑horizon search agents that can plan and execute multi‑step information‑seeking tasks. It addresses two core challenges: the scarcity of scalable synthetic tasks and the difficulty of verifying intermediate reasoning steps. By synthesizing large datasets from web documents and constructing evidence graphs, SearchArt creates verified task trajectories that guide a reinforcement‑learning pipeline. The resulting agents achieve performance comparable to state‑of‑the‑art closed models on benchmark benchmarks.  

## Key Contributions  
- Scalable synthetic dataset generation with an integrated verification pipeline that checks QA consistency, trajectory quality, and evidence relevance.  
- A multi‑stage training process combining supervised fine‑tuning and reinforcement learning policy optimization to learn adaptive search planning.  
- Demonstrated long‑horizon search capabilities with a modest 27B‑parameter model that matches or exceeds the best closed‑source agents on deepsearch and deepresearch benchmarks.  

## Methodology  
SearchArt builds a large corpus of QA pairs and their corresponding search trajectories by extracting information‑seeking queries from web documents, constructing evidence graphs that map retrieved snippets to answers, and applying a verification pipeline that jointly evaluates QA consistency, trajectory quality, and relevance before the data are used in training. The pipeline ensures only reliable synthetic examples enter the supervised fine‑tuning phase, after which an RL loop refines the agent’s search policy through iterative evidence aggregation.  

## Results  
The search agents trained with SearchArt score 74.39 on BrowseComp‑ZH, 70.06 on BrowseComp, and 52.55 on Deepresearch‑benchmark, matching or surpassing the best closed‑source models on both deepsearch and deepresearch benchmarks.  

## Significance  
This work demonstrates that long‑horizon autonomous search can be reliably trained using synthetic data with built‑in verification, reducing reliance on costly human‑annotated tasks. It opens a path toward scalable LLM agents that can explore web information over extended horizons without manual supervision and enables rapid iteration across diverse domains.  

## Related Concepts  
- long‑horizon search  
- synthetic dataset generation  
- verification pipeline  
- evidence graph  
- reinforcement learning policy optimization  
- supervised fine‑tuning  
- search trajectory  
- LLM agent training
