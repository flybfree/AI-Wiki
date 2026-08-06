# Summary: 2026-08-06_IntroducingInkling-Small.md
Saved: 2026-08-06 00:11
Source: 2026-08-06_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an efficient open‑weights Mixture‑of‑Experts transformer that delivers performance comparable to the larger Inkling model while using only a quarter of its parameters (276 B total, 12 B active). The article highlights how this model can be tuned with variable thinking effort and supports up to one million tokens in context, making it competitive on benchmarks such as Terminal‑Bench 2.1, HLE reasoning, and IFBench.  

## Key Takeaways  
- Inkling‑Small achieves performance near that of Inkling (975 B total) with a quarter of the compute budget (12 B active parameters).  
- Its variable thinking effort lets users balance cost and capability, enabling fine‑tuned inference for diverse tasks.  
- Benchmark comparisons show it is on par with other open models in its size class across reasoning, tool use, and instruction following.  

## Context  
The release underscores a growing industry trend toward MoE architectures that scale parameters while keeping active compute low, allowing large‑scale language agents to run more affordably. Open‑weight models like Inkling‑Small compete with recent flagship systems (e.g., Nemotron 3 Super/Ultra, DeepSeek V4 Flash) in the same parameter range but at a fraction of the cost, reflecting broader efforts to democratize high‑performance AI and reduce reliance on proprietary hardware.  

## Implications  
For developers and researchers, Inkling‑Small demonstrates that state‑of‑the‑art reasoning can be achieved with far less compute, encouraging more open deployment options and lowering barriers for resource‑constrained applications. This shift could reshape cost‑performance curves in AI services, prompting a move from massive closed models to modular, tunable MoE solutions that adapt effort dynamically based on user needs.
