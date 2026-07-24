# Summary: 2026-07-20_14-58-53Z_RethinkingHeterogeneousLLMMerging_AWeightedModelAv.md
Saved: 2026-07-24 00:25
Source: 2026-07-20_14-58-53Z_RethinkingHeterogeneousLLMMerging_AWeightedModelAv.md
Model: None

---

## Summary  
The paper investigates whether large language models (LLMs) that differ dramatically in parameter count can be merged simply by direct weighted averaging without any training or semantic alignment. By introducing a lightweight dimensional adaptation followed by ratio‑controlled interpolation, the authors present a training‑free merging recipe that works across diverse Qwen‑family model pairs and multiple benchmarks. Their experiments show that deterministic expansion preserves the source model’s function while small‑ratio interpolation can even outperform the stronger source checkpoint, yet near‑balanced interpolation often collapses and produces a “seesaw” effect where gains in some tasks coexist with regressions on others.

## Key Contributions  
- [Finding 1] Training‑free dimensional adaptation combined with ratio‑controlled interpolation enables effective merging of heterogeneous LLMs without training or alignment.  
- [Finding 2] Deterministic expansion (union‑style) preserves the source model’s functionality, while small‑ratio interpolation yields measurable improvements over strong source checkpoints on several tasks.  
- [Finding 3] Near‑balanced interpolation tends to collapse and exhibits a seesaw effect: gains in some capabilities are accompanied by regressions in others.

## Methodology  
The authors adopt two merging strategies: union‑style, where the smaller model is expanded into the larger parameter space, and intersection‑style, where the larger model is truncated to match the smaller space. Both approaches rely on a ratio‑controlled interpolation that scales the weights of the source and target checkpoints according to a predefined ratio. The adaptation step adjusts the dimensionality of each checkpoint so that their parameter spaces align, allowing simple weighted averaging to be performed deterministically.

## Results  
Across Qwen‑family model pairs tested on benchmarks covering mathematical reasoning, code generation, language understanding, commonsense reasoning, knowledge, and instruction following, deterministic expansion consistently preserves source function. Small‑ratio interpolation (e.g., 0.2–0.3) improves performance relative to the stronger source checkpoint in many tasks. However, when the interpolation ratio approaches 1.0, results degrade sharply; balanced merging often collapses into a flat performance plateau. The “seesaw” effect is evident: some benchmarks see gains while others regress, highlighting that simple averaging alone cannot guarantee monotonic improvement.

## Significance  
These findings demonstrate that a surprisingly strong baseline—simple parameter averaging augmented by lightweight adaptation and controlled ratios—can outperform many complex heterogeneous fusion methods at scale. The results suggest inherent limits to direct weighted fusion: the difficulty of aligning vastly different architectures may be bounded, implying that more elaborate techniques such as distillation or latent‑space routing cannot surpass this simple approach when training is prohibited.

## Related Concepts  
- Weighted model averaging (direct merging)  
- Heterogeneous LLM fusion methods (distillation, adapters, learned latent spaces, routing, feature alignment)  
- Dimensional adaptation for parameter space alignment  
- Ratio‑controlled interpolation in model combination
