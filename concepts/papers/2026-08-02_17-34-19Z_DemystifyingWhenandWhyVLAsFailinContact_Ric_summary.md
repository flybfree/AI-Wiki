# Summary: 2026-08-02_17-34-19Z_DemystifyingWhenandWhyVLAsFailinContact_RichTasksa.md
Saved: 2026-08-04 00:18
Source: 2026-08-02_17-34-19Z_DemystifyingWhenandWhyVLAsFailinContact_RichTasksa.md
Model: None

---

## Summary  
The paper seeks to uncover why Vision‑Language‑Action (VLA) models falter in contact‑rich manipulation tasks that demand precise physical interaction. It identifies two distinct failure modes: precision failures caused by a mismatch between the vision‑language policy and the action policy, and force failures arising from the noisy, non‑stationary nature of force signals. To address these issues, the authors introduce FACT—a combined correction framework that targets both problems simultaneously. This work moves beyond prior force‑augmentation tricks toward a principled understanding of VLA breakdowns.

## Key Contributions  
- Finding 1: Precision failures stem from a training objective misalignment between the visual‑language encoder and the downstream action policy, leading to suboptimal trajectory generation.  
- Finding 2: Force signals are inherently noisy and exhibit non‑stationary dynamics, causing systematic errors in force estimation during contact events.  
- Finding 3: FACT integrates a calibrated flow‑matching loss for precision correction with a structured regularizer that enforces realistic force profiles, jointly improving both failure modes.

## Methodology  
The authors conduct extensive rollout experiments across five real‑world contact‑rich tasks using a standard robot platform. They systematically compare FACT against the best prior baseline, measuring success rates and conducting ablations where each component (precision correction vs. force correction) is disabled to isolate its impact on performance.

## Results  
FACT achieves an average success rate of 66 % across the five tasks, whereas the previous best baseline reaches only 41 %. The improvement persists over roughly 2,500 rollouts, and ablation studies show that removing either correction reduces success by about 10 percentage points, confirming each mechanism’s necessity.

## Significance  
Understanding these failure modes enables more reliable physical interaction in robotics, moving beyond band‑aid solutions to principled architectural fixes. This research thus paves the way for VLA systems capable of handling precise, contact‑dependent actions without resorting to ad‑hoc force augmentation.

## Related Concepts  
Vision‑Language‑Action models, flow‑matching policy training, force signals, contact‑rich manipulation tasks, precision vs. force failures, regularization techniques, rollout evaluation, action policies, visual grounding.
