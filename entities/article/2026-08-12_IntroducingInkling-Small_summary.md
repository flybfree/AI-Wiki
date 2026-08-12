# Summary: 2026-08-12_IntroducingInkling-Small.md
Saved: 2026-08-12 00:06
Source: 2026-08-12_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer that delivers performance comparable to the larger Inkling model while using only a quarter of its parameters (276 B total, 12 B active versus 975 B total, 41 B active). The model supports multimodal reasoning over audio and images, offers variable thinking effort, and can handle up to one million tokens in context. By sweeping reasoning effort from minimal to xhigh, Inkling‑Small achieves output TFLOPs per sample that are competitive with other open‑weights models of similar size, delivering lower compute cost and price per token.

## Key Takeaways  
- Inkling‑Small attains comparable performance to Inkling with a 276 B total‑parameter footprint versus 975 B, reducing active parameters from 41 B to 12 B.  
- The model’s variable thinking effort and 1 M‑token context window enable fine‑tuned cost‑performance trade‑offs for diverse applications.  
- Benchmark results show it matches or exceeds other open‑weights models (e.g., Nemotron 3 Super, Qwen 3.5‑397B) on Terminal‑Bench 2.1, HLE reasoning, and IFBench.

## Context  
The release underscores a growing industry focus on scaling efficiency through Mixture‑of‑Experts architectures. Open‑weights models are increasingly competing with proprietary systems for cost‑effective deployment, especially in multimodal tasks where large context windows and variable reasoning effort are essential. This trend reflects broader efforts to make frontier AI more accessible while minimizing compute budgets.

## Implications  
For developers and enterprises, Inkling‑Small lowers the barrier to deploying powerful, multimodal reasoning agents without prohibitive cloud costs. Its efficiency model encourages further research into MoE scaling laws, prompting new standards for open‑weight benchmarking and cost‑performance analysis across the AI ecosystem.
