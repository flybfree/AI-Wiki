# Summary: 2026-07-25_14-23-00Z_BoneAgeTW2_AutomatedSkeletalMaturationAssessmentvi.md
Saved: 2026-07-27 22:37
Source: 2026-07-25_14-23-00Z_BoneAgeTW2_AutomatedSkeletalMaturationAssessmentvi.md
Model: None

---

## Summary
BoneAgeTW2 is an open‑source system that automates the Tanner‑Whitehouse 2 skeletal maturity protocol from image acquisition to clinical reporting. It uses YOLOv8 for precise detection of the 20 hand bones and an EfficientNet‑B3 model with 20 classification heads to assign maturation stages A–I simultaneously. The pipeline also generates PDF reports with interactive Gaussian distribution curves that compare each bone’s age to population norms.

## Key Contributions
- [Finding 1] Integration of YOLOv8 for accurate detection and localization of all 20 hand bones in pediatric radiographs.  
- [Finding 2] Deployment of a multi‑head EfficientNet‑B3 classifier that predicts maturation stages for each bone independently.  
- [Finding 3] Automatic generation of PDF clinical reports with Gaussian distribution curves for direct normative comparison.

## Methodology
The authors trained the detection and classification models on the RSNA Pediatric Bone Age Challenge dataset (12,611 radiographs). A pseudo‑labeling strategy was employed: global bone age annotations were used to infer per‑bone maturation stages, providing high‑quality training labels. YOLOv8 first identifies each hand bone with bounding boxes; then a shared EfficientNet‑B3 backbone processes the images and outputs 20 classification heads producing stage predictions. The system’s end‑to‑end workflow is fully automated, from image preprocessing to report generation.

## Results
Experimental evaluation shows that the YOLOv8 detector achieves an average mAP of 0.48 per bone, while the multi‑head classifier reaches a mean accuracy of 92 % across all stages. The generated reports align with clinical assessments in 95 % of cases, and distribution curves demonstrate strong correlation (Pearson r = 0.71) between predicted ages and population norms.

## Significance
By automating the labor‑intensive TW2 protocol, BoneAgeTW2 reduces assessment time for clinicians and improves consistency across studies. The open‑source release enables rapid adaptation to new datasets and fosters reproducibility in pediatric skeletal maturity research.

## Related Concepts
- Tanner‑Whitehouse 2 (TW2) staging system  
- YOLOv8 object detection  
- EfficientNet‑B3 convolutional neural network  
- Multi‑task classification with per‑bone heads  
- Gaussian distribution curves for normative comparison  
- Pseudo‑labeling in medical imaging
