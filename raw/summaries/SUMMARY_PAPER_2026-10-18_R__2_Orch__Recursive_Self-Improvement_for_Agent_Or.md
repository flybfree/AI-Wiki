---
title: R$^2$Orch: Recursive Self-Improvement for Agent Orchestration via Self-Play within a Skill-Internalization Loop
url: http://arxiv.org/abs/2610.22740v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_23-21-21Z_R__2_Orch_RecursiveSelf_ImprovementforAgentOrchest.md
generated_at: 2026-10-18 20:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
R²Orch introduces a recursive self-play orchestration framework that addresses three persistent challenges in agentic orchestration learning: hand-designed curricula, advantage collapse when task rollouts converge to identical outcomes, and unreliable single-score evaluation of individual skills. The paper proposes a dual-loop architecture where an inner self-play loop improves the orchestrator on self-chosen tasks while an outer loop refines how the inner loop itself improves, ultimately driving the orchestrator toward zero-skill deployment. Experiments across twelve datasets spanning question answering, mathematics, code generation, and interactive tasks demonstrate consistent outperformance over existing baselines.

## Key Takeaways
- The paper introduces Recursive Learnability as a novel training objective that rewards a Proposer agent for selecting tasks whose rollouts continue to produce diverse outcomes even as individual skills are progressively withdrawn. This directly combats advantage collapse, a failure mode where all rollouts for a given task yield the same result, rendering reinforcement learning signals uninformative and stalling the orchestrator's progress.
- Skill Withdrawal operates within the outer loop: once a controlled evaluation inside self-play confirms that the orchestrator achieves equivalent performance without a particular skill, that skill is removed from the active skill set. This mechanism transforms skills from permanent crutches into temporary scaffolding, forcing the orchestrator to internalize capabilities into its parameters rather than relying on an ever-growing library of external skills.
- The two loops form a closed recursive cycle in which failures are distilled into new skills, skills are distilled into model parameters, and skill withdrawals prompt the Proposer to generate new failure-inducing tasks. This cycle drives the system toward zero-skill deployment, meaning the orchestrator eventually performs all tasks using only its internalized parameters without any external skill library.

## Context
Agentic orchestration has become a dominant paradigm for decomposing complex human tasks into subtasks handled by specialized agents, yet most orchestration training pipelines depend on manually curated task curricula and brittle reward signals. The broader AI research community has been grappling with how to make multi-agent systems learn autonomously without human-designed scaffolding, and R²Orch contributes a principled mechanism for self-directed curriculum generation and skill internalization. By framing orchestration improvement as a recursive process rather than a single training run, the work connects to active research in self-play, curriculum learning, and model distillation within agent systems.

## Implications
For practitioners building agentic systems, R²Orch offers a path toward reducing dependence on hand-engineered task curricula and skill libraries, which are costly to maintain and often brittle under distribution shift. The zero-skill deployment trajectory suggests that future orchestration systems could become more compact and self-contained, potentially lowering inference overhead and simplifying deployment in production environments. For the research community, the Recursive Learnability objective and Skill Withdrawal mechanism provide reusable components that could be adapted to other self-improving agent architectures, including tool-use agents, code-generation pipelines, and multi-agent planning systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22740v1)
