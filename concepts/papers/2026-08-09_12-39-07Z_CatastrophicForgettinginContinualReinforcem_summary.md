# Summary: 2026-08-09_12-39-07Z_CatastrophicForgettinginContinualReinforcementLear.md
Saved: 2026-08-10 23:20
Source: 2026-08-09_12-39-07Z_CatastrophicForgettinginContinualReinforcementLear.md
Model: None

---

## Summary  
This paper investigates how task similarity influences catastrophic forgetting in continual reinforcement learning (CRL). Using interpretable Q‑learning on graph‑based tasks that aim to minimise the number of steps to reach a goal, the authors compare performance on previously learned tasks after training new ones with varying levels of complexity and similarity. Their experiments reveal that the relationship between task similarity and forgetting is not straightforward; instead, it exhibits complex fluctuations and high variability across different configurations.

## Key Contributions  
- [Finding 1] Task similarity does not have a statistically significant independent effect on catastrophic forgetting in CRL, suggesting that other factors dominate the forgetting dynamics.  
- [Finding 2] Complexity of tasks strongly predicts forgetting severity, even when task similarity is held constant, indicating that harder problems are more prone to erasing prior knowledge.  
- [Finding 3] The observed forgetting rates vary widely and are distributed unevenly across similarity measures, highlighting the lack of a uniform mapping between similarity and performance loss.

## Methodology  
The authors employ Q‑learning—a model‑free, interpretable reinforcement learning algorithm—to solve graph‑based navigation tasks where the objective is to reach a goal state in as few steps as possible. They train a policy on a new task and then evaluate its ability to retain performance on a previously learned task. The experiments systematically vary two dimensions: (i) the relative complexity of the tasks, measured by the number of nodes or edge types required for navigation, and (ii) the similarity between tasks, quantified using graph isomorphism metrics. By comparing step counts before and after training, they quantify catastrophic forgetting.

## Results  
The results show a non‑linear interaction: when task similarity is high but complexity is low, forgetting remains modest; however, when both similarity and complexity are high, forgetting spikes dramatically. Statistical tests fail to isolate similarity as the sole driver, confirming that complexity alone can cause significant performance degradation. Moreover, the forgetting percentages exhibit high inter‑experiment variability and an uneven spread across the similarity spectrum, suggesting that similarity measures may be poorly calibrated for this domain.

## Significance  
Understanding these dynamics is crucial because continual RL systems must balance learning new tasks without erasing valuable prior knowledge. By revealing that complexity often outweighs similarity in driving forgetting, the study guides designers toward task ordering strategies and regularisation techniques tailored to high‑complexity environments, ultimately improving long‑term retention.

## Related Concepts  
- Catastrophic Forgetting: loss of previously acquired skills during continual learning.  
- Continual Reinforcement Learning (CRL): training agents on a stream of tasks without catastrophic forgetting.  
- Q‑Learning: model‑free reinforcement learning that updates value estimates iteratively.  
- Graph‑Based RL: problems defined on graph structures where actions correspond to traversing edges or nodes.  
- Task Similarity Measures: metrics such as graph isomorphism distance used to quantify how alike two tasks are.
