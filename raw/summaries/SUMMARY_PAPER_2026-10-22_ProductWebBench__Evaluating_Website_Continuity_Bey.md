---
title: ProductWebBench: Evaluating Website Continuity Beyond Task Completion
url: http://arxiv.org/abs/2610.31118v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_11-33-00Z_ProductWebBench_EvaluatingWebsiteContinuityBeyondT.md
generated_at: 2026-10-22 21:34
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ProductWebBench introduces a benchmark that evaluates frontend coding agents not only on whether they complete a requested task, but also on whether the rest of the website continues to function correctly after the change. Across 8,737 evaluation runs from 13 models, the authors demonstrate that 28.2% of runs passing all requested-work checks still fail continuity checks such as blank routes, horizontal overflow, or console errors, revealing a critical gap in how current agents are assessed.

## Key Takeaways
- The benchmark defines "website continuity" as a second obligation beyond task completion: after a code change, the rest of the site must keep working. ProductWebBench operationalizes this through 320 Change tasks on existing repositories and 80 long-horizon Build tasks, each frozen with a repository snapshot, staged requirements, browser evidence, and deterministic checks before evaluation begins.
- A key finding is that 10.8% of runs push a browser state they had already passed back to failing, meaning agents regress previously verified functionality. Because the same checks run on the untouched repository, each regression carries exact provenance rather than a post-hoc label, and 18.3% of runs where both readings exist are caught breaking a verified state.
- Interaction failures represent a further blind spot: 29.5% of runs whose static DOM already passes still fail interaction checks, showing that agents can produce structurally valid HTML that breaks user-facing behavior. The benchmark uses a simulated user who reveals requirements one stage at a time, and every previously cleared check stays armed for the remainder of the run, enforcing cumulative correctness.

## Context
Current benchmarks for frontend coding agents, such as those evaluating single-page generation or isolated component creation, measure only whether a target artifact is produced. This paper addresses a gap in the AI evaluation landscape by shifting the unit of assessment from a single deliverable to a living system, reflecting how real engineering work operates within existing codebases. The staged-requirement design and persistent check-arming mechanism mirror realistic development workflows where incremental changes must not degrade previously verified functionality.

## Implications
For practitioners building or deploying frontend coding agents, these results indicate that task-completion scores alone are insufficient for production use, since nearly a third of otherwise "successful" runs introduce regressions or break interactive behavior. Industry teams relying on AI-assisted development should adopt continuity-aware evaluation pipelines that run regression checks against untouched baselines and test interaction, not just static DOM structure. The benchmark's provenance-tracking design also offers a template for future agent evaluation frameworks that need to attribute failures precisely rather than labeling them after the fact.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31118v1)
