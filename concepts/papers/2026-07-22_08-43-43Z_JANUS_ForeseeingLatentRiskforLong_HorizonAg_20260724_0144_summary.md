# Summary: 2026-07-22_08-43-43Z_JANUS_ForeseeingLatentRiskforLong_HorizonAgentSafe.md
Saved: 2026-07-24 01:44
Source: 2026-07-22_08-43-43Z_JANUS_ForeseeingLatentRiskforLong_HorizonAgentSafe.md
Model: None

---

## Summary  
The paper introduces Janus, a foresight‑oriented framework for long‑horizon agent safety that trains agents to anticipate delayed risks from partial trajectories. It does this by synthesizing diverse agent trajectories via multi‑agent simulation and learning a shared policy with two coupled tasks: an anticipation task that forecasts safety‑relevant futures and an adjudication task that decides safety based on both the observed prefix and anticipated future. The joint optimization uses CoAA‑RL, rewarding forecasts by their utility for downstream safety judgment, resulting in a guard model Vanguard that blocks unsafe actions before execution. Across four benchmarks, Vanguard improves average protection by 15.9 percentage points over baselines while increasing benign task completion by 5.1 percentage points.  

## Key Contributions  
- Janus framework for long‑horizon agent safety that anticipates delayed risks from partial trajectories.  
- Multi‑agent simulation to synthesize diverse trajectories and learn a shared policy with two coupled tasks (anticipation and adjudication).  
- CoAA‑RL joint optimization that rewards forecasts by their utility for downstream safety judgment, producing guard model Vanguard.  

## Methodology  
The authors approached the problem by first constructing a large set of agent trajectories through multi‑agent simulation to capture a wide range of possible behaviors. They then trained a single shared policy using two tasks: an anticipation task that predicts safety‑relevant futures and an adjudication task that decides safety based on both observed prefix and predicted future. These tasks are jointly optimized via CoAA‑RL, where the reward function evaluates how well forecasts contribute to correct safety judgments downstream. The resulting guard model Vanguard is deployed to block unsafe actions before they can be executed.  

## Results  
Experimental evaluation across four agent‑safety benchmarks shows that Vanguard achieves an average protection improvement of 15.9 percentage points over baseline guards, while benign task completion increases by 5.1 percentage points. This indicates both higher safety and no trade‑off in performance on safe tasks. The improvements are consistent across diverse scenarios, demonstrating robustness.  

## Significance  
This work matters because long‑horizon agents may act after observing only a short prefix of their trajectory, making it crucial to anticipate future risks before execution. Janus provides a proactive guard mechanism that can prevent operational failures without hindering legitimate actions, advancing the field toward reliable AI deployment.  

## Related Concepts  
Multi‑agent simulation, CoAA‑RL (Cooperative Adversarial Reinforcement Learning), anticipation task, adjudication task, shared policy learning, Vanguard guard model, long‑horizon safety forecasting.
