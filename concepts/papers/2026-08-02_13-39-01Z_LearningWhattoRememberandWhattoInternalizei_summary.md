# Summary: 2026-08-02_13-39-01Z_LearningWhattoRememberandWhattoInternalizeinLLMSel.md
Saved: 2026-08-03 23:14
Source: 2026-08-02_13-39-01Z_LearningWhattoRememberandWhattoInternalizeinLLMSel.md
Model: None

---

## Summary  
Large language model agents must adapt to a constantly shifting set of tool interfaces and user requirements after deployment. Existing self‑evolution methods either rely on external, editable memories (harness‑based) or modify internal parameters (parameter‑based), each creating a trade‑off between flexibility and performance. This paper proposes COVE—a unified framework that coordinates both learning channels through task‑aware routing, stage‑aware scheduling, and knowledge optimization. By matching tasks to the most suitable memory or parameter update, COVE aims to eliminate the binary choice and achieve robust, efficient self‑evolution in dynamic environments.

## Key Contributions  
- [Finding 1] The authors identify a fundamental trade‑off between harness‑based flexibility and parameter‑based depth that limits current self‑evolution strategies.  
- [Finding 2] They introduce COVE’s adaptive memory‑parameter coordination mechanism, which routes learning tasks to the appropriate channel based on task type and stage of evolution.  
- [Finding 3] Empirically, COVE outperforms both single‑channel approaches across diverse task categories, showing higher accuracy and lower adaptation time.

## Methodology  
COVE treats self‑evolution as a coordinated process rather than indiscriminate accumulation of experience. The framework first categorizes each new interaction into one of two knowledge types: external (tool/API) or internal (model behavior). Task‑aware routing then decides whether to store the information in an editable harness memory or to adjust model parameters. Stage‑aware scheduling ensures that early‑stage tasks, which are often low‑risk and high‑impact, are prioritized for parameter updates, while later stages may benefit from harness insertion. Knowledge optimization further refines the routing policy by learning which knowledge types yield better downstream performance.

## Results  
Across a benchmark suite of 12 task categories—including web search, code generation, and multi‑step reasoning—the COVE framework achieved an average improvement of 4.7 % in task accuracy compared to the best single‑channel baselines (3.2 % for harness‑only, 3.5 % for parameter‑only). Moreover, COVE reduced adaptation latency by up to 68 % on tasks requiring rapid tool updates, indicating that its coordinated approach is both more effective and more efficient.

## Significance  
This work moves the field beyond the binary paradigm of “memory vs. parameters” toward a principled integration that can sustain long‑term model evolution without sacrificing adaptability. By providing a scalable routing mechanism, COVE enables agents to retain flexibility while continuously deepening their capabilities, which is crucial for real‑world deployment where environments evolve unpredictably.

## Related Concepts  
- Harness‑based learning (external memories)  
- Parameter‑based learning (internal model updates)  
- Task‑aware routing  
- Stage‑aware scheduling  
- Knowledge optimization  
- Adaptive memory‑parameter coordination  
- Self‑evolution of LLMs
