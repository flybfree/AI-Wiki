# Summary: 2026-07-28_11-07-53Z_DoContextFilesHelpCodingAgents_ATwo_AgentAblationS.md
Saved: 2026-07-30 23:05
Source: 2026-07-28_11-07-53Z_DoContextFilesHelpCodingAgents_ATwo_AgentAblationS.md
Model: None

---

## Summary  
This paper investigates whether persistent context files such as AGENTS.md and CLAUDE.md improve the performance of two state‑of‑the‑art coding agents, Claude Code and Codex, on real‑world software repositories. By conducting a controlled ablation study across 17 tasks from three mixed repositories (15 shared and 2 exclusive to Codex) and 288 gold‑test evaluations, the authors show that injecting these context files yields no measurable gain in correctness for either agent—improvements are bounded at ≤ 10–15 percentage points. The study also uncovers a failure mode: agents struggle with implementation skill (feature design, pattern selection, wiring) rather than missing repository knowledge that could be supplied by the context file. Finally, the authors demonstrate that task difficulty is highly agent‑specific, with a Spearman correlation of 0.75 between tasks and each model’s informative band, offering an explanation for earlier contradictory findings.

## Key Contributions  
- [Finding 1] Context files do not measurably increase correctness on Claude Code or Codex; any improvement is statistically bounded to ≤ 10–15 pp via equivalence testing.  
- [Finding 2] Agents fail due to implementation skill deficits (feature design, pattern selection, exact wiring) rather than a lack of repository knowledge that context files could provide; the AGENTS.md file never converts a near‑miss into a pass on either model.  
- [Finding 3] Task difficulty correlates strongly with agent‑specific informative bands (Spearman ρ = 0.75), suggesting that single‑agent studies draw tasks from different agents’ informative ranges, which explains prior contradictions.

## Methodology  
The authors performed a two‑agent ablation study: they generated 17 real coding tasks from three repositories—two shared among Claude Code and Codex and one exclusive to Codex—and evaluated each task with both agents. Each run was scored by a gold‑test harness that measures exact correctness. The context file strategy (including AGENTS.md and CLAUDE.md) was either applied or removed, allowing an equivalence test to quantify any effect. A failure‑mode triage examined why tasks were failed, while a manipulation probe confirmed that the presence of the context file does not transform failures into successes.

## Results  
Correctness scores remained unchanged when context files were added (p > 0.05). The maximum observed improvement across all runs was 12 pp for Claude Code and 9 pp for Codex, both within the equivalence‑testing threshold. Failure analysis revealed that agents lacked proficiency in feature design and wiring rather than repository knowledge gaps. Moreover, a Spearman correlation of 0.75 between task difficulty and each agent’s informative band confirmed that tasks are not uniformly challenging across models.

## Significance  
These findings challenge the assumption that persistent context files universally aid coding agents; they reveal that effectiveness is limited to specific implementation skill gaps rather than knowledge retrieval. The agent‑specific informative band explains why earlier studies reported mixed results, guiding future work on task selection and model design for real repositories.

## Related Concepts  
persistent context files (AGENTS.md, CLAUDE.md), code generation agents, ablation study, gold‑test evaluation, equivalence testing, implementation skill vs. repository knowledge, informative band, Spearman correlation, failure‑mode triage, manipulation probe.
