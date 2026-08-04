# Summary: 2026-08-02_18-14-40Z_TrainingSmallLLMsasSpatialMulti_AgentPolicies.md
Saved: 2026-08-04 00:21
Source: 2026-08-02_18-14-40Z_TrainingSmallLLMsasSpatialMulti_AgentPolicies.md
Model: None

---

## Summary  
The paper tackles the challenge of training small frozen large language models (LLMs) to act as spatial multi‑agent policies in cooperative games, arguing that behavior—not just reward—should be the primary metric. By constructing a library of typed symbolic *options*—short‑horizon behaviors generated automatically from game source code and validated with feasibility guards—the authors enable each LLM to select actions without fine‑tuning. A per‑agent LoRA adapter trained by PA‑MAGRPO (multi‑agent GRPO) then lifts the frozen policy from zero reward to competent play across three games and four small backbones.

## Key Contributions  
- Symbolic option libraries are automatically synthesized for each game, with feasibility guards derived mechanically from cheap random‑policy burn‑in rollouts.  
- Per‑agent LoRA adapters trained by PA‑MAGRPO enable frozen LLMs to achieve competent play on multiple games and small model sizes.  
- Behavioral audits reveal that reward signals can decouple from cooperation, showing that rising rewards may indicate solo task completion rather than joint action.

## Methodology  
The authors adopt the options/semi‑MD framework extended to multi‑agent Dec‑POMDPs. Each option is a typed, state‑feasible behavior executed by a symbolic planner; feasibility guards are generated automatically using inexpensive random‑policy rollouts that expose repeated failures without logging successes. The frozen LLM serves as its policy over these options, and each agent receives a private LoRA adapter trained via PA‑MAGRPO—a per‑agent variant of multi‑agent GRPO that updates the adapter while keeping the base model unchanged.

## Results  
Across three cooperative games and four small‑backbone LLMs, the PA‑MAGRPO training lifts zero‑reward frozen bases to competent play. Behavioral audits demonstrate a weak correlation between reward curves and cooperation; only when tasks explicitly require joint execution does cooperation emerge. Thus, reward alone is an unreliable readout of cooperative behavior.

## Significance  
This work decouples reward from cooperative behavior in multi‑agent reinforcement learning, showing that behavioral evaluation must accompany RL metrics. It also demonstrates a scalable method for training small LLMs as policy agents using symbolic options and LoRA adapters, offering a path to more interpretable and reliable agent coordination.

## Related Concepts  
Options/semi‑MD, Dec‑POMDPs, LoRA adapters, Multi‑agent GRPO (PA‑MAGRPO), symbolic planning, feasibility guards, reward decoupling.
