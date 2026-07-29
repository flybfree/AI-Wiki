# Summary: 2026-07-28_08-10-25Z_AControlSystem_aDataset_andaRecipeforMakingFrozenL.md
Saved: 2026-07-28 20:21
Source: 2026-07-28_08-10-25Z_AControlSystem_aDataset_andaRecipeforMakingFrozenL.md
Model: None

---

## Summary  
The paper proposes a framework for training frozen LLM agents to acquire new domain capabilities by optimizing the small, human‑legible harness that wraps them—a prompt template, tool set, memory layer, planning strategy, and verification policy. It introduces an ε‑greedy contextual bandit combined with REINFORCE as a sample‑efficient reinforcement‑learning control system that scores actions on a multi‑objective reward (task success, verifier score, compliance, cost, latency, unsupported‑claim penalty). The authors evaluate this approach across three verifiable domains and two model providers, releasing the harness‑control code, task suite, training logs, and a deployment recipe.  

## Key Contributions  
- Introduces a sample‑efficient reinforcement‑learning control system for optimizing LLM harnesses without black‑box code changes.  
- Provides a cross‑domain verifiable task suite with detailed reward decomposition to assess each objective.  
- Releases an open‑source deployment recipe that enables organization‑specific domain adaptation of frozen LLMs.  

## Methodology  
The authors treat the harness as a discrete action space and use an ε‑greedy contextual bandit to select actions, updating a policy via REINFORCE. The reward function is multi‑objective: it rewards task success, verifier score, policy compliance, operational cost, latency, and penalizes unsupported claims. Training proceeds by generating trajectories from the DSPy bootstrap few‑shot prompt baseline, collecting per‑step logs that decompose the total reward into its constituent components.  

## Results  
Compared with static DSPy prompts, the RL‑optimized harness achieves higher task success rates on tool‑use workflows (≈ 12 % absolute gain), stronger HumanEval scores (≈ 8 % improvement), and better HotpotQA performance (≈ 5 % boost). Latency drops by 30 % on average, and compliance violations fall from 7 % to 2 %. Reward decomposition shows that task success contributes ~45 % of total reward, while latency and compliance each contribute ~15 %, with cost and unsupported‑claim penalties balancing the remaining share.  

## Significance  
This work demonstrates that frozen LLMs can be safely and audibly adapted to new domains through a transparent reinforcement‑learning loop, moving beyond opaque self‑modifying code. By releasing reproducible data and code, it lowers barriers for organizations to embed domain‑specific verification policies into LLM agents without sacrificing safety or interpretability.  

## Related Concepts  
- Frozen LLMs (static model weights)  
- Harness (prompt template + tool set + memory + planning + verification)  
- Reinforcement learning, contextual bandit, REINFORCE policy gradient  
- Multi‑objective reward design  
- DSPy (dynamic prompt system)  
- Verification policy and compliance checking
