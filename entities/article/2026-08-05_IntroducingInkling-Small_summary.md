# Summary: 2026-08-05_IntroducingInkling-Small.md
Saved: 2026-08-05 01:30
Source: 2026-08-05_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weight Mixture‑of‑Experts transformer that delivers performance comparable to its larger sibling Inkling while using only a quarter of the parameters and compute. The model leverages variable thinking effort, supports multi‑modal reasoning over audio and images, and offers a 1 M token context window.  

## Key Takeaways  
- Inkling‑Small achieves ~20% performance on Terminal‑Bench 2.1 with only 12B active parameters versus 40% for Inkling’s 41B.  
- Its variable thinking effort lets users tune cost‑performance trade‑offs, making it adaptable to different use cases.  
- The model is competitive with other open‑weight models of similar size (e.g., MiMo V2.5) in both efficiency and benchmark scores.  

## Context  
The release underscores a trend toward parameter‑efficient large language models that combine MoE architectures with dynamic reasoning budgets, enabling high‑quality output at lower compute costs—a key driver for sustainable AI deployment.  

## Implications  
For developers and researchers, Inkling‑Small demonstrates that open‑weight models can rival closed‑source alternatives in performance while drastically reducing resource consumption, encouraging broader adoption of large language systems in cost‑sensitive applications such as edge inference or real‑time assistants.
