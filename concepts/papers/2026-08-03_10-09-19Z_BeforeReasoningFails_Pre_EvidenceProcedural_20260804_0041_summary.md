# Summary: 2026-08-03_10-09-19Z_BeforeReasoningFails_Pre_EvidenceProceduralFailure.md
Saved: 2026-08-04 00:41
Source: 2026-08-03_10-09-19Z_BeforeReasoningFails_Pre_EvidenceProceduralFailure.md
Model: None

---

## Summary  
This paper investigates a procedural failure mode in agentic retrieval‑augmented generation (RAG) systems where the model retrieves candidate evidence but never inspects it before finalizing an answer. By analyzing saved tool‑call traces, we identify two distinct failure types: pre‑evidence discipline failures and post‑gold‑read failures. The authors introduce a minimal runtime invariant called Read‑Gate that forces the agent to read retrieved passages after search and before generating the response. Experiments on three benchmark question sets demonstrate that enforcing this invariant improves performance by 14.9–19.9 points when reading is otherwise skipped, and yields modest gains even in full reasoning cells.

## Key Contributions  
- [Finding 1] The authors prove that evidence‑conditioned reasoning can fail before the agent actually reads the retrieved snippets, revealing a procedural flaw rather than an answer‑side issue.  
- [Finding 2] They demonstrate that pre‑evidence discipline failures and post‑gold‑read failures are largely non‑redundant across different extractor models, with both‑trigger rates ranging from 11.2 % to 13.1 %.  
- [Finding 3] Enforcing a Read‑Gate invariant improves LLM‑Acc scores by 14.9–19.9 points on trajectories that would otherwise skip reading and raises them by 3.2–9.4 points in full minimal‑reasoning cells.

## Methodology  
The authors collect 12,000 paired agent trajectories from HotpotQA, 2WikiMultiHopQA, and MuSiQue, each containing a search phase, evidence retrieval, optional reading, and final answer generation. They reconstruct the full trajectory using saved tool‑call logs to label whether the model read the retrieved passages (gold‑read) or not. The Read‑Gate invariant is implemented as a lightweight runtime check that aborts finalization if the last action before answer generation was not an evidence‑reading operation. Experiments compare three extractor configurations (regex, spaCy, and a hybrid) under both reading and non‑reading conditions.

## Results  
Across all experiments, the both‑trigger failure rate is 11.2 %–13.1 %, indicating that failures are not simply due to missing evidence but also to skipping the reading step. When Read‑Gate is enforced, average LLM‑Acc increases from 78.4 % to 93.6 % on the minimal‑reasoning cells and reaches 92.1 % on full reasoning cells. The improvement persists across all extractor types, confirming that the effect is not tied to a specific parser.

## Significance  
These findings highlight that evidence gathering must be treated as a trajectory‑level control problem, separate from downstream reasoning quality. By treating reading as an invariant, RAG systems can avoid premature finalization and produce more accurate answers without sacrificing efficiency. The results also suggest that larger hidden thinking budgets do not automatically increase evidence inspection, offering a nuanced view of model behavior.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Agentic reasoning traces  
- Evidence inspection vs. gold reading  
- Read‑Gate invariant  
- Pre‑evidence discipline failure  
- Post‑gold read failure
