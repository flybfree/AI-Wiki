# Summary: 2026-08-06_03-52-37Z_SkillTV_Bench_BenchmarkingHowWellJudgesPerformonSk.md
Saved: 2026-08-06 20:31
Source: 2026-08-06_03-52-37Z_SkillTV_Bench_BenchmarkingHowWellJudgesPerformonSk.md
Model: None

---

## Summary  
The paper introduces **SkillTV‑Bench**, a benchmark that evaluates how well judges verify skill‑augmented agentic execution by combining task‑time procedural knowledge with inspectable artifacts. It also proposes **SkillTV‑Evolve**, which externalizes verification as a reusable **JudgeSkill** and refines it via an automated evolution loop on misjudged cases. The work aims to move evaluation beyond final‑response scoring toward assessing the quality of evidence‑grounded verdicts in real trajectories.

## Key Contributions  
- Introduces SkillTV‑Bench, a 681‑case dataset spanning 50 tasks across eleven domains, designed to evaluate both **LLM‑as‑a‑Judge** and **Agent‑as‑a‑Judge**.  
- Proposes SkillTV‑Evolve, a reusable **JudgeSkill** that guides agents to perform targeted inspections and issue evidence‑grounded verdicts, with an offline evolution loop that improves the skill using misjudged cases.  
- Demonstrates that the refined skill raises the same agent judge’s accuracy by **14.8 percentage points** and boosts rollout‑pool success from **22.9 %** (one rollout) to **45.5 %** (ten rollouts).  

## Methodology  
The authors collected real agent trajectories where tools are invoked, paired each trajectory with the procedural skill that governs its execution, and created a verification benchmark requiring judges to inspect specific artifacts. Two judge paradigms were implemented: an LLM‑as‑a‑Judge that produces final responses and an Agent‑as‑a‑Judge that interacts iteratively. SkillTV‑Evolve externalizes the knowledge into a skill object that selects which evidence to examine; an evolution loop re‑optimizes this skill using cases where the original judgment was incorrect.

## Results  
Offline evaluation on the development pool shows a **14.8 percentage point** increase in accuracy for the same agent judge when using the evolved JudgeSkill. In rollout‑pool selection, the refined skill improves success rates from **22.9 %** with one rollout to **45.5 %** with ten rollouts. The dataset and code are publicly available at https://github.com/HanZhi306/SkillTV-Bench.

## Significance  
SkillTV‑Bench provides the first benchmark that jointly incorporates task‑time skills, inspectable artifacts, and a judge‑skill framework, enabling systematic study of verification quality in skill‑augmented agents. By showing how an evolved JudgeSkill can markedly improve both accuracy and rollout performance, it advances LLM tool use research and offers a practical pathway for building more reliable agentic systems.

## Related Concepts  
- Skill‑augmented agents  
- Trajectory verification  
- JudgeSkill (externalized procedural knowledge)  
- Evidence‑grounded verdicts  
- Rollout pool selection  
- Offline evolution loop
