# Summary: 2026-08-24_IntroducingInkling-Small.md
Saved: 2026-08-24 00:11
Source: 2026-08-24_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer that delivers performance comparable to the larger Inkling model while occupying only a quarter of its parameter count (276 B total, 12 B active vs. 975 B total, 41 B active). The model supports multi‑modal reasoning over audio and images, a 1 M‑token context window, and variable thinking effort to balance cost and capability, making it competitive with other open models of similar size on benchmarks such as Terminal‑Bench 2.1, HLE (text‑only), and IFBench.

## Key Takeaways  
- [The model achieves near‑Inkling performance at a quarter of the total parameters, highlighting that only a small active subset drives capability.]  
- [Variable thinking effort lets users tailor reasoning depth, enabling cost‑performance trade‑offs without retraining.]  
- [Its MoE architecture and NVIDIA GB300 NVL72 training platform illustrate a path to scalable, efficient large‑language models.]

## Context  
The release occurs amid a surge of open‑weight, MoE‑based models (e.g., Nemotron 3 Super/Ultra, DeepSeek V4 Flash, Qwen 3.5‑A17B) that compete on both capability and compute efficiency. Industry trends favor smaller active parameter subsets to reduce inference cost while preserving reasoning ability, especially for agentic tools requiring multi‑modal input.

## Implications  
This work demonstrates that high‑fidelity reasoning can be achieved with far less raw compute, encouraging developers to adopt MoE strategies and variable effort mechanisms. For the field, it lowers barriers to deploying powerful agents in resource‑constrained environments, potentially accelerating adoption of AI assistants across sectors such as education, healthcare, and enterprise automation.
