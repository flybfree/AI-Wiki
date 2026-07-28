# Summary: 2026-07-23_21-22-36Z_DRC_Aid_Design_RuleCorrectionviaAgenticFrameworkut.md
Saved: 2026-07-27 23:22
Source: 2026-07-23_21-22-36Z_DRC_Aid_Design_RuleCorrectionviaAgenticFrameworkut.md
Model: None

---

## Summary  
DRC‑Aid automates the repair of design rule violations (DRVs) in semiconductor layouts by integrating verification tools into a closed‑loop agentic framework that treats DRC correction as a verification‑in‑the‑loop search. An off‑the‑shelf large language model evaluates local geometric context to select edits from a deterministic rule engine, while depth‑first search with backtracking and a global memory bank prevents cyclic re‑exploration. The system achieves LVS‑equivalent repairs in roughly 92 % of cases on benchmark FreePDK45 layouts, reducing total violations by about 98 %. This approach replaces manual or heuristic fixes with an intelligent, end‑to‑end solution.

## Key Contributions  
- [Finding 1] A closed‑loop agentic framework that formulates DRC repair as a verification‑in‑the‑loop search.  
- [Finding 2] A deterministic Rule Engine that converts tool‑reported violations into a bounded menu of geometric edits, with an LLM selecting the optimal edit via depth‑first search and backtracking.  
- [Finding 3] A global Memory Bank that records visited states to avoid cyclic re‑exploration and ensures termination.

## Methodology  
The authors model DRC repair as a combinatorial optimization problem where each violation can be corrected by applying one of several geometric edits. The deterministic Rule Engine parses verification tool reports into this limited edit menu. An off‑the‑shelf LLM evaluates the local layout context to rank these options, feeding them into a depth‑first search with backtracking that respects a budgeted depth limit and uses the Memory Bank to cache visited states and prevent revisiting identical configurations.

## Results  
On FreePDK45 layouts containing up to six DRVs, DRC‑Aid achieved DRC‑clean, LVS‑equivalent repairs in 92.5 % of cases while reducing total violations by ~98 %, leaving only partially repaired LVS‑equivalent candidates for the remaining 7.5 %. Compared with random selection (54.4 %) and deterministic heuristic (83.3 %), LLM‑based selection outperforms both, especially when six or more violations are present.

## Significance  
This work shows that large language models can act as intelligent decision makers within low‑level verification pipelines, bridging high‑level design intent to precise geometric compliance. By automating DRC repair without manual intervention, it accelerates layout closure and reduces yield loss in semiconductor manufacturing.

## Related Concepts  
- Design Rule Violations (DRVs)  
- Layout Verification (LVS)  
- Large Language Models (LLMs)  
- Depth‑First Search with Backtracking  
- Memory Bank for state caching  
- Deterministic Rule Engines
