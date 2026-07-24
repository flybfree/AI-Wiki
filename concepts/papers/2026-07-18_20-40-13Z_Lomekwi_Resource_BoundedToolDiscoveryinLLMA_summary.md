# Summary: 2026-07-18_20-40-13Z_Lomekwi_Resource_BoundedToolDiscoveryinLLMAgents.md
Saved: 2026-07-24 00:05
Source: 2026-07-18_20-40-13Z_Lomekwi_Resource_BoundedToolDiscoveryinLLMAgents.md
Model: None

---

## Summary  
The paper Lomekwi investigates how large language models (LLMs) discover and use tools, moving beyond the static success‑rate metrics of existing benchmarks. By framing tool discovery into three cognitive components—curiosity, recognition, and efficiency—the authors propose a resource‑bounded analysis that can be applied to both synthetic tasks like Voyager and real‑world emulations. Their work reveals that model size influences these components in non‑linear ways, offering a more nuanced view of LLM tool use. The contribution is a unified framework and empirical evidence linking recognition to inverse scaling with model capacity.

## Key Contributions  
- [Finding 1] A decomposition of tool discovery into curiosity (identifying needed parts), recognition (understanding the creation process), and efficiency (using the tool).  
- [Finding 2] Empirical observation that recognition performance scales inversely with model size, demonstrated through a combinatorial game experiment.  
- [Finding 3] Extension of this inverse scaling to an environment that emulates real‑world tasks, showing broader applicability.

## Methodology  
The authors first define the three sub‑components and map them onto existing discovery benchmarks such as Voyager. They then train a series of LLMs ranging from small to large models on these tasks, measuring each component’s performance. To isolate recognition, they introduce a combinatorial game where agents must discover both the set of tools and the rule that assembles them, recording success rates across model sizes. Additionally, they evaluate an environment designed to mimic everyday problem‑solving scenarios.

## Results  
Curiosity improves monotonically with larger models, while recognition drops sharply as model size increases, following an inverse relationship (e.g., 1/N scaling). Efficiency metrics show modest gains that plateau after a certain size threshold. The combinatorial game yields a clear power‑law decay in recognition accuracy, confirming the theoretical claim. In the real‑world emulation, similar inverse trends are observed for both curiosity and efficiency.

## Significance  
Understanding these dynamics is crucial because it explains why larger models may not always outperform smaller ones on tool discovery tasks. The findings challenge the assumption that bigger is better in this specific cognitive process and suggest design strategies to balance model size with recognition‑driven performance.

## Related Concepts  
- Tool use vs. tool discovery  
- Curiosity, recognition, efficiency decomposition  
- Resource‑bounded learning  
- Inverse scaling of model components
