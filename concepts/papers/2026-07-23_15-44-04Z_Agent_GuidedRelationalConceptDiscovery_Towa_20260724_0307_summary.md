# Summary: 2026-07-23_15-44-04Z_Agent_GuidedRelationalConceptDiscovery_TowardInter.md
Saved: 2026-07-24 03:07
Source: 2026-07-23_15-44-04Z_Agent_GuidedRelationalConceptDiscovery_TowardInter.md
Model: None

---

## Summary  
The paper proposes Agent‑Guided Relational Concept Discovery, a framework that learns interpretable concepts from raw REIMS data without predefined labels, enabling better generalization for surgical margin assessment. It uses an agent to refine semantic descriptions and ground them in a biochemical knowledge graph. This approach improves diagnostic metrics on cancer datasets and reduces false positives intraoperatively.

## Key Contributions  
- Introduces Agent‑Guided Concept Discovery, a self‑supervised concept discovery method that refines concepts via reasoning agents.  
- Integrates learned concepts with a biochemical knowledge graph to ensure metabolic consistency.  
- Demonstrates improved balanced accuracy and sensitivity over baseline models on Skin and Breast Cancer datasets, plus fewer false positives in an intraoperative case.

## Methodology  
The authors train deep learning models on labeled REIMS spectra, then employ a reasoning agent that iteratively improves semantic concept descriptions based on diagnostic relevance scores. The agent adjusts concept weights dynamically. Learned concepts are mapped to the biochemical knowledge graph via entity linking and constraint satisfaction, ensuring they align with known metabolic pathways.

## Results  
On Skin Cancer (n=120) and Breast Cancer (n=95) datasets, the proposed framework achieves 84.3 % balanced accuracy versus 76.1 % baseline; sensitivity rises from 78.9 % to 86.5 %. In a simulated intraoperative scenario with noisy spectra, false‑positive rate drops from 22 % to 9 %, indicating better generalization.

## Significance  
This work bridges the gap between black‑box deep learning and clinical interpretability, offering a pathway for real‑time surgical margin assessment where labeled data are unavailable. By grounding concepts in biochemical knowledge, it enhances trustworthiness and supports regulatory compliance.

## Related Concepts  
- Deep Learning  
- Rapid Evaporative Ionization Mass Spectrometry (REIMS)  
- Supervised vs Unsupervised Learning  
- Concept‑Based Learning  
- Reasoning Agent  
- Knowledge Graph Integration  
- Biochemical Ontology
