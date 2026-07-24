# Summary: 2026-07-22_04-46-49Z_TheWorldModelRemembers_theActorForgets_DreamRehear.md
Saved: 2026-07-24 01:26
Source: 2026-07-22_04-46-49Z_TheWorldModelRemembers_theActorForgets_DreamRehear.md
Model: None

---

## Summary  
The paper investigates why model‑based reinforcement‑learning agents forget when trained on task sequences despite an unbounded replay buffer that preserves every earlier experience. It shows that the world model retains reward discrimination, value estimates and termination structure while the actor collapses, attributing forgetting to a communication (channel) problem rather than a memory issue. The authors introduce graded dream rehearsal—a task‑label‑free, parameter‑constant continual learner—that recovers lost skills through supervised imitation on imagined rollouts without any environment interaction.  

## Key Contributions  
- [Finding 1] Component‑level probes across three seeds reveal that the world model retains essentially all measurable information about old tasks while the actor’s behavior collapses.  
- [Finding 2] Forgetting is a channel problem: the mismatch in how information flows between the frozen world model and the decaying actor causes loss of skill, not a failure to store data.  
- [Finding 3] Interleaved graded dream rehearsal enables task‑label‑free continual learning; it recovers skills on three out of three seeds with zero environment interaction and yields consistent gains over real‑episode cloning (paired difference +0.13, bootstrap CI [0.07, 0.24]).  

## Methodology  
The authors employed component‑level probes to measure retention in a never‑clear replay setting, froze the world model during training, and performed supervised self‑imitation on graded dreams derived from the frozen model. Dream grading was interleaved with RL updates, creating a continual learner that does not require additional environment episodes. Performance was evaluated across four‑task and eight‑task chains, comparing dream rehearsal to plain replay and matched real‑episode cloning baselines.  

## Results  
With only replay, no task chain survived (0/3 seeds). Dream rehearsal recovered three out of three tasks in a four‑task chain and all eight tasks in an eight‑task chain. The improvement over real‑episode cloning was statistically significant: a paired difference of +0.13 with a bootstrap 95 % CI [0.07, 0.24] and complete seed separation across the three seeds.  

## Significance  
This work provides the first empirical evidence that forgetting in model‑based RL is not due to memory loss but to a breakdown in communication between components. By demonstrating graded dream rehearsal as a load‑bearing solution, the paper advances continual reinforcement learning by enabling task‑label‑free skill retention without any further environment interaction, opening new avenues for practical and theoretical research.  

## Related Concepts  
DreamerV3 architecture, component‑level memory (world model vs actor), replay buffer, task chaining, continual reinforcement learning, supervised imitation in imagined rollouts, gradient descent on graded dreams, channel problem, parameter constant continual learner.
