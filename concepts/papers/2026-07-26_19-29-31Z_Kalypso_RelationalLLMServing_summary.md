# Summary: 2026-07-26_19-29-31Z_Kalypso_RelationalLLMServing.md
Saved: 2026-07-27 23:59
Source: 2026-07-26_19-29-31Z_Kalypso_RelationalLLMServing.md
Model: None

---

## Summary  
The paper introduces **Kalypso**, a system that makes large‑language‑model (LLM) serving aware of the relational structure of semantic queries while preserving query semantics and output accuracy. By enabling pipelined execution across operators, Kalypso can reuse key‑value cache (KV‑cache) states instead of recomputing them, which is a performance bottleneck in request‑centric LLM serving. The authors propose an adaptive, memory‑aware scheduler that continuously balances upstream parallelism, downstream progress, and GPU utilization to solve the online scheduling problem of pipelined operator execution under GPU memory pressure.

## Key Contributions  
- [Finding 1] Kalypso provides a relational abstraction for LLM serving that exposes an API for semantic query plans, allowing operators to be executed in pipeline order.  
- [Finding 2] The system introduces an adaptive, memory‑aware scheduling algorithm that reuses KV‑cache state before eviction, solving the online scheduling problem of balancing parallelism and GPU utilization.  
- [Finding 3] Experimental results show query completion times can be up to **4.57×** faster than baselines using request‑centric LLM serving across diverse workloads.

## Methodology  
Kalypso treats a semantic query as a relational plan composed of operators such as filtering, extraction, ranking, and transformation. The system’s API accepts this plan, which the scheduler interprets to order operator execution. Because operators share intermediate tuples, Kalypso reuses their KV‑cache across the pipeline rather than discarding it after each step. An adaptive scheduler monitors GPU memory pressure, dynamically adjusting allocations so that high‑throughput upstream work does not block downstream progress and GPU resources remain fully utilized.

## Results  
Across a suite of benchmark workloads—including filtering‑then‑ranking and extraction‑then‑joining tasks—the Kalypso pipeline reduced average query latency by up to **4.57×** compared with request‑centric LLM serving baselines. The adaptive scheduler also lowered GPU memory pressure, allowing longer runtimes without eviction spikes. Memory usage was comparable or lower than the baseline while achieving higher throughput.

## Significance  
This work demonstrates that query‑aware LLM serving can unlock substantial efficiency gains in semantic data processing pipelines. By making the relational structure visible to the model serving engine and reusing KV‑cache state, Kalypso reduces computational overhead and improves both latency and resource utilization—key concerns for real‑world applications that rely on large language models as semantic operators.

## Related Concepts  
- Relational algebra / query plans  
- Key‑value cache (KV‑cache) reuse in LLM inference  
- GPU memory pressure management  
- Adaptive scheduling algorithms  
- Request‑centric vs. query‑aware LLM serving
