# Summary: 2026-07-22_12-11-51Z_PRO_LONG_ProgrammaticMemoryEnablesLong_HorizonReas.md
Saved: 2026-07-24 01:49
Source: 2026-07-22_12-11-51Z_PRO_LONG_ProgrammaticMemoryEnablesLong_HorizonReas.md
Model: None

---

## Summary  
The paper introduces PRO‑LONG, a programmatic memory framework that enables large language model agents to perform long‑horizon reasoning by storing a complete, structured interaction log and retrieving relevant information efficiently via coding agents. It directly addresses the tradeoff between preserving context and making retrieval tractable, which is a persistent challenge for continual learning benchmarks such as ARC‑AGI‑3. On this benchmark, PRO‑LONG improves frontier models’ average pass@1 by 18 percentage points while using far fewer tokens than specialized harnesses. The approach matches or exceeds state‑of‑the‑art performance at a lower computational cost.

## Key Contributions  
- [Finding 1] Programmatic memory provides a structured interaction log that captures every observation and agent action.  
- [Finding 2] Recent coding agents can efficiently search this log to retrieve relevant context, mitigating the retrieval tractability issue.  
- [Finding 3] PRO‑LONG achieves higher pass@1 scores than specialized harnesses while using 4.2–5.8× fewer tokens.

## Methodology  
The authors designed PRO‑LONG as a minimal context‑management framework that records each observation and agent action in a structured log, then leverages a coding agent (e.g., Fable) to query the log for pertinent information when needed. The retrieval is performed via programmatic code that parses logs and selects pertinent entries, avoiding full context injection into the model.

## Results  
On the ARC‑AGI‑3 game set, PRO‑LONG boosts frontier models’ average pass@1 by 18 percentage points compared with a base coding agent. It matches or exceeds specialized harnesses up to 76.1% pass@1 while using 4.2–5.8× fewer tokens. With Fable 5, it reaches 97.4% best@2 at a total cost of $1,750.

## Significance  
This work demonstrates that programmatic memory can close the long‑horizon reasoning gap for LLMs, offering a scalable solution that reduces token usage and computational expense, enabling more efficient continual learning and exploration.

## Related Concepts  
- Long‑horizon reasoning  
- Programmatic memory  
- Context management tradeoff  
- Coding agents (e.g., Fable)  
- Retrieval tractability  
- Continual learning benchmarks (ARC‑AGI‑3)
