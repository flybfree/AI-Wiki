---
title: FWBC-VLA: Force-Aware Whole-Body Compensation for Contact-Rich Loco-Manipulation
url: http://arxiv.org/abs/2609.03889v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_14-10-47Z_FWBC_VLA_Force_AwareWhole_BodyCompensationforConta.md
generated_at: 2026-09-03 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes FWBC-VLA, a force‑aware framework that connects vision‑language‑action generation with whole‑body compensation for wheeled‑legged robots in contact‑rich loco‑manipulation. It introduces HSR‑Force to estimate sensorless residual torques and injects them as tokens into the VLA decoder, enabling perception of contact events. Real‑world tests on whiteboard wiping and door opening show improved control.

## Key Takeaways
- HSR‑Force provides a sensorless estimator that captures contact strength and its temporal changes without hardware sensors.
- The estimated contact state is tokenized and fed into the VLA action expert, allowing the policy to perceive onset, sustained loading, and release of contacts.
- Jointly feeding proprioceptive data, Jacobian‑derived force estimates, and contact tokens into a compensation generator yields corrective actions that are combined with manipulation actions before execution by WBC.

## Context
This work advances AI for embodied agents by integrating high‑level task perception with low‑level physical control, addressing the gap between semantic action generation and real‑world interaction. It demonstrates how sensorless force estimation can be embedded within vision‑language pipelines to improve robustness in unstructured environments.

## Implications
For robotics engineers, FWBC‑VLA reduces reliance on costly force/torque sensors while enhancing task reliability. Practitioners can leverage the framework for any wheeled‑legged platform needing contact‑aware manipulation without major hardware changes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03889v1)
