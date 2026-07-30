# Summary: 2026-07-30_Inkling_OurOpen-WeightsModel.md
Saved: 2026-07-30 00:04
Source: 2026-07-30_Inkling_OurOpen-WeightsModel.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling is an open‑weights Mixture‑of‑Experts transformer that contains 975 billion parameters (41 B active) and can process up to one million tokens, having been pretrained on 45 trillion multimodal tokens. The release also includes a lighter sibling, Inkling‑Small, with 12 B active parameters for low‑cost inference. Because the full model weights are publicly available, anyone can fine‑tune or even let the model fine‑tune itself via Tinker, as demonstrated by its self‑lipogram experiment.

## Key Takeaways  
- **Open‑weights enable full customization** – developers can modify the 975 B parameter base for specific tasks without needing proprietary access.  
- **Efficient thinking balances cost and performance** – Inkling’s Mixture‑of‑Experts architecture activates only a fraction of its parameters, delivering strong multimodal reasoning while keeping latency low.  
- **Self‑fine‑tuning showcases interactive capability** – the model can generate its own fine‑tuning job, dataset, objective, and evaluate it, proving that customization can be automated within Tinker.

## Context  
The Inkling launch fits a broader industry shift toward open‑source foundation models where companies release large multimodal checkpoints to accelerate research and deployment. This trend reduces reliance on closed APIs, encourages community contributions, and aligns with regulatory pushes for transparency in AI systems.

## Implications  
By making such a massive, multimodal model freely usable, Inkling lowers the barrier for customizing AI assistants, potentially spurring new applications that require tight integration with proprietary workflows. The self‑fine‑tuning demo also highlights how open models can be iteratively improved through user feedback, fostering a culture of continual learning and safety testing within the community.
