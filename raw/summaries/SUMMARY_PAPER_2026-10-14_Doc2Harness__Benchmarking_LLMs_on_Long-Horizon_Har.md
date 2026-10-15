---
title: Doc2Harness: Benchmarking LLMs on Long-Horizon Harness Engineering of Coding Agents
url: http://arxiv.org/abs/2610.20344v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_15-24-39Z_Doc2Harness_BenchmarkingLLMsonLong_HorizonHarnessE.md
generated_at: 2026-10-14 21:51
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Doc2Harness introduces the first deterministic benchmark specifically designed to evaluate how well large language models perform long-horizon harness engineering for coding agents, rather than merely measuring task success under a fixed harness. The benchmark operates in two stages: a build model constructs a complete candidate harness from an interface-only contract skeleton and a consolidated development document, and then the frozen harness is evaluated end-to-end across 328 test cases using four observable channels. Across nineteen frontier models, GPT-6 Astra achieved the highest pass rate at 53.05%, while the weakest model scored 27.44%, revealing a roughly 26-percentage-point gap and demonstrating that even the strongest model fails nearly half of all test cases.

## Key Takeaways
- Doc2Harness shifts the evaluation target from downstream task performance to harness engineering itself, which is the process of designing the scaffolding, tool interfaces, file management, and execution environment that wrap around a model. This is a critical distinction because existing benchmarks assume a fixed harness and thus cannot measure whether a model can build a correct harness from scratch.
- The benchmark's two-stage design enforces isolation: Stage 1 builds a candidate harness in a dedicated container using only an interface contract and a development document consolidating behavior across twelve frontier harnesses, while Stage 2 runs the frozen harness in separate containers driven by a scripted mock model. Scoring relies on four observable channels—requests sent to the model, files on disk, process exit codes, and command output—with positive controls to prevent vacuous passes, ensuring deterministic and reproducible evaluation.
- Failures cluster around how cross-cutting functionality is split across modules, indicating that the hardest part of harness engineering is not implementing individual components but correctly distributing shared logic such as error handling, state management, and tool routing across multiple modules. The 26-percentage-point spread between the best and worst models underscores that harness engineering remains a largely unsolved capability gap across current frontier models.

## Context
As LLM-driven agents are increasingly deployed on long-horizon coding tasks that require modifying real workspaces, invoking tools, and maintaining state across many steps, the quality of the surrounding harness—its tool definitions, file I/O handling, sandboxing, and orchestration logic—becomes as consequential as the underlying model's reasoning ability. Prior benchmarks such as SWE-bench or HumanEval evaluate agents under a fixed, human-designed harness, which conflates model capability with harness quality and leaves the engineering of the harness itself entirely unmeasured. Doc2Harness fills this gap by providing a deterministic, reproducible protocol that isolates harness construction from downstream task execution, enabling researchers to attribute failures specifically to harness design rather than to model reasoning.

## Implications
For AI researchers and benchmark developers, Doc2Harness establishes a new evaluation axis that can guide the design of next-generation agent scaffolds and inform which model capabilities are most limiting for autonomous software engineering. For industry practitioners deploying coding agents in production, the finding that even the strongest model fails nearly half of harness-engineering test cases—particularly around cross-cutting module decomposition—suggests that current agent frameworks still require substantial human-designed scaffolding and that fully autonomous harness construction is not yet viable. The benchmark's deterministic scoring channels and positive controls also offer a template for building more rigorous, reproducible agent evaluations beyond the current generation of task-success metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20344v1)
