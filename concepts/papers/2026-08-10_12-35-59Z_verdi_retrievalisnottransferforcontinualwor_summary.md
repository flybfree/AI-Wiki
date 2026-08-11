# Summary: 2026-08-10_12-35-59Z_verdi_retrievalisnottransferforcontinualworldmodel.md
Saved: 2026-08-10 23:48
Source: 2026-08-10_12-35-59Z_verdi_retrievalisnottransferforcontinualworldmodel.md
Model: None

---

## Summary  
The paper argues that retrieval is not transfer for continual world model optimization, contending that strategies validated on one model are merely hypotheses for another and become useful only after target‑side validation. To address this gap, the authors introduce VERDI, a framework that links evidence to reusable knowledge through an Optimization Fingerprint built from shared inference‑time probes. VERDI retrieves ranked prior hypotheses, validates each candidate with a frozen target verifier, and evolves probes when contradictions arise. Experiments on Ctrl‑World, Cosmos, and RoboCoin demonstrate substantial gains in efficiency and reliability.

## Key Contributions  
- Retrieval is not transfer: strategies are hypothesis‑level, not directly reusable across models without validation.  
- VERDI framework constructs an Optimization Fingerprint from shared inference‑time probes to guide evidence retrieval.  
- Experimental results show a 68 % reduction in search cost, a 69 % drop in GPU cost, and negative transfer reduced from 0.34 to 0.06 with 83 % sign accuracy.

## Methodology  
The authors approached continual optimization by first characterizing each world model using shared inference‑time probes that generate an Optimization Fingerprint. This fingerprint serves as a diagnostic signature of the model’s current state and guides retrieval of relevant prior hypotheses from a knowledge base. Each candidate hypothesis is validated on the target model with a frozen verifier; if contradictions are detected, probe evolution triggers to refine the diagnostic representation.

## Results  
Across three benchmark domains—Ctrl‑World, Cosmos family models, and RoboCoin—the VERDI pipeline reduces search cost by 68 % and GPU resource consumption by 69 %. It also cuts negative transfer from 0.34 to 0.06 and predicts whether a prior hypothesis will be beneficial with 83 % sign accuracy.

## Significance  
VERDI shifts the paradigm away from assuming that optimization strategies are directly reusable, instead providing an evidence‑licensed process that ensures only validated knowledge is transferred. This leads to more efficient continual learning, lower computational overhead, and higher reliability in world model optimization pipelines.

## Related Concepts  
retrieval, transfer, continual world model optimization, Optimization Fingerprint, inference‑time probes, frozen verifier, negative transfer, sign accuracy.
