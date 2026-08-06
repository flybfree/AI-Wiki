# Summary: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationforReinforcement.md
Saved: 2026-08-05 20:17
Source: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationforReinforcement.md
Model: None

---

## Summary  
The paper tackles the challenge of inducing exploration in reinforcement‑learning (RL) training when the action space is a large language model’s output rather than a discrete set. By appending a small, fixed set of instructions to task prompts during training and then self‑distilling the conditional rollouts into an unconditioned test‑time policy, the authors propose **Instruction‑Conditioned Exploration (ICE)**. This approach expands the behavioural coverage of pre‑trained LLMs such as Qwen3, leading to measurable gains in downstream reasoning tasks without altering the base model’s knowledge.

## Key Contributions  
- [Finding 1] ICE appends a small fixed set of instructions to every task prompt during training, thereby forcing the policy to explore a broader set of behaviours.  
- [Finding 2] The authors combine RL with self‑distillation: rollouts conditioned on the instruction set are distilled into an unconditioned test‑time policy that can be evaluated without the prompts.  
- [Finding 3] Empirically, ICE improves Qwen3‑1.7B’s pass@1 performance by 5 % at a 4K response length on mathematical reasoning tasks and this benefit persists up to an 8K context window.

## Methodology  
The methodology builds on the existing DAPO (Deterministic Approximate Policy Optimization) framework but replaces its deterministic rollout with stochastic instruction‑conditioned sampling. A small inventory of instructions—e.g., “solve the problem step by step,” “provide a concise answer,” etc.—is appended uniformly to each training prompt, ensuring that the policy is conditioned on these prompts throughout learning. The conditional policy is trained via RL, and its correct rollouts are distilled into an unconditioned version using standard self‑distillation techniques (e.g., minimizing KL divergence between the conditional and unconditional policies). This dual‑policy setup allows the model to generate diverse experiences during training while still delivering a clean, instruction‑free output at inference.

## Results  
The main experimental results show that for Qwen3‑1.7B, ICE yields a 5 % absolute increase in pass@1 on held‑out mathematical reasoning benchmarks when responses are limited to 4K tokens, and the improvement remains stable up to an 8K context length. In contrast, the same instruction set does not expand the coverage of Qwen3‑4B at 4K; thus, the benefit is model‑size dependent. The unconditioned distilled policy maintains comparable performance across both lengths, confirming that self‑distillation successfully removes instruction leakage.

## Significance  
ICE demonstrates a practical way to harness LLMs’ intrinsic exploration capabilities during RL training, addressing a longstanding limitation: the inability of large models to generate diverse experiences without external prompts. By integrating instruction conditioning with self‑distillation, the method enables smaller models (e.g., Qwen3‑1.7B) to achieve higher reasoning performance while preserving an unconditioned output at test time—a crucial requirement for real‑world deployment.

## Related Concepts  
- Reinforcement Learning (RL)  
- Large Language Models (LLMs) and their action‑space challenges  
- Exploration in RL with continuous or high‑dimensional outputs  
- Self‑distillation of policies to remove conditioning information  
- Instruction‑conditioned prompting for task adaptation
