# Summary: 2026-07-19_15-01-35Z_LosslessbutNotFree_AnEmpiricalAnatomyofSpeculative.md
Saved: 2026-07-24 00:11
Source: 2026-07-19_15-01-35Z_LosslessbutNotFree_AnEmpiricalAnatomyofSpeculative.md
Model: None

---

## Summary  
The paper introduces speculative decoding for large language models on consumer hardware, showing that it can be lossless while delivering measurable speedups. It provides a device‑agnostic implementation and an empirical analysis across multiple draft/target configurations on an Apple‑silicon laptop. The authors verify distribution equivalence at three levels, including a two‑sample χ² test over ~9,200 tokens and exact greedy‑sequence agreement. They conclude that verification must be truly parallel; otherwise the method slows down despite its theoretical benefits.

## Key Contributions  
- Finding 1: Speculative decoding can achieve a 1.61× wall‑clock speedup with K = 6 on a consumer laptop.  
- Finding 2: The acceptance profile drops sharply as K increases, indicating diminishing returns and that very large draft sizes are inefficient.  
- Finding 3: Some configurations decelerate because verification runs serially despite being parallel in theory, or because the draft model cannot out‑pace the target.

## Methodology  
The authors built a from‑scratch implementation supporting CUDA, MPS, and CPU backends. For each configuration they generate K draft tokens with a small draft model, then perform a single batched forward pass through the target model to score all drafts. Rejection sampling is applied to retain lossless output. Distribution equivalence is checked at three levels: (1) a statistical χ² test over ~9,200 tokens (χ² = 162.5, dof = 200, p = 0.976), (2) exact greedy‑sequence agreement across the full sequence, and (3) visual inspection of token‑wise outputs.

## Results  
The best configuration yields a 1.61× speedup at K = 6, with an acceptance profile ranging from 69.7% at K = 1 to 37.8% at the optimum. Three of five configurations are slower: two suffer because verification serializes parallel work (e.g., Metal backend), and one is slowed by a draft latency that exceeds the target’s generation time.

## Significance  
This empirical anatomy demonstrates that speculative decoding’s promise hinges on hardware‑level parallelism and a genuine latency gap between draft and target models. It offers a practical path for low‑cost AI inference on consumer devices but also highlights implementation pitfalls that can negate theoretical gains.

## Related Concepts  
Speculative decoding, batch scoring, rejection sampling, quantization, memory bandwidth bottleneck, distribution equivalence testing, wall‑clock speedup, consumer hardware constraints, latency gap, draft/target model interaction.
