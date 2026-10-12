---
title: Don't Guess, Just Ask: Evaluating Interactive Requirement Clarification for Repository-Level Software Development
url: http://arxiv.org/abs/2610.13022v1
type: paper-summary
date: 2026-10-11
source_paper: 2026-10-09_05-23-01Z_Don_tGuess_JustAsk_EvaluatingInteractiveRequiremen.md
generated_at: 2026-10-11 20:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ReqClarifyBench, an interactive benchmark designed to evaluate how well large language models can clarify vague user requirements before generating code at the repository level. The benchmark comprises 341 tasks across game, miniapp, and web development domains, each pairing a deliberately vague user intent with a human-validated requirement document and code evaluation artifacts. The authors evaluate six LLMs using LLM-based user simulators with diverse personas and find that stronger clarification effectiveness does not reliably lead to higher-quality requirement documents, and that coding-agent harnesses fail to improve document quality over their underlying base models.

## Key Takeaways
- The benchmark addresses a critical gap in existing evaluation frameworks: prior benchmarks assess code generation from complete or underspecified specifications, while prior clarification studies focus only on function-level tasks. ReqClarifyBench is the first benchmark to evaluate the full interactive requirement clarification process at the repository level, where misunderstandings can cascade into costly rework across an entire codebase.
- The evaluation reveals a significant disconnect between clarification effectiveness and document quality. An LLM that asks more questions or engages more interactively with a user simulator does not necessarily produce a more accurate or complete requirement document. Furthermore, performance varies substantially depending on the user persona simulated, meaning that an LLM's ability to clarify requirements is not uniform across different communication styles and levels of user expertise.
- Coding-agent harnesses, which wrap base LLMs with additional tooling and orchestration layers, do not further improve requirement document quality compared to the base LLMs alone. This finding challenges the assumption that adding scaffolding or agent frameworks inherently enhances an LLM's ability to elicit and structure requirements from vague user input.

## Context
As LLMs transition from generating isolated code snippets to handling repository-level software development, the bottleneck shifts from raw coding capability to understanding user intent. Real-world software projects rarely begin with perfectly specified requirements; instead, they start with vague descriptions that must be refined through dialogue. This paper sits at the intersection of human-computer interaction, software engineering, and LLM evaluation, addressing a stage of the development pipeline that existing benchmarks have largely ignored. By introducing persona-based user simulators and repository-scale tasks, the authors push evaluation beyond toy problems toward realistic development workflows.

## Implications
For practitioners building LLM-based end-to-end software development systems, these findings caution against assuming that more interactive clarification automatically yields better outcomes or that agent frameworks inherently improve requirement understanding. Teams deploying AI coding assistants should invest in persona-aware evaluation and direct measurement of requirement document quality rather than relying solely on clarification interaction metrics. The benchmark also provides a reusable evaluation resource for researchers seeking to improve how AI systems handle ambiguous, real-world software specifications before any code is written.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.13022v1)
