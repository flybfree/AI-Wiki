---

title: An Open-Source Two-Stage Computer Vision Pipeline for Fine-Grained Vehicle Classification using Vision Transformers
published: "2026-06-03T17:53:33Z"
authors: Gandhimathi Padmanaban, Fred Feng
url: http://arxiv.org/abs/2606.05149v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# An Open-Source Two-Stage Computer Vision Pipeline for Fine-Grained Vehicle Classification using Vision Transformers



**Source**: [Original Paper](http://arxiv.org/abs/2606.05149v1)
## Abstract
Vehicle body type is a significant determinant of cyclist injury severity in overtaking crashes, yet automated tools for classifying vehicles into injury-risk-relevant categories from naturalistic roadway video do not exist in the open literature. Standard object detection benchmarks provide only coarse vehicle labels (car, truck, bus, motorcycle), while existing fine-grained recognition systems are trained on controlled imagery and lack evaluation for deployment robustness across recording sites. This paper presents an open-source two-stage computer vision pipeline combining a pre-trained RT-DETR detector for coarse vehicle localization with a fine-tuned Vision Transformer (ViT-Base/16) for six-category body-type classification: passenger car, SUV, pickup truck, minivan, large van, and commercial truck. A confidence-based abstention mechanism withholds Stage 2 predictions when softmax output falls below 0.60, producing unknown labels rather than silent misclassifications. Evaluated on 3,805 annotated overtaking events from a bicycle-lane corridor in Ann Arbor, Michigan (in-distribution), the pipeline achieved 0.94 accuracy with per-class F1 scores from 0.91 (minivan) to 0.97 (SUV). On an independent out-of-distribution evaluation of 311 events from an open cycling dataset without retraining, accuracy was 0.89. Three of four well-represented categories maintained F1 at or above 0.90 under domain shift. The largest degradation was observed for minivan (F1 = 0.72), driven by abstention rate rising from 2.4% to 25.0% rather than active misclassification, consistent with the mechanism propagating genuine model uncertainty. The full pipeline, including inference scripts, training code, evaluation utilities, and model weights, is released as open-source software to support reproducibility and reuse across roadside video archives and cycling safety research.

## Metadata
- **Published**: 2026-06-03T17:53:33Z
- **Authors**: Gandhimathi Padmanaban, Fred Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.05149v1)