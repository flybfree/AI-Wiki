# Summary: 2026-07-22_09-05-43Z_MOF_Sleuth_Tool_GroundedRewardAlignmentforExplaina.md
Saved: 2026-07-24 01:38
Source: 2026-07-22_09-05-43Z_MOF_Sleuth_Tool_GroundedRewardAlignmentforExplaina.md
Model: None

---

## Summary  
The paper proposes MOF‑Sleuth, a reinforcement‑guided CIF auditing agent that links chemical evidence to LLM explanations for fine‑grained error detection in metal‑organic frameworks. It introduces a deterministic Forensic Lab and a Sleuth reasoning engine, and uses reward‑based RL to align tool measurements with evidence‑grounded diagnoses. The approach improves both detection accuracy and the quality of explainable attributions across benchmarks.  

## Semantic links
- [[concepts/papers/2026-07-30_15-35-43Z_HyperClaim_Fine_GrainedCross_ModalHypergrap_summary.md|Summary: 2026-07-30_15-35-43Z_HyperClaim_Fine_GrainedCross_ModalHypergraphReason.md]] — 4 title terms overlap; 14 summary/topic terms overlap; semantic match 0.11
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson4_AgentFrameworks.md|Lesson 4 — Agent Frameworks: The Loop Engine]] — 4 title terms overlap; 1 backlink; 5 summary/topic terms overlap

## Key Contributions  
- [Finding 1] MOF‑Sleuth achieves state‑of‑the‑art performance on four MOF CIF audit benchmarks, surpassing existing LLM and machine‑learning methods.  
- [Finding 2] The Chemically Grounded Diagnosis (Chem‑GD) metric reliably measures whether a correct diagnosis is supported by factual CIF evidence.  
- [Finding 3] Reinforcement learning couples tool outputs with chemical explanations, turning measurement data into supervision for evidence‑based reasoning.  

## Methodology  
The authors built MOF‑Sleuth as a two‑module system. The Forensic Lab parses each CIF to compute composition, geometry, connectivity, occupancy, coordination numbers, and charge, producing structured chemical evidence. Sleuth then employs this evidence to generate an explanation that cites specific atom‑site records, identifies error types, and outputs a binary decision. A reinforcement learning loop trains the Sleuth module by rewarding explanations that are both correct and grounded in the Lab’s evidence, thereby aligning tool measurements with chemically accurate diagnoses.  

## Results  
Experiments on four benchmark datasets show MOF‑Sleuth attains higher detection rates (up to 12 % improvement) and attribution precision compared with prior LLM‑only or model‑based approaches. The Chem‑GD metric correlates strongly with human‑annotated evidence quality, achieving an average score of 0.87 across tests. These gains demonstrate that evidence‑grounded explanations can be learned and evaluated automatically.  

## Significance  
By bridging the gap between raw CIF data and LLM outputs, MOF‑Sleuth enables reliable, interpretable auditing of large MOF repositories, reducing downstream errors in simulations and screening pipelines while providing transparent justifications for each decision.  

## Related Concepts  
- CIF (Crystal Information File) format  
- Metal‑organic framework (MOF)  
- Reinforcement learning (RL)  
- Evidence‑grounded explanation  
- Chemically Grounded Diagnosis (Chem‑GD)
