---
title: ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback
url: http://arxiv.org/abs/2608.17323v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_03-30-12Z_ORPA_OnlineResidualPolicyAdaptationforRobotManipul.md
generated_at: 2026-08-18 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Online Residual Policy Adaptation (ORPA), a method that corrects robot manipulation actions on the fly using human feedback without retraining the original policy. ORPA adds a lightweight module that predicts residual adjustments directly in joint space, enabling immediate adaptation to small errors and distribution shifts. Experiments on precision-sensitive tasks show higher success rates and faster recovery compared with baseline policies and rule‑based inverse kinematics.

## Key Takeaways
- ORPA provides real‑time correction of robot actions through a feedback‑conditioned residual module that operates in joint space, avoiding full policy retraining.
- The framework improves success rates on precision tasks by directly compensating for small execution errors and distribution shifts without dataset aggregation.
- Compared to baseline control policies and rule‑based inverse kinematics corrections, ORPA achieves faster recovery from perturbations.

## Context
Current imitation learning approaches like Action Chunking with Transformers rely on large datasets and full retraining when failures occur, which is impractical for real‑time robotic manipulation. This work addresses the gap by offering an online correction mechanism that can be integrated into existing controllers without costly offline updates.

## Implications
ORPA enables manufacturers to deploy robust manipulation systems in production environments where continuous adaptation is essential. Practitioners can reduce downtime and improve reliability, making advanced AI‑driven robots more viable for real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17323v1)
