# Summary: 2026-07-30_IntroducingInkling-Small.md
Saved: 2026-07-30 13:02
Source: 2026-07-30_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer released by Thinking Machines that delivers performance comparable to its predecessor Inkling while using only a quarter of the total parameters (276 B total, 12 B active). The model supports native reasoning over audio and images, offers up to 1 M token context, and employs variable thinking effort to balance cost and capability. Benchmarks such as Terminal‑Bench 2.1, HLE text‑only, and IFBench show that Inkling‑Small matches or exceeds many other open‑weights models in its weight class on both performance and efficiency.

## Key Takeaways  
- **Efficiency breakthrough:** Inkling‑Small achieves the same reasoning quality as Inkling (41 B active) with just 12 B active parameters, a quarter of the size.  
- **Variable thinking effort:** Users can dynamically adjust the amount of reasoning required per query, enabling cost‑effective scaling from minimal to high‑effort tasks.  
- **Open‑weight advantage:** Being fully open‑weights and built on NVIDIA GB300 NVL72 systems lowers deployment barriers compared with closed proprietary models.

## Context  
The release reflects a broader industry shift toward MoE architectures that compress massive model capacity into a smaller active subset, reducing compute demand. Open‑weight models are gaining traction as they democratize access to high‑capability AI, especially when paired with cost‑aware inference strategies like variable thinking effort. This trend aligns with the push for sustainable AI development, where performance per dollar and token is critical.

## Implications  
For researchers and practitioners, Inkling‑Small demonstrates that state‑of‑the‑art reasoning can be achieved without prohibitive hardware costs, encouraging wider adoption of MoE models in resource‑constrained environments. For developers, the variable thinking effort feature simplifies integration into diverse applications, allowing fine‑tuned trade‑offs between latency and accuracy. Ultimately, this model underscores a move toward more efficient, accessible AI that can be deployed at scale without sacrificing capability.
