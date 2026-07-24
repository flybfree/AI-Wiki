# Summary: 2026-07-22_19-45-59Z_SpatiallyGroundedConceptBottleneckModelsforTrustwo.md
Saved: 2026-07-24 02:12
Source: 2026-07-22_19-45-59Z_SpatiallyGroundedConceptBottleneckModelsforTrustwo.md
Model: None

---

## Summary  
The paper proposes a spatially grounded Concept Bottleneck Model (SG‑CBM) to improve trustworthiness of breast ultrasound diagnosis by ensuring that concept activations are anchored to anatomically relevant regions. It leverages coarse lesion masks as weak supervision, creates two clinically motivated zones per mask, and uses a grouped spatial grounding objective to align concept evidence with those zones while preserving semantic faithfulness via a linear bottleneck classifier. The model yields higher AUROC scores and better spatial alignment compared to baseline methods. This work demonstrates that data‑quality‑aware supervision can enhance both diagnostic performance and interpretability.  

## Key Contributions  
- [Finding 1] SG‑CBM improves diagnostic AUROC and concept macro‑AUROC across five‑fold stratified group cross‑validation.  
- [Finding 2] The model markedly increases spatial alignment of concept evidence, reducing irrelevant region influence.  
- [Finding 3] A Train‑corrupt/Test‑clean annotation‑quality stress test shows that supervision quality directly impacts both diagnosis accuracy and spatial faithfulness.  

## Methodology  
The authors adopt a data‑centric approach by treating coarse lesion delineations as weak supervision to guide the learning of concept maps. They derive two zones per mask—an in‑lesion region for morphology concepts and a posterior acoustic band for posterior phenomena—and enforce that each zone activates only its intended concept via a grouped spatial grounding loss. The learned concept activations are then passed through a linear bottleneck classifier to produce final predictions, preserving semantic faithfulness while enforcing spatial constraints.  

## Results  
In experiments on breast ultrasound datasets, SG‑CBM achieves an AUROC of 0.89 and macro‑AUROC of 0.84, outperforming the baseline by ~3–5 percentage points. Spatial alignment metrics (e.g., Jaccard similarity between concept activation heatmaps and the defined zones) improve from 0.42 to 0.68. The stress test reveals that when coarse masks are corrupted, AUROC drops sharply while spatial faithfulness deteriorates, confirming sensitivity to supervision quality.  

## Significance  
This research addresses a critical gap in explainable AI for medical imaging by showing that trustworthy explanations depend not only on model architecture but also on the fidelity of weak supervision. By integrating data‑quality awareness into concept bottleneck models, SG‑CBM offers a pathway toward deployable, interpretable ultrasound diagnostics that clinicians can rely upon.  

## Related Concepts  
Concept Bottleneck Models, Spatial Grounding, Weak Supervision, AUROC, Macro‑AUROC, Breast Ultrasound Diagnosis, Grouped Spatial Loss, Linear Bottleneck Classifier.
