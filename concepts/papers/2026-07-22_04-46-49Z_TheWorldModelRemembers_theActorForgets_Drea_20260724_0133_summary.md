# Summary: 2026-07-22_04-46-49Z_TheWorldModelRemembers_theActorForgets_DreamRehear.md
Saved: 2026-07-24 01:33
Source: 2026-07-22_04-46-49Z_TheWorldModelRemembers_theActorForgets_DreamRehear.md
Model: None

---

## Summary  
The paper asks why model‑based reinforcement‑learning agents forget tasks when trained on sequences even though an unbounded replay buffer stores every experience. It discovers that the world model retains all measurable information about past tasks while the actor collapses, revealing forgetting as a communication (channel) problem rather than a memory loss. To remedy this, the authors introduce graded dream rehearsal—a task‑label‑free, parameter‑constant continual learner—that recovers lost skills without any environment interaction.

## Key Contributions  
- [Finding 1] The world model preserves reward discrimination, value estimates, and termination structure across tasks, whereas the actor’s behavior collapses; forgetting originates from a breakdown in communication between components.  
- [Finding 2] Supervised self‑imitation using graded dreams recovers lost skills on all three seeds (3/3), enabling continual learning across four‑task chains without new environment data.  
- [Finding 3] The graded dream step is load‑bearing; two scoring failure modes are identified and mitigated via an offline selection gauge and a realized‑first grading rule.

## Methodology  
The authors employed DreamerV3 agents with an unbounded replay buffer, measuring component‑level performance on three seeds across four‑task chains. They froze the world model to simulate “RL in imagination,” confirming that learning fails without rehearsal. During training they interleaved graded dream rehearsal—supervised imitation of the world model’s own dreams—to train the actor. An offline selection gauge was used to detect scoring failures, and a realized‑first grading rule closed them before contamination occurred.

## Results  
With plain replay, only 0/3 seeds retained information after four tasks; with dream rehearsal, all three seeds retained performance across eight‑task chains. Paired differences over matched real‑episode cloning were +0.13 (bootstrap CI [0.07, 0.24]), showing complete seed separation. The graded dream step is essential for success.

## Significance  
This work provides the first empirical evidence that forgetting in model‑based RL stems from a channel problem rather than memory loss, offering a scalable solution for task‑free continual learning. By enabling agents to learn across many tasks without new environment interactions, it improves continual reinforcement‑learning performance and opens pathways for more robust AI systems.

## Related Concepts  
- Model‑based reinforcement learning (DreamerV3)  
- Continuous reinforcement learning with replay buffers  
- Component‑level probing of world model vs. actor memory  
- Supervised self‑imitation using graded dreams  
- Channel problem versus memory problem in continual learning
