# Summary: 2026-08-04_IntroducingInkling-Small.md
Saved: 2026-08-04 00:11
Source: 2026-08-04_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
The article introduces **Inkling‑Small**, an open‑weights MoE transformer that delivers performance comparable to the much larger Inkling model while using only a quarter of its parameters (276 B total versus 975 B). By leveraging 12 B active experts, Inkling‑Small achieves high reasoning and instruction‑following abilities on benchmarks such as Terminal‑Bench 2.1, HLE, and IFBench while keeping compute costs low and supporting a 1 M‑token context window.  

## Semantic links
- [[concepts/llm-models/OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 3 title terms overlap, 3 topic terms overlap, same area: home
- [[concepts/prompting/prompting-hub.md|Prompting and Instruction Design Hub]] — 2 title terms overlap, 4 topic terms overlap, same area: home
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation and Benchmarks Hub]] — 2 title terms overlap, 3 topic terms overlap, same area: home

## Key Takeaways  
- **Parameter efficiency:** Inkling‑Small matches the performance of Inkling with just one‑fourth of the total parameters, demonstrating that MoE can compress model size without sacrificing capability.  
- **Adaptive thinking effort:** The variable‑effort design lets users tune reasoning depth, balancing cost and accuracy for specific tasks or user needs.  
- **Open‑weight competitiveness:** Within its weight class (≈276 B total), Inkling‑Small competes with other open models like Qwen3.5‑397B‑A17B, MiMo V2.5, and Minimax M2.7 on both benchmarks and cost metrics.  

## Context  
The broader AI landscape is moving toward smaller, more efficient large language models that can run on commodity hardware or cloud services at lower expense. MoE architectures enable this by activating only a fraction of parameters per inference, reducing memory footprints and energy consumption. This trend supports the democratization of powerful generative AI, allowing developers to deploy sophisticated reasoning capabilities without massive compute budgets.  

## Implications  
For industry stakeholders, Inkling‑Small’s efficiency translates into lower operational costs, faster time‑to‑market for AI products, and a reduced environmental footprint. Its open‑weight release encourages community contributions and further model improvements, fostering a collaborative ecosystem that can accelerate innovation across sectors such as customer service bots, scientific research assistants, and real‑time decision support systems.
