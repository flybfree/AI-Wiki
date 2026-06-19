---

title: "Summary: Humanoid-GPT: Scaling Data and Structure for Zero-Shot Motion Tracking"
url: http://arxiv.org/abs/2606.03985v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-02_17-59-05Z_Humanoid_GPT_ScalingDataandStructureforZero_ShotMo.md
generated_at: "2026-06-11 10:52"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper presents Humanoid-GPT, a GPT‑style transformer trained on a billion frames of motion data to perform whole‑body control. The model achieves zero‑shot generalization to unseen motions and tasks while tracking highly dynamic behaviors. Experiments show unprecedented performance across multiple datasets.

## Key Takeaways
- The model is pre‑trained on a 2B‑frame retargeted corpus that unifies major mocap datasets, enabling massive data scaling.
- Causal attention allows the transformer to capture long‑range dependencies in motion sequences, supporting zero‑shot transfer.
- Scaling both data and model capacity yields a single generative architecture that tracks complex motions without task‑specific fine‑tuning.

## Context
The need for scalable, data‑efficient trackers has driven research toward large language models applied to robotics. This work demonstrates that similar scaling principles can improve robotic control systems beyond traditional MLP approaches.

## Implications
Humanoid‑GPT could serve as a foundation for real‑time humanoid control, reducing reliance on labeled datasets and enabling rapid adaptation to new tasks. Practitioners may adopt this framework to build flexible, zero‑shot capable robotic agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.03985v1)
