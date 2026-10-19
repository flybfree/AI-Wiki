---
title: OfficeTown: Generative Organizations for Evolving Agent Intelligence
url: http://arxiv.org/abs/2610.23194v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_09-32-16Z_OfficeTown_GenerativeOrganizationsforEvolvingAgent.md
generated_at: 2026-10-18 20:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
OfficeTown introduces a generative simulation framework that models professional organizations where tasks, context, and feedback emerge from continuing organizational work rather than isolated prompts. The authors construct OfficeTown Bench, comprising 406 tasks and 4,836 evaluation criteria across 23 simulated organizations in eight professional domains, and demonstrate that training on this organizational data substantially improves frontier models on external professional-work benchmarks such as GDPval, while revealing significant remaining headroom for current frontier models.

## Key Takeaways
- OfficeTown simulates organizations from natural-language descriptions, initializing members who coordinate work, delegate bounded assignments to assistant agents, and review deliverables. Artifacts, decisions, and unresolved matters persist across assignments, while responsibilities and permissions govern what each member can see and do, creating a realistic organizational memory and access-control structure that mirrors real professional environments.
- The benchmark OfficeTown Bench was curated with domain-expert feedback across 23 simulated organizations spanning eight professional domains, producing 406 tasks and 4,836 evaluation criteria. Frontier-model evaluations on this benchmark reveal substantial remaining headroom, indicating that current generalist agents still struggle significantly with multi-step, context-dependent professional work that requires organizational awareness and iterative refinement.
- Supervised fine-tuning and on-policy distillation on OfficeTown data substantially improve Qwen3.5-9B on external professional-work benchmarks including GDPval, and supplementary evaluations confirm that the principal–assistant harness (where a principal delegates to assistant agents) achieves higher scores than single-agent and multi-agent baselines, validating the organizational delegation structure as an effective training and inference paradigm.

## Context
Current AI agent research largely evaluates models on isolated tasks or static benchmarks, failing to capture how professional work accumulates context, decisions, and feedback over time within organizational hierarchies. OfficeTown addresses this gap by generating work-grounded data and environments through simulation, offering a scalable pipeline for producing training and evaluation resources that reflect the continuity, delegation, and review dynamics of real workplaces. This positions organizational simulation as a new axis for agent development beyond tool-use or single-task reasoning.

## Implications
For practitioners building generalist agents, OfficeTown demonstrates that training on organizationally structured, multi-step professional data yields transferable improvements on external benchmarks, suggesting that future agent development should incorporate persistent context, role-based permissions, and iterative review loops rather than treating each task in isolation. For industry, the framework provides a reproducible method to generate domain-specific evaluation suites with expert-curated criteria, enabling more rigorous and realistic assessment of agent capabilities before deployment in professional settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23194v1)
