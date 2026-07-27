# Summary: 2026-07-27_Inkling_OurOpen-WeightsModel.md
Saved: 2026-07-27 11:02
Source: 2026-07-27_Inkling_OurOpen-WeightsModel.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Tinker, the AI research team behind Thinking Machines, has released Inkling—a fully open‑weights Mixture‑of‑Experts transformer (975 B total parameters, 41 B active) that can process up to one million tokens and was trained on 45 trillion multimodal tokens. The release also includes a lighter preview model, Inkling‑Small, and invites customization via Tinker’s fine‑tuning platform, exemplified by the self‑fine‑tuned lipogram model that avoids using the letter “e”.  

## Key Takeaways  
- Inkling is an open‑weights foundation model with efficient multimodal reasoning, offering a balance of performance and cost for downstream customization.  
- The project introduces Tinker’s fine‑tuning console, enabling users to train and evaluate models directly within the platform, as demonstrated by Inkling’s self‑fine‑tuning experiment.  
- A family of progressively smaller models (Inkling‑Small) is being shared, expanding accessibility while maintaining strong performance on a single hardware budget.  

## Context  
The AI industry is moving toward open‑source foundation models that can be fine‑tuned for specific tasks without requiring full model access from proprietary providers. Open weights lower barriers to research and commercial adoption, foster community contributions, and accelerate iterative improvement through user‑driven experimentation. Inkling’s approach aligns with this trend by making a large‑scale Mixture‑of‑Experts model publicly available alongside tooling for customization.  

## Implications  
By releasing Inkling, Tinker not only expands the ecosystem of open‑weight models but also demonstrates how self‑directed fine‑tuning can generate novel capabilities (e.g., a lipogram assistant). This could democratize access to multimodal reasoning, encourage rapid prototyping for niche applications, and set a precedent for future model families that balance scale, efficiency, and user‑centric customization.
