# Summary: 2026-05-22_17-59-50Z_SkillOpt_ExecutiveStrategyforSelf_EvolvingAgentSki.md
Saved: 2026-05-25 00:01
Source: 2026-05-22_17-59-50Z_SkillOpt_ExecutiveStrategyforSelf_EvolvingAgentSki.md
Model: None

---


## Summary  
SkillOpt proposes a systematic approach to treat agent‑skill capabilities as external state that can be optimized with the same rigor applied to neural weight spaces. By converting rollout scores into bounded edit operations (add, delete, replace) on a single skill document and only accepting edits that strictly improve a held‑out validation metric, SkillOpt creates a controllable text‑space optimizer for self‑evolving agents. The method eliminates inference‑time model calls at deployment while delivering measurable gains across multiple benchmarks and execution harnesses. This work is the first to achieve such stable, zero‑cost skill training on large language models.

## Key Contributions  
- [Finding 1] SkillOpt introduces a textual learning‑rate budget, rejected‑edit buffer, and epoch‑wise slow/meta updates that stabilize skill evolution without runtime model calls.  
- [Finding 2] The optimizer treats the skill document as an external state, converting rollout scores into bounded add/delete/replace edits accepted only when they improve validation performance.  
- [Finding 3] SkillOpt outperforms all human and automated skill‑evolution baselines on 52 (model, benchmark, harness) evaluation cells and improves average no‑skill accuracy by up to +24.8 points in Codex agentic loops.

## Methodology  
SkillOpt builds a lightweight optimizer model that monitors rollout scores of an agent’s skill execution. When the score exceeds the validation threshold, the system generates candidate edits—insertions, deletions, or replacements—in the skill text. A textual learning‑rate budget controls edit magnitude, while a rejected‑edit buffer prevents redundant changes. The process proceeds in epochs with slow initial updates followed by meta‑learning to fine‑tune the optimizer’s policy, all without invoking the large language model during training.

## Results  
Across six benchmarks, seven target models (including GPT‑5.5), and three execution harnesses (direct chat, Codex, Claude Code), SkillOpt is best or tied on every cell, outperforming human and automated skill baselines such as Trace2Skill, TextGrad, GEPA, and EvoSkill. On GPT‑5.5 it lifts no‑skill accuracy by +23.5 points in direct chat, +24.8 inside the Codex loop, and +19.1 inside Claude Code. Transfer experiments confirm that optimized skill artifacts retain performance when moved across model scales or between execution environments.

## Significance  
SkillOpt demonstrates that skills can be treated as external state objects subject to disciplined optimization, mirroring weight‑space training. By providing zero inference‑time cost at deployment and enabling cross‑model transferability, it opens a path toward truly self‑evolving agents whose capabilities improve reliably over time.

## Related Concepts  
skill optimization, external state of frozen agent, textual learning‑rate budget, rejected‑edit buffer, epoch‑wise slow/meta update, rollout scoring, edit acceptance criteria, self‑evolving skills, text‑space optimizer, benchmark evaluation cells.

[[SkillOpt: Executive Strategy for Self-Evolving Agent Skills]]