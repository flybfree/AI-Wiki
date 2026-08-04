# Summary: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationwithAsymmetricRe.md
Saved: 2026-08-03 23:53
Source: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationwithAsymmetricRe.md
Model: None

---

## Summary  
The paper addresses the challenge of inducing exploration in post‑training large language models (LLMs) that are trained with reinforcement learning (RL), noting that the model’s action space is inherently high‑dimensional and task‑specific. To overcome this, the authors introduce **Instruction‑Conditioned Exploration (ICE)**, which injects a set of diverse instruction prompts into the training data to broaden the behaviours an LLM attempts during RL updates. Their novel contribution is the **Asymmetric‑RL/SD** objective, which combines reinforcement learning with self‑distillation to transfer the knowledge learned under each instruction to a single unconditioned test‑time policy. ICE improves Qwen3‑1.7B’s pass@1 on mathematical reasoning tasks by 5 % at both 4 K and 8 K response lengths, demonstrating that instruction‑guided exploration can be effectively distilled into a general policy.

## Key Contributions  
- **Instruction‑Conditioned Exploration (ICE)**: A framework that conditions RL training on multiple distinct prompts to increase behavioural diversity.  
- **Asymmetric‑RL/SD Objective**: An asymmetric reinforcement learning loss paired with self‑distillation that transfers explored, instruction‑specific behaviours into a single unconditioned policy.  
- **Empirical Improvement**: ICE yields a 5 % absolute gain in pass@1 on Qwen3‑1.7B’s mathematical reasoning benchmarks across both 4 K and 8 K contexts.

## Methodology  
The authors first curate a set of instruction prompts that each steer the LLM toward different problem classes (e.g., arithmetic, algebra, word problems). During RL training, these prompts are appended to the task description, effectively conditioning the agent’s actions. The Asymmetric‑RL loss is defined such that the reward for an action under one instruction does not directly penalize actions from another, preserving exploration across instructions. Self‑distillation is performed by having the model generate a distilled policy that mimics the best‑performing instruction‑conditioned behaviour while being evaluated on a common test set without conditioning. The combined objective thus balances learning from diverse experiences with knowledge transfer.

## Results  
On the held‑out Qwen3‑1.7B dataset, ICE trained with Asymmetric‑RL/SD achieved a 5 % absolute increase in pass@1 compared to DAPO (the baseline). This benefit was observed at both short (4 K) and long (8 K) response lengths, indicating robustness across varying context windows. The distilled policy also outperformed the original instruction‑conditioned model on downstream reasoning tasks, confirming effective knowledge transfer.

## Significance  
The work demonstrates that conditioning exploration in RL with LLMs can be systematically managed through prompts, leading to measurable gains in task performance without sacrificing generalisation. By integrating self‑distillation, it reduces the need for multiple fine‑tuned policies, offering a scalable path toward more efficient and adaptable AI agents.

## Related Concepts  
- Reinforcement Learning (RL)  
- Self‑Distillation  
- Instruction Tuning  
- Action Space Conditioning  
- Qwen3‑1.7B
