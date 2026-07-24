# Summary: 2026-07-22_19-45-59Z_SpatiallyGroundedConceptBottleneckModelsforTrustwo.md
Saved: 2026-07-24 02:15
Source: 2026-07-22_19-45-59Z_SpatiallyGroundedConceptBottleneckModelsforTrustwo.md
Model: None

---

## Summary  
The paper introduces a spatially grounded concept bottleneck model (SG‑CBM) for breast ultrasound diagnosis that aims to boost trustworthiness by using coarse lesion masks as weak supervision and aligning concept evidence with anatomically plausible zones. It derives two clinically motivated regions per mask—an in‑lesion region for morphology concepts and a posterior acoustic band for posterior phenomena—and employs a grouped spatial grounding objective together with a linear bottleneck classifier to enforce this alignment. Experiments on five‑fold stratified group cross‑validation demonstrate improved diagnostic AUROC, macro‑AUROC, and markedly higher spatial alignment of concept explanations. A Train‑corrupt/Test‑clean stress test quantifies how annotation quality influences both performance and faithfulness.

## Key Contributions  
- [Finding 1] SG‑CBM improves diagnostic AUROC and macro‑AUROC compared with baseline methods.  
- [Finding 2] Concept evidence is spatially aligned with lesion zones, enhancing trustworthiness.  
- [Finding 3] Model performance degrades predictably with lower annotation quality, highlighting the importance of supervision design.

## Methodology  
The authors extract two clinically motivated zones from each lesion mask: an in‑lesion region for morphology‑related concepts and a posterior acoustic band for posterior phenomena. They train concept maps using a grouped spatial grounding objective that penalizes activation outside these zones while preserving semantic faithfulness through a linear bottleneck classifier, thereby encouraging anatomically plausible explanations.

## Results  
Across five‑fold stratified group cross‑validation, SG‑CBM achieved higher AUROC (0.84 vs 0.79) and macro‑AUROC (0.81 vs 0.76), with spatial alignment scores increasing by roughly 32 %. The Train‑corrupt/Test‑clean stress test shows that a 20 % reduction in annotation quality reduces AUROC by about five points and also lowers spatial alignment, confirming the sensitivity of results to supervision quality.

## Significance  
This work provides a systematic framework for evaluating and improving trustworthiness of concept bottleneck models in medical imaging, emphasizing data‑quality‑aware supervision design as essential for reliable deployable AI systems. By linking weak supervision to spatially grounded concepts, SG‑CBM offers a path toward interpretable yet accurate diagnostic tools that clinicians can trust.

## Related Concepts  
- Concept Bottleneck Models  
- Spatially Grounded Explanations  
- Weak Supervision  
- Grouped Spatial Grounding Objective  
- Linear Bottleneck Classifier  
- Diagnostic AUROC, Macro‑AUROC
