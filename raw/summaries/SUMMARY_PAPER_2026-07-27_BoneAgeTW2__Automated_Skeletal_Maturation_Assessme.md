---
title: BoneAgeTW2: Automated Skeletal Maturation Assessment via the Tanner-Whitehouse 2 Method, Deep Learning, and Clinical Report Generation with Distribution Curves
url: http://arxiv.org/abs/2607.23224v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_14-23-00Z_BoneAgeTW2_AutomatedSkeletalMaturationAssessmentvi.md
generated_at: 2026-07-27 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary  
BoneAgeTW2 automates the Tanner‑Whitehouse 2 skeletal maturity protocol using YOLOv8 to detect and label each of the 20 hand bones in radiographs, then classifies their maturation stages with an EfficientNet‑B3 model. The system produces PDF reports that include interactive Gaussian distribution curves for every bone compared to population norms. Trained on the RSNA Pediatric Bone Age Challenge dataset through pseudo‑labeling, it offers a fully open‑source solution.

## Key Takeaways  
- YOLOv8 precisely detects and localizes all 20 hand bones from single radiographs.  
- A multi‑head EfficientNet‑B3 assigns maturation stages A to I simultaneously for each bone.  
- The generated PDF reports feature interactive Gaussian distribution curves enabling direct comparison with normative data.

## Context  
Automating skeletal maturity assessment reduces reliance on manual radiology interpretation and speeds up clinical decision making. This work advances AI applications in pediatric imaging by integrating deep detection, classification, and report generation into a single pipeline.

## Implications  
Clinicians can now obtain standardized bone age estimates quickly, improving diagnostic consistency across diverse populations. The open‑source codebase encourages broader adoption and further research into similar automated assessment tools for other clinical parameters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23224v1)
