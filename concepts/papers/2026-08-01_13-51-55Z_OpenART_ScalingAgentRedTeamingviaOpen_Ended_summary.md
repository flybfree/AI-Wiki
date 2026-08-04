# Summary: 2026-08-01_13-51-55Z_OpenART_ScalingAgentRedTeamingviaOpen_EndedEnviron.md
Saved: 2026-08-03 21:27
Source: 2026-08-01_13-51-55Z_OpenART_ScalingAgentRedTeamingviaOpen_EndedEnviron.md
Model: None

---

## Summary  
The paper introduces OpenART, an open‑ended arena designed to scale agent red‑team evaluation by evolving the environment over long‑horizon workflows. It proposes EMHA, a black‑box policy that coordinates authorized state transitions without updating model parameters, thereby exposing safety failures as task complexity grows. The framework generates thousands of validated stateful scenarios across 50 domains and evaluates them with agents using a median of 97 tool calls. Overall, the attack success rate (ASR) reaches 85 %, highlighting that environment evolution dramatically increases the exposure of unsafe behaviors.

## Key Contributions  
- OpenART provides over 10,000 validated stateful scenarios across 50 domains, enabling unified evaluation for 75 agent‑model configurations.  
- EMHA is a black‑box policy that performs feedback‑driven environment evolution without requiring parameter updates.  
- Environment evolution raises the attack success rate from ~2 % on simple settings to >17 % on complex ones, demonstrating that cumulative risk grows with task difficulty.

## Methodology  
The authors constructed an Evolutionary Markov Hypergraph Attack (EMHA) that treats each authorized state transition as a node in a hypergraph. EMHA receives the current environment state and a set of permissible actions, then selects transitions that maximize the likelihood of achieving the fixed task objective while preserving safety constraints. The process repeats iteratively, allowing the environment to evolve dynamically without any changes to the underlying agent or model parameters.

## Results  
Across all configurations, EMHA achieves a pooled Attack Success Rate (ASR) of 85 %. Simple environments show an ASR improvement from ~2 % to >17 % as complexity increases. The median number of tool calls per scenario is 97, and the dataset spans more than 500,000 tools and skills. Safety variation beyond model capability is attributed largely to runtime implementation details.

## Significance  
OpenART establishes a scalable foundation for studying agent safety in complex, evolving environments where early state changes propagate far into future actions. By systematically varying the environment rather than the task, it uncovers hidden failure modes that static benchmarks miss, guiding more robust AI system design and safety testing.

## Related Concepts  
stateful environments, cumulative risk, environment evolution, black‑box policy, attack surface expansion, agent red teaming, Markov hypergraph modeling.
