# Summary: 2026-08-17_IntroducingInkling-Small.md
Saved: 2026-08-17 00:06
Source: 2026-08-17_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Tiny AI researchers present Inkling‑Small, an open‑weights Mixture‑of‑Experts transformer that rivals the performance of its larger sibling Inkling while using only a quarter of the parameters (276 B total, 12 B active). The model supports audio and image reasoning, variable thinking effort, and a 1 M‑token context window, delivering competitive results across benchmarks such as Terminal‑Bench 2.1, HLE text‑only reasoning, and IFBench at a fraction of the compute cost.

## Key Takeaways
- Inkling‑Small achieves performance comparable to Inkling (975 B total) with just 276 B parameters, cutting active compute from 41 B to 12 B.  
- Its variable thinking effort lets users tailor the model’s reasoning intensity, balancing cost and output quality across tasks.  
- Benchmark comparisons show Inkling‑Small matches or exceeds many open‑weights models in size (e.g., MiMo V2.5, Kimi K2.6) while delivering lower TFLOPs per sample.

## Context  
The release highlights a growing trend toward efficient, parameter‑efficient AI: compressing large models into active‑expert subsets to reduce inference cost without sacrificing capability. This approach aligns with industry efforts to democratize access to high‑end reasoning capabilities through open‑source frameworks like Hugging Face and NVIDIA’s GB300 NVL72 hardware.

## Implications  
For developers, Inkling‑Small offers a practical alternative for deploying powerful multimodal agents on limited budgets or edge devices. For the broader AI community, it underscores that model size is less critical than active compute, paving the way for more sustainable and scalable reasoning systems in commercial and research settings.
