title: "Summary: 2026-06-22_17-56-25Z_TaperedLanguageModels.md"
# Summary: 2026-06-22_17-56-25Z_TaperedLanguageModels.md
Saved: 2026-06-23 00:00
Source: 2026-06-22_17-56-25Z_TaperedLanguageModels.md
Model: None

---


## Summary  
The paper investigates whether language model performance can be improved by non‑uniformly allocating parameters across layers, arguing that later layers refine the residual stream rather than transform it. It proposes Tapered Language Models (TLMs) in which MLP width tapers monotonically with depth under a fixed total budget, suggesting this aligns better with observed dynamics. Experiments demonstrate that tapered designs achieve higher perplexity and stronger benchmark scores without any additional compute or parameter cost.

## Key Contributions  
- [Finding 1] Uniform‑width models are suboptimal; allocating more capacity to earlier layers yields higher perplexity than later layers.  
- [Finding 2] A smooth cosine taper of MLP width across depth consistently outperforms uniform baselines across multiple architectures.  
- [Finding 3] The improvement is achieved with no extra parameter or compute cost, indicating a free lever in model design.

## Methodology  
The authors conducted controlled experiments comparing four model families (Transformer, Gated Attention, Hope‑attention, Titans) at three scales. They varied MLP width using a cosine taper schedule while keeping the total number of parameters constant, measuring perplexity and downstream task performance. Results were aggregated across architectures to assess generality.

## Results  
Tapered models achieved 2–4 % lower perplexity on standard benchmarks such as WikiText‑103 compared with uniform baselines; improvements persisted for all four architectures. No increase in parameter count or compute was observed, confirming that the taper is a design choice rather than an added resource.

## Significance  
This work reveals depth‑aware capacity allocation as an effective optimization strategy, offering a simple architectural tweak that can boost performance without costly modifications. It suggests that future model scaling and efficiency research should consider non‑uniform parameter distribution as a practical lever.

## Related Concepts  
Parameter budgeting, residual stream refinement, cosine scheduling, MLP width variation, transformer layers, non‑uniform learning dynamics.
