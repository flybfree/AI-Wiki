---
title: WEAVE: Weaving Real-World Code Evolution into Dependency-Structured Tasks for Benchmarking and Training Code Agents
url: http://arxiv.org/abs/2610.22039v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_15-12-56Z_WEAVE_WeavingReal_WorldCodeEvolutionintoDependency.md
generated_at: 2026-10-15 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
WEAVE is a framework that transforms verified pull request histories from real-world repositories into executable, dependency-structured tasks for benchmarking and training code agents. By organizing related PRs into bounded directed acyclic graphs (DAGs) using repository-calibrated typed change loci, WEAVE creates unified executable tasks that preserve the natural dependencies among code changes. The paper introduces Graph Credit, a deterministic test-grounded metric for measuring dependency-consistent partial progress, and demonstrates through experiments in task construction, agent evaluation, supervised fine-tuning, and reinforcement learning that WEAVE produces coherent tasks, more faithful progress measurement, and effective training signals for long-horizon code agents.

## Key Takeaways
- Existing repository-level benchmarks treat single issues or PRs as isolated task units, while multi-PR settings rely on coarse aggregation and structure-agnostic evaluation. This mismatch obscures the real dependencies among coordinated changes across a repository, limiting both progress measurement and learning signals for long-horizon code agents. WEAVE addresses this gap by leveraging repository-calibrated typed change loci to organize related PRs into bounded DAGs, instantiating each as a unified executable task that faithfully mirrors how real software engineering unfolds across multiple coordinated modifications.
- The Graph Credit metric provides a deterministic, test-grounded way to measure dependency-consistent partial progress rather than relying on flat scoring. This enables dense, verifiable rewards suitable for reinforcement learning training, giving code agents granular feedback at each stage of a multi-step task rather than only a binary pass/fail signal at the end.
- Experiments spanning task construction, agent evaluation, supervised fine-tuning, and reinforcement learning confirm that WEAVE yields coherent executable tasks, enables more faithful progress measurement than flat scoring approaches, and provides effective supervision and verifiable rewards for training code agents, demonstrating practical utility across multiple training paradigms.

## Context
The field of code agent research has advanced rapidly, with benchmarks like SWE-bench establishing evaluation standards for single-issue repository tasks. However, real-world software engineering—feature development, large-scale migrations, and systematic bug fixes—almost never happens in isolated single-PR changes. The gap between how benchmarks are structured and how software actually evolves has constrained progress measurement and limited the training signals available for agents that must handle long-horizon, multi-step coding tasks. WEAVE bridges this gap by grounding benchmark construction in verified PR histories and dependency structures, aligning evaluation and training more closely with authentic software development workflows.

## Implications
For practitioners building and evaluating code agents, WEAVE offers a path toward more realistic benchmarks that capture the coordinated, multi-PR nature of real software engineering, enabling more meaningful progress tracking and fairer comparisons between agent systems. For the training pipeline, the Graph Credit metric and dependency-structured task construction provide dense, verifiable reward signals that can improve reinforcement learning and supervised fine-tuning for agents handling complex, multi-step repository modifications. This work signals a shift in the field from isolated single-task evaluation toward structured, dependency-aware benchmarking that better reflects the long-horizon reasoning and coordination capabilities code agents need to be genuinely useful in production software environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22039v1)
