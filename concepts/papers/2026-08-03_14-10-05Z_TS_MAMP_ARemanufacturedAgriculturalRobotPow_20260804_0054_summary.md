# Summary: 2026-08-03_14-10-05Z_TS_MAMP_ARemanufacturedAgriculturalRobotPoweredbyS.md
Saved: 2026-08-04 00:54
Source: 2026-08-03_14-10-05Z_TS_MAMP_ARemanufacturedAgriculturalRobotPoweredbyS.md
Model: None

---

## Summary  
This paper introduces TS‑MAMP, a remanufactured agricultural robot that repurposes retired low‑speed electric‑vehicle (LSEV) powertrains and chassis to deliver affordable on‑device weed detection for smallholder farms. By integrating second‑life battery modules and a lightweight YOLOv10n detector running on a Jetson Nano, the authors demonstrate that circular‑economy principles can reduce BOM costs by ~60 % while maintaining high classification performance. The robot’s modular design enables rapid 5‑minute module changeovers and supports adjustable track widths for diverse field conditions. Overall, TS‑MAMP offers a cost‑effective pathway to AI‑enabled weeding that commercial automation cannot reach.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 11 summary/topic terms overlap
- [[concepts/papers/2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxon_summary.md|Summary: 2026-06-26_17-08-06Z_Agent_NativeImmuneSystem_Architecture_Taxonomy_and.md]] — 3 title terms overlap; 121 backlinks; 8 summary/topic terms overlap
- [[concepts/papers/2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMult_summary.md|Summary: 2026-07-23_12-40-47Z_pAI_Econ_claude_AGatedHuman_in_the_LoopMulti_Agent.md]] — 3 title terms overlap; 17 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- Finding 1: Reusing screened 48 V BLDC hub motors and lead‑acid battery modules cuts the powertrain‑and‑chassis bill of materials to under USD 450, a reduction of roughly 60 % compared with new components.  
- Finding 2: An NMS‑free YOLOv10n model achieves 80.87 % mean average precision (mAP)@0.5 on the Wanxi Crop‑Weed dataset, confirming that lightweight inference can meet real‑world detection needs without non‑maximum suppression.  
- Finding 3: The telescopic‑sleeve modular chassis permits continuous track width adjustment from 1200 mm to 2000 mm and rapid module swaps, illustrating a practical re‑engineering strategy for second‑life EV parts.

## Methodology  
The authors approached the problem by first identifying functional LSEV components that could be safely screened and balanced within a tight voltage envelope. They paired these motors via back‑EMF matching to create a lightweight drivetrain. Battery modules with 60–80 % state of health were matched in series/parallel to maintain a uniform 100 mV inter‑module deviation, preserving energy efficiency. For detection, they trained YOLOv10n using dual‑assignment loss and negative‑sample learning, then deployed the model on FP16 TensorRT for inference on a Jetson Nano. The robot’s chassis was fabricated from recyclable steel tubing with telescopic sleeves to allow modular reconfiguration.

## Results  
Experimental evaluation shows that the remanufactured powertrain reduces component cost by ~60 % (BOM ≈ USD 450, excluding perception and weeding modules). The YOLOv10n detector reaches 80.87 % mAP@0.5 on the Wanxi dataset, with a balanced trade‑off between precision and recall. On‑device inference runs at ≤30 ms per frame, confirming feasibility for real‑time weeding. Field tests demonstrate that the robot can traverse fields up to 200 kg static load while maintaining stable operation during module changes within five minutes.

## Significance  
TS‑MAMP bridges a critical gap in agricultural automation by making AI‑enabled weed detection economically accessible to smallholders, whose farms are often too small for high‑cost commercial robots. By leveraging second‑life EV parts and on‑device inference, the system exemplifies how circular‑economy strategies can generate sustainable value chains while reducing environmental impact.

## Related Concepts  
- Circular economy  
- Remanufacturing of electric‑vehicle components  
- Second‑life battery modules  
- YOLOv10n model  
- Jetson Nano inference  
- Modular robotics chassis  
- NMS‑free detection
