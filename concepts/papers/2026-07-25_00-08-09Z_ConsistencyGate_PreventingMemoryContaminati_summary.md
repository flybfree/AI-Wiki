# Summary: 2026-07-25_00-08-09Z_ConsistencyGate_PreventingMemoryContaminationinLLM.md
Saved: 2026-07-27 22:32
Source: 2026-07-25_00-08-09Z_ConsistencyGate_PreventingMemoryContaminationinLLM.md
Model: None

---

## Summary  
LLM agents that operate over many turns store facts in an external memory and reuse them as premises for later reasoning, which can lead to a failure mode called memory contamination when a hallucinated fact written early persists as a false premise throughout the conversation. Existing memory management techniques focus on retrieval and capacity but ignore write‑time correctness, leaving the problem of uncontrolled contamination unaddressed. We introduce ConsistencyGate, a model‑agnostic admission gate that evaluates each candidate fact for self‑consistency before committing it to memory. The gate queries the LLM multiple times to obtain soft support scores and admits only those whose average exceeds a threshold, thereby preventing contaminated facts from propagating downstream.

## Key Contributions  
- Finding 1: Memory contamination is a persistent false premise that propagates across long agent trajectories, undermining reasoning reliability.  
- Finding 2: Current memory‑management strategies lack write‑time correctness checks; utility‑ or recency‑based criteria cannot reliably filter hallucinated facts.  
- Finding 3: ConsistencyGate provides a universal admission mechanism that uses K LLM queries to generate soft support scores, admitting facts only when the average score surpasses a configurable threshold.

## Methodology  
The authors address the problem by constructing three benchmark corpora: LoCoMo‑Contam and MSC‑Contam, which embed controlled single‑detail corruptions in long‑term human conversations from LoCoMo and MSC, respectively; and MemContam, a synthetic corpus that isolates a near‑oracle upper bound for contamination. ConsistencyGate is implemented as a write‑time gate that, before committing a fact extracted from the source context c, runs K forward passes to obtain soft support scores and computes an average; admission occurs only if this average exceeds a user‑defined threshold. The mechanism reduces to a single forward pass in a log‑probability variant for latency‑sensitive deployments and requires no fine‑tuning of the underlying model.

## Results  
Across four LLM backbones, ConsistencyGate consistently lowers contamination rates on all three benchmarks compared with a write‑everything baseline. The improvement is most pronounced for facts that are only implicitly present in the source context, indicating that the gate effectively filters out noisy or hallucinated entries while preserving legitimate information. The authors release LoCoMo‑Contam, MSC‑Contam, MemContam, and the gate implementation to enable further research.

## Significance  
This work matters because it tackles a critical flaw in long‑term LLM agent reasoning: uncontrolled memory contamination can cascade into incorrect conclusions. By introducing a write‑time admission control that is model‑agnostic and lightweight, ConsistencyGate improves factual fidelity without sacrificing performance, paving the way for safer deployment of multi‑turn agents.

## Related Concepts  
memory contamination, hallucinated facts, external memory store, retrieval, capacity management, write‑time correctness, admission control, soft support score, self‑consistency, LoCoMo, MSC, MemContam, LLM agents, log‑probability variant.
