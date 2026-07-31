# Summary: 2026-07-29_19-31-50Z_BridgingInference_TimeScalingandEpisodicMemorywith.md
Saved: 2026-07-30 20:22
Source: 2026-07-29_19-31-50Z_BridgingInference_TimeScalingandEpisodicMemorywith.md
Model: None

---

## Summary  
The paper addresses a key limitation of current Large Language Model‑based agents: inference‑time scaling is powerful but suffers from stateless operation and redundant searches, while episodic memory mechanisms are costly because they rely on the model’s reasoning capacity. To bridge this gap, the authors introduce GAMER (Graph‑based Action‑centric Memory with Episodic Reasoning), a framework that models historical reasoning as a dynamic action‑centric graph. By decoupling the memory mechanism from LLMs and providing only a reduced context window, GAMER saves token/money usage compared to baseline memory mechanisms. The system also learns a dual‑stream Temporal Difference value function that distinguishes positive (suggested) actions from negative (risky) actions.

## Key Contributions  
- Proposes the GAMER framework that integrates inference‑time scaling with episodic memory via Action‑Centric Graphs.  
- Decouples the memory mechanism from LLMs, enabling a smaller context window and thus lower token/money consumption than existing baselines.  
- Introduces a dual‑stream Temporal Difference learning mechanism to estimate positive (suggestion) and negative (avoidance) values for each action node.

## Methodology  
The authors treat the agent’s past reasoning history as a graph whose nodes represent actions taken at specific times. A dual‑stream Temporal Difference algorithm trains two value estimators: one that rewards successful actions (positive) and another that penalizes failures (negative). During inference, these learned values are consulted to prioritize high‑value actions and avoid risky ones, allowing the system to perform an efficient search over the graph rather than exploring the full state space. This decoupling reduces the amount of context fed to the LLM while still providing rich episodic memory.

## Results  
Experiments on multiple benchmark tasks show that GAMER improves success rate by 20.81 % and progress rate by 6.17 % compared with vanilla baselines, demonstrating both higher performance and lower computational cost.

## Significance  
This work matters because it tackles the inefficiencies of current LLM‑driven agents: inference scaling is limited by statelessness, and memory mechanisms are computationally expensive. By offering a scalable, low‑cost episodic memory that operates independently from the model’s reasoning capacity, GAMER enables real‑world deployment where token budgets and energy consumption are critical.

## Related Concepts  
inference‑time scaling, episodic memory, action‑centric graphs, dual‑stream Temporal Difference learning, value function optimization, token/money usage reduction, graph search.
