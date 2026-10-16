---
title: SkillNEO: Non-Elitist Evolutionary Optimization of Agent Skills
url: http://arxiv.org/abs/2610.20926v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_20-57-26Z_SkillNEO_Non_ElitistEvolutionaryOptimizationofAgen.md
generated_at: 2026-10-15 22:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SkillNEO introduces a non-elitist evolutionary optimization framework for improving LLM agent skills, where intermediate versions that score below their predecessors are retained and further refined rather than discarded. Across 86 SkillsBench tasks spanning eight domains, the method raises GPT-5.4 Mini's average reward from 49.1% to 66.4%, and the resulting skills transfer to stronger models like GPT-5.5 and GPT-5.6 Luna, improving their performance by over 10 percentage points without additional editing.

## Key Takeaways
- Non-elitist evolution decouples the selection of a version to use from the selection of versions to keep improving, allowing low-reward intermediate versions to receive further edits. This addresses a critical failure mode in elitist approaches where partial repairs that have not yet yielded immediate reward gains are prematurely discarded, even though their benefits would emerge after additional interdependent edits.
- SkillNEO compares how related versions perform the same task to identify working steps that should be preserved and remaining failures that need fixing, and it can revisit earlier versions using evidence gathered from later iterations. This evidence-driven approach provides concrete guidance on what to keep and what to repair next, rather than relying solely on scalar reward scores.
- Skills evolved by a weaker model (GPT-5.4 Mini) transfer to stronger models without further editing: on 41 tasks with modified skills, reuse improves Luna by 10.5 percentage points and places GPT-5.5 10.6 points above its published original-skill reference. Execution records confirm these skills benefit stronger models even when Mini still fails some task requirements, demonstrating that partial procedural progress from weaker agents constitutes reusable knowledge.

## Context
This work sits at the intersection of LLM agent skill libraries, evolutionary search, and transfer learning for procedural knowledge. Prior skill-evolution methods typically apply elitist selection, keeping only the highest-scoring version at each generation, which mirrors classical evolutionary algorithms but is poorly suited to agent skills where improvements require multi-step, interdependent edits. SkillNEO reframes skill optimization as a non-elitist search guided by task-level execution evidence, a shift that parallels how human experts iteratively refine procedures by preserving working components while targeting specific failure modes.

## Implications
For practitioners building agentic systems, SkillNEO demonstrates that skill libraries can be bootstrapped from cheaper, weaker models and then deployed to more capable agents, reducing the compute cost of skill development while still improving downstream performance. The non-elitist selection strategy also suggests that current agent-training pipelines should avoid discarding intermediate skill versions based on immediate reward alone, since useful partial repairs may only become apparent after subsequent edits. For the broader field, the finding that a weaker model's partial progress can be converted into reusable procedural knowledge for stronger agents opens a practical pathway for scalable, cost-efficient agent skill curation across diverse task domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20926v1)
