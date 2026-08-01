# Summary: 2026-08-01_IntroducingInkling-Small.md
Saved: 2026-08-01 00:04
Source: 2026-08-01_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts (MoE) transformer that delivers performance comparable to the larger Inkling model while using only a quarter of its parameters and active compute. The 276 B‑parameter model runs on NVIDIA GB300 NVL72 hardware, supports up to 1 M tokens, and offers variable thinking effort to balance cost and capability across benchmarks such as Terminal‑Bench 2.1, HLE reasoning, and IFBench.

## Key Takeaways  
- Inkling‑Small achieves near‑Inkling performance with a 276 B total parameter count but only 12 B active parameters, cutting compute to roughly one quarter of the original model.  
- Its variable thinking effort lets users adapt reasoning intensity on demand, making it cost‑effective for diverse tasks and use cases.  
- Benchmark comparisons show Inkling‑Small competes with other open‑weights models (e.g., Qwen3.5‑397B‑A17B, MiMo V2.5) in size class on both performance and efficiency metrics.

## Context  
The release underscores a trend toward scaling AI models by increasing the proportion of active parameters rather than total parameter count, enabling high‑quality reasoning at lower compute costs. This approach aligns with industry efforts to democratize access to large language models through open weights and efficient architectures that can run on commodity hardware.

## Implications  
For developers and researchers, Inkling‑Small provides a practical alternative for deploying powerful multimodal agents without the prohibitive cost of full‑scale models like Inkling. Its efficiency could accelerate research in AI alignment, tool use, and instruction following while reducing operational expenses, potentially widening adoption across commercial and academic settings.
