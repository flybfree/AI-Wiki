# Summary: 2026-07-27_04-31-12Z_AdaptiveDataAdmissionandRetentionforStreamingFeder.md
Saved: 2026-07-27 22:51
Source: 2026-07-27_04-31-12Z_AdaptiveDataAdmissionandRetentionforStreamingFeder.md
Model: None

---

## Summary  
The paper tackles streaming federated learning under the constraint of limited client memory, where each new training sample incurs a time‑varying sampling cost that must be balanced against a budget. It proposes an adaptive framework that jointly decides which samples to admit on the server and how long to retain them on the client. By deriving an explicit error bound that accounts for instantaneous sample size, distinct‑sample growth, and reuse imbalance, the authors introduce a surrogate penalty that drives a structured retention rule. The resulting Active‑Constraint Drift‑Plus‑Penalty (ACDPP) policy combines a server‑side online admission region with a client‑side K‑step retention schedule to achieve sublinear regret while respecting cost and buffer limits.

## Key Contributions  
- [Finding 1] A learning‑error bound that explicitly captures the effects of instantaneous training sample size, distinct‑sample growth, and reuse imbalance through an effective sample‑size characterization.  
- [Finding 2] An Active‑Constraint Drift‑Plus‑Penalty (ACDPP) policy that integrates a server‑side online admission rule with a time‑varying rectangular region and a client‑side K‑step retention rule to minimize cumulative excess population risk under cost and buffer constraints.  
- [Finding 3] A sequence of comparison arguments linking the ACDPP bound to a constant‑admission oracle benchmark, yielding explicit sublinear regret guarantees and controlling sampling‑cost violation while keeping buffer occupancy within limits.

## Methodology  
The authors model the problem as a joint server‑client decision process subject to a cumulative sampling‑cost budget \(C\) and a maximum buffer size. They first compute an effective sample size that quantifies how many distinct samples contribute to learning error at any moment, accounting for both new arrivals and reuse. This bound is transformed into a surrogate penalty used in the ACDPP policy. The client retains the last \(K\) steps of data, while the server admits each incoming batch only if it fits within the remaining cost budget and does not overflow the buffer. Offline selection of the retention horizon determines the rectangular admission region’s height, ensuring that buffer violations are minimized.

## Results  
Theoretically, ACDPP achieves sublinear regret \(O(\sqrt{T}\log C)\) where \(T\) is the number of time steps and \(C\) the total sampling cost allowed. Experimentally, on several benchmark datasets (e.g., ImageNet‑10, CIFAR‑10 streaming), the policy’s prediction error remains within a constant factor of the oracle benchmark while strictly obeying both the cost budget and buffer constraints. The comparison shows that ACDPP is competitive with a simpler constant‑admission rule yet offers better risk control.

## Significance  
This work provides a principled, low‑memory strategy for streaming federated learning that reduces cumulative population risk without sacrificing learning performance. By balancing sampling costs and memory usage through adaptive admission and retention, it enables scalable training of large federated systems where each client holds only a limited history of data.

## Related Concepts  
Effective sample size, sampling‑cost budget, buffer constraints, active constraint drift penalty, K‑step retention rule, rectangular admission region, sublinear regret, oracle benchmark, streaming federated learning.
