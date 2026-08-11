# Summary: 2026-08-11_IntroducingInkling-Small.md
Saved: 2026-08-11 00:19
Source: 2026-08-11_IntroducingInkling-Small.md
Model: nvidia/nemotron-3-nano-4b

---

## Summary  
Inkling‑Small is an open‑weights Mixture‑of‑Experts (MoE) transformer that delivers performance comparable to the larger Inkling model while using only a quarter of its parameters and compute resources. The 276 B total‑parameter model activates just 12 B experts, supports audio‑ and image‑based reasoning, a 1 M‑token context window, and variable thinking effort, making it highly adaptable for cost‑sensitive applications.

## Key Takeaways  
- **Parameter efficiency:** Inkling‑Small’s 276 B total parameters (versus Inkling’s 975 B) achieve comparable reasoning and instruction‑following scores on Terminal‑Bench 2.1, HLE, and IFBench benchmarks.  
- **Variable thinking effort:** Users can sweep the amount of active experts from minimal to xhigh, balancing performance against compute cost in real time.  
- **Open‑weight advantage:** The model is released as an open‑weights artifact, enabling community evaluation and integration without licensing barriers.

## Context  
The article highlights a broader shift toward MoE architectures that promise high capacity with sparse activation, reducing the massive GPU/TPU requirements of full‑parameter models. Open‑weight releases are increasingly common, allowing researchers to benchmark efficiency directly against proprietary systems and fostering competition in model size versus performance trade‑offs.

## Implications  
By delivering a 75 % reduction in active parameters while maintaining state‑of‑the‑art reasoning capabilities, Inkling‑Small lowers the financial barrier for deploying large language models at scale. This encourages broader adoption across industries—from research labs to commercial products—where compute budgets are tight and latency constraints matter.
