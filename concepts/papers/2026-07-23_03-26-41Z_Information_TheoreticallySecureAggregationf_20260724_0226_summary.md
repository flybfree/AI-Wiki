# Summary: 2026-07-23_03-26-41Z_Information_TheoreticallySecureAggregationforLight.md
Saved: 2026-07-24 02:26
Source: 2026-07-23_03-26-41Z_Information_TheoreticallySecureAggregationforLight.md
Model: None

---

## Summary  
The paper proposes an information‑theoretically secure aggregation scheme for sign‑based federated learning that remains robust to device dropouts and malicious participants. It achieves end‑to‑end security under the honest‑majority assumption while only revealing the aggregated gradient sign to the server. Two novel techniques dramatically lower communication and latency costs. The framework is lightweight, scalable, and practical for large‑scale FL deployments.

## Key Contributions  
- **Information‑theoretic security**: Secure computation of the majority‑vote (MV) polynomial using single‑round secure multiplication, guaranteeing that only the final aggregated sign leaves the device.  
- **Inverse‑form exponent reduction**: Halves the effective degree of the MV polynomial, cutting both communication and computational overhead.  
- **Robustness via MDS decoding**: Leverages inherent maximum‑distance‑separable code properties to tolerate up to 20 % dropouts and adversarial behavior with accuracy gains.

## Methodology  
The authors address the vulnerability of sign‑based FL by designing a secure aggregation protocol that computes the MV polynomial offline with linear complexity, then performs single‑round secure multiplication online. The inverse‑form exponent representation reduces the polynomial degree, while MDS codes enable efficient decoding in a single communication round, achieving low latency and minimal storage.

## Results  
Experimental results show online communication reduced by up to 99.5 % and latency lowered by up to 85.7 % compared with conventional approaches. Accuracy improves by 20.65 % when handling dropouts and 10.74 % against adversarial attacks, demonstrating both efficiency and robustness.

## Significance  
This work provides a practical foundation for large‑scale, low‑latency federated learning on resource‑constrained devices while preserving strong privacy guarantees, enabling broader adoption of secure FL in real‑world scenarios.

## Related Concepts  
sign‑based FL, majority vote aggregation, information‑theoretic security, MDS codes, single‑round multiplication, inverse‑form exponent reduction.
