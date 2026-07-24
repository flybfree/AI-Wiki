# Summary: 2026-07-17_04-39-04Z_AEGIS_Assay_AwareProtocolValidationandRuntimeMonit.md
Saved: 2026-07-23 23:51
Source: 2026-07-17_04-39-04Z_AEGIS_Assay_AwareProtocolValidationandRuntimeMonit.md
Model: None

---

## Summary  
AEGIS is a two‑layer guardian for open‑source liquid handling robots that validates assay protocols and monitors runtime execution. It combines a rule‑based assay database with an LLM to catch protocol violations before pipetting, while also using visual trajectory analysis to detect physical failures such as partial dispense or missing tips. The system is fully open source and designed specifically for the Opentrons OT‑2 platform.  

## Key Contributions  
- [Finding 1] The AEGIS system combines a rule‑based assay validator with an LLM to achieve F1=0.97 on protocol validation across five assay families.  
- [Finding 2] YOLO‑cropped pipette trajectories are modeled via PCA, yielding average precision 0.89 and operating‑point F1 0.71 for runtime monitoring.  
- [Finding 3] The VLM self‑vote gate improves partial‑dispense recall to 5/5 while keeping cost low (~$1.63 per plate).  

## Methodology  
The authors tackled two failure modes: protocol violations and physical execution errors. For Layer 1, they built a curated assay rule database and fine‑tuned an LLM on OT‑2 Python code, integrating it with the robot’s API to pre‑flight validate protocols. For Layer 2, they captured four‑frame pipette trajectories after YOLO cropping, fitted a PCA world model, and deployed a vision‑language model (VLM) that self‑votes on observed events. The pipeline is lightweight: rule checking is deterministic, while VLM inference is triggered only when confidence drops below a threshold.  

## Results  
On a 24‑protocol benchmark spanning five assay families, AEGIS achieved an adjusted F1 of 0.97, outperforming rules‑only (F1≈0.85) and LLM‑only baselines. Runtime monitoring reached average precision 0.89, operating‑point F1 0.71 (AUROC 0.80), with a small‑pipette resolution limit of F1 0.47. In live demonstrations on five replicates per condition, the system deterministically caught no‑tip failures and partial dispense events; VLM recall for partial dispense reached 5/5 while cost stayed near $1.63 per plate versus $10.33 for an always‑VLM baseline.  

## Significance  
AEGIS bridges pre‑flight assay validation with real‑time visual monitoring, enabling open‑source labs to run reliable experiments without expensive proprietary hardware or APIs. Its modular design reduces false positives and operational cost, making it a practical solution for self‑driving laboratories that rely on low‑cost liquid handlers.  

## Related Concepts  
- Open‑source liquid handling robots (e.g., Opentrons OT‑2)  
- Assay rule databases and protocol validation  
- Large language model (LLM) reasoning over code  
- YOLO image detection and trajectory reconstruction  
- PCA world modeling for multi‑object tracking  
- Vision‑language models (VLM) for event classification  
- Open‑source AI pipelines
