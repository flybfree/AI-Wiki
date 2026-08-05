# Summary: 2026-08-02_23-47-18Z_V_Mem_Modality_RoutedRetrievalforLong_TermMultimod.md
Saved: 2026-08-03 23:34
Source: 2026-08-02_23-47-18Z_V_Mem_Modality_RoutedRetrievalforLong_TermMultimod.md
Model: None

---

## Summary  
The paper V‑Mem tackles the problem of long‑term multimodal agentic memory where queries and evidence can be text or image, yet most retrieval systems fail because they assume a single similarity space. It identifies two gaps: a modality gap that makes cross‑modal matches harder, and a similarity‑relevance gap where the nearest embedding is not the answer. V‑Mem resolves these by routing retrieval according to the query’s modality and the evidence’s modality, both inferred from the query alone. The system also closes the relevance gap with an LLM‑generated anchor that better aligns with the target content.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 6 summary/topic terms overlap

## Key Contributions  
- [Finding 1] Two fundamental gaps—modality gap (query and evidence belong to different modalities) and similarity‑relevance gap (closest embedding is not the answer).  
- [Finding 2] V‑Mem organizes conversation into rounds and returns only target‑modality content from the same round, avoiding cross‑modal comparisons.  
- [Finding 3] It employs an LLM‑generated anchor that sits closer to relevant evidence than the query does, enabling accurate retrieval of combined text‑image answers.

## Methodology  
The authors propose a modality‑routed retrieval framework: each multimodal query is parsed for its dominant modality (text or image). The memory index stores content in separate modalities per round. For a text‑only query seeking an image, V‑Mem creates a caption‑like anchor; for an image‑plus‑text query, it adds extracted keywords to the textual part of the anchor. Retrieval is performed within each modality without mixing them, preserving the round structure.

## Results  
On Mem‑Gallery, V‑Mem achieves an LLM‑judge score of 0.82, outperforming the second best system (0.56) by a large margin; for image‑only queries it scores 0.87 while baselines stay below 0.47. On LoCoMo, V‑Mem scores 0.69 versus 0.58 for the next best method.

## Significance  
These results demonstrate that routing retrieval by modality and using LLM anchors can dramatically improve long‑term multimodal agent memory, moving agents from mediocre to near‑human performance on complex text‑image interactions.

## Related Concepts  
modality gap, similarity‑relevance gap, joint embedding space, round organization, modality‑routed retrieval, LLM‑generated anchor, cross‑modal retrieval.
