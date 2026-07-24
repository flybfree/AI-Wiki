# Summary: 2026-07-22_08-43-43Z_JANUS_ForeseeingLatentRiskforLong_HorizonAgentSafe.md
Saved: 2026-07-24 01:37
Source: 2026-07-22_08-43-43Z_JANUS_ForeseeingLatentRiskforLong_HorizonAgentSafe.md
Model: None

---

## Summary  
The paper introduces Janus, a foresight‑oriented framework for long‑horizon agent safety that enables an internal “guard” model to anticipate delayed risks arising from partial trajectories of tool‑using agents. By jointly training an anticipation task and an adjudication task with a reinforcement‑learning algorithm, the guard can block unsafe actions before they are executed while preserving benign task completion. Across four benchmark suites, Janus‑trained guards improve average protection by 15.9 percentage points and increase successful benign completions by 5.1 percentage points over baseline systems.

## Key Contributions  
- [Finding 1] A dual‑task RL architecture that couples foresight (anticipation) with safety adjudication, using a shared policy optimized via CoAA‑RL.  
- [Finding 2] Multi‑agent simulation to synthesize diverse trajectories, enabling the guard to learn a robust representation of both observed prefixes and predicted futures.  
- [Finding 3] Empirical gains: a 15.9 pp increase in protection and a 5.1 pp rise in benign task completion compared with baselines.

## Methodology  
The authors model long‑horizon safety as a joint optimization problem where the guard must forecast future states that are safety‑relevant and then decide whether to permit an action based on both the current prefix and the anticipated outcome. CoAA‑RL (Cooperative Action Anticipation with Reward) rewards the anticipation policy by its utility for downstream safety judgments, allowing the two tasks to be trained simultaneously. Multi‑agent simulators generate a rich set of partial trajectories, which are fed into the shared policy network to produce forecasts and safety decisions.

## Results  
In four agent‑safety benchmarks—including tool use, multi‑step planning, and resource allocation—the Janus guard outperformed baseline agents by an average of 15.9 percentage points in preventing unsafe actions while completing benign tasks 5.1 percentage points more often than the best baselines. The improvement is measured as a proportion of protected steps versus total steps across simulated runs.

## Significance  
This work bridges the gap between reactive safety filters and proactive foresight, offering a scalable method to embed long‑term risk awareness into autonomous agents that interact with complex tools. By training guards on both anticipation and adjudication, Janus can anticipate failures before they manifest, reducing catastrophic outcomes without sacrificing productivity.

## Related Concepts  
- Long‑horizon safety  
- Agent guard models  
- Cooperative RL (CoAA‑RL)  
- Multi‑agent simulation for trajectory synthesis  
- Dual‑task reinforcement learning
