# Summary: 2026-08-03_14-12-18Z_Harness_R1_LearningtoEditExecutableRuntimeHarnesse.md
Saved: 2026-08-04 00:03
Source: 2026-08-03_14-12-18Z_Harness_R1_LearningtoEditExecutableRuntimeHarnesse.md
Model: None

---

## Summary  
The paper introduces Harness‑R1, the first method that learns to edit an existing executable runtime harness in response to observed agent failure trajectories. By treating the harness as a learnable component rather than a static script, Harness‑R1 enables continuous improvement of the agent’s execution environment without retraining the model itself. The approach uses online reinforcement learning with group‑relative policy optimization and cold‑start supervised fine‑tuning to adapt the editing policy directly from real‑world failures. This co‑evolution of harness edits and target agents yields measurable gains in task success rates across multiple benchmarks.

## Key Contributions  
- [Finding 1] Harness‑R1 makes failure‑conditioned, lifecycle‑wide editing of an executable runtime a learned capability, turning the harness into a dynamic component.  
- [Finding 2] The method employs online reinforcement learning with group‑relative policy optimization, initializing the editor via cold‑start supervised fine‑tuning and updating only the engineer from outcome rewards.  
- [Finding 3] Harness‑R1 improves vanilla Qwen3.5‑9B success from 44.3 % to 53.6 % (+9.3 pp) and, after a target‑specific engineer is added, raises the average further to 64.2 % (+5.0 pp), showing gains persist before and after fine‑tuning the target.

## Methodology  
The authors post‑train a dedicated harness engineer that operates on an existing executable runtime. A separate 9B‑parameter model converts batches of observed agent failures into validated patches for the target. Fresh, same‑batch reruns of the frozen target provide outcome rewards, allowing the engineer to be trained online with group‑relative policy optimization. Cold‑start supervised fine‑tuning supplies an initial editing policy that is later refined through reinforcement learning; only the engineer’s parameters are updated throughout training.

## Results  
Across WebShop, ALFWorld, and DBBench, Harness‑R1 lifts vanilla Qwen3.5‑9B success from 44.3 % to 53.6 %, a gain of nine point three percentage points. When a target‑specific engineer is introduced, the average rises from 59.2 % to 64.2 %, an additional five point zero improvement. These gains hold both before and after fine‑tuning the target model, indicating that harness edits are effective independently of target updates.

## Significance  
Harness‑R1 demonstrates that resilience can be built into LLM deployments by learning from failure rather than merely fixing bugs statically. By co‑evolving the harness engineer with the agent, the system becomes more adaptable to diverse tasks and environments, reducing reliance on manual intervention and improving overall performance.

## Related Concepts  
- Executable runtime harness  
- Reinforcement learning (online RL)  
- Group‑relative policy optimization  
- Cold‑start supervised fine‑tuning  
- Failure trajectory analysis  
- Task success reward shaping  
- Co‑evolution of components
