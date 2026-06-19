---

title: "Summary: Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation"
url: http://arxiv.org/abs/2605.28812v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-27_17-59-02Z_BeyondBinary_Sim_to_RealDexterousManipulationwithP.md
generated_at: "2026-06-11 10:49"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper addresses the sim-to-real gap in contact-rich manipulation by introducing a physics‑grounded tactile representation called Center-of-Pressure (CoP). The authors demonstrate that CoP preserves dense contact information, enabling zero‑shot transfer of policies from simulation to real hardware on a multi‑fingered hand. Their results show that CoP‑conditioned policies outperform both coarse binary‑contact and raw taxel baselines.

## Key Takeaways
- Center-of-Pressure is introduced as an effective tactile representation that retains rich contact data while remaining robust for sim-to-real transfer.
- A sensor calibration scheme based on differentiable dynamics estimates taxel orientations without requiring ground‑truth force measurements.
- CoP‑conditioned policies achieve zero‑shot sim-to-real performance and surpass binary‑contact and raw‑taxel baselines.

## Context
Simulation‑to‑real reinforcement learning struggles with tactile modalities because real contact data are sparse and costly to collect. Existing approaches often reduce touch into low‑dimensional features, losing essential information for complex tasks. This work demonstrates that physics‑based representations can bridge the gap without sacrificing detail.

## Implications
The CoP framework offers a scalable path toward realistic dexterous robotics by leveraging simulated tactile data. Practitioners can develop policies that generalize to real hardware with minimal additional training, reducing reliance on expensive real‑world interaction. This could accelerate research and deployment of human‑like manipulation systems in industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.28812v1)
