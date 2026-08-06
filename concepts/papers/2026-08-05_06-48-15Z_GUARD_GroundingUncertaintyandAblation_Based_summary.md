# Summary: 2026-08-05_06-48-15Z_GUARD_GroundingUncertaintyandAblation_BasedRiskDet.md
Saved: 2026-08-05 20:31
Source: 2026-08-05_06-48-15Z_GUARD_GroundingUncertaintyandAblation_BasedRiskDet.md
Model: None

---

## Summary  
GUARD is a test‑time failure detection method that quantifies how well diffusion‑based vision‑language‑action (VLA) policies ground their actions in multimodal evidence without altering the pretrained model. By probing the influence of token‑indexed key‑value (KV) cache entries, constructing counterfactual caches through ablation, and comparing denoising responses to the original conditioning, GUARD derives a diagnostic stream that flags grounding failures. The approach yields transferable signals across diverse policies, tasks, and domains, improving detection performance relative to existing runtime monitors.

## Key Contributions  
- [Finding 1] GUARD provides a test‑time failure detection framework that measures grounding without modifying the pretrained VLA policy.  
- [Finding 2] It constructs counterfactual caches by ablating salient KV entries and compares their denoising responses to the original conditioning, producing a calibrated diagnostic stream (sensitivity, attention entropy, modality bias, grounding efficiency).  
- [Finding 3] The method delivers a transferable failure signal that improves average unseen‑task ROC‑AUC by 5.73 points while staying within 0.19 points of the best seen‑task performance.

## Methodology  
The authors estimate the influence of each token‑indexed entry in the final VLA model’s key‑value cache, then create counterfactual caches by removing those entries. The denoising responses of these altered caches are compared to the original conditioning; differences generate a diagnostic stream that is calibrated online and fed into a lightweight temporal classifier for real‑time failure detection.

## Results  
GUARD achieves the best ROC‑AUC on four out of five unseen‑task settings across benchmark policies (Pi0, SmolVLA, Alpamayo‑1.5) and environments (LIBERO, SimplerEnv, MetaWorld, PhysicalAI‑AV). It ranks second on the remaining setting. The method improves the average unseen‑task ROC‑AUC by 5.73 percentage points over the strongest competing runtime monitor while its seen‑task average is within 0.19 points of the best reported value.

## Significance  
By directly probing action‑head dependence on multimodal evidence, GUARD reveals a universal failure signal that can be applied across different diffusion‑based VLA policies, tasks, embodied agents, and domains, thereby enhancing robustness and safety in autonomous systems.

## Related Concepts  
diffusion‑based VLA, key‑value cache, ablation testing, grounding, ROC‑AUC, temporal classifier, multimodal evidence, counterfactual caches.
