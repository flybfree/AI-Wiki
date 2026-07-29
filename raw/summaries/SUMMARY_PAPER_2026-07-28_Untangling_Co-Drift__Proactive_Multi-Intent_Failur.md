---
title: Untangling Co-Drift: Proactive Multi-Intent Failure Prediction and Root-Cause Disambiguation for Self-Driving Networks
url: http://arxiv.org/abs/2607.25989v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_17-06-24Z_UntanglingCo_Drift_ProactiveMulti_IntentFailurePre.md
generated_at: 2026-07-28 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MILD, a framework for proactive failure prediction and root‑cause disambiguation in self‑driving networks by treating telemetry, analytics, and actuation as three macro‑intents. It shows that co‑drift causes cascading anomalies across intents and that existing reactive methods are insufficient. MILD uses teacher‑augmented Mixture‑of‑Experts with a joint objective to predict failures and assign root causes, delivering KPI diagnostics via SHAP and multi‑horizon urgency.

## Key Takeaways
- A single fault in one macro‑intent can propagate as co‑drift that triggers anomalies in the other two intents. 
- MILD shifts from reactive drift detection to proactive failure prediction using a teacher‑augmented Mixture‑of‑Experts architecture with a hybrid objective. 
- The framework provides KPI‑level diagnostics through SHAP explainability and estimates urgency across multiple horizons.

## Context
Self‑driving networks must maintain continuous telemetry, real‑time analytics, and programmatic actuation while minimizing human intervention. Current monitoring systems rely on threshold crossing, which is too slow to enable timely remediation. This paper addresses the need for a unified, proactive approach that can predict failures before they cascade.

## Implications
MILD enables closed‑loop assurance in autonomous networks by delivering early warnings and clear root‑cause attribution. Practitioners can reduce downtime and improve safety by acting on intent‑level diagnostics rather than symptom alerts. This advances AI reliability in edge‑to‑cloud SDN environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25989v1)
