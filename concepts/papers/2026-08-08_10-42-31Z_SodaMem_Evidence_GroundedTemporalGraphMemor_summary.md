# Summary: 2026-08-08_10-42-31Z_SodaMem_Evidence_GroundedTemporalGraphMemoryforLLM.md
Saved: 2026-08-10 22:53
Source: 2026-08-08_10-42-31Z_SodaMem_Evidence_GroundedTemporalGraphMemoryforLLM.md
Model: None

---

## Summary  
The paper SodaMem tackles the challenge of maintaining up‑to‑date, provenance‑aware memory for large language model agents that operate over long conversational horizons. It introduces an evidence‑grounded temporal graph memory that records typed FactEvents with explicit provenance spans and stores them using a hybrid indexing scheme, enabling planners to retrieve only relevant citations before generating responses. Experiments on the LongMemEval‑S benchmark show that SodaMem achieves 92.8 % accuracy at a cost of roughly $0.0016 per question, outperforming higher‑cost alternatives while staying within Flash‑tier compute budgets. The work thus bridges the gap between factual recall and computational efficiency for LLM agents.

## Key Contributions  
- [Finding 1] SodaMem extracts typed FactEvents with mandatory provenance spans, providing a structured store of facts that includes mention time, occurrence time, and validity intervals.  
- [Finding 2] The system persists these events as nodes in a temporal graph using SUPERSEDES/CONTRADICTS/UPDATES edges under hybrid lexical‑dense indexing, ensuring accurate temporal reasoning.  
- [Finding 3] A planner‑reader loop gathers citable evidence before composing the final answer, delivering both high accuracy and low per‑question cost.

## Methodology  
The authors first parse user dialogue into FactEvents, annotating each with a provenance span that links source text to the event. These events are indexed in two complementary ways: a lexical index for fast term retrieval and a dense graph index that stores temporal relationships as directed edges (SUPERSEDES, CONTRADICTS, UPDATES). The planner queries the graph for events whose validity interval overlaps the current conversation window, then feeds the retrieved citations to the reader model. This loop repeats until a satisfactory answer is produced. All components are implemented in Python and released on GitHub.

## Results  
On LongMemEval‑S, SodaMem’s store‑of‑record configuration achieved 92.8 % accuracy (464/500 questions; best of N=3). The average cost per question was $0.00161 with a median of $0.00111, corresponding to ~18.3k tokens and ~14.6k tokens respectively for the DeepSeek‑V4‑Flash model used as both reader and judge. A cost‑accuracy map shows SodaMem dominating several higher‑cost, lower‑accuracy points, indicating that its hybrid indexing yields near‑frontier performance at Flash‑tier spend.

## Significance  
SodaMem demonstrates that LLM agents can maintain factual consistency over weeks of interaction without incurring prohibitive compute costs. By grounding memory in explicit provenance and using a planner‑reader loop, it improves both accuracy and efficiency, offering a practical solution for long‑term conversational AI systems where upkeep is critical.

## Related Concepts  
- FactEvent extraction  
- Temporal graph reasoning (SUPERSEDES/CONTRADICTS/UPDATES)  
- Hybrid lexical‑dense indexing  
- Planner‑reader loop in LLM agents  
- Cost‑accuracy tradeoff analysis
