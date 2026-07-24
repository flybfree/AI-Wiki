# Summary: 2026-07-21_11-14-33Z_FishingOutFreeRiders_Shapley_BasedRewardAttributio.md
Saved: 2026-07-24 01:04
Source: 2026-07-21_11-14-33Z_FishingOutFreeRiders_Shapley_BasedRewardAttributio.md
Model: None

---

## Summary  
The paper addresses the challenge of attributing contributions in parallel reasoning for large language models, where uniform rewards create ambiguous learning signals and unstable training. It proposes Parallel Shapley, a reinforcement‑learning framework that quantifies marginal contributions of each reasoning path using Shapley values. By treating paths as players in a cooperative game, the method yields fine‑grained, interpretable reward signals that “fish out free riders.” The approach improves training stability and model performance on multi‑step reasoning tasks.

## Key Contributions  
- Introduces Parallel Shapley, a reinforcement‑learning framework that attributes path‑level contributions using Shapley values.  
- Develops a generative reward model together with Monte Carlo sampling to approximate marginal utilities efficiently.  
- Demonstrates improved accuracy and more stable training on mathematical reasoning benchmarks compared to existing baselines.

## Methodology  
The authors model each reasoning path as a player in a cooperative game whose total utility is the final answer. They compute Shapley values by iteratively calculating the marginal contribution of removing each path, using a generative reward model to estimate utilities. Monte Carlo sampling approximates these computations for scalability. The reinforcement‑learning agent receives rewards proportional to its contribution, encouraging non‑redundant and beneficial paths while penalizing free riders.

## Results  
Experiments on standard math reasoning datasets such as MATH and GSM8K show that Parallel Shapley yields higher accuracy than baseline methods like REINFORCE and PPO. Training exhibits lower loss variance and greater stability, and the framework provides interpretable attribution scores for each path, enabling diagnostic analysis.

## Significance  
By offering a principled way to allocate rewards based on marginal contributions, the method mitigates the pitfalls of uniform reward assignment in parallel reasoning. This leads to better model generalization, more reliable training dynamics, and clearer insights into which paths are truly useful—critical considerations as LLMs scale.

## Related Concepts  
- Reinforcement Learning (RL)  
- Shapley values (cooperative game theory)  
- Generative reward models  
- Monte Carlo approximation  
- Multi‑path reasoning in LLMs
