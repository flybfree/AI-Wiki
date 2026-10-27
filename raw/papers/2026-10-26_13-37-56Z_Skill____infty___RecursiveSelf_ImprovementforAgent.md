---
title: Skill$^{\infty}$: Recursive Self-Improvement for Agent Skill Optimization
published: 2026-10-26T13:37:56Z
authors: Wangcheng Tao, Zhanglu Yan, Han Wu, Weng-Fai Wong
url: http://arxiv.org/abs/2610.35434v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill$^{\infty}$: Recursive Self-Improvement for Agent Skill Optimization

## Abstract
Recursive self-improvement (RSI), in which a system also improves the way it improves, is a long-standing aspiration on the path to AGI. Language agents increasingly store procedural knowledge in reusable skills. Optimizing skills offers a direct way to achieve RSI, because the optimization procedure itself can be encoded as a skill. Existing skill optimizers, however, follow a hand-designed procedure. Even methods that evolve a meta-skill confine it to a fixed pipeline and relearn it for each task. We present Skill$^{\infty}$, which makes skill optimization recursively self-improving: a meta agent follows a meta-skill to optimize task skills and optimizes the meta-skill itself using the same procedure. The optimization is agent-led. The meta agent diagnoses execution traces, proposes candidates, requests independent reviews, and allocates the search budget. The meta-skill defines these steps, allowing self-improvement to rewrite them. This meta-skill is also decoupled from task skills, refined on multiple skill optimization tasks and then reused to optimize task skills across diverse domains. As in deployment, skills at both levels are standard packages loaded through native skill discovery. On 83 SkillsBench tasks, Skill$^{\infty}$ reaches a pass rate of 60.7%, compared with 56.4% for human-curated skills and 54.5% for SkillEvolver.

## Metadata
- **Published**: 2026-10-26T13:37:56Z
- **Authors**: Wangcheng Tao, Zhanglu Yan, Han Wu, Weng-Fai Wong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.35434v1)