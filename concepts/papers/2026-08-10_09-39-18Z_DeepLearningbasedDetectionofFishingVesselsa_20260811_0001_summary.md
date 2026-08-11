# Summary: 2026-08-10_09-39-18Z_DeepLearningbasedDetectionofFishingVesselsandFishi.md
Saved: 2026-08-11 00:01
Source: 2026-08-10_09-39-18Z_DeepLearningbasedDetectionofFishingVesselsandFishi.md
Model: None

---

## Summary  
The paper proposes a deep‑learning framework that detects small‑scale fishing vessels using nightlight (NTL) imagery from the SDGSAT‑1 satellite, with a focus on the western coast of India where many vessels operate without Automatic Identification System (AIS). It introduces a dual‑branch YOLO11 architecture that jointly processes 10‑meter panchromatic and 40‑meter RGB data to improve detection of low‑contrast objects in NTL scenes. The model achieves high precision, recall and F1 scores, detecting thousands of vessel instances across the 2022‑23 temporal dataset. Crucially, cross‑matching with AIS shows that only a minority of detections correspond to reported transmissions, indicating a large proportion of “dark vessels” that remain undetected by conventional systems.

## Key Contributions  
- Finding 1: The dual‑branch YOLO11 architecture outperforms single‑branch implementations (YOLOv5s, YOLOv8s, YOLO11s) with a precision of 0.99, recall of 0.93, F1‑score of 0.96 and mAP@50 of 0.96.  
- Finding 2: The model successfully detects 31 525 vessel instances across the western‑coast dataset, demonstrating strong performance on small objects within NTL imagery.  
- Finding 3: Spatio‑temporal analysis reveals peak fishing activity from January to April and a primary activity corridor parallel to the coastline within 50–100 km, corresponding to productive continental shelf zones.

## Methodology  
The authors collected nightlight images from SDGSAT‑1 covering both panchromatic (10 m resolution) and RGB (40 m resolution) bands for the western Indian coast. A custom dual‑branch YOLO11 network was built: each branch processes one modality separately, producing feature maps that are concatenated before feeding into the standard YOLO detection head. The model was trained on a labeled subset of NTL scenes and evaluated using standard object‑detection metrics.

## Results  
The experimental results show that the dual‑branch YOLO11 reaches 99 % precision, 93 % recall and an F1‑score of 0.96, with mAP@50 of 0.96—significantly higher than baseline single‑branch models. Over the temporal period 2022–23, the detector identified 31 525 vessel instances. Cross‑matching with AIS data revealed that 7 146 detections (22.7 %) correspond to reported transmissions, while 24 379 (77.3 %) are classified as potential dark vessels.

## Significance  
This work provides a practical tool for maritime surveillance by enabling reliable detection of fishing vessels that evade AIS reporting, thereby supporting regulatory compliance and fisheries management in Indian waters. The high detection rates and identified “dark‑vessel” prevalence highlight gaps in current monitoring systems and suggest the need for integrated satellite‑based nightlight analysis.

## Related Concepts  
- Nightlight imagery (NTL) from SDGSAT‑1 satellite  
- Dual‑branch YOLO11 architecture  
- Small‑object detection in low‑contrast scenes  
- Automatic Identification System (AIS) data  
- Maritime surveillance and dark‑vessel monitoring  
- Continental shelf fishing activity patterns
