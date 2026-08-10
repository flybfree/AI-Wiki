# Summary: 2026-08-10_IntroducingInkling-Small.md
Saved: 2026-08-10 00:02
Source: 2026-08-10_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer that delivers performance comparable to the much larger Inkling model while using only a quarter of its parameters (12 B active vs. 41 B). The new model supports reasoning over audio and images, a 1 M‑token context window, and variable thinking effort, making it both efficient and adaptable for diverse tasks.

## Key Takeaways  
- Inkling‑Small cuts the number of active parameters from 41 B to 12 B yet maintains competitive performance across Terminal‑Bench 2.1, HLE (text‑only reasoning) and IFBench benchmarks.  
- Its variable thinking effort lets users tune cost versus accuracy, balancing output TFLOPs per sample with dollar cost per sample.  
- The model’s efficiency rivals other open‑weights models in the 276 B total‑parameter range, demonstrating that large‑scale reasoning can be achieved at a fraction of the compute.

## Context  
The AI industry is increasingly focused on scaling models without proportional increases in energy and cost. MoE architectures like Inkling‑Small illustrate how sparse activation strategies enable high‑capacity inference with far fewer active parameters. Open‑weight releases such as this one accelerate community adoption, reduce reliance on proprietary hardware, and provide a benchmark for efficiency metrics that are now standard in model comparisons.

## Implications  
By delivering comparable reasoning capabilities at a quarter of the compute cost, Inkling‑Small lowers barriers to deploying powerful agents in resource‑constrained environments. This shift encourages developers to prioritize parameter efficiency over sheer size, potentially reshaping training pipelines and deployment strategies across sectors from research labs to production services.
