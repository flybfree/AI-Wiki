# Summary: 2026-08-09_09-55-42Z_REVEAL_ARubric_GuidedAgentforExplicitEvidenceSuffi.md
Saved: 2026-08-10 23:16
Source: 2026-08-09_09-55-42Z_REVEAL_ARubric_GuidedAgentforExplicitEvidenceSuffi.md
Model: None

---

## Summary  
The paper introduces REVEAL, a rubric‑guided agent that verifies whether retrieved evidence is sufficient for long‑video question answering. It tackles the fragmentation caused by fixed temporal chunking and static memory banks by building an adaptive visual‑similarity preprocessing pipeline and an online video memory. REVEAL uses automatically constructed rubrics to explicitly check evidence sufficiency, pinpoint missing clues, and trigger re‑retrieval when needed. The framework improves over existing closed‑source and open‑source methods without any additional training.

## Key Contributions  
- Adaptive visual‑similarity preprocessing creates natural event units and an offline‑online video memory that captures global context while remaining question‑conditioned online.  
- An automatic rubric library enables explicit sufficiency verification of retrieved evidence, identifies gaps in missing clues, and directs targeted re‑retrieval for complementary information.  
- REVEAL consistently outperforms both closed‑source and open‑source state‑of‑the‑art long‑video QA systems across multiple benchmarks.

## Methodology  
The authors first group adjacent frames using visual similarity to form coherent event units, which are stored offline in a structured memory bank. During inference, REVEAL retrieves evidence from this memory that is relevant to the current query. A set of rubrics—each defining sufficiency criteria such as temporal continuity, causal linkage, or fine‑grained action—evaluates whether the retrieved clips satisfy these conditions. If any criterion fails, the system pinpoints the missing clue and re‑queries adjacent frames or alternative memory entries to fill the gap before finalizing the answer.

## Results  
Experiments on several long‑video QA datasets show REVEAL achieving higher accuracy than both closed‑source baselines (e.g., LLaVA) and open‑source baselines (e.g., VideoQA). The gains range from 3.2 % to 5.8 % absolute improvement, demonstrating that explicit sufficiency verification yields more reliable reasoning than stopping at semantic relevance alone.

## Significance  
By focusing on evidence sufficiency rather than mere retrieval relevance, REVEAL produces answers that incorporate the decisive causal or fine‑grained cues often missed by prior methods. This leads to more trustworthy long‑video QA outputs and reduces hallucinations caused by incomplete information.

## Related Concepts  
Retrieval‑augmented generation, memory banks, temporal chunking, multimodal knowledge graphs, rubric‑based verification, evidence sufficiency, adaptive preprocessing.
