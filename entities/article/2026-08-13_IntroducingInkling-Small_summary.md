# Summary: 2026-08-13_IntroducingInkling-Small.md
Saved: 2026-08-13 00:07
Source: 2026-08-13_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer that delivers performance comparable to the larger Inkling model while using only a quarter of its parameters (276 B total vs. 975 B). Its 12 B active experts, variable thinking effort, and up‑to‑1 M token context enable efficient reasoning over audio, images, and text at a fraction of the compute cost.

## Key Takeaways  
- Inkling‑Small achieves near‑Inkling performance with just 12 B active parameters, illustrating the power of Mixture‑of‑Experts compression.  
- The model’s variable thinking effort lets users adjust reasoning depth, balancing output quality and computational expense.  
- Compared to other open‑weight models (e.g., Nemotron 3 Super, Qwen 3.5‑397B), Inkling‑Small offers a strong performance‑to‑compute ratio at a modest cost.

## Context  
The AI research field is increasingly focused on scaling large language models while keeping compute and energy costs manageable. Open‑weight models like Inkling‑Small aim to democratize access to high‑capability reasoning agents, competing with proprietary systems such as Gemini or Claude that require massive infrastructure. The emergence of Mixture‑of‑Experts architectures provides a path to “sparse” activation, where only a fraction of parameters are active per inference.

## Implications  
For developers and enterprises, Inkling‑Small suggests that powerful multimodal reasoning can be deployed on commodity hardware without prohibitive expense, accelerating prototyping and real‑world integration. It also pressures larger models to adopt more efficient architectures, potentially reshaping the competitive landscape for AI services and prompting a shift toward cost‑aware model selection in production pipelines.
