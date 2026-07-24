# Summary: 2026-07-22_19-45-59Z_SpatiallyGroundedConceptBottleneckModelsforTrustwo.md
Saved: 2026-07-24 02:16
Source: 2026-07-22_19-45-59Z_SpatiallyGroundedConceptBottleneckModelsforTrustwo.md
Model: None

---

## Summary  
The paper proposes a spatially grounded concept bottleneck model (SG‑CBM) to improve trustworthiness of breast ultrasound diagnosis by using weakly supervised lesion masks as ground truth. It introduces two clinically relevant zones per mask—an in‑lesion region for morphology concepts and a posterior acoustic band for posterior phenomena—and employs a grouped spatial grounding objective that aligns predicted concept activations with these anatomical zones. A linear bottleneck classifier preserves semantic faithfulness, yielding both higher diagnostic performance and more spatially aligned explanations.

## Key Contributions  
- [Finding 1] SG‑CBM improves AUROC and macro‑AUROC of diagnosis compared to baseline methods.  
- [Finding 2] The model markedly increases spatial alignment between concept evidence and lesion regions.  
- [Finding 3] A stress test shows that supervision quality critically influences both diagnostic accuracy and explanation trustworthiness.

## Methodology  
The authors construct a data‑centric framework where coarse lesion masks serve as weak supervision, defining an in‑lesion region for morphology concepts and a posterior acoustic band for posterior phenomena. They train concept maps using a grouped spatial grounding loss that penalizes misalignment between predicted activations and these zones, while a linear bottleneck classifier ensures the final diagnosis remains semantically faithful.

## Results  
Across five‑fold stratified group cross‑validation on breast ultrasound data, SG‑CBM achieves higher AUROC (e.g., 0.84 vs 0.79) and macro‑AUROC for concept predictions, with visual inspection confirming sharper spatial correspondence to lesions. The Train‑corrupt/Test‑clean annotation‑quality test quantifies that poor supervision degrades both diagnosis and alignment.

## Significance  
This work demonstrates that trustworthy AI in healthcare requires not only high accuracy but also data‑quality‑aware supervision and systematic validation of explanation fidelity, guiding future deployment pipelines.

## Related Concepts  
- Concept Bottleneck Models  
- Spatial grounding  
- Weak supervision  
- AUROC  
- Macro‑AUROC
