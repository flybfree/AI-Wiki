# Summary: Introducing Inkling-Small
Saved: 2026-10-25
Source: 2026-08-03_IntroducingInkling-Small.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://thinkingmachines.ai/news/inkling-small/)

---

## Summary
Thinking Machines has released Inkling-Small, an open-weights Mixture-of-Experts model designed to achieve performance comparable to its larger predecessor, Inkling, while utilizing significantly fewer computational resources. With 276 billion total parameters and only 12 billion active parameters, the model offers a quarter of the size of the original Inkling but maintains competitive capabilities in reasoning, agentic tool use, and instruction following. The release emphasizes efficiency through variable thinking effort controls, allowing users to balance cost and performance across various benchmarks.

## Key Takeaways
- **Architectural Efficiency:** Inkling-Small is a Mixture-of-Experts transformer trained on NVIDIA GB300 NVL72 systems, featuring 276B total parameters but only 12B active parameters during inference, compared to the original Inkling’s 41B active parameters.
- **Performance Parity:** The model achieves comparable performance to the larger Inkling model across key benchmarks, including Terminal-Bench 2.1 for agentic tool use, Humanity's Last Exam (HLE) for reasoning, and IFBench for instruction following, while being more efficient in terms of compute and cost.
- **Variable Reasoning Control:** A core feature is the ability to adjust "thinking effort" from minimal to xhigh, enabling users to tailor the model’s computational expenditure to specific use cases, thereby optimizing the trade-off between output quality and operational costs.

## Context
This release occurs within a competitive landscape of open-weights large language models, including competitors such as Nemotron 3 Super/Ultra, DeepSeek V4 Flash, Qwen3.5, Kimi K2.5/K2.6, and GLM 5.2. The article positions Inkling-Small against these peers in terms of both performance metrics (pass@1) and efficiency metrics (TFLOPs per task and estimated output cost per sample). It highlights a growing industry trend toward optimizing active parameter usage rather than just total model size, leveraging Mixture-of-Experts architectures to deliver high capability with lower inference costs. The inclusion of native reasoning over audio and images and a 1M token context window aligns with current demands for multimodal and long-context capabilities in AI systems.

## Implications
The introduction of Inkling-Small suggests a strategic shift in model development toward maximizing utility per compute unit, making high-performance reasoning more accessible to users who cannot afford the computational overhead of larger models like the original Inkling. By offering variable thinking effort, Thinking Machines provides a flexible tool for developers and enterprises to fine-tune operational costs without sacrificing baseline performance. This approach challenges existing open-weights models in the same weight class, potentially driving further innovation in efficient transformer architectures and cost-effective inference strategies. The emphasis on open weights also supports broader adoption and customization within the AI community, fostering competition and transparency in model capabilities.
