# Summary: 2026-08-18_IntroducingInkling-Small.md
Saved: 2026-08-18 00:12
Source: 2026-08-18_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer that delivers performance on par with the larger Inkling model while using only a quarter of its parameters (276 B total, 12 B active). The article highlights that this reduction in compute—from 41 B to 12 B active weights—does not sacrifice reasoning, instruction‑following, or multimodal capabilities, and it enables users to adjust “thinking effort” for cost‑performance trade‑offs.  

## Key Takeaways  
- Inkling‑Small (276 B total, 12 B active) matches Inkling’s benchmark scores despite being roughly one‑fourth the size.  
- Variable thinking effort lets developers scale performance and cost by toggling between minimal to xhigh reasoning levels.  
- The model competes with other open‑weights LLMs (e.g., Qwen3.5, MiMo V2.5) in both efficiency and output quality across benchmarks such as Terminal‑Bench 2.1 and IFBench.  

## Context  
The release reflects a growing industry trend toward parameter‑efficient AI, where models combine sparse activation of experts to achieve high performance with lower compute budgets. This approach aligns with the push for sustainable AI deployment, enabling broader access to powerful reasoning capabilities without prohibitive cloud costs.  

## Implications  
For developers and enterprises, Inkling‑Small offers a practical path to embed advanced multimodal reasoning into applications while keeping operational expenses low, potentially accelerating adoption of AI agents in cost‑sensitive domains such as education, customer support, and research assistance.
