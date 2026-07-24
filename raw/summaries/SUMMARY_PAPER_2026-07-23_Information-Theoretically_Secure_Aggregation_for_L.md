---
title: Information-Theoretically Secure Aggregation for Lightweight Federated Learning: Resilient to Dropouts and Adversaries
url: http://arxiv.org/abs/2607.20890v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_03-26-41Z_Information_TheoreticallySecureAggregationforLight.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an information‑theoretically secure aggregation scheme for sign‑based federated learning that is resilient to both dropouts and malicious participants. By using single‑round secure multiplication of a reduced MV polynomial, the framework achieves end‑to‑end security while only revealing the final aggregated sign to the server.

## Key Takeaways
- The proposed method reduces online communication by up to 99.5% through inverse‑form exponent reduction and single‑round secure multiplication compared with conventional approaches.  
- It lowers latency by up to 85.7% while maintaining information‑theoretic security under the honest‑majority assumption.  
- The framework leverages MDS‑code decoding, providing robustness against dropouts (accuracy gain up to 20.65%) and adversarial behavior (gain up to 10.74%).

## Context
Federated learning relies on efficient communication between devices and a central server, yet security remains a critical concern. Existing secure aggregation techniques often require multiple rounds or heavy computation, making them unsuitable for resource‑constrained environments.

## Implications
This work offers a practical solution that balances privacy, efficiency, and scalability, encouraging adoption of sign‑based FL in large‑scale deployments. Practitioners can implement the framework with minimal overhead while ensuring robust security against both random failures and coordinated attacks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20890v1)
