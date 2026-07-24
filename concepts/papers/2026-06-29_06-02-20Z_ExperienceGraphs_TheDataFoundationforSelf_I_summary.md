# Summary: 2026-06-29_06-02-20Z_ExperienceGraphs_TheDataFoundationforSelf_Improvin.md
Saved: 2026-07-23 23:36
Source: 2026-06-29_06-02-20Z_ExperienceGraphs_TheDataFoundationforSelf_Improvin.md
Model: None

---

## Summary  
The paper proposes Experience Graphs as a data foundation for self‑improving agents, treating the structured search output of long‑horizon tasks—such as code generation or scientific discovery—as a durable database state. It introduces Trellis, a queryable graph database that enables crash recovery, horizontal scaling, and closed‑loop training without requiring agents to retain internal state. By modeling experience graphs as first‑class DB objects, the authors achieve a 10× speedup and a 52 % reduction in token cost on a production optimizer.

## Key Contributions  
- [Finding 1] Experience Graphs capture executable artifacts, tool outputs, rewards, sibling comparisons, and causal lineage from long‑horizon agentic tasks.  
- [Finding 2] Trellis treats the experience graph as a first‑class database entity, enabling queries for frontier selection, cross‑session reuse, training data extraction, and time‑travel reconstruction.  
- [Finding 3] Empirical results on KernelEvolve show 10× speedup and 52 % lower token cost via cross‑session reuse.

## Methodology  
The authors instrument agents to emit structured experience records that are stored in a relational graph database. Trellis provides APIs for query operations: SELECT frontier, JOIN across sessions, materialized view extraction for training data, and time‑travel queries to reconstruct past knowledge states. The design decouples state from computation, allowing agents to be stateless compute units.

## Results  
Experiments on KernelEvolve demonstrate that Trellis reduces token consumption by 52 % while achieving up to 10× faster inference through reuse of previously computed experiences. Cross‑session graph retrieval speeds up frontier selection, and crash recovery restores the full experience graph without loss.

## Significance  
This work shifts experience logs from disposable JSON checkpoints to a persistent institutional asset, enabling reliable agent operation across failures and scaling. It fosters cumulative learning and efficient training loops, turning inference‑time search into a durable resource that can be queried, reused, and trained on.

## Related Concepts  
- Experience Graphs: structured representation of agentic search outcomes.  
- Trellis: graph database for experience storage and querying.  
- Stateless compute agents: decoupling state from computation.  
- Materialized views: extracting training data from graphs.  
- Time‑travel queries: reconstructing past knowledge states.
