# Summary: 2026-07-29_20-42-38Z_VAmoSBench_VoiceAgentSimulationBench.md
Saved: 2026-07-30 20:22
Source: 2026-07-29_20-42-38Z_VAmoSBench_VoiceAgentSimulationBench.md
Model: None

---

## Summary  
The paper introduces VAmoS Bench, a standardized benchmark that evaluates complete voice‑agent systems end‑to‑end in a stateful customer‑support scenario, measuring not only component quality but also whether the agent resolves calls without human handoff (containment). By providing 100 realistic scenarios with adversarial pressure and real SQL tool usage, VAmoS Bench captures both observable behavior and underlying data integrity. This work moves voice‑agent evaluation beyond isolated metrics to a holistic assessment of containment and correctness.

## Key Contributions  
- Introduces VAmoS Bench as the first comprehensive benchmark for voice‑agent systems focusing on end‑to‑end performance and containment.  
- Provides a modular evaluation protocol with stateful backend, tool invocations, and binary assertions that detect database integrity violations.  
- Offers an evolving leaderboard enabling continuous comparison of new agents across scenarios.

## Methodology  
The authors designed VAmoS Bench by creating 100 realistic customer‑support call scenarios where each scenario seeds a PostgreSQL database representing a credit‑card support case. A simulated caller interacts with Riley, the virtual agent, over audio; some scenarios include adversarial pressure (e.g., repeated questioning). The system records full dialogue and tool usage logs, which are then compared to predefined binary assertions using a grader that checks both observable behavior and underlying data changes.

## Results  
Evaluation shows current agents achieve approximately 85 % containment but fail on 12 % of scenarios where they modify the database without proper safeguards or leak protected information. Latency averages 420 ms, with a word error rate around 3 %. The leaderboard ranks agents based on containment and assertion pass rates.

## Significance  
VAmoS Bench addresses a critical gap in voice‑agent evaluation by measuring real‑world containment and data integrity, guiding the development of more reliable automated support systems that can handle complex customer interactions without compromising privacy or correctness.

## Related Concepts  
Voice agent, speech‑to‑speech pipeline, conversational AI, containment, SQL tool usage, binary assertions, adversarial pressure, leaderboard benchmarking.
