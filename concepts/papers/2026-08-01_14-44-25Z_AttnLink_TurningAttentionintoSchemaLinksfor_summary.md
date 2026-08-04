# Summary: 2026-08-01_14-44-25Z_AttnLink_TurningAttentionintoSchemaLinksforText_to.md
Saved: 2026-08-03 20:30
Source: 2026-08-01_14-44-25Z_AttnLink_TurningAttentionintoSchemaLinksforText_to.md
Model: None

---

## Summary  
AttnLink proposes an attention‑based framework that converts the internal attention of a large language model into continuous relevance scores for schema items in Text‑to‑SQL tasks, enabling efficient ranking of candidate spans without resorting to autoregressive decoding. The authors introduce two variants: AttnLink‑U, which probes pretrained attention without any parameter updates, and AttnLink‑S, which aligns the attention distribution with gold schema spans using direct supervision. By combining a set‑mass objective with an adaptive probability‑floor regularizer, AttnLink‑S can capture multiple relevant schema items while maintaining inference speed. The method achieves high mAP scores on benchmark datasets and supports post‑hoc precision‑recall control via temperature scaling.

## Key Contributions  
- [Finding 1] Attention can be directly transformed into a continuous relevance score for each schema item, bypassing the need for explicit scoring mechanisms.  
- [Finding 2] AttnLink‑S uses direct supervision to align attention vectors with gold spans and incorporates a set‑mass objective plus an adaptive probability‑floor regularizer to improve coverage.  
- [Finding 3] The framework enables post‑hoc precision‑recall control through temperature scaling and cumulative mass selection, enhancing downstream SQL generation.

## Methodology  
The authors extract attention weights from the generation start position to every candidate span across the LLM’s encoder‑decoder architecture. For AttnLink‑U they compute scores by averaging these raw weights. In AttnLink‑S a lightweight adapter is trained to map raw attention vectors to calibrated relevance scores while preserving the original distribution; this mapping follows a set‑mass loss that encourages coverage of multiple spans and an adaptive floor regularizer that prevents over‑confidence.

## Results  
On Spider, BIRD, and Spider2‑SQLite, AttnLink‑S reaches mAPs of 99.22 %, 95.95 % and 83.29 % respectively, with schema‑linking latency measured in milliseconds. It also achieves the best or tied‑best execution accuracy for SQL generation across seven out of nine generator‑dataset settings.

## Significance  
By leveraging existing attention mechanisms without retraining large models, AttnLink offers a fast, scalable alternative to traditional score‑based linking that preserves contextual modeling capacity and enables fine‑grained control over output quality. This approach reduces computational overhead while improving both retrieval precision and generation accuracy.

## Related Concepts  
Text‑to‑SQL, schema linking, attention mechanisms, set‑mass loss, temperature scaling, cumulative mass selection, prefill decoding, LLM probing, direct supervision.
