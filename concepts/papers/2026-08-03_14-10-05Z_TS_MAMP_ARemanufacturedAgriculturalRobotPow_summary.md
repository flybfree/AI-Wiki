# Summary: 2026-08-03_14-10-05Z_TS_MAMP_ARemanufacturedAgriculturalRobotPoweredbyS.md
Saved: 2026-08-04 00:33
Source: 2026-08-03_14-10-05Z_TS_MAMP_ARemanufacturedAgriculturalRobotPoweredbyS.md
Model: None

---

## Summary  
The paper proposes TS‑MAMP (Telescopic‑Sleeve Modular Agricultural Mobile Platform), a remanufactured agricultural robot that repurposes retired low‑speed electric‑vehicle components to deliver affordable, on‑device weed detection. By integrating second‑life 48 V brushless‑DC hub motors and partially degraded lead‑acid battery modules, the authors achieve a powertrain‑and‑chassis bill of materials under USD 450 (excluding perception hardware). A lightweight YOLOv10n detector trained without non‑maximum suppression attains 80.9 % mean average precision on the Wanxi Crop‑Weed dataset, confirming that AI inference can run locally on a Jetson Nano. The modular chassis also supports adjustable track width and rapid module swaps, enabling smallholder farms to deploy functional robots at minimal capital cost.

## Key Contributions  
- [Finding 1] Reusing screened second‑life EV powertrains cuts the BOM cost of the robot’s mechanical and electrical system by ~60 %, dropping it below USD 450.  
- [Finding 2] The NMS‑free YOLOv10n detector reaches 80.87 % mAP@0.5 (and 58.41 % over the range 0.5–0.95) on a standard weed detection benchmark, proving high‑precision on‑device inference.  
- [Finding 3] The telescopic‑sleeve modular chassis delivers ≥200 kg static load, adjustable track width (1200–2000 mm), and ≤5‑minute module changeover.

## Methodology  
The authors followed a circular‑economy design workflow: retired 48 V brushless‑DC hub motors are paired through back‑EMF matching to balance torque, while lead‑acid battery modules screened for ≥60 % state of health are balanced within a 100 mV inter‑module voltage deviation. The chassis is built as a telescopic sleeve allowing quick disassembly and re‑assembly. A YOLOv10n model is trained with dual‑assignment learning and negative‑sample weighting to eliminate non‑maximum suppression, then exported to TensorRT for FP16 inference on a Jetson Nano. All hardware integration is performed under 3R (reduce, reuse, recycle) principles.

## Results  
- Powertrain‑and‑chassis BOM cost: USD < 450 (perception and weeding modules excluded).  
- Static load capacity: ≥200 kg.  
- Track width adjustable from 1200 mm to 2000 mm.  
- Module changeover time: ≤5 minutes.  
- Detection performance: mAP@0.5 = 80.87 %; mAP@0.5–0.95 = 58.41 %.  
- Inference runs at ~30 fps on Jetson Nano using FP16 TensorRT.

## Significance  
TS‑MAMP demonstrates that second‑life EV components can be re‑engineered into cost‑effective, AI‑enabled agricultural robots, opening a remanufacturing pathway for smallholder fields left out of commercial automation. By lowering capital expenditure and enabling local inference, the system supports sustainable farming practices while reducing electronic waste.

## Related Concepts  
circular economy; remanufactured EV powertrains; state‑of‑health screening; YOLOv10n; NMS‑free detection; dual‑assignment training; negative‑sample learning; TensorRT FP16 inference; Jetson Nano; modular agricultural robotics; 3R principles.
