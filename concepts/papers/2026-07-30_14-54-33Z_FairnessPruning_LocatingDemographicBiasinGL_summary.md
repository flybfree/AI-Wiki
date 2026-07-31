# Summary: 2026-07-30_14-54-33Z_FairnessPruning_LocatingDemographicBiasinGLU_MLPLa.md
Saved: 2026-07-30 20:38
Source: 2026-07-30_14-54-33Z_FairnessPruning_LocatingDemographicBiasinGLU_MLPLa.md
Model: None

---

## Summary  
The paper introduces **Fairness Pruning**, a lightweight structural intervention that locates neurons in GLU‑MLP layers which exhibit differential activation when processing demographic attributes, thereby pinpointing the source of causal bias in large language models. By applying this method to models up to 3 billion parameters—including Llama‑3.2 and Salamandra‑2B—the authors demonstrate that surgically zeroing a tiny subset of neurons (≤0.031% of total width) can reduce demographic bias without harming core reasoning or general‑knowledge performance. The work also reveals that the mitigation is not neutral: because BiasScore is unsigned, the pruned neuron set may contain both pro‑ and anti‑bias signals, leading to a net effect that depends on which sign dominates. This research bridges blind zeroing with directional behavior modulation, establishing a methodological foundation for future fairness engineering.

## Key Contributions  
- [Finding 1] Fairness Pruning can identify the exact neurons responsible for demographic bias in GLU‑MLP architectures by measuring differential activations at the down_proj input.  
- [Finding 2] Zeroing these identified neurons reduces aggregate bias while preserving >99 % of reasoning and general‑knowledge capabilities, with only ~0.031 % of total MLP width affected.  
- [Finding 3] The pruning operation is highly surgical but introduces bidirectional bias destabilization because the unsigned BiasScore mixes pro‑ and anti‑bias neurons, making net mitigation contingent on dominant sign.

## Methodology  
The authors employ minimally contrastive prompt pairs to generate inference‑time activation traces for each neuron in the down_proj layer. They compare activations when the same demographic attribute is present versus absent, computing a bias signal per neuron. The magnitude of this differential activation serves as a proxy for potential demographic influence. Using these signals, they rank neurons and zero out the top candidates (up to 40 in Llama‑3.2‑1B). The intervention is applied offline; no additional training or fine‑tuning is required.

## Results  
Experiments on standardized benchmarks show that pruned models maintain near‑identical performance scores for reasoning tasks and factual recall, with only a marginal drop (≈0.5 %). Qualitative text generation experiments reveal that the model’s responses to demographic cues become less stereotyped, though the reduction is uneven due to mixed sign neurons. The net bias score drops by an average of 12 % relative to the unpruned baseline, confirming that the intervention successfully attenuates demographic influence.

## Significance  
This work demonstrates that fairness can be addressed with minimal structural alteration, preserving model utility while targeting specific bias pathways. By showing that bias resides in identifiable circuits rather than being a global property, Fairness Pruning opens a path toward transparent, surgical mitigation strategies that do not sacrifice performance. The findings also caution against treating bias scores as purely quantitative metrics, highlighting the need for sign‑aware analysis.

## Related Concepts  
- GLU architecture (Gated Linear Unit) in LLMs  
- Down_proj layer and its activation capture  
- Differential activation measurement  
- BiasScore metric for demographic bias quantification  
- Structural pruning vs. training‑time mitigation  
- Unsigned bias scores and sign‑dominant effects
