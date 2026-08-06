# Summary: 2026-08-04_18-00-01Z_SpecDrop_Parameter_FreeCategory_ConditionedRouting.md
Saved: 2026-08-05 22:21
Source: 2026-08-04_18-00-01Z_SpecDrop_Parameter_FreeCategory_ConditionedRouting.md
Model: None

---

## Summary  
Mixture‑of‑experts (MoE) networks aim to achieve specialization by learning routing, gates, and loss terms, yet at a fixed total‑parameter budget the learned routers often underperform equal‑weight no‑routing baselines. SpecDrop proposes a simple, parameter‑free routing scheme that assigns each branch a fixed weight based on its assigned category while allowing small leakage to other branches; inference uses only the superclass label and no auxiliary losses. The contribution is showing that this deterministic allocation can outperform dense models when the training signal aligns with the modular structure, revealing that granularity alignment matters more than algorithm choice.

## Key Contributions  
- Finding 1: SpecDrop reaches 79.23 % on CIFAR‑100 and 79.89 % on ImageNet‑1K, exceeding parameter‑matched dense baselines by +4.75 points (CIFAR) and +6.53 points (ImageNet).  
- Finding 2: The routing mechanism yields near‑perfect branch‑category alignment (≈58 %/100%) and produces masking gains of 0.00 on CIFAR but +1.06 on ImageNet, indicating the output‑space restriction is internalized during training.  
- Finding 3: In fuzzy partitions where a single unit spans multiple categories (e.g., LoRA‑tuned Llama‑3.2), SpecDrop collapses to the matched No‑Routing control with seed noise, confirming that granularity alignment determines routing benefit.

## Methodology  
The authors replace learned routers with a fixed weight schedule \(p_a\) for each branch’s assigned category and a small leakage \(p_i>0\) elsewhere; the denominator is constant across branches. Routing is deterministic at inference based solely on the superclass label, requiring no additional loss terms or extra parameters.

## Results  
SpecDrop surpasses dense baselines by 4.75 points on CIFAR‑100 and 6.53 points on ImageNet‑1K while maintaining comparable performance to no‑routing+SE controls. Branch‑category alignment is high (≈58 %/100%) and the masking benefit of SpecDrop over dense models is 0.00 vs +1.06 points respectively.

## Significance  
This work demonstrates that a simple, parameter‑free routing strategy can unlock the full potential of modular MoE architectures when training signals are coarse‑grained to match expert categories. It shifts focus from algorithmic complexity to granularity alignment, offering a scalable way to improve MoE efficiency without extra parameters.

## Related Concepts  
Mixture‑of‑experts (MoE), routing layers, category supervision, No‑Routing baselines, gradient masking, LoRA fine‑tuning, seed noise, output‑space restriction.
