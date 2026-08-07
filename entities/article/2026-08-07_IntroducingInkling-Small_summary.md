# Summary: 2026-08-07_IntroducingInkling-Small.md
Saved: 2026-08-07 00:03
Source: 2026-08-07_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Researchers at Thinking Machines AI have introduced Inkling‑Small, an open‑weights Mixture‑of‑Experts (MoE) transformer that delivers performance comparable to the much larger Inkling model while using only a quarter of its parameters. The 276 B total‑parameter system activates just 12 B experts at any given time, enabling reasoning over audio and images with a 1 M‑token context window and variable thinking effort.

## Key Takeaways  
- Inkling‑Small achieves the same performance as Inkling (975 B parameters) despite having only 276 B total parameters and 12 B active experts, demonstrating remarkable efficiency.  
- Its MoE architecture supports “variable thinking effort,” allowing users to adjust cost versus performance by scaling expert usage during inference.  
- Benchmark results show that Inkling‑Small is competitive with other open‑weight models such as Nemotron 3 Super on Terminal‑Bench 2.1, HLE reasoning, and IFBench.

## Context  
The release reflects the broader AI community’s push to reconcile scale with efficiency. MoE techniques promise to unlock high‑capacity capabilities without linearly increasing compute, aligning with trends toward smaller, more deployable models that can run on edge devices or within limited cloud budgets. This shift also supports sustainability goals by reducing energy consumption per inference.

## Implications  
For the field and industry, Inkling‑Small lowers the barrier for accessing state‑of‑the‑art reasoning capabilities, making large‑scale AI more affordable and environmentally friendly. It encourages developers to adopt MoE strategies, fostering innovation in resource‑constrained applications such as mobile assistants, real‑time translation, and on‑device analytics.
