# Summary: 2026-08-02_21-36-59Z_DeepAgenticSearchforRepository_LevelCodeQuestionAn.md
Saved: 2026-08-04 00:23
Source: 2026-08-02_21-36-59Z_DeepAgenticSearchforRepository_LevelCodeQuestionAn.md
Model: None

---

## Summary  
The paper investigates two dominant paradigms for answering questions that span an entire code repository: (1) semantic search, which retrieves pre‑indexed code blocks from a vector store, and (2) deep agentic search, a planner‑subagent pipeline that isolates the sub‑agent’s context to avoid “context rot.” The authors empirically compare these approaches on SWE‑QA, showing that deep agentic search yields higher answer correctness at the expense of compute cost. They also introduce a taxonomy that reveals where failures occur, especially at the hand‑off between planner and sub‑agent.

## Key Contributions  
- [Finding 1] Deep agentic search achieves 65.2 % correct answers on SWE‑QA versus 46.2 % for semantic search, indicating superior accuracy despite higher cost.  
- [Finding 2] A failure taxonomy shows that 41.8 % of deep‑agent failures are caused by the planner‑subagent hand‑off, producing fluent yet incorrect answers.  
- [Finding 3] For read‑only queries over a static repository, pure retrieval remains cheaper and more accurate than deep agentic search.

## Methodology  
The authors implement both paradigms on the SWE‑QA benchmark, measuring answer accuracy and token consumption per query. Each failed run is recorded and classified into failure modes to build a taxonomy that captures systematic weaknesses of the planner‑subagent pipeline.

## Results  
Deep agentic search outperforms semantic search in correctness (65.2 % vs 46.2 %) but requires roughly twice as many tokens per query, reflecting higher computational expense. The failure taxonomy confirms that the majority of errors stem from the hand‑off stage, where the sub‑agent’s output is silently accepted without verification.

## Significance  
These findings clarify a long‑standing trade‑off in code agents: richer context can improve answer quality but introduces hidden costs and error propagation. For static read‑only queries, retrieval remains the more efficient strategy, guiding future system design toward cost‑aware context engineering.

## Related Concepts  
Semantic search, deep agentic search (also called grep‑search), context rot, code agents such as Claude Code or Codex, planner‑subagent architecture, SWE‑QA benchmark, token cost, taxonomy of failures.
