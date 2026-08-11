# Summary: 2026-07-28_22-23-34Z_StealthBench_MeasuringOperationalStealthinAutonomo.md
Saved: 2026-07-29 21:33
Source: 2026-07-28_22-23-34Z_StealthBench_MeasuringOperationalStealthinAutonomo.md
Model: None

---

## Summary  
The paper introduces StealthBench, a benchmark to measure operational stealth in autonomous offensive‑security agents across six OPSEC dimensions. It aims to evaluate whether such agents can achieve both successful task completion and maintain stealth without compromising security tradecraft. By analyzing real bug‑bounty and red‑team trajectories, the authors create 14 dockerized scenarios where agents exhibit stealth failures. The study quantifies safe success, Stealth@Solve, and reckless solve rates using a three‑model LLM judge panel.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 3 title terms overlap; 17 backlinks; 7 summary/topic terms overlap

## Key Contributions  
- Finding 1: No model exceeds 54% safe success rate (solved and stealthy) across all task families.  
- Finding 2: OPSEC failures are systematic across different model families, indicating a lack of stealth‑aware training.  
- Finding 3: StealthBench provides an open benchmark with leaderboard, evaluation harness, and dataset for both research and operational monitoring.

## Methodology  
The authors extracted 11 hand‑verified OPSEC incidents from real bug‑bounty and red‑team trajectories, expanded them into 14 dockerized task scenarios that simulate common offensive tasks. Agents are evaluated on whether they complete the task while preserving stealth; the evaluation is performed by a majority‑vote of three large language model judges trained to detect tradecraft violations such as credential leakage or resource deletion.

## Results  
The main experimental results show that the safe success rate (both solved and stealthy) never exceeds 54% across all models. Stealth@Solve, which measures tradecraft quality among successful solves, is also low, indicating that agents often solve tasks but reveal their presence. The reckless solve rate—solutions that are discovered—varies but remains high, confirming cover‑blowing incidents.

## Significance  
This work matters because it quantifies the stealth gap in autonomous offensive tools, highlighting that current models lack operational tradecraft awareness. By releasing StealthBench publicly, researchers can develop stealth‑aware agents and automated OPSEC monitoring systems, improving security posture of autonomous deployments.

## Related Concepts  
Operational Security (OPSEC), Autonomous Offensive‑Security Agents, Tradecraft, Stealth, Bug bounty / red team scenarios, Large language model evaluation panels, Dockerized task environments.
