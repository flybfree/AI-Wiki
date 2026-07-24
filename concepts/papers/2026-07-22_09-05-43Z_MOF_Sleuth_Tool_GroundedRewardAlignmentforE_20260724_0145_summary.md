# Summary: 2026-07-22_09-05-43Z_MOF_Sleuth_Tool_GroundedRewardAlignmentforExplaina.md
Saved: 2026-07-24 01:45
Source: 2026-07-22_09-05-43Z_MOF_Sleuth_Tool_GroundedRewardAlignmentforExplaina.md
Model: None

---

## Summary  
The paper tackles the problem of fine‑grained, explainable auditing of crystal information files (CIFs) that describe metal‑organic frameworks (MOFs). By coupling a deterministic “Forensic Lab” that extracts precise chemical and structural evidence with an LLM‑driven “Sleuth” reasoning engine, MOF‑Sleuth produces evidence‑grounded diagnoses instead of coarse labels. The authors further introduce Chemically Grounded Diagnosis (Chem‑GD), a metric that evaluates whether a correct error is justified by the CIF‑derived facts. Reinforcement learning aligns tool measurements with this explanation level, rewarding both accurate answers and the cited chemical evidence.

## Key Contributions  
- MOF‑Sleuth introduces a reinforcement‑guided CIF auditing agent composed of a deterministic Forensic Lab that computes composition, geometry, connectivity, occupancy, coordination, and charge evidence, and a Sleuth engine that translates this evidence into explanations, error types, and binary decisions.  
- Chemically Grounded Diagnosis (Chem‑GD) is a new metric that assesses the factual relevance of CIF‑derived evidence to a correct diagnosis, providing an explicit link between chemical facts and language‑model output.  
- The authors demonstrate that RL reward alignment can turn raw tool measurements into supervision at the level of cited chemical evidence, improving both detection performance and attribution quality.

## Methodology  
The methodology proceeds in three stages. First, the Forensic Lab parses each CIF to generate a structured set of chemical and structural facts—including composition, bond connectivity, atomic occupancy, coordination numbers, and formal charge. Second, Sleuth ingests these facts and formulates an explanation that cites specific evidence items; it also classifies the error type (e.g., missing atom, incorrect bond) and outputs a binary audit result. Third, reinforcement learning fine‑tunes the Sleuth model by rewarding not only correct final decisions but also the inclusion of relevant CIF evidence in the generated text, using Chem‑GD as the supervisory signal. This loop iteratively aligns tool measurements with chemically grounded explanations.

## Results  
Across four benchmark MOF datasets, MOF‑Sleuth achieves state‑of‑the‑art performance among both LLM‑based and MOF‑specific machine‑learning methods. The system improves detection rates by up to 12 % relative to prior approaches, provides clearer attribution of error sources, and yields explanations that are more faithful to the underlying CIF evidence. Chem‑GD scores consistently exceed random baselines, confirming that the model’s diagnoses are indeed grounded in factual CIF information.

## Significance  
This work bridges the gap between high‑precision chemical reasoning and language‑model output for MOF CIF auditing, offering a reliable pathway to fine‑grained error detection without costly manual inspection. By rewarding evidence citation through RL, it makes explanations interpretable and actionable, which is crucial as automated screening pipelines scale in computational chemistry.

## Related Concepts  
- CIF (Crystal Information File) files describing MOF structures.  
- Metal‑organic frameworks (MOFs).  
- Reinforcement learning for tool calibration.  
- Evidence‑grounded explanations.  
- Chemical reasoning and verification.
