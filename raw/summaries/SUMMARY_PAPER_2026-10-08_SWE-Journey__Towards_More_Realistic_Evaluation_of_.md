---
title: SWE-Journey: Towards More Realistic Evaluation of Coding Assistants through Long-Horizon, Multi-Turn Interaction
url: http://arxiv.org/abs/2610.11559v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_09-21-49Z_SWE_Journey_TowardsMoreRealisticEvaluationofCoding.md
generated_at: 2026-10-08 21:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SWE-Journey introduces a new benchmark designed to evaluate coding assistants like Claude Code and Codex under conditions that more closely mirror real-world software development workflows, specifically addressing gaps in task horizon length and multi-turn interaction realism. The paper finds that while models achieve over 75% test pass rates when interacting with software architects, performance drops below 25% when interacting with non-coders, revealing a significant capability gap in supporting users who lack technical expertise.

## Key Takeaways
- The authors propose a weak-to-strong synthesis pipeline that automatically constructs long-horizon coding tasks, addressing the critical gap between short, isolated benchmark problems and the extended chains of development work that real coding assistants must handle in continuously evolving repositories. This pipeline enables the creation of tasks that span multiple development stages rather than single-file edits.
- To address the interaction gap, the team mined four representative user personas from real interaction data and built a user-simulation agent that reproduces realistic code-assistance interactions, including requirement clarification, iterative adaptation, and multi-turn dialogue. This moves evaluation beyond single-prompt scenarios toward the conversational dynamics that actual users experience.
- The evaluation identifies three key capabilities during interaction: asking right (formulating appropriate questions), finding right (locating correct code or solutions), and fixing right (implementing correct modifications). These capabilities are the primary bottlenecks explaining why coding assistants fail to support non-coders reliably, despite performing adequately for expert users.

## Context
Current coding assistant benchmarks such as SWE-bench evaluate models on isolated bug-fixing tasks with single-turn interactions, which poorly reflects how developers and non-developers actually use tools like Claude Code and Codex in production environments. As LLM agents increasingly serve as primary interfaces for software development, the community needs evaluation frameworks that capture the full complexity of long-horizon project work and the heterogeneous skill levels of real users. SWE-Journey fills this evaluation gap by combining automated task synthesis with realistic user simulation.

## Implications
For practitioners building coding assistants, these findings signal that current systems are not yet reliable enough to serve non-coders as primary development tools, and that improving interaction quality—particularly question-asking and iterative correction—is as important as raw code-generation capability. For the broader AI research community, the benchmark provides a more rigorous and realistic evaluation standard that will likely drive future model development toward better multi-turn reasoning and user-adaptive behavior rather than optimizing for single-shot code completion.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11559v1)
