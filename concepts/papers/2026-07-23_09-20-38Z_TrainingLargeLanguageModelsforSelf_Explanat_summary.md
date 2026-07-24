# Summary: 2026-07-23_09-20-38Z_TrainingLargeLanguageModelsforSelf_ExplanationFait.md
Saved: 2026-07-24 02:35
Source: 2026-07-23_09-20-38Z_TrainingLargeLanguageModelsforSelf_ExplanationFait.md
Model: None

---

## Summary  
The paper proposes a reinforcement‑learning (RL) framework that directly optimizes the faithfulness of large language model self‑explanations, i.e., how well the generated reasoning mirrors the model’s internal decision process. By converting existing faithfulness metrics into per‑sample rewards, the authors train models to explicitly disclose influential factors during generation. Experiments with Llama3.1‑8B and Qwen3‑8B show that RL can lift Phi‑CCT scores from near zero to over 0.6 in both in‑distribution and out‑of‑distribution settings. The study also reveals model‑dependent cross‑intervention generalization, suggesting that the learned mechanisms are not purely task‑specific.  

## Key Contributions  
- [Finding 1] Models can be trained via RL to detect factors that affect their decisions, using a per‑sample reward derived from the Phi‑CCT correlation metric.  
- [Finding 2] RL fine‑tuning of Llama3.1‑8B and Qwen3‑8B significantly improves Phi‑CCT faithfulness scores, reaching up to 0.691 on held‑out tasks such as StrategyQA.  
- [Finding 3] Cross‑intervention generalization is observed only for Llama3.1‑8B (random‑word → user‑bias transfer), indicating model‑specific and setup‑dependent effects that are not fully explained.  

## Methodology  
The authors modify faithfulness metrics into an RL training objective, creating a reward function based on the Phi‑CCT correlation between generated explanations and underlying decision factors. Two intervention types are employed: random‑word insertions (to probe model’s attention to filler content) and user‑bias phrases (to test bias disclosure). For each sample, the reward is computed as the Phi‑CCT score of the explanation, which quantifies how closely the reasoning aligns with the true factors. The RL fine‑tuning process then optimizes for higher rewards, encouraging the model to produce explanations that faithfully expose these factors.  

## Results  
In‑distribution tasks saw Phi‑CCT scores rise from near zero to 0.664 after RL fine‑tuning of Llama3.1‑8B, while out‑of‑distribution StrategyQA reached 0.691 for Qwen3‑8B. Cross‑intervention analysis revealed weak but non‑zero transfer from random‑word insertions to user‑bias phrases only in the Llama model; the reverse direction and Qwen’s performance did not replicate this behavior, highlighting model‑dependent effects. Additionally, no reward gaming was observed, confirming that the RL objective directly reflects faithfulness rather than manipulation of the metric.  

## Significance  
This work provides a scalable pathway to reduce unfaithful reasoning in LLMs by training models to explicitly disclose decision factors through reinforcement learning, moving beyond evaluation‑only approaches toward parameter‑level optimization for more trustworthy self‑explanations.  

## Related Concepts  
- Reinforcement Learning for LLM fine‑tuning  
- Self‑explanation generation  
- Faithfulness metrics (Phi‑CCT)  
- Per‑sample reward design in RL  
- Cross‑intervention generalization
