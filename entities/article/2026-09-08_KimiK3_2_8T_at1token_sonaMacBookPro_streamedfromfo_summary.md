# Summary: Kimi K3 (2.8T) at 1 token/s on a MacBook Pro, streamed from four SSDs
Saved: 2026-10-25
Source: 2026-09-08_KimiK3_2_8T_at1token_sonaMacBookPro_streamedfromfo.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://github.com/argonautlabsai/deltafin)

---

## Summary
The article describes "Deltafin," a specialized software fork designed to run the full, unpruned 2.8-trillion-parameter Kimi K3 model on consumer hardware, specifically an Apple Silicon MacBook Pro. By streaming data from four SSDs and utilizing speculative execution where a draft model guesses ahead while K3 verifies every token, Deltafin achieves a throughput of approximately 0.29 tokens per second. The project emphasizes maintaining exact model quality without quantization or pruning, contrasting its approach with other methods that compress weights to fit smaller hardware footprints.

## Key Takeaways
- **Full Model Integrity:** Deltafin runs the complete Kimi K3 architecture, including all 16 routed experts and the full 2.8T parameters, ensuring no quality reduction through pruning or aggressive quantization (such as re-encoding to ~3 bits). The system prioritizes exact fidelity to Moonshot’s original release over speed compromises that alter model weights.
- **Consumer Hardware Feasibility:** Despite Kimi K3 typically requiring infrastructure with roughly 4.8 TB of aggregate VRAM across 16 nodes, Deltafin demonstrates the ability to run this massive model on a $15,000 home setup using an M1 Max laptop and external SSDs. This challenges the notion that frontier models are exclusively accessible via million-dollar data center infrastructure.
- **Performance Metrics:** The current benchmark on an M1 Max achieves 0.2901 tokens per second (3.447 seconds per token), representing a 1.9% improvement over previous updates. Historical data shows significant optimization progress, with throughput increasing from 0.0141 tokens/s in late July 2026 to nearly 0.3 tokens/s by September 2026.

## Context
This project exists within the broader trend of "self-hosted AI," where developers seek to run large language models locally rather than relying on cloud APIs. Kimi K3 is described as targeting high-end infrastructure, making its deployment on consumer hardware an extreme technical constraint. Deltafin serves as an experimental counterpoint to other projects that achieve higher speeds by compressing the model’s expert bank, which the authors argue introduces unmeasured quality costs. The project is framed not as a commercial product but as a research exploration into the limits of consumer hardware capabilities.

## Implications
Deltafin suggests that it is possible to access frontier-level AI models on personal computers without sacrificing model integrity, potentially democratizing access to high-quality AI tools for researchers and hobbyists. By proving that full-parameter models can run on home setups, even at slow speeds, the project highlights a pathway for local AI development that avoids reliance on expensive cloud infrastructure. Furthermore, the iterative performance improvements documented in the article demonstrate that significant efficiency gains are possible through software optimization and hardware configuration (such as SSD streaming), offering insights that could benefit other projects aiming to optimize large model inference on constrained resources.
