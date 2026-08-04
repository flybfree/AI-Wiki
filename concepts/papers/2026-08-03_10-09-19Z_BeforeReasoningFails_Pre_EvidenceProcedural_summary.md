# Summary: 2026-08-03_10-09-19Z_BeforeReasoningFails_Pre_EvidenceProceduralFailure.md
Saved: 2026-08-03 23:52
Source: 2026-08-03_10-09-19Z_BeforeReasoningFails_Pre_EvidenceProceduralFailure.md
Model: None

---

## Summary  
The paper investigates procedural failures in agentic RAG where agents retrieve candidate snippets but do not inspect them before finalizing answers, describing this as a pre‑evidence discipline failure. It also identifies a second mode—post‑gold‑read failure—where the agent reads evidence yet still produces incorrect outputs. The authors propose a minimal runtime invariant called Read‑Gate that forces an agent to read retrieved evidence after search and before generating the final answer. Experiments on multiple QA datasets demonstrate that enforcing this reading step improves performance substantially.

## Key Contributions  
- Finding 1: The two failure types are largely non‑redundant, with both‑trigger rates in [11.2 %, 13.1 %] across regex and spaCy entity extractors.  
- Finding 2: Forced reading via Read‑Gate boosts LLM‑Acc by 14.9–19.9 points on trajectories that would otherwise skip reading and by 3.2–9.4 points in full minimal‑reasoning cells.  
- Finding 3: Hidden thinking budgets do not necessarily increase evidence inspection; the issue is procedural rather than budget‑driven.

## Methodology  
The authors analyze 12,000 paired agent trajectories from HotpotQA, 2WikiMultiHopQA, and MuSiQue. For each trajectory they extract tool‑call traces, retrieved snippets, read passages, and final answers to classify failures into pre‑evidence discipline (agent never reads evidence) and post‑gold‑read (agent reads but still fails). Using these logs they evaluate Read‑Gate as a minimal runtime invariant that inserts a forced reading step between search and answer generation.

## Results  
Across regex and spaCy entity extractors, the both‑trigger failure rate is 11.2–13.1 %. Forced reading improves LLM‑Acc scores by 14.9–19.9 points on trajectories that would otherwise skip reading and by 3.2–9.4 points in full minimal‑reasoning cells. Diagnostic analysis shows no increase in evidence inspection with larger hidden thinking budgets.

## Significance  
This work demonstrates that evidence gathering is a trajectory‑level control problem, separate from answer reasoning. By treating reading as a procedural invariant, the study provides a systematic way to diagnose and mitigate failures before they manifest in outputs, offering practical guidance for improving agentic RAG systems.

## Related Concepts  
- Agentic RAG (retrieval‑augmented generation)  
- Evidence‑gathering  
- Read‑Gate runtime invariant  
- Hidden thinking budget  
- Pre‑evidence discipline failure  
- Post‑gold‑read failure
