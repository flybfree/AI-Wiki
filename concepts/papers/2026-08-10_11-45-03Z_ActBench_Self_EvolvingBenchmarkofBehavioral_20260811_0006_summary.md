# Summary: 2026-08-10_11-45-03Z_ActBench_Self_EvolvingBenchmarkofBehavioralSafetyi.md
Saved: 2026-08-11 00:06
Source: 2026-08-10_11-45-03Z_ActBench_Self_EvolvingBenchmarkofBehavioralSafetyi.md
Model: None

---

## Summary  
ActBench is a self‑evolving benchmark designed to evaluate the behavioral safety of cowork agents by analyzing their execution trajectories rather than only their final outputs. The work introduces a novel reward‑guided beam search that jointly maximizes attack effectiveness and task utility, while employing reflection diagnostics to revise payloads when failures occur. A dual evidence verification system combines log‑based checks with LLM‑generated trajectory analyses to certify both safety and utility. By constructing 600 adversarial cases across 213 scenarios, the benchmark quantifies risk behaviors, execution spaces, and API usage in a reproducible manner.

## Key Contributions  
- [Finding 1] ActBench provides a self‑evolving benchmark that pairs benign tasks with task‑reachable payloads, preserving instruction, configuration, initial state, rating model, and trusted records while injecting adversarial behavior.  
- [Finding 2] The reward‑guided beam search jointly optimizes the trade‑off between attack potency and task completion, and a reflection mechanism diagnoses checkpoint failures to guide payload revision.  
- [Finding 3] A dual evidence verification framework uses log evidence for factual safety checks and LLM‑based trajectory evidence for behavioral risk assessment.

## Methodology  
The authors built ActBench by generating 600 cases from 213 distinct scenarios, spanning 15 risk behaviors, six execution spaces, and 48 web‑service APIs. Each case contains a benign task paired with an adversarial variant that retains the original instruction and configuration but includes a hidden payload reachable through the task. To evaluate safety, they employ a reward‑guided beam search that selects trajectories maximizing both utility and attack success while using reflection to diagnose checkpoint failures and revise payloads. Safety is further verified via two evidence streams: (i) raw log data confirming no unauthorized state changes or API calls, and (ii) LLM‑generated trajectory reports summarizing the execution path.

## Results  
The benchmark was evaluated on 15 large language models and six open‑source cowork agents over 24,000 trajectories. Under a fixed harness, attack success rates ranged from 10.1 % to 94.4 %, whereas under a fixed base model they varied from 73.7 % to 94.4 %. The results reveal that model differences dominate variance more than agent‑specific differences, and attacks remain highly successful across all harnesses.

## Significance  
ActBench demonstrates that behavioral safety in cowork agents is far from guaranteed; even benign tasks can be subverted with high success rates. By providing a dynamic, self‑evolving benchmark, the work enables systematic assessment of risk behaviors and guides the development of safer agent designs through reward‑guided optimization.

## Related Concepts  
Behavioral safety, cowork agents, execution trajectories, reward‑guided beam search, reflection diagnosis, dual evidence verification (log evidence + LLM trajectory evidence), benchmarking, adversarial payload injection.
