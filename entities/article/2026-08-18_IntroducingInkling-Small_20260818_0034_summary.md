# Summary: 2026-08-18_IntroducingInkling-Small.md
Saved: 2026-08-18 00:34
Source: 2026-08-18_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Tinker AI has unveiled Inkling‑Small, an open‑weights Mixture‑of‑Experts transformer that delivers performance on par with its larger sibling Inkling while using only a quarter of the total parameters (276 B vs. 975 B). The model leverages NVIDIA GB300 NVL72 hardware, supports audio and image reasoning, offers variable thinking effort to balance cost and capability, and can handle up to one million tokens in context.

## Key Takeaways  
- Inkling‑Small achieves comparable benchmark scores (Terminal‑Bench 2.1, HLE, IFBench) as the 975 B‑parameter Inkling but with just 12 B active parameters, a dramatic reduction in compute and cost.  
- The model’s variable thinking effort lets users dynamically allocate resources, making it adaptable to low‑budget or high‑performance use cases without retraining.  
- Benchmark comparisons show that Inkling‑Small is competitive with other open‑weights models of similar size (e.g., Qwen3.5‑397B‑A17B, MiMo V2.5) in both performance and efficiency.

## Context  
The AI industry is increasingly focused on scaling models while minimizing compute expense, a challenge highlighted by the exponential growth of parameter counts. Open‑weight releases like Inkling‑Small aim to democratize access to high‑capability systems, enabling researchers and developers to experiment without costly GPU clusters. The use of MoE architectures also reflects broader trends toward sparse activation that can match dense models’ performance with far fewer active parameters.

## Implications  
By delivering a 276 B model that rivals the 975 B counterpart at lower cost, Inkling‑Small could accelerate adoption of large language models in resource‑constrained environments such as edge devices or cloud‑scale services. Its variable thinking effort further reduces wasteful compute, aligning performance with actual user needs and potentially lowering overall AI deployment expenses across the sector.
