# Summary: 2026-08-03_06-24-36Z_DeferredExposureofFutureTrajectoriesforVerifiableR.md
Saved: 2026-08-03 23:41
Source: 2026-08-03_06-24-36Z_DeferredExposureofFutureTrajectoriesforVerifiableR.md
Model: None

---

## Summary  
The paper addresses a bias introduced when autonomous driving vision‑language‑action (VLA) models are trained with teacher models that see the ground‑truth future trajectory, which causes the models to anchor their reasoning on the outcome rather than infer decisions from scene evidence. This leads to less causally faithful chain‑of‑thought (CoT) explanations and more severe hallucinations in challenging scenes. To remedy this, the authors introduce Autonomous‑Driving Multiple‑Choice Question (AD‑MCQ), a framework that treats planning as selecting among explicit trajectory candidates, and propose Deferred Exposure of Future Trajectories for RLVR (DEFT‑RLVR), which makes trajectories verification targets rather than pre‑decision anchors. The contribution is both the AD‑MCQ formulation and the DEFT‑RLVR method, which decouples high‑level reasoning from low‑level trajectory synthesis.

## Key Contributions  
- [Finding 1] Teacher models exhibit trajectory anchoring bias when exposed to ground‑truth trajectories.  
- [Finding 2] Removing the GT eliminates this bias but open‑ended generation couples reasoning with geometric synthesis, creating a trade‑off between flexibility and accuracy.  
- [Finding 3] DEFT‑RLVR provides a verifiable VLM‑only decision framework that improves reasoning while preserving or even enhancing general visual capabilities.

## Methodology  
The authors first conduct an ablation study to quantify the impact of trajectory exposure, using causal scenario analysis to demonstrate how GT trajectories bias CoT generation. They then design AD‑MCQ as a multiple‑choice planning task where each option corresponds to a pre‑computed trajectory segment generated offline; the VLM must select the correct candidate based on visual evidence alone. DEFT‑RLVR is implemented by storing these candidate trajectories as verification targets and prompting the model to reason about which target matches the current scene, thereby separating decision making from trajectory generation.

## Results  
Experiments show that DEFT‑RLVR reduces hallucination rates by up to 38 % compared with baseline models, improves task success in causally challenging scenes, and maintains or enhances general visual performance. AD‑MCQ enables scalable difficulty tuning through candidate construction, allowing researchers to generate a wide range of reasoning challenges without modifying the model architecture.

## Significance  
By decoupling trajectory generation from reasoning, DEFT‑RLVR offers a principled path toward verifiable autonomous driving that supports auditability and safety verification without costly real‑world simulation. This approach makes it easier to evaluate whether a VLM’s decisions are grounded in scene evidence rather than on pre‑determined outcomes.

## Related Concepts  
Vision‑Language Action models, chain‑of‑thought supervision, trajectory anchoring bias, open‑ended trajectory synthesis, multiple‑choice planning, deferred exposure, RLVR (Reality‑Verified Language Vision Reasoner).
