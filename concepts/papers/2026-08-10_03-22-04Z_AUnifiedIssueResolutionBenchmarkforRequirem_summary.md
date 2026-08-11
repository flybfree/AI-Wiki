# Summary: 2026-08-10_03-22-04Z_AUnifiedIssueResolutionBenchmarkforRequirementClar.md
Saved: 2026-08-10 23:34
Source: 2026-08-10_03-22-04Z_AUnifiedIssueResolutionBenchmarkforRequirementClar.md
Model: None

---

## Summary  
The paper introduces **SWE‑RPG**, a repository‑level benchmark that evaluates coding agents on the full chain of requirement clarification, implementation planning, and code generation, providing validated ground‑truth references for each intermediate step. By coupling executable patch evaluation with these GTs, SWE‑RPG enables retrospective diagnosis of why a trajectory fails, moving beyond a simple pass/fail outcome to understand the reasoning process that leads to correct or incorrect patches.

## Key Contributions  
- **SWE‑RPG benchmark** integrates executable patch verification with ground‑truth references for requirement clarification and implementation planning, allowing agents to be assessed on all stages of their workflow.  
- The evaluation shows an average resolved rate of only **31.5 %** across Claude Code, Codex, and OpenCode using six large language model backends (e.g., Claude‑Sonnet‑5, GPT‑5.6‑Terra), indicating that current agents still struggle to produce correct patches in existing repositories.  
- Intermediate‑GT diagnosis reveals that **implicit requirement recovery** is the dominant bottleneck, accounting for **24.5 %–46.0 %** of agent runs where the task ultimately fails.

## Methodology  
The authors assembled a dataset of 163 tasks drawn from 31 Python and Java repositories (113 bug fixes, 50 feature additions). Each task is paired with executable ground‑truth references that capture the correct clarification statements, planning decisions, and final code. Three coding agents—Claude Code, Codex, and OpenCode—are run with six LLM backends; after each step the system checks whether the output matches the GTs and whether the patch passes automated tests. The evaluation records both success/failure of the final artifact and the diagnostic breakdown across clarification, planning, and code‑generation phases.

## Results  
The primary quantitative result is an average resolved rate of **31.5 %** for the three agents on SWE‑RPG. Diagnostic analysis further shows that implicit requirement recovery is the most frequent failure mode, occurring in roughly a quarter to almost half of all runs. The breakdown indicates that while clarification and planning steps are sometimes correct, many trajectories diverge because agents cannot infer or articulate hidden user requirements before generating code.

## Significance  
SWE‑RPG provides a unified benchmark that captures the full reasoning chain of coding agents, offering a granular view of where failures occur beyond binary pass/fail outcomes. By isolating implicit requirement recovery as a major obstacle, the study guides future research toward more robust mechanisms for understanding and expressing unstated constraints in code generation.

## Related Concepts  
- Requirement clarification  
- Implementation planning  
- Code generation  
- Repository‑level evaluation  
- Ground‑truth references (GTs)  
- Coding agents  
- LLM backends  
- Patch validation
