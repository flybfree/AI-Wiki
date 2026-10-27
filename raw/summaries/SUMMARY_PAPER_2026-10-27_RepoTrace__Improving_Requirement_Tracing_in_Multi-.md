---
title: RepoTrace: Improving Requirement Tracing in Multi-Round Agent Interactions
url: http://arxiv.org/abs/2610.35333v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_12-30-22Z_RepoTrace_ImprovingRequirementTracinginMulti_Round.md
generated_at: 2026-10-27 00:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces RepoTrace, a requirement-driven repository understanding harness designed to address the degradation of code agents during multi-round software engineering interactions. By analyzing 2,656 agent trajectories from EvoCode-Bench, the authors identify "requirement focus misalignment" as a recurring failure pattern where agents confuse primary modification targets with unrelated code. RepoTrace constructs a requirement-code correspondence by combining repository structure with requirement semantics, injecting this mapping into the agent context to help agents trace requirements across iterative interactions. The approach yields substantial improvements in per-round reward scores across multiple models and agent harnesses while significantly reducing regression errors.

## Key Takeaways
- The authors analyzed 2,656 agent trajectories in EvoCode-Bench and identified "requirement focus misalignment" as a systematic failure pattern, where agents struggle to distinguish the primary modification targets of a requirement from unrelated code in the repository, leading to degraded performance as interaction rounds increase.
- RepoTrace works by combining repository structure with requirement semantics to construct a requirement-code correspondence that is injected into the agent context, enabling code agents to follow repository architecture, trace requirements across multi-round interactions, and identify core code elements corresponding to the current requirement.
- Experimental results demonstrate significant performance gains: RepoTrace improves mean per-round reward by +19.99 on GLM-5.2 and +10.22 on Claude Code, increases average per-round reward from 0.163 to 0.371 on Terminus-2 with DeepSeek-V4-Pro across rounds, and reduces average regression errors by 56.78%, demonstrating effectiveness across different models and agent harnesses.

## Context
This paper addresses a critical bottleneck in the emerging field of autonomous code agents and AI-assisted software engineering. As large language model-based agents are increasingly deployed for iterative software maintenance and modification tasks, their performance degrades over multiple interaction rounds due to an inability to maintain coherent understanding of requirements and code relationships. This work sits at the intersection of software engineering automation, agent-based AI systems, and repository understanding, contributing to the broader challenge of making AI agents reliable for sustained, multi-step software engineering workflows rather than single-shot code generation tasks.

## Implications
For practitioners building AI-powered software development tools, RepoTrace offers a practical harness-level intervention that improves agent reliability without retraining models, making it applicable across diverse model backends and agent frameworks. The 56.78% reduction in regression errors is particularly significant for industry adoption, as maintaining existing software integrity during iterative modifications is a core requirement in production environments. By releasing source code and agent trajectories, the authors enable reproducible benchmarking and further research into agent context management strategies, potentially accelerating progress toward autonomous software maintenance systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35333v1)
