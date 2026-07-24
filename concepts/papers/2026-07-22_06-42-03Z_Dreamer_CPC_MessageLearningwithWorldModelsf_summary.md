# Summary: 2026-07-22_06-42-03Z_Dreamer_CPC_MessageLearningwithWorldModelsforDecen.md
Saved: 2026-07-24 01:31
Source: 2026-07-22_06-42-03Z_Dreamer_CPC_MessageLearningwithWorldModelsforDecen.md
Model: None

---

## Summary  
The paper proposes Dreamer‑CPC, a decentralized model‑based multi‑agent reinforcement learning method that learns messages from latent world models rather than current observations, enabling coordination when information is missing. It integrates Collective Predictive Coding (CPC) into the DreamerV3 architecture to generate and exchange historical state messages. The approach addresses partial observability by leveraging accumulated history within each agent’s world model. Experiments show superior performance over IPPO‑CPC and no‑communication baselines.  

## Key Contributions  
- Finding 1: Dreamer‑CPC learns messages from latent states of its own world model, capturing temporal information absent in current observations.  
- Finding 2: The method outperforms existing CPC‑based decentralized MARL methods (IPPO‑CPC) by up to 5× episode return in the CatchApple environment.  
- Finding 3: Communication grounded in world‑model dynamics enables coordination where other approaches fail due to missing observations.  

## Methodology  
Each agent maintains a personalized world model and a message module. The world model predicts future states from past observations and actions, producing latent state representations. A CPC‑inspired decoder infers messages from these latent states, which are then exchanged between agents. This decouples communication from immediate sensory input, allowing the system to reason about history.  

## Results  
In Observer (a non‑cooperative information‑sharing task) Dreamer‑CPC matches IPPO‑CPC performance. In CatchApple, a newly introduced task where observations are temporarily missing, Dreamer‑CPC achieves 4–5 times higher episode return than IPPO‑CPC and a no‑communication baseline, demonstrating effective coordination.  

## Significance  
This work demonstrates that message learning from world‑model latent dynamics can enhance decentralized decision‑making under partial observability, offering a scalable alternative to communication schemes reliant solely on current observations. It provides theoretical insight into how predictive coding can be applied to MARL.  

## Related Concepts  
Decentralized multi‑agent reinforcement learning; World models; Predictive coding; Collective predictive coding (CPC); DreamerV3 architecture; Partial observability; Message learning; Latent state representation.
