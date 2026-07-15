# Summary: 2026-07-14_17-59-31Z_DoAIAgentsKnowWhenaTaskIsSimple_TowardComplexity_A.md
Saved: 2026-07-15 00:02
Source: 2026-07-14_17-59-31Z_DoAIAgentsKnowWhenaTaskIsSimple_TowardComplexity_A.md
Model: None

---

## Summary  
The paper investigates whether AI agents can recognize when a task is simple and avoid unnecessary work, arguing that current LLM‑based agents follow a maximum‑context strategy that wastes effort on trivial edits. To address this gap the authors propose a complexity‑aware execution framework called **E3** (Estimate → Execute → Expand) and formalize two new concepts: *minimum‑sufficient execution* and the *Agent Cognitive Redundancy Ratio* (ACRR). Their approach reduces token usage, file inspections, and overall cost while maintaining high success rates on a deterministic benchmark.

## Key Contributions  
- **Formalization of Minimum‑Sufficient Execution** – they define a precise notion of the smallest set of operations that can reliably complete a task.  
- **Introduction of Agent Cognitive Redundancy Ratio (ACRR)** – a metric quantifying how much extra work an agent performs beyond what is strictly necessary.  
- **E3 algorithm** – a policy that estimates the optimal operating point, executes only the minimal viable path, and expands scope only when verification fails.

## Methodology  
The authors built **MSE‑Bench**, a deterministic simulator containing 121 edit tasks with controlled difficulty levels, to evaluate task‑aware execution. They implemented E3 as a policy that first estimates the required effort, then executes the minimal sufficient steps, and finally expands only if verification fails. A companion harness called **LLM‑Case** tests a live gpt‑4o agent on a real open‑source library; each candidate patch is graded by running the project’s pytest suite against a measured oracle.

## Results  
On MSE‑Bench E3 achieves 100 % success, matching the strongest baseline while cutting overall cost by **85 %**, token consumption by **91 %**, and inspected files by **92 %**; it also outperforms an adaptive retrieval baseline by **16 %**. In the real‑world LLM‑Case experiment E3 remains the leanest and fastest policy at comparable task success, with its only limitation being a provider rate‑limit rather than incorrect edits.

## Significance  
Task‑aware execution aligns AI effort with engineering reality, reducing waste and supporting **Engineering‑Grounded AI (EGAI)**. By providing a reusable framework for cost‑sensitive autonomous agents, the work demonstrates that intelligent agents can be designed to respect the complexity of tasks they perform.

## Related Concepts  
- Minimum‑sufficient execution  
- Agent Cognitive Redundancy Ratio (ACRR)  
- E3 algorithm (Estimate → Execute → Expand)  
- Complexity‑aware reasoning and task estimation  
- Verification‑driven expansion  
- MSE‑Bench benchmark  
- LLM‑Case harness  
- Engineering‑Grounded AI (EGAI)
