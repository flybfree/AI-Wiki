# Summary: 2026-08-25_17-56-35Z_RecursiveExperiential_WorkingMemoryEvolutionforLon.md
Saved: 2026-08-25 21:52
Source: 2026-08-25_17-56-35Z_RecursiveExperiential_WorkingMemoryEvolutionforLon.md
Model: None

---

## Summary  
The paper tackles the difficulty of recursive self‑improvement (RSI) in long‑horizon tasks by proposing a memory architecture that keeps track of task progress while steering skill selection from an Experiential Memory. By coupling this Working Memory with a fixed Meta‑Agent, execution is turned into structured evidence that localizes failures to specific memory components, allowing the Meta‑Agent to generate validation‑gated updates to Skill Memory in a bounded recursive loop. The approach aims to continuously reshape accumulated experience so that agents can maintain coherent long‑horizon behavior as their histories grow.  

## Key Contributions  
- [Finding 1] Recuris introduces a recursive Experiential‑Working Memory architecture where Working Memory monitors task progress and directs skill invocation from Experiential Memory, grounding actions in current needs rather than the full history.  
- [Finding 2] A fixed Meta‑Agent consumes localized execution evidence to produce validation‑gated updates that reshape Skill Memory, forming a self‑reinforcing memory‑evolution loop.  
- [Finding 3] Empirical evaluation shows Recuris improves task success in 35 of 37 model‑benchmark pairs and lifts frontier models by up to +32.2 points on the longest tasks, with common long‑horizon failures dropping by up to 80 %.  

## Methodology  
The authors designed Recuris as a memory hierarchy: Experiential Memory stores past experiences, Working Memory tracks the current task state and selects appropriate skills from that store, and Skill Memory holds reusable skill representations. Execution of a skill produces evidence that is tagged with which component (Experiential, Working, or Skill) it originated from. The Meta‑Agent reads this evidence, validates it, and writes back targeted updates to Skill Memory. This process repeats recursively, each iteration refining the memory structures while producing new evidence for further refinement.  

## Results  
Across four long‑horizon benchmarks and ten language models, Recuris achieved success in 35 of 37 completed model‑benchmark pairs. For GPT‑5.6 Sol it added +17.8 points; for Claude Opus 5 it raised performance to 87.9 % (a +15.6 point gain). On Qwen3.6‑27B and Qwen3.6‑35B, gains were +16.6 and +13.5 points respectively on SkillFlow. The advantage expands with longer interaction horizons to a maximum of +32.2 points, and overall failure rates decline by up to 80 % compared with baseline models.  

## Significance  
Recuris provides a scalable foundation for recursive self‑improvement by converting accumulated experience into progressively effective long‑horizon behavior. The bounded memory‑evolution loop reduces the risk of history‑obscured skill selection, enabling agents to maintain coherent goals over extended tasks without catastrophic forgetting or misaligned actions. This work demonstrates that structured, evidence‑driven memory updates can be a practical pathway toward achieving RSI in real‑world long‑horizon AI systems.  

## Related Concepts  
- Experiential Memory  
- Working Memory  
- Skill Memory  
- Meta‑Agent  
- Recursive Self‑Improvement (RSI)  
- Bounded memory evolution loop  
- Evidence localization
