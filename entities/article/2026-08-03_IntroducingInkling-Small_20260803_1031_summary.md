# Summary: 2026-08-03_IntroducingInkling-Small.md
Saved: 2026-08-03 10:31
Source: 2026-08-03_IntroducingInkling-Small.md
Model: qwen3.6:35b

---

## Summary
Thinking Machines has released Inkling-Small, an efficient open-weights model that delivers performance comparable to its larger counterpart, Inkling, while utilizing only a quarter of the parameters. This Mixture-of-Experts transformer features 276 billion total parameters with 12 billion active during inference, enabling native reasoning over audio and images alongside a massive one-million-token context window. By significantly reducing computational requirements without sacrificing benchmark accuracy, Inkling-Small offers a highly cost-effective alternative for developers seeking powerful multimodal capabilities.

## Key Takeaways
- **Efficient Architecture**: Inkling-Small utilizes a Mixture-of-Experts design with 276B total parameters but only 12B active parameters, achieving performance parity with the larger 975B-parameter Inkling model at a fraction of the size and compute cost.
- **Multimodal and Long-Context Capabilities**: The model supports native reasoning across audio and image modalities and handles context windows up to 1M tokens, making it suitable for complex, data-intensive tasks that require deep understanding of diverse inputs.
- **Variable Thinking Effort**: A key feature is the ability to adjust "thinking effort" from minimal to extreme levels, allowing users to dynamically balance inference speed, cost, and performance based on specific use-case requirements across benchmarks like Terminal-Bench 2.1 and HLE.

## Context
The AI landscape is currently undergoing a significant shift toward efficiency and accessibility in large language models. As foundational models grow larger, the industry faces increasing pressure to reduce inference costs and environmental impact. Competitors such as Qwen, Kimi, and GLM are also releasing highly optimized models that challenge traditional size-performance trade-offs. The release of Inkling-Small arrives at a critical juncture where open-weights models must demonstrate not just raw capability, but superior efficiency to gain traction in both academic research and commercial applications.

## Implications
This release democratizes access to high-end multimodal reasoning capabilities by making them computationally affordable for a broader range of developers and organizations. The emphasis on variable thinking effort sets a new standard for adaptive AI systems, allowing enterprises to optimize their operational costs without compromising on quality. Furthermore, the competitive performance against other major open-weights models suggests that future innovation will focus less on sheer parameter count and more on architectural efficiency, such as Mixture-of-Experts designs, potentially accelerating the adoption of advanced reasoning models in real-world industrial workflows.
