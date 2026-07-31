# Summary: 2026-07-30_05-41-44Z_Albilich_SteerableProof_StateOrchestrationforLLM_B.md
Saved: 2026-07-30 20:27
Source: 2026-07-30_05-41-44Z_Albilich_SteerableProof_StateOrchestrationforLLM_B.md
Model: None

---

## Summary  
The Albilich project aims to create an open‑source, agentic harness that orchestrates long‑horizon reasoning in large language models (LLMs) for mathematical research while integrating computer algebra systems (CAS). By coupling LLMs with persistent SQLite context management and literature retrieval, Albilich enables a human‑steerable workflow where the model can plan, execute, and revise proofs over extended problem spaces. The system’s primary contribution is demonstrating that such orchestration dramatically improves both proof generation efficiency and correctness when CAS tools are available.  

## Key Contributions  
- [Finding 1] Albilich solved all ten problems on the RealMath benchmark using CAS integration, achieving a perfect score (10/10).  
- [Finding 2] On the Kourovka Notebook’s open group‑theory problems, Albilich produced a counterexample to Problem 21.142 and provided a proof strengthening for Problem 20.2.  
- [Finding 3] Ablation studies show that enabling CAS reduces token usage by roughly 32% on Problem 17.91, while the absence of an advisor agent raises verifier‑rejection rates and prevents synthesis of viable proof routes.  

## Methodology  
Albilich is built as a modular agentic harness that combines four core components: (1) long‑horizon reasoning via LLMs, (2) computer algebra system (CAS) integration for symbolic manipulation, (3) literature retrieval to fetch relevant theorems and examples, and (4) persistent SQLite‑based context management to maintain state across turns. The agents coordinate proof steps, retrieve external knowledge, invoke CAS operations, and store intermediate results in a durable database, enabling reproducible research workflows.  

## Results  
Experimental evaluation on RealMath yielded 10/10 correct solutions with CAS, while the same benchmark without CAS achieved 9/10. On Kourovka Notebook problems, Albilich delivered a counterexample to Problem 21.142 and an enhanced proof for Problem 20.2. Token‑level analysis revealed that enabling CAS cut token consumption by 32% on Problem 17.91. Conversely, removing the advisor agent increased verifier rejection rates and halted proof synthesis on Problem 21.142, underscoring the necessity of human guidance for complex routes.  

## Significance  
These findings validate Albilich as a scalable, human‑steerable environment that leverages CAS to boost LLM performance in mathematical research, offering a reproducible platform for autoresearch and reducing manual effort through persistent context handling.  

## Related Concepts  
- Large language model (LLM) reasoning  
- Proof‑state orchestration  
- Computer algebra system (CAS) integration  
- Persistent SQLite context management  
- Agentic harness design  
- Verification and token efficiency analysis
