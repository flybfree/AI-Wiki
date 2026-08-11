# Summary: 2026-08-10_03-22-04Z_AUnifiedIssueResolutionBenchmarkforRequirementClar.md
Saved: 2026-08-10 23:38
Source: 2026-08-10_03-22-04Z_AUnifiedIssueResolutionBenchmarkforRequirementClar.md
Model: None

---

## Summary  
The paper introduces SWE‑RPG, a repository‑level benchmark that jointly evaluates requirement clarification, implementation planning, and code generation for coding agents, providing ground‑truth references for each intermediate step to enable detailed diagnosis of failures. It combines executable patch evaluation with validated GTs across 163 tasks in Python and Java repositories, assessing three popular agents (Claude Code, Codex, OpenCode) using six large language model backbones. The benchmark shows that current agents resolve only about one‑third of user requests on average.

## Key Contributions  
- SWE‑RPG integrates requirement clarification and planning ground‑truths alongside final patch tests to assess the full trajectory from request parsing to artifact submission.  
- Evaluation reveals implicit requirement recovery as the dominant bottleneck, accounting for 24.5 %–46 % of failed agent runs across all models.  
- The average resolved rate is only 31.5 %, highlighting significant limitations in current coding agents’ ability to satisfy user requests.

## Methodology  
The authors constructed SWE‑RPG by selecting 31 repositories (Python and Java) and generating 163 tasks: 113 bug fixes and 50 feature additions. For each task they provide three ground‑truth artifacts—requirement clarification statements, implementation plans, and the correct final patch. Agents are evaluated using six LLM backbones; a full trajectory includes request parsing → clarification → planning → code generation → submission. Success is measured at each stage rather than solely on test pass/fail.

## Results  
The average resolved rate across all agents is 31.5 %. Implicit requirement recovery is the primary failure mode, responsible for roughly one‑quarter to half of unsuccessful runs (24.5 %–46 %). Other bottlenecks include plan feasibility and code correctness. Claude Code performs best, while OpenCode shows the lowest performance.

## Significance  
SWE‑RPG provides a unified benchmark that goes beyond final test outcomes, enabling researchers to diagnose where coding agents diverge from requirements or planning. This insight guides targeted improvements in implicit requirement recovery and repository‑grounded planning, which are essential for reliable agent‑assisted code modification.

## Related Concepts  
- Requirement clarification  
- Implementation planning  
- Code generation  
- Coding agents  
- Repository‑level evaluation  
- Ground‑truth references (GT)  
- Implicit requirements  
- Patch debugging
