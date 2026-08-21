# Summary: 2026-08-21_IntroducingInkling-Small.md
Saved: 2026-08-21 00:20
Source: 2026-08-21_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an efficient open‑weights Mixture‑of‑Experts (MoE) model that delivers performance comparable to the larger Inkling model while using only a quarter of its total parameters. By leveraging 12 B active experts out of 276 B total and offering variable thinking effort, it provides a cost‑effective alternative for tasks ranging from reasoning over audio/images to instruction following, all within a 1 M‑token context window.

## Key Takeaways  
- Inkling‑Small (276 B total, 12 B active) matches the performance of Inkling (975 B total, 41 B active) on benchmarks such as Terminal‑Bench 2.1, HLE reasoning, and IFBench despite its smaller size.  
- The model’s variable thinking effort lets users fine‑tune cost versus accuracy, making it adaptable to diverse user budgets and use cases.  
- Compared with other open‑weights models in the 100–400 B range (e.g., Qwen3.5‑397B, MiMo V2.5, Minimax M2.7), Inkling‑Small offers a favorable trade‑off between compute cost and output quality.

## Context  
The AI community is increasingly focused on scaling models while minimizing computational expense, especially for open‑source deployments. MoE architectures enable high parameter counts with only a fraction of experts active per inference, reducing latency and energy consumption. This trend aligns with broader industry moves toward more sustainable AI, where cost‑per‑token metrics are critical for adoption in edge and cloud environments.

## Implications  
The release of Inkling‑Small demonstrates that large‑scale reasoning capabilities can be achieved without the prohibitive compute budgets required by full‑parameter models, potentially democratizing access to advanced AI tools. For developers and researchers, this means faster prototyping, lower operational costs, and a clearer path toward integrating powerful language agents into real‑world applications where budget constraints are paramount.
