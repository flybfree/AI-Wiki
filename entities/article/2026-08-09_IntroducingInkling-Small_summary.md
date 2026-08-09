# Summary: 2026-08-09_IntroducingInkling-Small.md
Saved: 2026-08-09 00:02
Source: 2026-08-09_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts (MoE) transformer that delivers performance comparable to the larger Inkling model while using only a quarter of its parameters and active compute. The 276 B total‑parameter model runs on NVIDIA GB300 NVL72 hardware, supports up to one million tokens, and offers variable thinking effort to balance cost and capability across audio‑image reasoning, tool use, and instruction following.

## Key Takeaways  
- Inkling‑Small achieves near‑Inkling performance with 12 B active parameters versus 41 B in the full model, cutting compute by a factor of four.  
- Its variable thinking effort lets users tune reasoning depth, making it adaptable for low‑cost or high‑performance tasks.  
- Benchmarks show Inkling‑Small competes with other open‑weights models (e.g., Qwen3.5‑397B, MiMo V2.5) in size and efficiency across Terminal‑Bench 2.1, HLE, and IFBench.

## Context  
The release underscores a trend toward MoE architectures that enable massive model capacity with sparse activation, reducing hardware demands while preserving state‑of‑the‑art reasoning abilities. This approach aligns with industry efforts to democratize access to large language models through open weights and efficient inference.

## Implications  
For developers and enterprises, Inkling‑Small offers a cost‑effective alternative for deploying powerful multimodal agents without the expense of full‑scale models, potentially accelerating adoption in resource‑constrained environments such as edge AI or mobile applications.
