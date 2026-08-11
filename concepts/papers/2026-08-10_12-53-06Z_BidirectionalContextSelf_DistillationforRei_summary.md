# Summary: 2026-08-10_12-53-06Z_BidirectionalContextSelf_DistillationforReinforcem.md
Saved: 2026-08-10 23:49
Source: 2026-08-10_12-53-06Z_BidirectionalContextSelf_DistillationforReinforcem.md
Model: None

---

## Summary  
The paper addresses the challenge of enabling large language model (LLM) agents to translate external natural‑language skills into effective actions, a capability that is currently limited by reinforcement learning (RL) training that focuses only on task‑level rewards. To overcome this gap, the authors introduce BCSD—Bidirectional Context Self‑Distillation—a framework that merges self‑distillation with RL to improve skill utilization. Unlike prior methods that use a single privileged context, BCSD evaluates each trajectory from two complementary views: an augmented view that adds higher‑level Meta‑Skill guidance and a reduced view that prunes general guidance for task specificity. By combining these token‑level signals they rescale the RL advantage, yielding agents that better exploit provided skills.

## Key Contributions  
- [Finding 1] BCSD introduces a bidirectional context self‑distillation mechanism that simultaneously processes an augmented (Meta‑Skill) and reduced view of external skill guidance.  
- [Finding 2] The framework rescales the RL advantage using complementary token‑level signals, improving the policy’s sensitivity to subtle differences in skill usage.  
- [Finding 3] Empirical experiments on ALFWorld and WebShop show BCSD outperforms baseline methods across all model scales.

## Methodology  
BCSD builds upon standard self‑distillation by training a policy to predict its own outputs from two distinct context representations of the same skill. The augmented view injects higher‑level Meta‑Skill tokens that provide overarching guidance, while the reduced view strips away non‑essential information, yielding task‑specific tokens. During RL, the advantage signal is linearly combined from both views, allowing the model to learn a balanced representation that captures both macro and micro skill cues.

## Results  
Across multiple LLM scales (from 7B to 130B parameters), BCSD achieves the highest cumulative reward on ALFWorld (≈ 2.8 points higher than the best prior) and surpasses all baselines on WebShop (≈ 1.9 points advantage). Ablation experiments confirm that removing either the augmented or reduced view reduces performance, confirming their complementary roles.

## Significance  
By integrating self‑distillation with RL and leveraging dual context views, BCSD tackles a longstanding limitation in skill‑based LLM agents: the inability to learn how effectively they translate external guidance into actions. This work opens a path toward more adaptable, reusable skills that can be fine‑tuned without retraining the entire model.

## Related Concepts  
- Self‑distillation  
- Reinforcement learning (RL) for LLMs  
- External natural‑language skill prompts  
- Meta‑skill guidance  
- Token‑level signal rescaling
