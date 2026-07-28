# Summary: 2026-07-27_17-34-09Z_DenialofDeadline_Network_DrivenAccuracyCollapseinD.md
Saved: 2026-07-28 00:15
Source: 2026-07-27_17-34-09Z_DenialofDeadline_Network_DrivenAccuracyCollapseinD.md
Model: None

---

## Summary  
The paper investigates how modern inference pipelines that combine a fast‑path and a high‑accuracy slow‑path can be sabotaged by shaped workload attacks, leading to “accuracy collapse.” By abstracting the pipeline into a router, a merger, and two latency deadlines, the authors show that contention on shared resources can push benign users’ slow‑path predictions beyond their deadline. The merger then discards those late predictions, eroding the benefit of cloud‑based inference while the fast path continues to serve timely outputs. This work demonstrates that such attacks degrade prediction quality without requiring access to model weights or victim data.

## Key Contributions  
- **Finding 1:** Shaped workload attacks (e.g., Yo‑Yo bursts) exploit contention at shared resources along the slow path, causing latency spikes that force the merger to drop predictions.  
- **Finding 2:** The latency increase from 92 ms to 2 s for benign users under a 4000‑request burst reduces object‑tracking quality by approximately 7.0 HOTA points on average.  
- **Finding 3:** Accuracy degradation varies widely (2.0–18.7 HOTA points) depending on video intervals targeted, and rare classes such as stop signs lose up to half their pre‑attack accuracy.

## Methodology  
The authors model a two‑tier edge‑cloud multi‑object tracking pipeline with a fast path that runs locally and a slow path that invokes cloud inference. A coordination layer consists of a router that schedules slow‑path jobs and a merger that decides whether to incorporate their results based on deadline compliance. They simulate realistic traffic using Yo‑Yo burst attacks, measuring p99 latency and HOTA (Hamming‑Optimal‑Tracking‑Accuracy) scores before and after each attack.

## Results  
With 4000 burst‑shaped requests, benign users’ p99 latency rises from 92 ms to 2 s, eliminating the slow‑path benefit. The average HOTA score drops by 7.0 points, corresponding to a ~15 % quality loss. Sensitivity analysis shows degradation can range from 2.0 to 18.7 HOTA points across different video intervals; stop signs lose roughly 49 % of their pre‑attack accuracy.

## Significance  
These findings reveal that workload attacks can cause severe accuracy collapse in distributed inference pipelines without compromising the attacker’s ability to access model weights or victim data, highlighting a critical vulnerability. The results motivate further research into defenses for routing decisions, merging logic, scheduling policies, and resource isolation in such architectures.

## Related Concepts  
- Distributed inference pipeline (fast path / slow path)  
- Latency deadline enforcement  
- Coordination layer with router and merger components  
- Shaped workload attacks (Yo‑Yo bursts)  
- Contention on shared resources  
- HOTA metric for object detection quality  
- Edge‑cloud multi‑object tracking scenario
