# Summary: Introducing Inkling-Small
Saved: 2026-10-25
Source: 2026-08-02_IntroducingInkling-Small.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://thinkingmachines.ai/news/inkling-small/)

---

## Summary
Thinking Machines has released Inkling-Small, an open-weights Mixture-of-Experts (MoE) model designed to offer performance comparable to its larger predecessor, Inkling, while significantly reducing computational requirements. The model features 276 billion total parameters with only 12 billion active per inference, trained on NVIDIA GB300 NVL72 systems. It supports native reasoning over audio and images, a one-million-token context window, and variable thinking effort to balance cost and performance across various benchmarks.

## Key Takeaways
- **Architectural Efficiency:** Inkling-Small utilizes an MoE architecture with 276B total parameters but only 12B active parameters during inference, making it roughly one-quarter the size of the original Inkling model (which has 41B active parameters). This design allows for substantial compute savings while maintaining competitive performance levels.
- **Benchmark Performance:** The model demonstrates strong results in agentic tool use (Terminal-Bench 2.1), reasoning (Humanity's Last Exam text-only), and instruction following (IFBench). It is positioned as competitive with other open-weights models in its weight class, such as Nemotron 3 Super, DeepSeek V4 Flash, and Qwen3.5-397B-A17B, particularly when considering efficiency metrics like TFLOPs per task.
- **Variable Reasoning Control:** A key feature is the ability to adjust "thinking effort" from minimal to xhigh. This allows users to explicitly trade off computational cost against performance quality, providing a flexible tool for developers who need to optimize for specific budget or latency constraints without sacrificing capability entirely.

## Context
The release of Inkling-Small occurs within a rapidly evolving landscape where open-weights models are increasingly challenging proprietary systems in terms of raw capability and efficiency. By leveraging NVIDIA’s GB300 NVL72 hardware, Thinking Machines highlights the importance of specialized infrastructure for training high-parameter MoE models. The inclusion of native multimodal reasoning (audio/image) and extended context windows (1M tokens) aligns with current industry trends toward more versatile, long-context AI agents capable of handling complex, multi-step tasks without external tool reliance for basic reasoning.

## Implications
This development signifies a shift toward highly efficient, specialized open-weights models that can democratize access to high-performance AI capabilities. By offering comparable performance to larger models at a fraction of the compute cost, Inkling-Small lowers the barrier to entry for deploying sophisticated reasoning agents in production environments. The explicit control over thinking effort provides developers with granular control over operational costs, potentially accelerating the adoption of AI agents in cost-sensitive applications. Furthermore, the competitive positioning against other major open-weights models suggests a maturing ecosystem where efficiency and architectural optimization are becoming as critical as raw parameter count for achieving state-of-the-art results.
