---
title: "Summary: 2026-06-03_17-53-33Z_AnOpen_SourceTwo_StageComputerVisionPipelineforFin.md"
date: 2026-06-03
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-03_17-53-33Z_AnOpen_SourceTwo_StageComputerVisionPipelineforFin.md


**Source**: [Original Paper](http://arxiv.org/abs/2606.05149v1)
Saved: 2026-06-04 00:00
Source: 2026-06-03_17-53-33Z_AnOpen_SourceTwo_StageComputerVisionPipelineforFin.md
Model: None

---


## Summary  
The paper proposes an open‑source two‑stage computer vision pipeline that first localizes vehicles using a pre‑trained RT‑DETR detector and then classifies their body types with a fine‑tuned Vision Transformer (ViT‑Base/16) for six injury‑relevant categories. A confidence‑based abstention mechanism outputs “unknown” when the softmax score falls below 0.60, preventing silent misclassifications that could hide genuine uncertainty. The pipeline is evaluated on naturalistic overtaking video from Ann Arbor and shown to maintain high accuracy even under domain shift.  

## Key Contributions  
- Introduces a two‑stage CV pipeline combining RT‑DETR detection with ViT classification for fine‑grained vehicle body‑type identification.  
- Implements confidence‑based abstention, yielding “unknown” labels instead of silent misclassifications to improve reliability when model uncertainty is high.  
- Releases the complete inference scripts, training code, evaluation utilities and model weights as open‑source software for reproducibility across roadside video archives.  

## Methodology  
The authors first run the pre‑trained RT‑DETR detector on each frame of a naturalistic overtaking video to obtain bounding boxes around vehicles. Those detections are then fed into a ViT‑Base/16 classifier that has been fine‑tuned on six body‑type categories: passenger car, SUV, pickup truck, minivan, large van and commercial truck. The classifier outputs softmax probabilities; if the maximum probability is below 0.60, the system abstains and records an “unknown” label rather than a low‑confidence prediction. This two‑stage flow ensures that localization errors are mitigated by only classifying when the model is confident enough.  

## Results  
On 3,805 annotated overtaking events from a bicycle‑lane corridor in Ann Arbor (in‑distribution), the pipeline achieved an overall accuracy of 0.94 with per‑class F1 scores ranging from 0.91 (minivan) to 0.97 (SUV). An independent out‑of‑distribution test on 311 events from another open cycling dataset, without retraining, yielded an accuracy of 0.89. Three well‑represented categories retained F1 ≥ 0.90 despite domain shift, while minivan dropped to 0.72 due primarily to the abstention rate rising from 2.4 % to 25 %, indicating genuine uncertainty rather than misclassification.  

## Significance  
This work delivers a reliable, open‑source tool for cyclist safety research by accurately identifying injury‑risk vehicle types in naturalistic video without producing false negatives that could mask dangerous situations. The confidence‑based abstention improves robustness to unseen scenes and the released code encourages broader adoption across roadside video archives and safety studies.  

## Related Concepts

- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/ai-safety/ai-safety-hub.md|AI Safety Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]
