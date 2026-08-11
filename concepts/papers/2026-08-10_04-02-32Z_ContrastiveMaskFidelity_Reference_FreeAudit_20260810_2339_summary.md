# Summary: 2026-08-10_04-02-32Z_ContrastiveMaskFidelity_Reference_FreeAuditingofGr.md
Saved: 2026-08-10 23:39
Source: 2026-08-10_04-02-32Z_ContrastiveMaskFidelity_Reference_FreeAuditingofGr.md
Model: None

---

## Summary  
Semantic segmentation in remote sensing suffers from coarse, incomplete, or misaligned ground‑truth masks, which can inflate overlap scores and create an evaluation paradox where model performance is judged against imperfect labels rather than the image itself. To resolve this, the authors introduce Contrastive Mask Fidelity (CMF), a training‑free, reference‑free metric that evaluates competing class masks directly from visual evidence without relying on human annotations. CMF composites keep and erase counterfactual views of each mask and asks a frozen vision‑language judge whether class evidence is concentrated inside the mask and absent outside. This approach enables an audit of ground truth rather than assuming it is flawless.

## Key Contributions  
- [Finding 1] CMF provides a reference‑free, contrastive metric that scores masks by comparing them to image evidence using keep/erase view generation and a frozen vision‑language judge.  
- [Finding 2] The audit of 10,731 image‑class pairs across ten remote‑sensing benchmarks reveals systematic class‑dependent annotation distortion: man‑made classes (buildings, roads, cars) favor candidate masks on 62–85 % of pairs, whereas ambiguous land cover more often favors human annotations.  
- [Finding 3] Blind three‑annotator consensus shows that CMF matches expert judgment on 81 % of pairs, outperforming keep‑only scoring, model confidence, and a trained label‑quality baseline.

## Methodology  
CMF constructs two counterfactual views for each candidate mask: one where the mask is kept intact and another where it is erased. These views are fed to a frozen vision‑language judge that classifies whether the evidence (e.g., object classes) is present inside the mask and absent outside. The metric scores the difference between the two view predictions, yielding a fidelity value for each mask. Candidate masks are generated from Seg‑Probe, an open‑vocabulary probe built on SegEarth‑OV3, which selects masks that best match the image evidence without human supervision.

## Results  
CMF is evaluated on ten remote‑sensing datasets; it outperforms prior baselines on nine of the ten. The audit of 10,731 image‑class pairs across all benchmarks demonstrates the systematic bias described above. When applied to a blinded three‑annotator consensus task, CMF aligns with expert decisions on 81 % of pairs, significantly exceeding keep‑only scores (≈65 %), model confidence (≈70 %), and a trained label‑quality baseline (≈62 %). Conservative class‑wise arbitration further improves cross‑domain transfer compared to raw annotations and matched replacement controls.

## Significance  
CMF shifts the focus from assuming ground truth is perfect to auditing it, offering a scalable tool for remote‑sensing semantic segmentation that can improve annotation quality and model training. By exposing systematic annotation distortions—particularly in man‑made classes—the method helps researchers prioritize data cleaning and better understand label reliability.

## Related Concepts  
Semantic segmentation, remote sensing, mask fidelity, contrastive learning, vision‑language alignment, open‑vocabulary probe, class‑dependent annotation distortion, blind consensus evaluation.
