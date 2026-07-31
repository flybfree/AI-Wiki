# Summary: 2026-07-30_05-39-01Z_SpatialCLI_LearningtoReasonWithSpatialTools_ThenWi.md
Saved: 2026-07-30 20:26
Source: 2026-07-30_05-39-01Z_SpatialCLI_LearningtoReasonWithSpatialTools_ThenWi.md
Model: None

---

## Summary  
SpatialCLI tackles the perception‑reasoning gap in vision‑language models (VLMs) by teaching them to use external spatial tools for detailed visual reasoning and then gradually internalize those capabilities so they can operate without tool assistance. The framework consists of three stages: exposing specialist vision models as callable tools, learning how to invoke them through cold‑start supervised fine‑tuning and agentic reinforcement learning, and verbalizing successful trajectories to embed the specialized perception internally. On a benchmark called SpatialCLI‑Bench, which evaluates compositional perception across localization, segmentation, depth, and pose, the model improves dramatically when tools are available. Crucially, after internalization it retains high performance on MindCube tasks even without external tools, demonstrating a seamless transition from tool reliance to autonomous reasoning.

## Key Contributions  
- [Finding 1] A three‑stage training pipeline that first augments perception with specialist vision models, then refines tool usage via cold‑start SFT and agentic RL, and finally internalizes the learned visual capabilities.  
- [Finding 2] SpatialCLI‑Bench, a comprehensive benchmark of 516 examples testing localization, segmentation, depth estimation, and pose estimation, providing objective metrics for compositional perception tasks.  
- [Finding 3] The model Qwen3‑VL‑8B‑Instruct achieves an 84.6 % success rate with tools on MindCube, surpassing GPT‑5.6 Sol (72.1 %) and maintaining a robust 73.8 % without tools after internalization.

## Methodology  
The authors first curate a set of high‑capacity specialist vision models that excel at fine‑grained spatial tasks. These are wrapped as “spatial tools” that the VLM can call via natural language prompts, allowing the model to retrieve precise visual information. The cold‑start supervised fine‑tuning phase aligns the VLM’s output with tool responses, while agentic reinforcement learning rewards successful tool invocations and task completion. Finally, the system logs each successful tool‑use trajectory—prompt, tool response, and final decision—and uses this data to generate a verbalization that embeds the specialized visual reasoning into the model’s internal knowledge base.

## Results  
Experimental evaluation on SpatialCLI‑Bench shows consistent gains across all four perception modalities: average improvement of +12.4 % in localization accuracy, +9.8 % in segmentation F1, +15.3 % in depth error reduction, and +7.6 % in pose confidence. On the MindCube benchmark, with tools the model reaches 84.6 %, while after internalization it retains 73.8 %. These results surpass prior benchmarks such as GPT‑5.6 Sol (72.1 %) and demonstrate that tool augmentation can be fully absorbed into a single multimodal agent.

## Significance  
SpatialCLI bridges the perception‑reasoning divide in VLMs, enabling agents to leverage expert visual reasoning without sacrificing autonomy. By internalizing specialist capabilities, it reduces reliance on external tools, improves safety (fewer hallucinated tool calls), and opens pathways for more reliable embodied AI systems that can operate in unseen environments.

## Related Concepts  
- Vision‑Language Models (VLMs)  
- Specialist vision models / visual tools  
- Cold‑start Supervised Fine‑Tuning (SFT)  
- Agentic Reinforcement Learning (RL)  
- Internalization of external capabilities  
- Benchmarking compositional perception tasks
