# Summary: 2026-08-05_13-29-16Z_Skill_Use_CanLLMsActuallyUseSkillsinAgenticHarness.md
Saved: 2026-08-05 20:36
Source: 2026-08-05_13-29-16Z_Skill_Use_CanLLMsActuallyUseSkillsinAgenticHarness.md
Model: None

---

## Summary  
The paper investigates whether large language model (LLM) agents can autonomously recognize and apply structured skills in agentic harnesses, a capability that has been largely unexamined beyond isolated skill‑quality assessments. To address this gap, the authors introduce **Skill‑Use**, a benchmark that evaluates three facets of skill use—triggering, procedural compliance, and boundary adherence—under progressive disclosure where agents only see a skill name and brief description before retrieving the full procedure. The study pairs 79 real skills with 177 executable tasks across nine domains, runs experiments in isolated Docker sandboxes, and scores trajectories with a rubric‑based metric called **Skill‑Use (SU)**.  

## Key Contributions  
- [Finding 1] Reliable skill use remains out of reach; the strongest configuration achieves an SU score of only 0.613.  
- [Finding 2] Triggering and procedural compliance are identified as independent bottlenecks that limit overall performance.  
- [Finding 3] The Skill‑Use score is highly sensitive to the agent harness, indicating that skill use behaves as a capability conditioned on the harness rather than an intrinsic property of the model.  

## Methodology  
The authors approached the problem by constructing a benchmark that isolates each facet of skill use. For each skill, agents are presented only its name and a short description; they must retrieve the complete procedural document before execution. The **Skill‑Use (SU)** score aggregates three sub‑scores: trigger (whether the relevant skill is invoked), compliance (how faithfully the procedure is followed), and boundary (avoidance of forbidden operations). Experiments were conducted with eight LLMs under two distinct agent harnesses, each running tasks in isolated Docker containers. A trajectory‑based rubric records the sequence of actions, enabling precise scoring of trigger, compliance, and boundary adherence.  

## Results  
Across all configurations, the highest SU achieved was 0.613, far below a desirable threshold for reliable skill use. Triggering occurred in only about half of the trials, and when triggered, procedural compliance suffered from systematic deviations, leading to low boundary scores. Moreover, model rankings shifted dramatically depending on which harness was employed, demonstrating that the same LLM performed differently under different environments. These results confirm that skill‑use is not a stable capability but rather a contingent outcome of the harness architecture.  

## Significance  
The findings underscore that evaluating LLM agents solely on skill quality or task success is insufficient; they reveal that skill use depends critically on how skills are exposed and constrained within an agentic harness. This challenges existing benchmarks that treat skills as static resources, suggesting a need for more nuanced evaluation frameworks that capture trigger dynamics, procedural fidelity, and safety boundaries.  

## Related Concepts  
- LLM agents  
- Skills (structured documents)  
- Agentic harnesses  
- Progressive disclosure  
- Trigger/compliance/boundary metrics  
- Benchmarking of skill use  
- Docker sandbox isolation  
- Trajectory‑based scoring
