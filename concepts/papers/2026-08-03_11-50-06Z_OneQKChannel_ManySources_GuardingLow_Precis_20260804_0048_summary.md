# Summary: 2026-08-03_11-50-06Z_OneQKChannel_ManySources_GuardingLow_PrecisionAtte.md
Saved: 2026-08-04 00:48
Source: 2026-08-03_11-50-06Z_OneQKChannel_ManySources_GuardingLow_PrecisionAtte.md
Model: None

---

## Summary  
The paper investigates why bfloat16 transformers collapse during training, showing that low‑precision errors in the streaming softmax accumulator cause a runaway in the query‑key (QK) channel. It demonstrates that fixing only QK prevents collapse even when other sources of error remain active, indicating a shared failure locus rather than isolated faults. The authors propose QK‑Guard, a controller that activates parameter‑free QK normalization to stop the collapse. This work isolates the QK channel as the critical conduit for precision loss and provides a scalable guard mechanism.

## Key Contributions
- [Finding 1] The streaming softmax accumulator’s low‑precision errors trigger a runaway in the query‑key spectral direction, causing abrupt training failure.  
- [Finding 2] Intervening only on QK stabilizes training while other source faults persist, proving fault source is not the failure channel.  
- [Finding 3] A dormant controller (QK‑Guard) that activates when attention logits saturate prevents collapse across all tested architectures and scales to 60k steps.

## Methodology  
The authors reproduce GPT‑2‑class collapse by deliberately degrading bfloat16 accumulation, then compare outcomes of repairing the accumulator versus correcting only QK weights. They use a causal probe to track singular values of the QK matrix, showing that the largest singular value dominates early runaway. Experiments are conducted on two GPU architectures (A100 and H100) with various model sizes.

## Results  
Repairing the accumulator restores stability; fixing only QK also stabilizes training while other errors remain; QK‑Guard matches always‑on normalization over 60k steps, whereas non‑QK actions fail at trigger. The controller activates precisely when logits saturate, halting the runaway.

## Significance  
By identifying a single shared channel (QK) that propagates low‑precision errors, the work enables uniform interventions across models and scales, reducing training instability without per‑source repairs.

## Related Concepts  
bfloat16 precision loss, streaming softmax accumulator, query‑key spectral runaway, QK normalization, attention logit saturation, singular value analysis, controller‑based guard mechanisms.
