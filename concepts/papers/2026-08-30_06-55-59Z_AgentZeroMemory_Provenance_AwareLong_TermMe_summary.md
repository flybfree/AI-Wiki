# Summary: 2026-08-30_06-55-59Z_AgentZeroMemory_Provenance_AwareLong_TermMemoryfor.md
Saved: 2026-08-31 21:06
Source: 2026-08-30_06-55-59Z_AgentZeroMemory_Provenance_AwareLong_TermMemoryfor.md
Model: None

---

## Summary  
The paper introduces **Agent Zero Memory**, a provenance‑aware long‑term memory system for LLM agents that stores user conversations, files, and sources in three parallel structures to capture the full history faithfully without fabrication. It integrates an episodic timeline, an associative entity‑event knowledge graph, and a citation‑locked hierarchical documentary memory while using an intent gate and source router to enable self‑contained retrieval with minimal latency. The approach formalizes a reading discipline where every learned item carries its origin, timestamp, and evidence pointer, and answers are generated only from opened evidence, abstaining rather than guessing. Experiments on LongMemEval (95.60 %) and LoCoMo (93.60 %) set new state‑of‑the‑art levels, outperforming prior methods by +0.73 and +1.10 points respectively.

## Key Contributions  
- **Provenance‑aware multi‑modal memory architecture** that separates temporal events, entity‑event links, and citation‑locked facts into three distinct systems.  
- **Intent gate and source router** that make retrieval self‑contained, reducing latency while preserving ground‑truth grounding.  
- **Formal reading discipline** that restricts citations to evidence the reader actually opened, structurally excluding fabrication.

## Methodology  
The authors designed Agent Zero Memory as a system where each user interaction is parsed into three memory components: an episodic timeline records when changes occur, an associative knowledge graph links people and projects across sessions, and a hierarchical documentary memory (HDM) stores durable facts with provenance metadata. Retrieval begins with an intent gate to filter out unnecessary processing, followed by a source router that routes the query to each of three concurrent agentic searches—each employing hybrid embedding‑lexical search under user‑defined filters—to retrieve relevant items from its respective memory system. The results are integrated into a single answer while respecting citation locks; if no valid evidence exists, the system abstains rather than fabricates an answer.

## Results  
On LongMemEval, Agent Zero Memory achieves 95.60 % accuracy, improving over the strongest prior systems by +0.73 points. On LoCoMo it reaches 93.60 %, a gain of +1.10 points relative to top baselines. A controlled study across eight backbone LLMs shows that adding memory raises accuracy by up to 3.4 points while reducing cost per query by ~30× and latency by up to 20× compared with model‑only approaches, indicating that quality is driven primarily by memory rather than the underlying language model.

## Significance  
This work demonstrates that memory can be a primary driver of conversational quality, not merely an auxiliary boost, offering a scalable, trustworthy long‑term memory for LLM agents in high‑stakes domains such as healthcare and finance where factual accuracy is critical. By enforcing provenance constraints through citation locks, the system eliminates fabrication, enabling reliable agentic behavior that can be audited and verified.

## Related Concepts  
- Provenance  
- Episodic Memory Events timeline  
- Associative Knowledge Graph  
- Hierarchical Documentary Memory (HDM)  
- Citation Lock  
- Intent Gate  
- Source Router  
- Agentic Search  
- Hybrid Embedding‑Lexical Retrieval
