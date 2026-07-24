# Summary: 2026-06-27_14-23-21Z_ReGuide_FromTest_TimeGuidancetoSelf_ImprovingDiffu.md
Saved: 2026-07-23 23:36
Source: 2026-06-27_14-23-21Z_ReGuide_FromTest_TimeGuidancetoSelf_ImprovingDiffu.md
Model: None

---

## Summary  
Behavior‑cloned diffusion policies are expressive but suffer from covariate shift, where small deviations from demonstrated states can cause task failure. ReGuide addresses this by treating test‑time guidance as a source of reusable on‑policy recovery data, enabling the policy to generate corrective rollouts and then fine‑tune or retrain itself using those trajectories. The framework introduces Phase‑Conditioned Guidance (PCG) for targeted correction and two integration strategies—ReGuide‑FT (fine‑tuning) and ReGuide‑FS (full retraining)—that can be composed iteratively. Empirically, it boosts success rates dramatically across multiple robotics benchmarks.

## Key Contributions  
- [Finding 1] PCG constructs phase‑specific latent targets that identify the drifted‑but‑recoverable regime, applying guidance only where needed to avoid unnecessary correction effort.  
- [Finding 2] ReGuide‑FT and ReGuide‑FS integrate guided rollouts back into training via fine‑tuning or full retraining, creating a self‑improving loop that reuses the same corrected trajectories.  
- [Finding 3] Experiments on Robomimic Can, Square, Transport, and Tool Hang show base‑policy success improvements of 1.3–7.7× and outperform LPB in test‑time‑only settings; matched‑data ablations confirm that gains stem from the recovery data rather than extra rollouts alone.

## Methodology  
The authors treat guided rollouts as reusable on‑policy recovery data by first using PCG to generate phase‑specific latent targets. Guidance is applied exclusively within the drift‑recoverable regime, steering the diffusion model toward the estimated clean action that matches its training distribution. Successful corrected trajectories are then fed into ReGuide‑FT (a fine‑tuning step) or ReGuide‑FS (a full retraining step). The two strategies can be chained, allowing iterative self‑improvement without relying on expensive expert corrections or synthetic augmentations.

## Results  
On Robomimic Can, Square, Transport, and Tool Hang, the base policy’s success rate is increased by a factor of 1.3–7.7× compared with the original behavior‑cloned model. In test‑time‑only evaluations, ReGuide outperforms LPB, demonstrating that the self‑improving loop can be applied without additional rollouts. Matched‑data ablations reveal that the observed gains are attributable to the guided recovery data rather than merely more training steps.

## Significance  
ReGuide bridges test‑time guidance and self‑improvement, offering a scalable method to maintain diffusion policy performance under covariate shift. By reusing corrected trajectories as on‑policy data, it reduces reliance on costly external corrections while preserving the expressiveness of behavior‑cloned policies—a key advance for real‑world robotics where drift is inevitable.

## Related Concepts  
- Behavior‑cloned diffusion policies  
- Covariate shift  
- Phase‑Conditioned Guidance (PCG)  
- On‑policy recovery data  
- Fine‑tuning vs. full retraining  
- Test‑time guidance  
- Diffusion models
