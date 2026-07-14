---

title: "Summary: FACTR 2: Learning External Force Sensing for Commodity Robot Arms Improves Policy Learning"
url: http://arxiv.org/abs/2606.12406v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-10_17-59-35Z_FACTR2_LearningExternalForceSensingforCommodityRob.md
generated_at: "2026-06-11 10:57"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-06-10 17-59-35Z Factr2 Learningexternalforcesensingforcommodityrob


## Summary
Neural External Torque Estimation (NEXT) estimates external joint torques from free-motion data, enabling force-feedback teleoperation on low-cost arms without dedicated sensors. The paper also introduces Force-Informed Re‑Sampling Training (FIRST), which up‑samples contact segments during behavior cloning to improve policy learning. Together they achieve over 17% progress gains across five long-horizon tasks.

## Key Takeaways
- NEXT trains in one minute from ten minutes of free-motion data and matches the accuracy of dedicated joint‑torque sensors.
- FIRST up‑samples pre-contact and contact segments during behavior cloning to provide more force information.
- The combined approach yields over 17% improvement in task progress compared with prior force‑aware policies.

## Context
This work addresses the gap between high performance in manipulation tasks and the cost of adding dedicated force sensors, a common bottleneck for off‑the‑shelf robots. By leveraging only existing joint encoders, it makes advanced force feedback accessible to low‑cost robotic arms.

## Implications
The results suggest that AI methods can compensate for missing hardware, opening doors for teleoperation in resource‑constrained settings. Practitioners can adopt these techniques without purchasing new sensors, accelerating deployment of safe and precise manipulation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.12406v1)
