# Summary: 2026-08-12_10-15-19Z_AgentSkillsCanBeHarmful_AnEmpiricalStudyofSkill_In.md
Saved: 2026-08-12 21:32
Source: 2026-08-12_10-15-19Z_AgentSkillsCanBeHarmful_AnEmpiricalStudyofSkill_In.md
Model: None

---

## Summary  
This paper investigates how the reuse of pre‑defined “agent skills” can cause both functional failures and efficiency regressions in large language model (LLM) agents, revealing that seemingly useful guidance may actually hinder performance. The authors introduce a differential analysis framework and a taxonomy‑guided attribution tool to pinpoint which specific skills are responsible for each failure or cost increase.

## Key Contributions  
- Skill induced functional failures are rarely caused by obviously irrelevant skills; instead, seemingly relevant skills often make the agent incorrectly implement or omit task‑required implementation elements.  
- Skill‑induced efficiency regressions cannot be explained solely by longer prompts; other factors such as added verification steps and heavy pipelines drive token usage and execution time.  
- Within the “Excessive Procedure” category, excessive verification (67 cases) and heavy implementation pipelines (30 cases) are the largest contributors to both functional failures and efficiency regressions.

## Methodology  
The authors built a differential analysis framework that compares a target skill‑guided run against either a no‑skill baseline or a semantically matched reference run that solves the same task more cheaply. This approach is applied to two benchmark suites, SkillsBench and SWE‑Skills‑Bench, which contain thousands of skill‑task pairs. To automate attribution, they developed SkillTriage—a taxonomy‑driven tool that normalizes paired cases, extracts differential evidence, and generates concise triage reports.

## Results  
The analysis uncovered 307 skill‑induced failures across the combined benchmarks: 125 functional failures (e.g., incorrect output) and 182 efficiency regressions (higher token count or longer runtime). The most frequent failure sources are “Excessive Procedure,” with verification steps accounting for 67 cases and heavy implementation pipelines for 30. SkillTriage successfully attributed these outcomes, demonstrating that the same skill can cause both functional and cost problems.

## Significance  
These findings highlight a critical risk in LLM agent design: reusing skills without careful evaluation may degrade task success or inflate computational costs. The work underscores the need for safer, cost‑aware mechanisms to reuse guidance, informing future research on skill validation, attribution, and resource management.

## Related Concepts  
Agent Skills, LLM Agents, Differential Analysis Framework, SkillTriage Tool, SkillsBench Benchmark, SWE‑Skills‑Bench Benchmark, Excessive Procedure Category.

## Original Paper Reference

- [Read the original paper](http://arxiv.org/abs/2608.11888v1)
