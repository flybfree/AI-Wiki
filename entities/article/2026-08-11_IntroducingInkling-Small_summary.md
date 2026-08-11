# Summary: 2026-08-11_IntroducingInkling-Small.md
Saved: 2026-08-11 00:04
Source: 2026-08-11_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer that delivers performance on par with the much larger Inkling model (975 B total parameters) while using only a quarter of its compute—276 B total parameters, 12 B active. The model supports native reasoning over audio and images, offers variable thinking effort to balance cost and capability, and can handle up to one million tokens in context. Benchmarks such as Terminal‑Bench 2.1, HLE (text‑only), and IFBench show that Inkling‑Small is competitive with other open‑weights models of similar size on both accuracy and efficiency.

## Key Takeaways  
- **Compute reduction:** By activating only 12 B parameters out of the total 276 B, Inkling‑Small cuts active compute to a quarter of Inkling’s 41 B while maintaining comparable reasoning performance.  
- **Adaptive thinking effort:** The variable‑effort design lets users tune the model’s output cost by adjusting how much reasoning is performed, enabling fine‑grained control over price versus quality.  
- **Open‑weight accessibility:** As an open‑weights model, Inkling‑Small democratizes access to high‑capacity AI, allowing researchers and developers to experiment without licensing fees.

## Context  
Mixture‑of‑Experts (MoE) architectures have become a primary strategy for scaling language models while keeping active compute low. Open‑weight releases like Inkling‑Small reflect a broader industry trend toward releasing state‑of‑the‑art performance within affordable compute budgets, fostering competition and rapid innovation in the AI ecosystem.

## Implications  
The efficiency gains of Inkling‑Small have tangible implications for both research and industry: they lower the financial barrier to deploying large‑scale reasoning models, encourage more frequent experimentation with multimodal capabilities (audio, images), and push the frontier of cost‑effective AI services. By demonstrating that a quarter‑size model can rival a full‑size one on benchmarks, Inkling‑Small signals a new paradigm where performance and price are tightly coupled, accelerating adoption across diverse applications.
