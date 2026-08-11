# Summary: 2026-08-07_18-00-02Z_KeepItSimple_Multi_KeyEpisodicMemoryRetrievalforUl.md
Saved: 2026-08-10 22:38
Source: 2026-08-07_18-00-02Z_KeepItSimple_Multi_KeyEpisodicMemoryRetrievalforUl.md
Model: None

---

## Summary  
Ultra‑long videos that span hours to days pose a challenge for current Multi‑modal Large Language Models (MLLMs) because end‑to‑end processing is computationally infeasible. This paper introduces **MERIT**, a simple yet effective agentic framework that separates memory construction from retrieval, allowing high‑recall episodic memory building without prior knowledge of the downstream query and then performs query‑specific composition at inference time. By using a multi‑key episodic representation and an on‑demand temporal expansion mechanism, MERIT achieves state‑of‑the‑art understanding across three long‑video benchmarks.

## Key Contributions  
- [Finding 1] The authors propose **MERIT**, a two‑stage paradigm that constructs query‑agnostic memory and retrieves it at inference time.  
- [Finding 2] They formulate an **episodic multi‑key representation** that enables precise retrieval via simple key‑matching, allowing fine‑grained memory access.  
- [Finding 3] A **neighbor filtering mechanism** is introduced to capture broader semantic context without building a global memory, by expanding temporal scope only around retrieved segments.

## Methodology  
The method follows a query‑agnostic construction followed by retrieval‑based inference. First, the system builds an episodic representation using multi‑key tokens that encode fine‑grained video events; this step focuses on high recall rather than complex relational modeling. At inference, MERIT matches the user’s query to these keys and then expands the temporal window around each retrieved segment to include neighboring frames, capturing broader context without pre‑computing a massive global memory. The composition of high‑level relations is deferred to this stage, keeping construction lightweight.

## Results  
MERIT attains state‑of‑the‑art performance on three long‑video benchmarks: **EgoLifeQA**, **LVBench**, and **Video‑MME (Long)**. Quantitative results show higher recall and F1 scores compared with prior approaches that rely on full global memory construction, confirming the effectiveness of the key‑matching and on‑demand expansion strategies.

## Significance  
This work demonstrates that ultra‑long video understanding can be achieved with a simple two‑stage pipeline: a lightweight, high‑recall memory build followed by efficient retrieval. By avoiding costly global memory construction, MERIT reduces computational load and latency, making it practical for real‑world applications where videos may last hours or even days.

## Related Concepts  
- Multi‑modal Large Language Models (MLLMs)  
- Episodic memory in AI systems  
- Retrieval‑based inference  
- Key‑matching retrieval mechanisms  
- Temporal expansion / neighbor filtering  
- Two‑stage processing architectures
