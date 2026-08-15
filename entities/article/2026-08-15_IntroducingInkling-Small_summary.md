# Summary: 2026-08-15_IntroducingInkling-Small.md
Saved: 2026-08-15 00:08
Source: 2026-08-15_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an efficient open‑weights Mixture‑of‑Experts transformer that matches the performance of its larger sibling Inkling while using only a quarter of the parameters and compute. The model leverages variable thinking effort to adapt reasoning intensity, supports up to 1 M tokens, and delivers strong results across benchmarks.

## Key Takeaways  
- Inkling‑Small (276B total, 12B active) achieves comparable performance to Inkling (975B total, 41B active) with far lower compute.  
- Its variable thinking effort lets users balance cost and performance by scaling reasoning intensity from minimal to xhigh.  
- Benchmarks show it is competitive with other open‑weights models of similar size on Terminal‑Bench 2.1, HLE, IFBench.

## Context  
The release underscores a shift toward parameter‑efficient AI where active compute rather than total parameters drives capability. Mixture‑of‑Experts architectures enable large models to be deployed at lower cost, aligning with industry trends toward sustainable and scalable LLM deployment.

## Implications  
This advancement makes high‑performance reasoning accessible for resource‑constrained applications, encouraging developers to adopt smaller, smarter models that can dynamically allocate effort, potentially reducing cloud costs and enabling broader adoption of AI agents in real‑world settings.
