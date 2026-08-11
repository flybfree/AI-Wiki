# Summary: 2026-08-02_18-14-40Z_TrainingSmallLLMsasSpatialMulti_AgentPolicies.md
Saved: 2026-08-04 00:18
Source: 2026-08-02_18-14-40Z_TrainingSmallLLMsasSpatialMulti_AgentPolicies.md
Model: None

---

## Summary  
This paper proposes a framework for training tiny language‑model agents to act as spatial multi‑agent policies in cooperative games, treating the LLM as a policy that selects from a library of symbolic options rather than learning raw actions. By integrating an options/semi‑MDD structure and automatically synthesizing feasibility guards from cheap rollouts, the authors enable frozen LLMs on modest backbones to achieve competent play across three spatial tasks. The approach decouples reward signals from cooperative behavior, showing that high rewards can arise from solitary task completion while true collaboration remains absent. This work advances the field by demonstrating that small LLMs can serve as reliable policy agents when guided by structured symbolic options and automated guard generation.

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 4 title terms overlap; 29 backlinks; 13 summary/topic terms overlap

## Key Contributions  
- [Finding 1] The authors introduce a systematic way to generate symbolically defined, state‑feasible options for spatial games using a frontier coding model, eliminating manual design of action policies.  
- [Finding 2] They develop PA‑MAGRPO, a per‑agent LoRA‑based multi‑agent reinforcement learning variant that fine‑tunes frozen LLMs to select appropriate options and achieve measurable performance gains.  
- [Finding 3] Empirical audits reveal that reward curves do not reliably indicate cooperation; instead, cooperative behavior emerges only when the task architecture forces joint execution.

## Methodology  
The methodology combines symbolic planning with reinforcement learning: first, a coding model parses game source code to produce a set of typed options that are feasible under the current state. Second, feasibility guards—simple heuristics derived from random‑policy burn‑in rollouts—are automatically synthesized to prevent impossible option execution without human intervention. Each agent’s LLM is then fine‑tuned via PA‑MAGRPO, which treats the option selection as a policy gradient problem while preserving the frozen base model. The whole pipeline runs on small backbones (e.g., 7B parameters) and requires no manual tuning of reward shaping.

## Results  
Experiments across three spatial cooperative games show that agents trained with PA‑MAGRPO can complete tasks with success rates up to 85 % compared to near‑zero performance of the frozen baseline. Moreover, behavioral audits demonstrate that when one agent monopolizes the task, its reward climbs sharply while the partner’s activity remains idle—highlighting the decoupling of reward and cooperation. The approach scales to four small backbones without additional engineering effort.

## Significance  
This work proves that even tiny language models can act as reliable policy agents in multi‑agent spatial environments when equipped with a structured options framework, thereby reducing computational cost while preserving performance. It also clarifies the limitations of reward‑centric evaluation, urging researchers to complement quantitative metrics with behavioral audits.

## Related Concepts  
- Options / Semi‑MDD: formalizing short‑horizon behaviors as typed actions.  
- Dec‑PMDPs: multi‑agent extensions for asynchronous option execution.  
- LoRA adapters: low‑rank fine‑tuning of frozen LLMs to inject task‑specific knowledge.  
- Multi‑Agent GRPO (MA‑GRPO): framework for joint policy optimization in cooperative settings.
