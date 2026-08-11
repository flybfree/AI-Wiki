# Summary: 2026-08-09_01-08-19Z_CAP_AScalableBenchmarkforEvaluatingCross_SiteBrows.md
Saved: 2026-08-10 23:10
Source: 2026-08-09_01-08-19Z_CAP_AScalableBenchmarkforEvaluatingCross_SiteBrows.md
Model: None

---

## Summary  
The paper introduces CAP, a scalable benchmark for evaluating cross‑site browser agents that perform complex UI interactions and visual perception. It aims to address the gap between end‑to‑end task success metrics and real‑world browsing challenges. By decomposing websites into structured site cards and recombining them, CAP creates 420 tasks across 108 sites and 24 domains. The evaluation framework reveals low agent success rates, highlighting perception bottlenecks.

## Key Contributions  
- [Finding 1] CAP provides a scalable benchmark with fine‑grained task decomposition that captures complex actions and visual perception.  
- [Finding 2] The benchmark spans 108 websites across 24 domains, offering diverse real‑world scenarios for agent testing.  
- [Finding 3] Experiments show that perception‑heavy interactions remain a major bottleneck, exposing large gaps between current agents and human browsing.

## Methodology  
The authors built CAP by first abstracting each website into a site card that records user‑facing functions, complex execution operations, and perceptual requirements. These cards are then recomposed to generate realistic cross‑site workflows. Quality control ensures tasks reflect actual UI flows. Evaluation uses an agent‑as‑a‑judge framework where agents perform tasks while a human verifies outcomes.

## Results  
Using state‑of‑the‑art browser agents, CAP reports overall success rates below 30 %, with perception tasks scoring significantly lower than pure text actions. The variance across domains underscores the difficulty of multi‑site coordination.

## Significance  
This benchmark forces researchers to confront the true complexity of web browsing beyond simple task completion, guiding more realistic agent design and evaluation.

## Related Concepts  
Cross‑site navigation, visual perception in browsers, end‑to‑end task success, UI interaction decomposition, agent‑as‑a‑judge framework, scalable benchmarking.
