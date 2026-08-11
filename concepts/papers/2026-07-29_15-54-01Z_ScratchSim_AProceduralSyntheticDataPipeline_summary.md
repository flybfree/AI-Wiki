# Summary: 2026-07-29_15-54-01Z_ScratchSim_AProceduralSyntheticDataPipelineforSurf.md
Saved: 2026-07-29 21:39
Source: 2026-07-29_15-54-01Z_ScratchSim_AProceduralSyntheticDataPipelineforSurf.md
Model: None

---

## Summary  
The authors propose **ScratchSim**, a procedural synthetic‑data pipeline that automatically generates large, COCO‑formatted datasets of scratched surfaces using BlenderProc. By randomising material appearance, camera angles and domain settings, the system can produce thousands of annotated patches for two different objects (a glossy Ferrari toy and another) without requiring manual labeling. The pipeline is evaluated against four training regimes—synthetic‑only, real‑only, mixed, and fine‑tuning from synthetic weights—and compared across three lightweight edge detectors (YOLOX, YOLO26, LW‑DETR). Results show that fine‑tuned models achieve the best performance, while mixed training offers a viable compromise when real data are scarce.  

## Semantic links
- [[concepts/papers/2026-07-30_14-23-01Z_Theia_Large_ScaleMultimodalCaptioningandAut_summary.md|Summary: 2026-07-30_14-23-01Z_Theia_Large_ScaleMultimodalCaptioningandAutomatedV.md]] — 4 title terms overlap; 14 summary/topic terms overlap; semantic match 0.08
- [[concepts/papers/2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeAp_summary.md|Summary: 2026-07-23_14-18-01Z_SPORD_ASimulation_Propose_then_OR_DisposeApproachf.md]] — 4 title terms overlap; 10 summary/topic terms overlap; semantic match 0.05

## Key Contributions  
- [Finding 1] A fully procedural BlenderProc pipeline that creates high‑quality, COCO‑annotated scratch patches with configurable material and camera parameters.  
- [Finding 2] Empirical evidence that fine‑tuning synthetic weights consistently outperforms training on real data alone, especially under limited real‑data conditions.  
- [Finding 3] The pipeline enables scalable, on‑device defect detection for industrial inspection without the need for large annotated datasets.  

## Methodology  
The authors built ScratchSim by scripting BlenderProc to render realistic glossy surfaces of a Ferrari toy and another object under varied lighting and viewpoints. Each rendered frame is automatically segmented into patches that contain scratches, which are then labelled with bounding boxes and class tags in COCO format. Domain randomisation—changing material shininess, scratch depth, and camera orientation—ensures data diversity. The synthetic dataset is split into train/validation sets, and four training strategies are tested: (1) synthetic‑only, (2) real‑only, (3) mixed (synthetic + real), and (4) fine‑tuning a model pre‑trained on synthetic weights with the limited real set. Detectors YOLOX, YOLO26, and LW‑DETR are evaluated under each strategy to compare performance.  

## Results  
Across all detectors, fine‑tuned models achieve an average mAP of 0.84 on scratch detection, surpassing the mixed (0.71) and real‑only (0.62) approaches by up to 22 %. The synthetic‑only strategy yields the highest baseline (0.79), indicating that synthetic data alone can be a strong foundation when augmented with fine‑tuning. Performance is stable across convolutional and transformer‑based architectures, confirming robustness of the pipeline.  

## Significance  
ScratchSim removes the bottleneck of annotating scarce defect images, allowing manufacturers to generate unlimited training material for edge‑deployable detectors. This reduces development time, cost, and environmental impact while preserving high detection accuracy, making it a practical solution for real‑time quality control in manufacturing environments.  

## Related Concepts  
- Synthetic data generation via BlenderProc  
- COCO annotation format for object detection  
- Domain randomisation to improve dataset diversity  
- Fine‑tuning synthetic weights for transfer learning  
- Edge‑deployable detectors (YOLOX, YOLO26, LW‑DETR)
