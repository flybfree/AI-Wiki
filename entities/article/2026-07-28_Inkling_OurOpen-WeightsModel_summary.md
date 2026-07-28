# Summary: 2026-07-28_Inkling_OurOpen-WeightsModel.md
Saved: 2026-07-28 00:15
Source: 2026-07-28_Inkling_OurOpen-WeightsModel.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Tinker AI introduces Inkling, an open‑weights Mixture‑of‑Experts transformer that combines 975 B total parameters (41 B active) and supports a 1 M token context window. The model is pretrained on 45 trillion multimodal tokens and is released for fine‑tuning, with a lighter Inkling‑Small variant also shared. A playful demonstration shows the model can fine‑tune itself to become a “lipogram” assistant that never uses the letter **e**, illustrating both customization capability and self‑improvement.

## Key Takeaways  
- Inkling is an open‑weights, multimodal foundation model (975 B total parameters) designed for easy fine‑tuning on Tinker.  
- The platform enables users to experiment with the model, including self‑fine‑tuning tasks that generate novel behavior.  
- A smaller sibling, Inkling‑Small (12 B active parameters), offers comparable performance at lower cost and latency.

## Context  
The release aligns with a broader industry shift toward open‑weights models that democratize access to large foundation systems, allowing researchers and developers to tailor AI capabilities without proprietary restrictions. By providing both a full‑scale model and a lightweight variant, Tinker AI addresses the trade‑off between performance and computational efficiency, echoing trends seen in projects like LLaMA, Mistral, and Google’s Gemma.

## Implications  
This move could accelerate customization pipelines across industries—from creative content generation to domain‑specific assistants—by lowering entry barriers for fine‑tuning. Moreover, the self‑fine‑tuning experiment demonstrates a potential path toward continual learning models that improve themselves through user interaction, hinting at future AI systems that evolve autonomously while remaining transparent and open.
