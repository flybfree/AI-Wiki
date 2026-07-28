# Summary: 2026-07-28_Inkling_OurOpen-WeightsModel.md
Saved: 2026-07-28 00:15
Source: 2026-07-28_Inkling_OurOpen-WeightsModel.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling is a newly released open‑weights Mixture‑of‑Experts (MoE) foundation model that can be customized and run locally via the Tinker platform. Trained on 45 trillion multimodal tokens, it has 975 billion total parameters with 41 billion active, supports a 1 million‑token context window, and includes a lighter Inkling‑Small variant (12 billion active) for lower cost. The article highlights that while Inkling is not the strongest model overall, its multimodal abilities, efficient thinking, and open‑weights nature make it an attractive base for fine‑tuning.

## Key Takeaways  
- Inkling is an open‑weights MoE transformer (975 B total, 41 B active) that handles text, images, audio, and video up to a million tokens.  
- A smaller sibling, Inkling‑Small (12 B active), offers comparable performance at reduced cost and latency.  
- The Tinker console enables self‑fine‑tuning; the model even wrote its own lipogram fine‑tuning job that avoids using the letter “e” in all responses.

## Context  
The AI industry is moving toward open‑weights models to democratize access, reduce reliance on proprietary APIs, and accelerate research. Open‑source foundation models like GPT‑3.5/4 have set high benchmarks, yet many remain closed. Inkling joins this trend by providing a full‑weight model for customization, alongside a lightweight alternative, illustrating how open ecosystems can compete with commercial offerings while offering unique trade‑offs.

## Implications  
This release lowers the barrier to fine‑tuning large multimodal models, encouraging developers to experiment and create domain‑specific assistants. It also signals that efficiency (active parameters) matters as much as raw size for practical deployment, prompting research into tighter cost‑performance curves. The self‑fine‑tuning demo demonstrates a closed‑loop workflow—model generation, training, evaluation, and rollout—that could become standard practice in the next wave of open AI tools.
