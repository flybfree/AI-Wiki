# Summary: 2026-08-10_09-39-18Z_DeepLearningbasedDetectionofFishingVesselsandFishi.md
Saved: 2026-08-10 23:44
Source: 2026-08-10_09-39-18Z_DeepLearningbasedDetectionofFishingVesselsandFishi.md
Model: None

---

## Summary  
This paper proposes a deep‑learning framework that detects small‑scale fishing vessels using nightlight (NTL) imagery from the SDGSAT‑1 satellite, specifically targeting “dark vessels” that lack AIS signals. By integrating a dual‑branch YOLO11 architecture that fuses 10‑m panchromatic and 40‑m RGB bands, the model achieves state‑of‑the‑art performance for maritime surveillance along India’s western coast. The approach not only improves detection rates over single‑band alternatives but also quantifies how many of the identified vessels are illegal or unregistered.  

## Key Contributions  
- [The dual‑branch YOLO11 model, which processes both panchromatic and RGB NTL bands in parallel, delivers higher precision (0.99) and recall (0.93) than single‑band YOLOv5s, YOLOv8s, or standard YOLO11s.]  
- [Cross‑matching with AIS data shows that 77 % of detected vessels are potential dark vessels, highlighting a significant gap in current monitoring.]  
- [Spatio‑temporal analysis reveals peak fishing activity from January to April within a 50–100 km coastal corridor on the productive continental shelf.]  

## Methodology  
The authors built a custom YOLO11 architecture with two convolutional backbones: one tuned for the high‑resolution 10‑m panchromatic imagery and another for the broader 40‑m RGB imagery. These feature maps are concatenated, preserving modality information before feeding into the detection head. The model was trained on a temporal dataset covering 2022–23, using standard YOLO loss functions to maximize mAP@50.  

## Results  
The dual‑branch YOLO11 achieved an F1‑score of 0.96 and mAP@50 of 0.96, outperforming all single‑band baselines. Over the entire dataset it identified 31 525 vessel instances; only 7 146 (22.7 %) had corresponding AIS transmissions, while 24 379 (77.3 %) were classified as dark vessels. Peak activity occurred in January–April along a corridor parallel to the coastline within 50–100 km of shore.  

## Significance  
This work extends maritime surveillance by providing a reliable, automated means to spot illegal fishing operations that evade AIS reporting. The high detection precision and recall reduce false alarms while capturing most illicit vessels, supporting regulatory enforcement and conservation efforts in Indian waters.  

## Related Concepts  
- Nightlight (NTL) imagery from satellite constellations  
- Automatic Identification System (AIS) tracking  
- Dark vessels as unregistered fishing craft  
- YOLO11 deep‑learning object detector  
- Spatio‑temporal analysis for activity pattern detection
