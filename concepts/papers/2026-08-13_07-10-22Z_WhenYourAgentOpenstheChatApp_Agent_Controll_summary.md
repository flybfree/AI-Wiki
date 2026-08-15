**Original paper:** [https://arxiv.org/abs/2608.12888v1](https://arxiv.org/abs/2608.12888v1)

# Summary: 2026-08-13_07-10-22Z_WhenYourAgentOpenstheChatApp_Agent_ControlledSearc.md
Saved: 2026-08-13 22:41
Source: 2026-08-13_07-10-22Z_WhenYourAgentOpenstheChatApp_Agent_ControlledSearc.md
Model: None

---

## Summary  
The paper investigates whether the performance gains of agent‑memory systems stem from built‑in semantic structures or from effective retrieval over raw chat logs. It introduces ReFind, an agent‑controlled search interface that queries unmodified conversation archives using only lexical indexing and four chat‑native controls, thereby showing that rich memory representations are not necessary for high accuracy.  

## Key Contributions  
- [Finding 1] The authors demonstrate that a simple iterative keyword‑search loop combined with four specific user‑driven refinements can outperform state‑of‑the‑art graph‑based and tree‑based memory systems on conversational tasks.  
- [Finding 2] ReFind achieves the highest mean accuracy (58.2) across a suite of QA, event ordering, and fact‑consolidation benchmarks while using only GPT‑4o‑mini as its backbone, without constructing any semantic index.  
- [Finding 3] The results hold on LongMemEval‑S/M, where ReFind reaches 93.2 ± 3.3 for precise retrieval and 89.3 ± 6.0 for fact tracking, matching or exceeding the best structured memory models.  

## Methodology  
The authors treat the conversation archive as a raw sequence of turns indexed lexically at turn granularity. ReFind operates in two stages: (1) an agent‑driven search loop where the user can expand context, narrow time windows, skip already inspected sessions, and fuse rankings; (2) a reasoning stage that synthesizes retrieved evidence into answers. No LLM is used to generate embeddings or knowledge graphs; all indexing is purely lexical.  

## Results  
Across MemoryAgentBench’s incremental multi‑turn setting, ReFind scores 58.2 % mean accuracy—significantly above HippoRAG 2 (53.2 %). Component ablation studies isolate the contributions of agent control, chat‑native controls, and pure lexical retrieval. On LongMemEval‑S/M with GPT‑5‑mini, ReFind reaches 93.2 ± 3.3 for precise retrieval and 89.3 ± 6.0 for fact tracking.  

## Significance  
These findings suggest that elaborate memory structures provide only marginal benefits when agents can directly search raw logs; conversely, well‑designed agentic search interfaces can match or surpass structured memory systems in performance and efficiency.  

## Related Concepts  
- Agent‑controlled retrieval  
- Lexical indexing of conversation turns  
- Iterative keyword search loops  
- Session‑aware rank fusion  
- Temporal narrowing  
- Structured memory (graph, tree)
