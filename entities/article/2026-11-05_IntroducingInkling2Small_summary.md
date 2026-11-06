# Summary: 2026-11-05_IntroducingInkling2Small.md
Saved: 2026-11-05 21:51
Source: 2026-11-05_IntroducingInkling2Small.md
Model: qwen3.8-flash-next-iq3_xxs

---

## Summary
Thinking Machines has released Inkling 2 Small, a Mixture-of-Experts (MoE) model featuring 594 billion total parameters and 17 billion active parameters, marking the second generation of their model series. The model demonstrates significant performance improvements in agentic coding, vision, and reasoning, achieving an Artificial Analysis Intelligence Index score of 31. Initially available via closed weights on the Tinker platform, the full model weights are scheduled for release under an Apache 2.0 license following external safety testing.

## Key Takeaways
- **Advanced Architecture and Capabilities:** Inkling 2 Small utilizes a Mixture-of-Experts architecture with support for image inputs and variable effort, enabling it to surpass previous models in long-horizon autonomous tasks, including generating complex procedural environments like city simulators and PC emulators from scratch.
- **Enhanced Agentic Coding Performance:** The model was trained using reinforcement learning on hundreds of thousands of long-horizon coding tasks, incorporating agentic graders that evaluate problem-solving approaches rather than just code correctness. This results in superior performance on benchmarks like FrontierCode v2.0 and DeepSWE v1.1 compared to competitors such as GLM-5.3-Flash and Kimi K3.
- **Phased Open Weights Strategy:** Thinking Machines is adopting a "safe path to open weights" approach, initially offering the model with closed weights for safety and red-teaming purposes before releasing full Apache 2.0 licensed weights next week, balancing accessibility with responsible AI deployment practices.

## Context
This release occurs in a competitive landscape where large language models are increasingly evaluated on their ability to perform autonomous, multi-step tasks rather than just static text generation. The shift toward MoE architectures reflects industry efforts to maximize efficiency by activating only a subset of parameters during inference. Furthermore, the emphasis on "agentic" capabilities highlights a broader industry trend toward AI systems that can interact with environments, use tools, and self-correct through visual feedback loops, moving beyond simple chat interfaces to complex creative and engineering workflows.

## Implications
The introduction of Inkling 2 Small signals a maturation in open-weight model development, where safety testing is integrated directly into the release pipeline rather than treated as an afterthought. By demonstrating strong performance in vision-based iterative design and autonomous coding, the model suggests that future AI agents will be capable of handling complex, multi-modal workflows with minimal human intervention. This could accelerate adoption in software development and creative industries, while also setting a precedent for how high-performance models can be released responsibly without compromising on capability or transparency.
