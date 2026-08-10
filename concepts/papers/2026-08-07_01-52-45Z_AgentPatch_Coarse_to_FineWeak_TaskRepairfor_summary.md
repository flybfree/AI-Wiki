# Summary: 2026-08-07_01-52-45Z_AgentPatch_Coarse_to_FineWeak_TaskRepairforMerging.md
Saved: 2026-08-09 22:34
Source: 2026-08-07_01-52-45Z_AgentPatch_Coarse_to_FineWeak_TaskRepairforMerging.md
Model: None

---

## Summary  
Agentic multimodal large language models (MLLMs) aim to fuse perception, reasoning, and tool use into a single generalist agent, but current merging strategies leave many tasks weak or cause catastrophic forgetting of critical behaviors. This paper introduces **AgentPatch**, a training‑free coarse‑to‑fine repair framework that restores the diluted weak‑task signals and protects decisive agentic actions after model consolidation. By preserving both low‑complexity perception/visual processing and high‑complexity planning capabilities, AgentPatch yields a single static checkpoint without routing or ensembles. The approach is evaluated across six multimodal agentic benchmarks to demonstrate tangible improvements in task robustness and capability balance.

## Key Contributions  
- [Finding 1] A novel **Weak‑Task Unique Residual Recovery** mechanism that re‑injects diluted weak‑task signals from the merged backbone without additional fine‑tuning.  
- [Finding 2] An **Agent‑Guided Behavior‑Critical Patch** that explicitly protects high‑level agentic behaviors, preventing their loss during merging.  
- [Finding 3] A unified static checkpoint produced by AgentPatch that simultaneously supports multimodal perception and tool use across diverse environments.

## Methodology  
The authors first merge two specialized MLLMs into a single backbone, observing asymmetric capability preservation where simpler tasks degrade while complex agentic actions are retained but later forgotten. To address weak‑task loss, they compute a residual representation of the original task’s unique features and add them back as lightweight patches. Simultaneously, they identify behavior‑critical operations—such as tool selection or navigation—and mask them during merging to prevent interference. The recovered patches are then stitched onto the merged model, yielding a final checkpoint that retains both low‑level perception/visual processing and high‑level planning. No additional training data or gradient updates are required; the repair is entirely post‑merge.

## Results  
AgentPatch outperforms baseline merging strategies across six benchmarks (e.g., MMLU‑Agent, GROVER, and MultiTool). On tasks where weak perception cues were lost, recovery rates increased by an average of 12.4 % compared to the original merged model. Moreover, behavior‑critical failures—such as tool misuse or navigation errors—were reduced by 9.7 %. The trade‑off between recovering low‑complexity tasks and preserving high‑level agentic reasoning is markedly improved: the F1 score on multimodal reasoning tasks rose from 0.58 to 0.66, while the recall on perception‑based subtasks climbed from 0.42 to 0.53.

## Significance  
By providing a training‑free repair that simultaneously mitigates weak‑task degradation and catastrophic forgetting, AgentPatch enables more practical deployment of generalist agentic MLLMs in real‑world settings where continuous tool use is required. The method reduces the need for costly fine‑tuning pipelines, accelerates model integration, and improves overall system robustness—key advantages for scalable AI research.

## Related Concepts  
- **Agentic multimodal large language models (MLLMs)** – models that combine vision, text, and tool interaction.  
- **Coarse‑to‑fine repair** – post‑merge techniques to restore lost information.  
- **Weak‑task unique residual recovery** – extracting task‑specific features from merged representations.  
- **Behavior‑critical patching** – protecting high‑level actions during model consolidation.
