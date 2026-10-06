---
title: Runaway Reaction: When Benign Skills Compose into Malicious Behavior
published: 2026-10-05T07:59:28Z
authors: Zunlong Zhou, Ziyuan Yang, Mengyu Sun, Yi Zhang
url: http://arxiv.org/abs/2610.05943v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Runaway Reaction: When Benign Skills Compose into Malicious Behavior

## Abstract
Agent skills package task-specific knowledge and procedures that can be composed to support complex agent tasks, while public marketplaces provide a growing pool of reusable skills. Existing security vetting, however, largely evaluates skills in isolation, leaving composition-induced risks underexplored. Such risks arise because composing benign skills expands the agent's capability space, enabling behaviors unavailable to any skill alone. Interestingly, we find that directly composing benign skills can already induce malicious behaviors, even when every individual skill passes security vetting. We further find that some target malicious behaviors remain difficult to realize through direct composition, even when the selected skills collectively provide the required capabilities. To systematically instantiate these attacks, we present Compositional Risk Induction via Multi skill Execution (CRIME). CRIME first uses the Malicious Plot Casting (MPC) module to decompose a target malicious behavior into complementary requirements and identify suitable benign skill compositions from public skill repositories. For compositions that cannot directly realize the target behavior, the Runaway Reaction Steering (RRS) module uses execution feedback to iteratively refine the selected skills toward the target while requiring each skill to remain benign under standalone vetting. The resulting composition is then passed to the Skill Reaction Chamber (SRC) module, where the skill pair is executed in a sandbox and the resulting environmental consequences are examined to determine whether the target behavior has occurred. Unsuccessful cases are returned to RRS for further refinement. Furthermore, we construct a benchmark of 4,000 public skills across eight cybersecurity behaviors for systematic evaluation of composition-induced vulnerabilities.

## Metadata
- **Published**: 2026-10-05T07:59:28Z
- **Authors**: Zunlong Zhou, Ziyuan Yang, Mengyu Sun, Yi Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05943v1)