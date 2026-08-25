---
title: Mitigating Explanation Leakage in Financial Fraud Detection Systems
url: http://arxiv.org/abs/2608.22607v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_21-26-21Z_MitigatingExplanationLeakageinFinancialFraudDetect.md
generated_at: 2026-08-24 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DP-FedSHAP, a differential privacy framework that protects federated learning models while providing TreeSHAP explanations. By applying client‑level DP only to the post‑hoc SHAP vectors, it avoids exposing raw model internals to Membership Inference Attacks. Experiments on the imbalanced IEEE‑CIS Fraud Detection dataset show that DP-FedSHAP achieves a good balance between explanation fidelity and privacy preservation while maintaining competitive AUPRC scores compared with a weight‑level DP baseline.

## Key Takeaways
- Client‑level differential privacy is applied only to TreeSHAP vectors, not to the underlying model weights.  
- The proposed architecture reduces information leakage that could enable Membership Inference Attacks on federated networks.  
- On the fraud detection benchmark, DP-FedSHAP maintains a high AUPRC while preserving privacy, outperforming weight‑level DP in explanation clarity.

## Context
Explainable AI is essential for regulatory compliance and trustworthy model deployment, yet centralized explanations can compromise data privacy in federated settings. This research addresses the tension between transparency and security by integrating differential privacy directly into post‑hoc XAI outputs, a technique that has not been widely explored in financial fraud contexts.

## Implications
Practitioners can deploy federated models with meaningful explanations without violating privacy regulations or opening themselves to adversarial attacks. The findings provide a practical template for balancing model interpretability and security in sensitive domains such as finance and healthcare.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22607v1)
