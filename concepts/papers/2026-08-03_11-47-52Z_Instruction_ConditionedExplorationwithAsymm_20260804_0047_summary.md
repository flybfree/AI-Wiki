# Summary: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationwithAsymmetricRe.md
Saved: 2026-08-04 00:47
Source: 2026-08-03_11-47-52Z_Instruction_ConditionedExplorationwithAsymmetricRe.md
Model: None

---

## Summary  
The paper tackles the challenge of inducing exploration in post‑trained large language models (LLMs) during reinforcement learning, where the high‑dimensional action space is limited by prompt constraints. It introduces Instruction‑Conditioned Exploration (ICE), which injects a variety of instruction prompts at training time to broaden behavioural coverage, and pairs it with an Asymmetric‑RL/SD objective that self‑distills learned experiences into an unconditioned test‑time policy. The combined method improves quantitative performance on mathematical reasoning tasks for Qwen3-1.7B by 5 % relative to the DAPO baseline and retains this gain up to an 8K response length, demonstrating a robust trade‑off between exploration and task accuracy.

## Key Contributions  
- ICE injects multiple instruction prompts during training to systematically explore diverse behaviours.  
- Asymmetric‑RL/SD objective transfers learned experiences from conditioned to unconditioned test‑time policy via self‑distillation.  
- The combined approach yields a 5 % absolute improvement in pass@1 on Qwen3-1.7B at both 4K and 8K response lengths compared with DAPO.

## Methodology  
Authors augment each training step with one of several instruction conditions, prompting the model to perform distinct tasks or reasoning styles. The Asymmetric‑RL/SD objective comprises two components: (i) standard RL reward maximization conditioned on the prompt, and (ii) a self‑distillation loss that aligns the unconditioned policy’s output distribution with the conditional one. Training proceeds iteratively, balancing exploration across instructions while preserving performance.

## Results  
Experiments show that ICE + Asymmetric‑RL/SD improves Qwen3-1.7B pass@1 by 5 % at a 4K context and maintains this gain up to an 8K context, outperforming the DAPO baseline. Ablation studies confirm that instruction diversity is essential for exploration breadth, while distillation transfer is crucial for transferring those behaviours to test‑time.

## Significance  
This work provides a scalable framework for enhancing LLM capabilities via reinforcement learning without catastrophic forgetting, enabling more robust and diverse task execution in downstream applications such as automated reasoning or code generation. The approach bridges RL and language modeling, offering a systematic way to broaden behavioural coverage while preserving factual accuracy.

## Related Concepts  
Reinforcement Learning, Self‑Distillation, Instruction Tuning, Action Space Exploration, Qwen3-1.7B, DAPO, Pass@1 metric
