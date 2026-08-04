# Summary: 2026-08-02_21-36-59Z_DeepAgenticSearchforRepository_LevelCodeQuestionAn.md
Saved: 2026-08-04 00:23
Source: 2026-08-02_21-36-59Z_DeepAgenticSearchforRepository_LevelCodeQuestionAn.md
Model: None

---

## Summary  
The paper investigates two code‑agent strategies for answering repository‑level questions: semantic search using a pre‑built vector index and deep agentic search where a planner delegates work to a sub‑agent operating in an isolated context window. By benchmarking both methods on the SWE‑QA dataset, the authors find that while deep agentic search is praised for mitigating context rot, it actually yields lower accuracy than semantic search and incurs higher failure rates at the handoff point between planner and sub‑agent.  

## Key Contributions  
- [Finding 1] Deep agentic search’s accuracy on SWE‑QA (46.2 %) is significantly lower than that of semantic search (65.2 %).  
- [Finding 2] The majority of deep agentic search failures (≈41.8 %) stem from the planner‑sub‑agent handoff, producing fluent yet incorrect answers.  
- [Finding 3] Protecting the main context window with a sub‑agent may add overhead; for read‑only queries over an indexed repository, plain retrieval remains cheaper and more reliable.  

## Methodology  
The authors evaluate both approaches on SWE‑QA, which contains 10 000 code questions paired with correct answers. For semantic search they retrieve relevant code blocks from a dense vector index built once per repository and feed them to the main agent. For deep agentic search they instantiate a planning sub‑agent that works within a limited context window; the planner queries this sub‑agent, receives a condensed result, and then generates an answer. All runs are recorded, and any incorrect output is classified into failure modes using a taxonomy derived from debugging logs.  

## Results  
The benchmark shows semantic search achieving 65.2 % correct answers at minimal cost, whereas deep agentic search reaches only 46.2 % correct answers while incurring higher latency and more complex error handling. The taxonomy reveals that handoff failures dominate the error profile, accounting for nearly half of all mistakes.  

## Significance  
These findings challenge the assumption that context‑protection is a free benefit; instead they demonstrate that it can degrade performance on read‑only queries when an index exists. Practitioners should weigh the trade‑off between accuracy and cost, preferring retrieval for static code questions.  

## Related Concepts  
Deep Agentic Search, Context Pollution, Context Rot, Semantic Search, Vector Index, SWE‑QA benchmark, Retrieval Cost Analysis, Planner‑Subagent Handoff.
