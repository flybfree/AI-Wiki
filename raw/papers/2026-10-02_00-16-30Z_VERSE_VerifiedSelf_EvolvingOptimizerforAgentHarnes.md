---
title: VERSE: Verified Self-Evolving Optimizer for Agent Harnesses
published: 2026-10-02T00:16:30Z
authors: Zekai Wang, Yingqiang Ge, Zekun Wang, Hai Wang, Yuhui Xu, Joshua Frandsen, Shancong Fu, Ashia C. Wilson, Chandan K. Reddy
url: http://arxiv.org/abs/2610.02616v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VERSE: Verified Self-Evolving Optimizer for Agent Harnesses

## Abstract
Harness evolution improves an LLM agent's prompts, tools, and workflow, while the optimizer's own tools and procedures often remain fixed. We study whether an optimizer can improve another agent more effectively by also improving how it diagnoses failures, develops edits, and tests their effects. Two observations guide our design. In a controlled study, optimizer self-evolution fails to improve performance without execution-based verification, but achieves the best result of that study when verification is available. Across five executors, self-evolving optimizers build their own tools for failure analysis, verification, training audits, and workflow control. Motivated by these findings, we introduce VERSE, a Verified Self-Evolving optimizer for agent harnesses. VERSE lets the optimizer test draft edits, replay failures, and perturb suspected steps before submission, while tracking fixes and regressions across rounds. Using this feedback, the optimizer revises both the executor harness and its own prompts, skills, tools, hooks, and notes, while the weights of the optimizer and executor models stay fixed. Under a shared protocol with disjoint training, validation, and test tasks, VERSE improves all four evaluated harness optimizers on held-out SWE-rebench tasks and newer out-of-distribution tasks in five languages. Its best validation-selected harness reaches 42.3% and 37.7% accuracy, respectively, against 39.2% and 29.3% for the strongest baselines. Code is available at https://github.com/wzekai/VERSE.

## Metadata
- **Published**: 2026-10-02T00:16:30Z
- **Authors**: Zekai Wang, Yingqiang Ge, Zekun Wang, Hai Wang, Yuhui Xu, Joshua Frandsen, Shancong Fu, Ashia C. Wilson, Chandan K. Reddy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02616v1)