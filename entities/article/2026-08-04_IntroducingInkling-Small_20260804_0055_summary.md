# Summary: 2026-08-04_IntroducingInkling-Small.md
Saved: 2026-08-04 00:55
Source: 2026-08-04_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an efficient open‑weights Mixture‑of‑Experts transformer that matches the performance of its larger sibling Inkling while using only a quarter of the parameters and active compute. The model leverages variable thinking effort to adapt reasoning depth, supports up to 1 million tokens, and delivers strong results on benchmarks such as Terminal‑Bench 2.1, HLE (text‑only), and IFBench.  

## Semantic links
- [[concepts/llm-models/2026-07-10_OpenSourceModelsStateOfTheArt.md|Open-Source Models State of the Art — 2026-07-10]] — 3 title terms overlap, 3 topic terms overlap, same area: home
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation and Benchmarks Hub]] — 2 title terms overlap, 3 topic terms overlap, same area: home
- [[concepts/reasoning/reasoning-hub.md|Reasoning and Inference Hub]] — 2 title terms overlap, 2 topic terms overlap, same area: home

## Key Takeaways  
- Inkling‑Small achieves comparable performance to Inkling with just 12 B active parameters versus 41 B in the original model.  
- Its variable thinking effort lets users balance cost and performance by scaling reasoning depth dynamically.  
- The model is competitive with other open‑weights models of similar size, offering high efficiency across multiple tasks.  

## Context  
The release underscores a trend toward parameter‑efficient AI where large models are replaced by sparse Mixture‑of‑Experts architectures that activate only a fraction of parameters per inference. This approach reduces compute costs and energy consumption while maintaining state‑of‑the‑art reasoning capabilities, especially for multimodal tasks like audio‑visual reasoning.  

## Implications  
For developers and enterprises, Inkling‑Small enables more affordable deployment of powerful AI agents without the prohibitive cost of full‑scale models, fostering broader adoption in resource‑constrained environments such as edge devices or cloud services with strict budgeting. It also encourages research into adaptive inference strategies that can dynamically allocate compute to tasks.
