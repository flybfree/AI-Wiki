# Summary: 2026-08-09_20-31-52Z_FromRecoverytoDrop_off_HowActionPost_trainingReduc.md
Saved: 2026-08-10 23:29
Source: 2026-08-09_20-31-52Z_FromRecoverytoDrop_off_HowActionPost_trainingReduc.md
Model: None

---

## Summary  
The paper investigates how action post‑training degrades a vision‑language model’s ability to decode depth, a primitive of spatiogeometric understanding. It compares the base VLM Molmo2‑ER with its action‑post‑trained counterpart MolmoAct2‑LIBERO and finds that while the base improves at later layers, the VLA exhibits a persistent floor and an additional late‑layer “cliff” where depth decodability collapses sharply. The authors attribute this degradation to interference in the accumulated MLP writes of the late decoder layers.

## Key Contributions  
- [Finding 1] Action post‑training introduces a universal floor that reduces depth decodability across all decoder layers, indicating a baseline loss not present in the untrained model.  
- [Finding 2] The VLA suffers an additional late‑layer drop (the cliff) where its depth decoding performance plummets despite the base’s improvement, suggesting a non‑uniform degradation pattern.  
- [Finding 3] Ablating only the late‑layer MLP recovers most of the lost terminal decodability, whereas interventions on attention or the untrained base VLM do not produce comparable recovery.

## Methodology  
The authors probe depth perception from every decoder layer of weight‑matched VLM/VLA pairs by measuring how well each layer can reconstruct a 3‑D depth map. They employ causal ablation experiments: removing the late‑layer MLP versus mutating matched attention or performing the same intervention on the untrained base VLM. This isolates whether the observed cliff is caused specifically by the late‑layer MLP’s accumulated writes.

## Results  
The base VLM shows monotonic improvement in depth decoding across its layers, confirming that action post‑training does not inherently improve this primitive. The VLA exhibits a floor at early layers and then a sharp cliff after a certain point; ablation of the late‑layer MLP recovers roughly 80 % of the terminal performance loss, whereas matched attention ablations or base‑only interventions leave the deficit largely untouched.

## Significance  
These findings reveal that action post‑training can harm fine‑grained spatial reasoning, which is critical for downstream tasks requiring spatiogeometric understanding. The results caution against assuming that adding an action module uniformly benefits a VLM and highlight the need to monitor layer‑wise performance degradation.

## Related Concepts  
- Depth perception (spatiogeometric understanding)  
- Vision‑language model (VLM) architecture  
- Action post‑training for vision‑language‑action models (VLA)  
- Decoder MLP writes and their accumulation  
- Causal ablation studies in transformer layers
