# Summary: 2026-08-05_19-06-42Z_Multi_AgentReinforcementLearningforOnlineTrafficSc.md
Saved: 2026-08-06 20:26
Source: 2026-08-05_19-06-42Z_Multi_AgentReinforcementLearningforOnlineTrafficSc.md
Model: None

---

## Summary  
The paper addresses the need for adaptive scheduling in time‑sensitive networking (TSN) within mobile edge computing (MEC) to support latency‑critical extended reality (XR) applications. It proposes a decentralized multi‑agent reinforcement learning framework where each TSN queue is modeled as an autonomous agent that can coordinate with others. The Heterogeneous‑Agent Proximal Policy Optimization (HAPPO) algorithm explicitly captures inter‑queue dependencies and jointly optimizes service delivery across all queues. Simulation results show the approach reduces average frame waiting times by up to 26.8% and worst‑case delays by about 16.8%, outperforming static or centralized methods.

## Key Contributions  
- Adaptive decentralized MARL framework for TSN scheduling that models each queue as an autonomous agent.  
- HAPPO algorithm explicitly captures heterogeneous inter‑agent dependencies and jointly optimizes service delivery.  
- Demonstrated up to 26.8% reduction in average frame waiting time and 16.8% improvement in worst‑case delay in simulated XR‑driven MEC environments.

## Methodology  
The authors model the TSN queueing system as a set of interacting agents, each representing a network buffer with its own service policy. They employ HAPPO, an extension of Proximal Policy Optimization (PPO) that incorporates heterogeneous agent states and inter‑agent communication to enforce dependency constraints. The algorithm updates policies locally while coordinating through shared information about traffic load and queue depth, enabling decentralized yet coordinated optimization.

## Results  
Simulations conducted on a variety of XR traffic scenarios with dynamic arrival rates and bursty bursts show significant gains compared to baseline static schedulers and centralized RL models. The proposed HAPPO‑based MARL reduces average frame waiting time by up to 26.8% and worst‑case delay by approximately 16.8%, outperforming the best existing approaches.

## Significance  
This work bridges the gap between theoretical TSN scheduling and real‑world dynamic MEC environments, offering a scalable solution for latency‑sensitive XR applications. By enabling decentralized coordination without sacrificing performance, it supports future edge computing infrastructures where centralized control is impractical.

## Related Concepts  
- Time‑Sensitive Networking (TSN)  
- Mobile Edge Computing (MEC)  
- Multi‑Agent Reinforcement Learning (MARL)  
- Heterogeneous‑Agent Proximal Policy Optimization (HAPPO)  
- Queueing theory and frame waiting time
