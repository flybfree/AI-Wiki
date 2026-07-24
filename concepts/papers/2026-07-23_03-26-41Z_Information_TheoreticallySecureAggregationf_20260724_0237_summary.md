# Summary: 2026-07-23_03-26-41Z_Information_TheoreticallySecureAggregationforLight.md
Saved: 2026-07-24 02:37
Source: 2026-07-23_03-26-41Z_Information_TheoreticallySecureAggregationforLight.md
Model: None

---

## Summary  
The paper proposes an information‑theoretically secure aggregation scheme for sign‑based federated learning that is resilient to device dropouts and adversarial attacks. It builds on the majority vote polynomial while transmitting only a single aggregated bit. Two efficiency enhancements—exponent reduction and single‑round secure multiplication—cut communication and latency dramatically. The framework leverages MDS‑code decoding to maintain high accuracy under both failure modes.

## Key Contributions  
- Finding 1: A lightweight, information‑theoretically secure aggregation protocol for sign‑based FL using single‑round secure multiplication.  
- Finding 2: An inverse‑form exponent reduction that halves the MV polynomial degree, lowering communication and computation.  
- Finding 3: Robustness to dropouts and adversarial behavior via MDS‑code based decoding, yielding accuracy improvements.

## Methodology  
The authors treat sign aggregation as computing a majority vote polynomial. They apply single‑round secure multiplication to compute this polynomial offline with linear complexity, then transmit only the final aggregated sign. To reduce degree, they use inverse‑form exponent reduction, which simplifies the polynomial and halves its effective size. Decoding is performed using MDS codes, enabling efficient recovery of correct signs even when some are missing or corrupted.

## Results  
Experiments on simulated FL scenarios show online communication reduced by up to 99.5% compared with conventional secure aggregation, latency cut by up to 85.7%, and model accuracy gains of 20.65% under dropout conditions and 10.74% against adversarial attacks.

## Significance  
The work provides a practical solution for large‑scale, low‑latency FL where both privacy and resilience are critical, enabling deployment on resource‑constrained devices without sacrificing performance or security.

## Related Concepts  
sign‑based federated learning, majority vote polynomial, information‑theoretic security, single‑round secure multiplication, exponent reduction, MDS codes, decentralized aggregation, lightweight FL.
