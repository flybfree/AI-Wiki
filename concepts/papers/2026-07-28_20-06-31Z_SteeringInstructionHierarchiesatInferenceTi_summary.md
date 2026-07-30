# Summary: 2026-07-28_20-06-31Z_SteeringInstructionHierarchiesatInferenceTime.md
Saved: 2026-07-29 22:12
Source: 2026-07-28_20-06-31Z_SteeringInstructionHierarchiesatInferenceTime.md
Model: None

---

## Summary  
The paper addresses the problem that language model instruction hierarchies are violated because higher priority inputs do not override lower ones, and proposes V‑Steer as a training‑free inference‑time method to restore privileged influence by editing cached value vectors. It uses direct logit attribution on the first next token prediction to identify problematic heads and then performs in‑place multiplicative edits to boost privileged spans and suppress conflicts. The approach is compatible with fused attention backends and incurs only a one‑time prefill overhead.

## Key Contributions  
- [Finding 1] V‑Steer restores privileged influence by editing cached value vectors at prompt positions.  
- [Finding 2] Direct logit attribution identifies heads where lower priority spans dominate privileged ones, then boosts privileged spans and suppresses conflicting lower priority spans through in‑place multiplicative edits to cached V tensors.  
- [Finding 3] The method is training‑free, compatible with fused attention backends, adds only a one prefill overhead, raises primary constraint accuracy from under 18 % up to 92 %, outperforms prompt‑only baselines, and matches or exceeds SOTA training methods on three of four LLM scales.  

## Methodology  
The authors approached the problem by treating instruction hierarchies as a safety assumption that must be enforced at inference time. They leveraged direct logit attribution on the first next token prediction to pinpoint which attention heads are dominated by lower‑priority spans, thereby quantifying the conflict. Using this attribution, they performed in‑place multiplicative edits on the cached value vectors (V tensors) associated with prompt positions: increasing values for privileged spans and decreasing those for conflicting lower‑priority spans. This editing is done without retraining or modifying model weights, only adjusting intermediate activations that are later fused into attention outputs.

## Results  
Across models ranging from 7B to 70B parameters, V‑Steer raised primary constraint accuracy on controlled role‑conflict benchmarks from under 18 % to 92 %. On broader instruction hierarchy evaluations it significantly outperformed prompt‑only baselines. The method matched or exceeded the state‑of‑the‑art training‑based approaches on three of four model scales, while incurring negligible decoding‑speed overhead due to its one‑time prefill cost and compatibility with fused attention backends.

## Significance  
This work demonstrates that instruction hierarchy safety can be enforced at inference time without retraining, addressing a critical gap in current LLM deployment where higher priority inputs are routinely overridden. By operating on cached value vectors, V‑Steer offers a lightweight, scalable solution that preserves model performance and decoding efficiency while ensuring compliance with safety assumptions.

## Related Concepts  
- Instruction hierarchies: the principle that higher‑priority prompts should override lower ones.  
- Direct logit attribution: measuring influence of specific attention heads on token predictions.  
- Cached value vectors (V tensors): intermediate activations stored during forward pass, used for in‑place edits.  
- Fused attention backends: implementations where attention outputs are combined with other operations before being passed to the next layer.
