# Summary: 2026-08-07_01-54-52Z_OnlineMonitoringandCorrectiveSteeringofProgramming.md
Saved: 2026-08-09 22:34
Source: 2026-08-07_01-54-52Z_OnlineMonitoringandCorrectiveSteeringofProgramming.md
Model: None

---

## Summary  
The paper tackles the inefficiency and error prone behavior of programming agents when fixing large‑scale GitHub issues, especially those that require coordinated changes across multiple locations or lack sufficient description detail. It introduces **LivePlan**, a real‑time monitoring system that detects behavioral drifts without invoking an LLM for every decision, and only consults an LLM advisor to propose high‑level corrections when needed. By decoupling judgment from advising, LivePlan avoids the costly re‑planning loops of prior approaches. The authors evaluate LivePlan on top of SWE‑agent across five LLMs using SWE‑bench Verified and Pro datasets.

## Key Contributions  
- **Finding 1:** A deterministic rule‑based monitor can reliably detect inefficiencies such as drift, repeated actions, or premature termination in an agent’s trajectory.  
- **Finding 2:** Decoupling the judging component from the advising component prevents misleading re‑planning and reduces unnecessary LLM interventions.  
- **Finding 3:** LivePlan yields a consistent improvement of up to 15.2 % (average 9.9 %) in issue resolution rates with only an additional cost of $0.08 per instance, concentrating gains on medium‑hard problems.

## Methodology  
LivePlan is built as a wrapper around SWE‑agent that continuously observes the agent’s execution log. The monitor runs locally and flags deviations from the intended plan using simple heuristics (e.g., repeated failed commits, out‑of‑scope actions). When an issue is flagged, LivePlan triggers the LLM advisor to generate a high‑level corrective step; this advice is then fed back into SWE‑agent for execution. The system was tested on five different LLMs—three serving as executor agents and two as advisors—across both benchmark suites (Verified and Pro).  

## Results  
Compared with vanilla SWE‑agent, LivePlan achieved a mean resolution rate increase of 9.9 % across the combined test set, reaching a peak of 15.2 % on the hardest instances. The extra computational expense was modest: $0.08 per instance. Importantly, the method showed minimal regression on already successful runs and added new successes where previous baselines failed. Alternative approaches that relied solely on LLM‑driven re‑planning performed worse or incurred higher costs.

## Significance  
The work demonstrates that lightweight, rule‑based monitoring can substantially boost the effectiveness of automated programming agents without sacrificing performance or incurring prohibitive expense. By limiting LLM usage to genuine problem detections, LivePlan offers a scalable solution for long‑horizon GitHub issue fixing tasks in large codebases.

## Related Concepts  
- Programming agents (e.g., SWE‑agent)  
- Large language model (LLM) advisors and executors  
- Deterministic rule‑based monitoring  
- Trajectory correction / drift detection  
- Cost‑aware algorithmic design
