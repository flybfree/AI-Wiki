---
title: PROBE: Frontier Coding Agents Find Different Bugs Than Maintainers Fix
url: http://arxiv.org/abs/2610.35987v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_12-04-46Z_PROBE_FrontierCodingAgentsFindDifferentBugsThanMai.md
generated_at: 2026-10-27 22:39
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces PROBE, a benchmark comprising all 2,457 bugs fixed over 18 months across 20 diverse GitHub repositories, designed to evaluate whether frontier coding agents can proactively discover the same bugs that human maintainers would repair. The authors find that all evaluated coding agents achieve recall below 21% and precision under 9% against the reference set, revealing a substantial gap between what agents can find and what maintainers actually fix. Notably, while stronger models improve recall from 8% to 17%, precision does not improve, and the distribution of bugs agents discover differs substantially from those maintainers address.

## Key Takeaways
- Frontier coding agents consistently fail to match human maintainer bug-finding capabilities, achieving recall below 21% and precision under 9% across all tested models. Scaling model capability increases recall from 8% to 17% but does not improve precision, suggesting that current architectures are not fundamentally better at identifying the specific bugs maintainers prioritize.
- Despite the low precision scores relative to the reference set, both LLM-based evaluators and human evaluators judge 85% of the agents' findings as valid bugs. This discrepancy indicates that the reference set captures only a partial view of real bugs and that agents are finding genuine issues that simply do not align with what maintainers chose to fix.
- The distribution of bugs discovered by coding agents is remarkably similar across different agents but diverges substantially from the distribution of bugs actually fixed by maintainers. This suggests agents converge on a particular class of bugs while systematically missing the categories that human developers prioritize in practice.

## Context
Proactive bug discovery is a critical software-engineering challenge, and coding agents are already widely deployed in this domain, yet their true capabilities for repository-wide bug finding remain understudied. Prior evaluations of coding agents have focused on generating patches for known bugs or solving isolated coding tasks, leaving the harder question of whether agents can independently identify the full set of bugs a human maintainer would repair largely unexamined. PROBE addresses this gap by constructing a comprehensive, longitudinal reference set from real-world repositories and providing a matching methodology to assess candidate findings against it.

## Implications
For practitioners deploying coding agents in production codebases, these findings caution against assuming that agents will surface the same issues human maintainers prioritize, meaning teams should not treat agent-generated bug reports as a substitute for human code review. For model developers, the benchmark provides a concrete, reproducible evaluation target that highlights where current architectures fall short, particularly in precision and in matching the bug-type distributions that matter in real software maintenance. The low recall across all frontier models underscores that proactive bug discovery remains an open research problem with significant practical relevance for software reliability and security.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35987v1)
