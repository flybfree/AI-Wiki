# Summary: 2026-08-05_12-52-14Z_AgenticReinforcementLearningwithObservation_Calibr.md
Saved: 2026-08-05 20:35
Source: 2026-08-05_12-52-14Z_AgenticReinforcementLearningwithObservation_Calibr.md
Model: None

---

## Summary  
Large language model agents are trained via reinforcement learning that relies on sparse trajectory‑level rewards, which provide limited guidance for individual token updates. Existing On‑Policy Self‑Distillation (OPSD) mitigates this by re‑scoring generated tokens under a privileged replay view to obtain dense supervision, but the support can be contaminated by both the scaffold itself and any shifts introduced by future observations. To resolve this confounding, we introduce Observation‑Calibrated Self‑Distillation (OCSD), which derives an observation residual from two structurally matched views—Full and Observation‑Ablated—that isolate the effect of the actual observation. OCSD then applies this residual to modulate token‑level GRPO updates at high‑uncertainty steps while preserving trajectory‑level direction, yielding a more reliable supervision signal.

## Key Contributions  
- **Finding 1:** The replay scaffold and future observations both influence token scores, causing a confounding problem in OPSD.  
- **Finding 2:** We propose Observation‑Calibrated Self‑Distillation (OCSD), which computes an observation residual by contrasting Full and Observation‑Ablated replay views.  
- **Finding 3:** Applying the calibrated residual to token‑level updates improves performance across multiple benchmarks while keeping trajectory guidance intact.

## Methodology  
The authors construct two replay views that are identical except for the presence of the actual future observation: the *Full* view includes it, while the *Observation‑Ablated* view removes it. By subtracting the scores from these views, they obtain an *observation residual* that reflects only changes attributable to the observation itself and not to the scaffold. This residual is used as a calibration factor in token‑level GRPO updates; at steps where model confidence is high (low uncertainty), the update direction remains unchanged, but when confidence drops, the residual modulates the magnitude of the gradient, effectively down‑weighting or up‑weighting updates based on observed data.

## Results  
Experiments were conducted on three tasks—ALFWorld (simulation), WebShop (online shopping), and Search‑QA (question answering)—using Qwen3 models at small, medium, and large scales. OCSD consistently outperformed strong baselines such as standard OPSD and conventional RL agents, achieving higher reward scores and lower token‑level error rates. Diagnostic analyses confirmed that the residual aligns more closely with local environment feedback than raw replay scores, indicating successful calibration.

## Significance  
By separating confounding sources of supervision from those arising solely from future observations, OCSD enables a cleaner, more reliable token‑level learning signal in agentic reinforcement learning. This improves training efficiency and performance without sacrificing the trajectory‑level guidance that RL relies on, offering a novel calibration technique for self‑distillation methods.

## Related Concepts  
- Reinforcement Learning with Sparse Rewards  
- On‑Policy Self‑Distillation (OPSD)  
- Gradient Policy Optimization (GRPO)  
- Observation Calibration  
- Token‑level Supervision  
- Structured View Contrast
