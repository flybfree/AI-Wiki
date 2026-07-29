# Summary: 2026-07-28_17-06-24Z_UntanglingCo_Drift_ProactiveMulti_IntentFailurePre.md
Saved: 2026-07-28 23:00
Source: 2026-07-28_17-06-24Z_UntanglingCo_Drift_ProactiveMulti_IntentFailurePre.md
Model: None

---

## Summary  
The paper tackles the problem of co‑drift in self‑driving networks, where a fault in one macro‑intent (continuous telemetry, real‑time analytics, or programmatic actuation) propagates to others, producing ambiguous failures that are hard to diagnose. It introduces MILD—a proactive framework that predicts intent‑level failures and attributes their root cause before thresholds are breached. By integrating a teacher‑augmented Mixture‑of‑Experts architecture with a joint optimization objective, MILD delivers KPI‑level diagnostics via SHAP explainability and urgency estimation across multiple horizons.

## Key Contributions  
- Introduces the concept of three macro‑intents (continuous telemetry, real‑time analytics, programmatic actuation) as formal intent health metrics.  
- Proposes MILD, a teacher‑augmented Mixture‑of‑Experts model that jointly predicts failure across intents and disambiguates root causes.  
- Demonstrates high detection rates (>90 %), short remediation lead times (under 5 seconds), and accurate intent‑level attribution in three progressively realistic environments.

## Methodology  
The authors model the self‑driving control loop as a sequence of macro‑intent functions, each representing an intent that must be continuously satisfied. They formalize co‑drift by capturing causal coupling between these intents. MILD employs a hybrid objective: a prediction loss for failure timing and a root‑cause attribution loss using SHAP scores. A teacher network guides expert selection, enabling multi‑horizon forecasting of both failure probability and the primary fault source.

## Results  
Experiments on a statistical benchmark, a microservices application, and an SDN edge‑to‑cloud testbed show detection rates exceeding 90 %, remediation lead times under five seconds, and SHAP explanations that correctly identify the primary fault within each intent. Compared with traditional threshold‑based methods, MILD reduces false alarms by roughly forty percent while maintaining precise intent‑level disambiguation.

## Significance  
By enabling proactive rather than reactive monitoring, MILD supports closed‑loop assurance in autonomous networks, allowing timely interventions without human oversight—critical for safety and reliability in next‑generation self‑driving systems.

## Related Concepts  
Co‑drift, macro‑intent formulation, Mixture‑of‑Experts, SHAP explainability, multi‑horizon modeling, proactive failure prediction, root‑cause disambiguation.
