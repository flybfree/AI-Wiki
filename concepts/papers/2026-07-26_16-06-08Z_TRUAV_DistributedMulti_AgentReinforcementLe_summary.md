# Summary: 2026-07-26_16-06-08Z_TRUAV_DistributedMulti_AgentReinforcementLearningf.md
Saved: 2026-07-27 21:29
Source: 2026-07-26_16-06-08Z_TRUAV_DistributedMulti_AgentReinforcementLearningf.md
Model: None

---

## Summary  
The paper introduces TRUAV, a distributed multi‑agent reinforcement learning (D‑MARL) framework that jointly plans UAV trajectories and enhances routing in UAV‑aided IoT‑enabled vehicular ad‑hoc networks. By replacing centralized state aggregation with independent local Q‑learning agents, the system operates under bandwidth and energy constraints typical of dense urban deployments. The approach leverages a potential‑game‑inspired reward to promote spatial diversity among agents while accounting for energy consumption. Numerical experiments on a simulated 200‑vehicle urban environment demonstrate that TRUAV achieves network coverage and packet delivery ratios comparable to centralized deep RL methods, with lower relay delay and improved energy efficiency.

## Key Contributions  
- [Finding 1] A fully distributed D‑MARL algorithm based on independent tabular Q‑learning eliminates the need for global state exchange.  
- [Finding 2] The potential‑game‑inspired reward design simultaneously optimizes spatial diversity, routing awareness, and energy consumption among UAV agents.  
- [Finding 3] Simulations show that TRUAV attains network coverage and packet delivery ratios comparable to centralized deep RL while reducing relay delay and improving energy efficiency.

## Methodology  
Each UAV runs a local Q‑learning agent that observes only locally available information: vehicle density, its own packet queue state, and the positions of neighboring UAVs. The reward function is derived from a potential game, encouraging agents to spread out spatially, avoid congestion, and minimize energy use. The system thus forms an equilibrium where each agent’s trajectory contributes to overall network performance without central coordination.

## Results  
In the large‑scale urban simulation with 200 mobile vehicles, TRUAV achieved a network coverage ratio of 96 % and a packet delivery success rate of 94 %, matching the performance of centralized deep reinforcement learning baselines. Relay delay was reduced by an average of 18 % compared to centralized methods, and total UAV energy consumption dropped by roughly 22 %. These results confirm that distributed Q‑learning can rival or surpass centralized approaches under realistic constraints.

## Significance  
TRUAV addresses a critical bottleneck in smart‑city IoT deployments: the impracticality of centralized trajectory planning due to bandwidth and energy limits. By enabling scalable, low‑latency routing with minimal communication overhead, TRUAV paves the way for reliable UAV‑assisted VANETs that support real‑time applications such as autonomous navigation and edge computing.

## Related Concepts  
- Distributed Multi-Agent Reinforcement Learning (D‑MARL)  
- Tabular Q‑learning  
- Potential game reward design  
- UAV‑aided IoT networks  
- Vehicular Ad Hoc Networks (VANETs)  
- Energy‑aware reinforcement learning
