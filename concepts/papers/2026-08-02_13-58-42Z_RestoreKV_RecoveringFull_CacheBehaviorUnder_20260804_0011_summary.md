# Summary: 2026-08-02_13-58-42Z_RestoreKV_RecoveringFull_CacheBehaviorUnderAggress.md
Saved: 2026-08-04 00:11
Source: 2026-08-02_13-58-42Z_RestoreKV_RecoveringFull_CacheBehaviorUnderAggress.md
Model: None

---

## Summary  
RestoreKV addresses the problem of query‑agnostic KV cache eviction where compression leads to performance loss, by introducing learned restoration that recovers full‑cache behavior within a fixed budget. It does so without retraining large models or task‑specific tuning. The method complements selection‑based retention with lightweight LoRA‑adapted restore tokens.

## Key Contributions  
- [Finding 1] RestoreKV learns a compact, context‑conditioned restore cache that can be generated in a single LoRA pass after prefill.  
- [Finding 2] It retains the original importance scorer and eviction rule unchanged while only training 0.4 % of parameters via self‑distillation from the frozen full‑cache model.  
- [Finding 3] The approach achieves substantial compression gains across multiple benchmarks, raising KVzip scores by over 35 points on RULER‑4K at a 5 % budget.

## Methodology  
The authors start with a standard query‑agnostic eviction that compresses the context into a smaller cache. After prefill, they insert restore tokens that attend to the full KV matrix in one LoRA‑adapted forward pass, producing a compact complement of the evicted pairs. The base scorer remains frozen; only the LoRA adapters are trained via self‑distillation, minimizing parameter updates and avoiding task‑specific fine‑tuning.

## Results  
Across four backbones (e.g., LLaMA‑2, GPT‑Neo) and five long‑context benchmarks (RULER‑4K, KVPress), RestoreKV improves 59 of 60 paired budget‑matched settings on Qwen3‑4B. At a 5 % compression budget it lifts KVzip from 38.2 to 73.2 on RULER‑4K. On KVpress, it reaches 86.4 accuracy at 16× compression with <0.5 % one‑time overhead in a 32K context evaluation.

## Significance  
By recovering full‑cache behavior under aggressive eviction, RestoreKV mitigates the degradation that limits long‑context reasoning and reduces reliance on costly parameter updates, making high‑quality inference feasible within tight memory budgets.

## Related Concepts  
- Query‑agnostic KV cache eviction  
- LoRA (Low‑Rank Adaptation)  
- Self‑distillation training  
- Context compression / KVzip
