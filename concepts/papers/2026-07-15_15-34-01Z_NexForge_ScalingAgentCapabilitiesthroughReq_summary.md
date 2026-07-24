# Summary: 2026-07-15_15-34-01Z_NexForge_ScalingAgentCapabilitiesthroughRequiremen.md
Saved: 2026-07-23 23:43
Source: 2026-07-15_15-34-01Z_NexForge_ScalingAgentCapabilitiesthroughRequiremen.md
Model: None

---

## Summary  
The paper introduces **NexForge**, a requirement‑driven framework that automatically synthesizes diverse, executable agent tasks and expert trajectories for large language model (LLM) post‑training fine‑tuning without relying on domain‑specific substrate tools. By taking high‑level capability requirements as input, NexForge constructs representative real‑world scenarios and then performs distribution‑aware compilation to generate task directives that include files, dependencies, and runtime configurations. The framework produces a large corpus of terminal and office tasks (up to 43 200) that can be used to train LLMs end‑to‑end. This approach dramatically improves performance on benchmark suites compared with manually curated datasets.

## Key Contributions  
- **Requirement‑driven task synthesis decouples LLM training from substrate tools**, eliminating the need for manual engineering of skill graphs or repositories.  
- **Automatic generation of a large, diverse set of terminal and office tasks** (3 600 terminal, 2 000 office) along with expert rollouts and training trajectories.  
- **Scalable dataset up to 43.2 K tasks yields state‑of‑the‑art open‑source results**, matching or surpassing several proprietary frontier models.

## Methodology  
The authors start by mining real‑world demand to build representative scenarios that capture the distribution of user needs. They then apply a distribution‑aware compilation step that automatically retrieves or constructs the necessary files, dependencies, and runtime configurations for each synthesized task directive. For every directive, NexForge creates an expert rollout—an interactive sequence of actions and observations—and assembles these into training trajectories suitable for supervised fine‑tuning (SFT). Crucially, no domain‑specific infrastructure is required; the entire pipeline runs on generic LLM pipelines.

## Results  
The base Qwen3.5‑35B‑A3B model improves from 22.5 % to **52.0 %** on Terminal‑Bench 2.0 and from **813 to 1 338 Elo** on GDPval after training with NexForge’s 3.6 K terminal tasks. Scaling the dataset to 43.2 K tasks raises performance to **58.4 %**, bringing it within reach of Claude Opus (4.6). Further scaling leads to the Nex‑N2 model family, which attains **75.3 %** on Terminal‑Bench 2.1 and **1 585 Elo** on GDPval—state‑of‑the‑art open‑source performance that exceeds several proprietary systems.

## Significance  
NexForge removes the bottleneck of substrate‑bound task generation, enabling rapid scaling of agent training data while reducing human bias toward predefined tools. By generating tasks directly from capability requirements, it produces more representative and diverse datasets, which translates into measurable gains in LLM reasoning and execution abilities. The framework also democratizes access to high‑quality agent training data through publicly available models (Nex‑N2), fostering community research and competition.

## Related Concepts  
- Requirement‑driven synthesis  
- Executable agents  
- Post‑training fine‑tuning (SFT) for LLMs  
- Task generation and skill graph independence  
- Distribution‑aware compilation  
- Terminal‑Bench 2.0 benchmark  
- GDPval evaluation suite
