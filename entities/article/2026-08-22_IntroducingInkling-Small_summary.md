# Summary: Introducing Inkling-Small
Saved: 2026-10-25
Source: 2026-08-22_IntroducingInkling-Small.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://thinkingmachines.ai/news/inkling-small/)

---

## Summary
Thinking Machines has released Inkling-Small, an open-weights Mixture-of-Experts (MoE) model designed to offer performance comparable to its larger predecessor, Inkling, while utilizing significantly fewer computational resources. The model features 276 billion total parameters with only 12 billion active per inference, aiming to provide high efficiency across reasoning, agentic tool use, and instruction-following benchmarks. By incorporating variable thinking effort controls, Inkling-Small allows users to dynamically balance cost and performance, positioning it as a competitive option within its specific weight class against other leading open-weights models.

## Key Takeaways
- **Architectural Efficiency:** Inkling-Small is an MoE transformer with 276B total parameters but only 12B active parameters during inference, trained on NVIDIA GB300 NVL72 systems. This represents a substantial reduction in compute requirements compared to the full Inkling model, which has 975B total and 41B active parameters.
- **Benchmark Performance:** The model claims comparable performance to Inkling across key benchmarks including Terminal-Bench 2.1 (agentic tool use), Humanity's Last Exam (text-only reasoning), and IFBench (instruction following). It is described as competitive with other models in its weight class, such as Nemotron 3 Super, DeepSeek V4 Flash, and Qwen3.5-397B-A17B.
- **Variable Thinking Effort:** A core feature of Inkling-Small is its ability to adjust "thinking effort" from minimal to extra-high (xhigh). This allows users to tailor the model's computational output per task, optimizing for either speed/cost or maximum accuracy depending on the specific use case requirements.

## Context
The release of Inkling-Small occurs in a competitive landscape where open-weights models are increasingly vying for dominance against proprietary closed-source systems. The article highlights a growing industry focus on efficiency and cost-effectiveness rather than raw parameter count alone. By comparing performance against TFLOPs (floating point operations) and estimated output costs, the article reflects a broader shift in AI evaluation metrics toward practical deployment viability. The inclusion of native reasoning over audio and images, along with a 1M token context window, aligns with current trends toward multimodal capabilities and long-context processing in frontier model development.

## Implications
This release suggests that high-performance reasoning capabilities can be achieved with significantly lower active parameter counts through efficient MoE architectures and variable inference strategies. For developers and enterprises, the ability to tune "thinking effort" provides a mechanism to control operational costs without sacrificing quality on critical tasks, potentially democratizing access to advanced reasoning tools. Furthermore, by releasing open weights, Thinking Machines contributes to the ecosystem of transparent, inspectable models, allowing for community validation and adaptation. The emphasis on efficiency metrics like output TFLOPs per sample indicates that future model development may prioritize computational economy alongside raw capability, influencing how organizations select and deploy AI systems for production environments.
