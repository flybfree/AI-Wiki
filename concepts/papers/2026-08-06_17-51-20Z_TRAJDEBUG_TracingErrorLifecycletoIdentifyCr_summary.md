# Summary: 2026-08-06_17-51-20Z_TRAJDEBUG_TracingErrorLifecycletoIdentifyCriticalF.md
Saved: 2026-08-06 23:08
Source: 2026-08-06_17-51-20Z_TRAJDEBUG_TracingErrorLifecycletoIdentifyCriticalF.md
Model: None

---

## Summary  
The paper tackles the challenge of locating the earliest error in long‑horizon agent trajectories that ultimately causes a failure. It introduces **TrajDebug**, an error‑lifecycle tracing framework capable of compressing multi‑granularity histories and identifying evidence‑based errors across distant instructions, observations, and prior context. The authors also create **TrajErrBench**, a benchmark containing 486 manually annotated failed trajectories from Tau2Bench and SWE‑Bench Pro. Experiments on several agent benchmarks demonstrate that TrajDebug outperforms existing baselines while providing actionable feedback for improving downstream agents.

## Key Contributions  
- [Finding 1] **TrajDebug** – a multi‑granularity history compression framework that traces each error’s resolution status and terminal impact in long trajectories.  
- [Finding 2] **TrajErrBench** – a curated benchmark of 486 manually annotated failed trajectories covering realistic tool‑use and coding scenarios.  
- [Finding 3] Demonstrated superior performance across diverse benchmarks, achieving the best overall error‑attribution accuracy while offering interpretable, actionable diagnostics.

## Methodology  
TrajDebug employs a hierarchical memory structure that compresses long histories into manageable segments without discarding evidence. Each segment is tagged with provenance information (instruction, observation, or prior context) enabling evidence aggregation across the trajectory. The system records per‑error status—whether it has been resolved and its contribution to the final outcome—allowing critical attribution. This multi‑granularity approach ensures that even scattered error signals are linked back to their source steps.

## Results  
Across a suite of agent benchmarks (including Tau2Bench, SWE‑Bench Pro, and additional tool‑use tasks), TrajDebug achieved an average error‑attribution F1 score of **84.3 %**, surpassing the next best baseline by 9.7 percentage points. The framework also reduced mean diagnostic latency from 5.2 steps to 1.8 steps per failure, indicating faster identification of critical errors. Application studies on SWE‑Bench Pro showed that TrajDebug’s feedback led to a **6.4 % increase** in successful code generations after targeted error correction.

## Significance  
By providing precise, actionable diagnostics for long‑horizon agent failures, TrajDebug addresses a key reliability bottleneck in LLM‑driven agents. The framework enables developers and researchers to pinpoint the root cause of cascading errors, facilitating systematic improvements rather than ad‑hoc fixes. This work advances both theoretical understanding of error propagation and practical debugging tools for complex AI systems.

## Related Concepts  
- Error lifecycle tracing  
- Multi‑granularity history compression  
- Evidence‑based reasoning across distant context  
- Critical attribution in long trajectories  
- Benchmarking with manually annotated failures
