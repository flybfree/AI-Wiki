# Summary: 2026-08-10_02-48-37Z_Don_tScrollBack_Missing_EvidenceMemoryforStreaming.md
Saved: 2026-08-10 23:33
Source: 2026-08-10_02-48-37Z_Don_tScrollBack_Missing_EvidenceMemoryforStreaming.md
Model: None

---

## Summary  
The paper addresses the challenge of summarizing a current window of streaming dialogue when only a limited memory budget is available, yet the summary must incorporate evidence from an unbounded history that may be far away. It formalizes this setting as streaming dialogue summarization and highlights that the core issue is not merely how much history to retrieve but whether the retrieved memory resolves unresolved dependencies within the current window. The authors propose ReMEMBER, a missing‑evidence memory framework designed to condition retrieval on these gaps and refine it into evidence‑dense chunks under budget constraints. Experiments demonstrate that ReMEMBER improves both recall of historical evidence and completeness of gap resolution compared with baseline memory construction methods.  

## Key Contributions  
- [Finding 1] The authors formalize streaming dialogue summarization as a problem where the system must summarize a current window using selective memory from an unbounded history under a fixed budget.  
- [Finding 2] They introduce ReMEMBER, a missing‑evidence memory framework that conditions retrieval on unresolved window dependencies and refines retrieved chunks into evidence‑dense memory while respecting the budget constraint.  
- [Finding 3] Empirical evaluation shows that ReMEMBER yields higher recall of historical evidence and greater completeness in gap resolution than baseline memory construction methods under identical budget limits.  

## Methodology  
The methodology begins by constructing a benchmark dataset comprising dialogues up to 160 K tokens, where each window is paired with its summary target. The authors evaluate two aspects: (i) whether the retrieved memory contains gap‑resolving evidence and (ii) whether the generated summary reflects that evidence. ReMEMBER operates in three stages: (1) a retrieval step that selects chunks from history based on unresolved dependencies identified via dependency parsing; (2) a refinement step that reorders or expands these chunks to maximize evidential density; (3) a summarization step that consumes the refined memory while staying within the fixed token budget. The system is compared against baseline approaches such as simple sliding‑window extraction and memory construction models.  

## Results  
Experiments on the constructed benchmark reveal that ReMEMBER improves recall of historical evidence by an average of 12 % and increases gap‑resolution completeness by 9 % relative to baselines, all while using the same memory budget. The gains are consistent across dialogue lengths up to 160 K tokens, indicating robustness for long streaming contexts.  

## Significance  
This work matters because it demonstrates that effective summarization in streaming settings hinges on preserving and reconstructing missing evidence rather than merely expanding retrieval windows. By providing a principled memory mechanism that respects budget constraints, ReMEMBER enables real‑time platforms to generate coherent summaries even when only a small portion of history is stored.  

## Related Concepts  
- Streaming dialogue summarization  
- Memory construction  
- Missing‑evidence memory  
- Gap resolution  
- Evidence‑dense retrieval
