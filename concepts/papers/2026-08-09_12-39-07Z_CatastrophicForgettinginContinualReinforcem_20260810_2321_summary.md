# Summary: 2026-08-09_12-39-07Z_CatastrophicForgettinginContinualReinforcementLear.md
Saved: 2026-08-10 23:21
Source: 2026-08-09_12-39-07Z_CatastrophicForgettinginContinualReinforcementLear.md
Model: None

---

## Summary  
This paper investigates how task similarity influences catastrophic forgetting in continual reinforcement learning (RL). By applying interpretable Q‑learning on graph‑based tasks that aim to minimise the number of steps to reach a goal, the authors examine performance degradation on previously learned tasks after training on new ones. Their main contribution is to reveal a complex, non‑linear relationship between task similarity and forgetting severity, which varies with both similarity levels and task complexity. The study also highlights high variability in forgetting outcomes and an uneven distribution of similarity measures, suggesting that these factors interact in ways that are not yet fully understood.

## Key Contributions  
- Demonstrated that task similarity does **not** have a statistically significant independent effect on catastrophic forgetting in continual RL.  
- Observed complex, fluctuating patterns in forgetting severity as a function of both task complexity and similarity, indicating an interdependence between these variables.  
- Highlighted the high variability and uneven distribution of similarity measures across experiments, underscoring the need for more robust similarity definitions.

## Methodology  
The authors employed interpretable reinforcement learning—specifically Q‑learning—on graph‑structured tasks where the objective is to minimise the number of steps required to reach a goal. They trained the agent on a sequence of tasks, each with varying relative levels of complexity and similarity to previously learned tasks. After training on a new task, they measured performance on all earlier tasks to quantify forgetting. The experiments systematically varied both similarity (e.g., graph isomorphism metrics) and complexity (e.g., number of nodes or edge types), allowing them to explore the joint influence on forgetting.

## Results  
The experimental results reveal a complex dynamic: as task similarity increases, forgetting does not consistently worsen; instead, it fluctuates dramatically. Moreover, high task complexity amplifies these fluctuations, producing both severe and mild degradation across the same similarity level. The data show pronounced variability in forgetting scores and an uneven distribution of similarity values, with no clear statistical evidence that similarity alone drives forgetting. These findings suggest that the interplay between similarity and complexity is crucial for understanding continual learning stability.

## Significance  
Understanding this interplay matters because continual RL systems must balance learning new tasks while preserving old ones; misestimating how similarity affects forgetting can lead to unreliable performance across diverse environments. The paper contributes a nuanced view of forgetting in graph‑based RL, guiding future work on robust similarity metrics and adaptive training schedules.

## Related Concepts  
- Catastrophic forgetting: loss of ability to perform previously learned tasks.  
- Continual reinforcement learning: learning sequentially without catastrophic forgetting.  
- Q‑learning: a model‑free, interpretable RL algorithm.  
- Graph‑based tasks: environments represented as graphs where actions correspond to traversing edges or nodes.  
- Task similarity: quantitative measure of how alike two tasks are (e.g., graph isomorphism).  
- Complexity: characteristics such as number of nodes or edge types that affect learning difficulty.
