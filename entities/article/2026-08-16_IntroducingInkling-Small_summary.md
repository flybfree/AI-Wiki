# Summary: 2026-08-16_IntroducingInkling-Small.md
Saved: 2026-08-16 00:07
Source: 2026-08-16_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an efficient open‑weights Mixture‑of‑Experts transformer released by Thinking Machines, offering performance comparable to its larger sibling Inkling while using only a quarter of the parameters and active compute. The model supports audio‑image reasoning, variable thinking effort, and a 1 million‑token context window, making it competitive with other 276 B‑parameter models across benchmarks.  

## Key Takeaways  
- Inkling‑Small achieves similar reasoning and instruction‑following performance to the 975 B‑parameter Inkling model but operates on just 12 B active parameters, a quarter of the compute.  
- Its variable thinking effort lets users tailor cost‑performance trade‑offs across tasks such as Terminal‑Bench 2.1, HLE reasoning, and IFBench.  
- The model’s efficiency is comparable to other open‑weights models in its size class, challenging the notion that massive parameter counts are necessary for high quality.  

## Context  
The release of Inkling‑Small reflects a growing trend toward parameter‑efficient AI where Mixture‑of‑Experts architectures enable large‑scale capabilities with far fewer active parameters. This aligns with industry efforts to reduce compute costs and carbon footprints while maintaining state‑of‑the‑art performance on benchmarks.  

## Implications  
For developers, Inkling‑Small provides a practical alternative for deploying reasoning agents that can run locally or at lower cloud costs, potentially accelerating adoption of multimodal AI tools. For the broader field, it underscores that efficiency gains are achievable without sacrificing quality, encouraging further research into scalable, cost‑effective model designs.
