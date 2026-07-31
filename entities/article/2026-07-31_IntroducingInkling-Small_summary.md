# Summary: 2026-07-31_IntroducingInkling-Small.md
Saved: 2026-07-31 00:04
Source: 2026-07-31_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts transformer that delivers performance on the order of its predecessor Inkling while occupying only a quarter of the total parameters (12 B active vs 41 B). It supports audio and image reasoning, variable thinking effort, and a 1 M‑token context window, making it competitive with other large open models in both capability and efficiency.  

## Key Takeaways  
- Inkling‑Small achieves comparable performance to the full‑size Inkling model using just 12 B active parameters, a dramatic reduction in compute (≈3× less).  
- The variable thinking effort feature lets users fine‑tune cost versus capability, enabling easy adaptation for specific use cases.  
- Benchmarks show Inkling‑Small is on par with other open‑weights models of similar size across Terminal‑Bench 2.1, HLE reasoning, and IFBench tasks.  

## Context  
The release reflects a growing trend toward Mixture‑of‑Experts (MoE) architectures that allocate compute only to the most relevant experts, thereby shrinking active parameter counts while preserving large‑scale capabilities. This approach aligns with industry pushes for cost‑effective AI deployment and open‑source model sharing, where models like Inkling‑Small can be evaluated against a diverse set of benchmarks (Terminal‑Bench 2.1, HLE, IFBench) to gauge both performance and output TFLOPs per sample or dollar cost per token.  

## Implications  
For developers and researchers, Inkling‑Small demonstrates that state‑of‑the‑art reasoning can be achieved with far fewer resources, lowering barriers to entry for high‑quality AI services. It encourages a shift from monolithic, compute‑heavy models toward modular, efficient designs that balance performance and cost, potentially accelerating innovation across sectors such as education, healthcare, and enterprise automation where large language models are increasingly deployed.
