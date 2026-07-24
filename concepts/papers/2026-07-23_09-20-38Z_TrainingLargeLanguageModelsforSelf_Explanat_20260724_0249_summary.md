# Summary: 2026-07-23_09-20-38Z_TrainingLargeLanguageModelsforSelf_ExplanationFait.md
Saved: 2026-07-24 02:49
Source: 2026-07-23_09-20-38Z_TrainingLargeLanguageModelsforSelf_ExplanationFait.md
Model: None

---

## Summary  
The paper introduces a reinforcement‑learning (RL) framework that directly optimizes the faithfulness of an LLM’s self‑explanations by turning faithfulness metrics into a per‑sample reward. It asks whether models can learn to identify influential factors in their reasoning and then disclose those factors, using two interventions—random‑word insertions and user‑bias phrases—as training signals. Experiments with fine‑tuned Llama3.1‑8B and Qwen3‑8B show that RL can raise Phi‑CCT scores from near zero to as high as 0.691 on held‑out tasks, indicating a scalable path toward more faithful reasoning.

## Key Contributions  
- **Direct RL optimization of faithfulness**: The authors convert existing faithfulness metrics into an RL reward function, enabling parameter updates that directly improve the model’s ability to generate faithful self‑explanations.  
- **Models can detect influential factors**: Experiments demonstrate that fine‑tuned LLMs learn to recognize which inserted words or biases are most relevant to their decisions, thereby exposing those factors in the output.  
- **Intervention‑driven improvement**: Random‑word and user‑bias insertions as interventions raise in‑distribution Phi‑CCT scores up to 0.664 and out‑of‑distribution scores up to 0.691 on StrategyQA, showing measurable gains.

## Methodology  
The authors modify the faithfulness metric (Phi‑CCT) into a per‑sample reward that RL can maximize. They insert either random words or user‑bias phrases at inference time, compute the Phi‑CCT correlation for each sample, and use this as the reward signal. Fine‑tuning proceeds with an RL algorithm (likely PPO) on Llama3.1‑8B and Qwen3‑8B, evaluating both interventions separately and then testing cross‑intervention generalization.

## Results  
In‑distribution Phi‑CCT scores for Llama3.1‑8B rise from near zero to 0.664 after RL fine‑tuning, while out‑of‑distribution scores on StrategyQA reach 0.691. Cross‑intervention generalization is modest: the model trained only with random‑word insertions shows non‑zero transfer to user‑bias phrases, whereas Qwen3‑8B does not replicate this effect. No reward gaming was observed; improvements are genuine.

## Significance  
By aligning LLM generation with its internal decision factors through RL, the work offers a scalable mechanism to reduce unfaithful reasoning, improving both safety and interpretability of large language models without requiring extensive human annotation or complex prompting frameworks.

## Related Concepts  
- Reinforcement Learning for language model fine‑tuning (RL fine‑tuning)  
- Self‑explanation in LLMs  
- Faithfulness metrics such as Phi‑CCT  
- Intervention‑based training strategies  
- Reward shaping and RL reward design
