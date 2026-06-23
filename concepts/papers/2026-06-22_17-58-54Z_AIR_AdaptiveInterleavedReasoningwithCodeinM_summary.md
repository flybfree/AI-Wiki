# Summary: 2026-06-22_17-58-54Z_AIR_AdaptiveInterleavedReasoningwithCodeinMLLMs.md
Saved: 2026-06-23 00:01
Source: 2026-06-22_17-58-54Z_AIR_AdaptiveInterleavedReasoningwithCodeinMLLMs.md
Model: None

---


## Summary  
Multimodal large language models (MLLMs) have traditionally struggled to perform numerical computation because existing interleaved‑reasoning approaches are limited to visual manipulation and rely on static heuristics. This paper introduces an adaptive interleaved reasoning framework that integrates code execution into MLLM training, enabling the model to solve complex numeric problems beyond vision‑only tasks. The solution combines a two‑stage cold‑start data pipeline, RL‑curated datasets, and an adaptive tool‑invocation strategy driven by a group‑constrained reward function. Empirical results show that reinforcement learning boosts performance by an average of 6.1 percentage points across benchmarks, with interleaved reasoning accuracy improving by 9.9 pp and overall tool‑use success exceeding 95 %.  

## Key Contributions  
- Adaptive interleaved reasoning framework for MLLMs that supports numerical computation beyond visual manipulations.  
- Two‑stage cold‑start data construction pipeline paired with filtering strategies to generate high‑quality RL datasets.  
- Group‑constrained reward function enabling adaptive tool‑invocation during reinforcement learning training.  

## Methodology  
The authors built a three‑component solution: first, they generated task instances using code generation and annotation in the cold‑start stage; second, they applied filtering criteria to retain only tasks that require interleaved reasoning and numeric computation; third, they trained an MLLM via reinforcement learning where the reward function groups tool calls together, allowing the model to learn when and how to invoke each component. This adaptive strategy lets the model dynamically select which reasoning step to perform next, rather than following a fixed heuristic sequence.  

## Results  
After RL training with the group‑constrained reward function, the model achieved an average gain of 6.1 percentage points on evaluation benchmarks compared to prior methods. Specifically, accuracy for interleaved reasoning samples rose by 9.9 pp, and the overall success rate of tool‑use exceeded 95 %. These gains surpass baseline approaches that rely solely on visual heuristics or static code insertion.  

## Significance  
This work demonstrates that reinforcement learning combined with adaptive tool selection can overcome the limitations of traditional visual‑only interleaved reasoning in MLLMs, opening a path toward models capable of handling complex numerical tasks without predefined constraints. The findings suggest a scalable pathway for integrating code execution into multimodal systems, enhancing both accuracy and reliability across diverse problem domains.  

## Related Concepts  
- Interleaved reasoning  
- Reinforcement learning (RL)  
- Multimodal large language models (MLLMs)  
- Tool‑use in AI  
- Group‑constrained reward functions
