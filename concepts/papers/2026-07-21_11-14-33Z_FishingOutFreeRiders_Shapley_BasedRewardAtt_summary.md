# Summary: 2026-07-21_11-14-33Z_FishingOutFreeRiders_Shapley_BasedRewardAttributio.md
Saved: 2026-07-24 00:44
Source: 2026-07-21_11-14-33Z_FishingOutFreeRiders_Shapley_BasedRewardAttributio.md
Model: None

---

## Summary  
The paper addresses the problem of ambiguous reward attribution in parallel reasoning within large language models, where multiple reasoning paths lead to the same answer yet receive a uniform reward. It proposes Parallel Shapley, a reinforcement‑learning framework that attributes fine‑grained, path‑level contributions using Shapley values. This enables more stable training and interpretable learning signals. The approach effectively “fishes out free riders” by proportionally rewarding useful paths.

## Key Contributions  
- Introduces Parallel Shapley as a Shapley‑based reward attribution method for multi‑path reasoning.  
- Develops a generative reward model to estimate path utilities and approximates marginal contributions via Monte Carlo sampling.  
- Demonstrates that the method yields more stable training, interpretable reward distribution, and improved accuracy over baseline uniform‑reward methods.

## Methodology  
The authors treat each reasoning path as a player in a cooperative game, computing Shapley values to quantify how much removing a particular path would change the final utility. A generative reward model is trained on human judgments of path usefulness, providing estimates of path utilities. During RL training, Monte Carlo sampling approximates the expected marginal contribution for each path, allowing efficient gradient computation without exhaustive enumeration.

## Results  
Experiments on standard mathematical reasoning benchmarks (e.g., MATH, GSM8K) show that Parallel Shapley improves accuracy by 4–7 % over strong baselines while reducing reward variance. The method also yields a more balanced distribution of rewards across paths, indicating fewer “free riders” and higher convergence speed.

## Significance  
By providing interpretable, path‑level reward signals, Parallel Shapley enhances the reliability of RL training for complex reasoning tasks, paving the way toward robust multi‑step LLM applications where diverse strategies are valuable.

## Related Concepts  
- Shapley values  
- Cooperative game theory  
- Reinforcement learning  
- Generative reward models  
- Monte Carlo approximation  
- Parallel reasoning in LLMs  
- Marginal contribution analysis
