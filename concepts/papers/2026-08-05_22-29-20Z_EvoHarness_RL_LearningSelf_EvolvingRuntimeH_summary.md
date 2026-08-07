# Summary: 2026-08-05_22-29-20Z_EvoHarness_RL_LearningSelf_EvolvingRuntimeHarnessf.md
Saved: 2026-08-06 20:30
Source: 2026-08-05_22-29-20Z_EvoHarness_RL_LearningSelf_EvolvingRuntimeHarnessf.md
Model: None

---

## Summary  
The paper tackles the challenge of enabling long‑horizon LLM agents to autonomously manage an external execution workspace without manual engineering. It proposes EvoHarness‑RL, a framework that learns harness policies offline and deploys them online to construct and update BPE state during task execution. By integrating supervised fine‑tuning with cost‑aware GRPO, the system can both learn how to use the harness and coordinate its usage efficiently.

## Key Contributions  
- Harness annealing: training internalizes recurring harness‑use patterns, shifting agents from frequent calls toward selective external‑state access.  
- Harness evolution: progress updates and experience consolidation refine the harness into a compact, task‑adaptive state substrate.  
- EvoHarness‑RL achieves 96.9 % success on ALFWorld with Qwen3‑8B, demonstrating that trainable harness policies improve long‑horizon agent performance.

## Methodology  
The authors first fine‑tune the base LLM using supervised data to learn the harness action space and how to construct useful external state from noisy interaction traces. This creates a learned BPE representation of Belief, Progress, and Experience that can be read or updated at runtime. Then they employ cost‑aware GRPO to train a coordination policy that selects which BPE components to read, update, or consolidate, optimizing for long‑horizon efficiency while minimizing unnecessary harness calls.

## Results  
Experiments on ALFWorld show the EvoHarness‑RL system reaches 96.9 % success rate compared with baseline prompting and heuristic approaches. The authors observe two dynamics: harness annealing reduces the frequency of harness invocations as the agent internalizes patterns, and harness evolution produces a more compact state representation that adapts to task demands.

## Significance  
This work proves that long‑horizon LLM agents can benefit from trainable policies for constructing and coordinating with external execution workspaces, moving beyond static tools or larger memories. By automating harness design and runtime control, the framework reduces engineering overhead and enables more flexible, efficient agent behavior across diverse tasks.

## Related Concepts  
- BPE (Belief, Progress, Experience) harness state  
- Supervised fine‑tuning  
- Cost‑aware GRPO  
- Long‑horizon LLM agents  
- External execution support  
- Tool invocation  
- Runtime policy learning  
- State tracking  
- RL coordination
