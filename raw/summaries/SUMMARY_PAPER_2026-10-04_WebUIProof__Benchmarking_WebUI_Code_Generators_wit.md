---
title: WebUIProof: Benchmarking WebUI Code Generators with UI-Agent Execution Harness
url: http://arxiv.org/abs/2610.02617v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_00-17-11Z_WebUIProof_BenchmarkingWebUICodeGeneratorswithUI_A.md
generated_at: 2026-10-04 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
WebUIProof introduces an execution-oriented benchmark for evaluating WebUI code generation that moves beyond static checks like build success or screenshot comparisons. The benchmark provides structured specifications paired with dense, executable interaction tests across general WebUIs and 3D interactive simulations, evaluated through a UI-agent harness that iteratively plans, acts, observes, and asserts in a headless browser. The authors find that even when pages render successfully, commercial LLMs frequently fail on interaction-based requirements, particularly for 3D simulation interfaces, and demonstrate that RL training with executable interaction test rewards can improve functional completion in compact models.

## Key Takeaways
- WebUIProof addresses a critical gap in existing benchmarks by replacing free-form prompts and static validation (build success, visual screenshots) with structured specifications and executable interaction tests that verify functional correctness under actual user interaction, covering two task families: general WebUIs such as dashboards, games, and interactive tools, and 3D interactive simulations including particle systems, galaxy simulations, and physics dynamics.
- The UI-agent harness operates through an iterative plan-act-observe loop in a headless browser, locating DOM elements, performing user-like actions, observing resulting UI and DOM state changes, and checking specified assertions, enabling outcome-level evaluation rather than superficial rendering checks.
- Evaluation across eight commercial LLMs reveals frequent failures on interaction-based requirements even when pages compile and render successfully, with 3D simulation interfaces showing particularly poor performance. However, the harness can serve as a training signal: RL fine-tuning of compact models like Qwen2.5 14B and MIMO 7B using rewards derived from executable interaction tests improves functional completion rates while simultaneously reducing build failures.

## Context
This paper sits at the intersection of code generation evaluation and interactive UI testing, a growing concern as LLMs are increasingly deployed to generate front-end code for applications, dashboards, and simulations. Prior benchmarks in code generation have largely focused on static correctness—whether code compiles or produces a visually plausible output—leaving a significant blind spot around whether generated interfaces actually function correctly when users interact with them. WebUIProof fills this gap by operationalizing functional correctness through executable tests, aligning evaluation methodology with how users actually experience software.

## Implications
For practitioners building AI-assisted development tools, this work signals that current LLMs cannot be trusted to produce functionally correct interactive UIs without execution-based validation, underscoring the need for automated testing pipelines in AI code-generation workflows. For the research community, the UI-agent harness offers a reusable evaluation infrastructure and a novel RL reward signal derived from interaction tests, potentially enabling more capable smaller models to be trained specifically for interactive code generation rather than relying solely on large commercial LLMs. Industry teams deploying generative UI tools should treat rendering success as insufficient and adopt interaction-level testing before shipping AI-generated interfaces to end users.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02617v1)
