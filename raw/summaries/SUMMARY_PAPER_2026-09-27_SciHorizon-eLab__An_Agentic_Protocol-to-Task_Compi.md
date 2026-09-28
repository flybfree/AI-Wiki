---
title: SciHorizon-eLab: An Agentic Protocol-to-Task Compiler for Scalable Benchmarking of Scientific Embodied Agents
url: http://arxiv.org/abs/2609.30971v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-25_08-18-45Z_SciHorizon_eLab_AnAgenticProtocol_to_TaskCompilerf.md
generated_at: 2026-09-27 21:22
model: qwen3.6-35b-a3b
---

## Summary
SciHorizon-eLab introduces an agentic protocol-to-task compiler that automates the conversion of natural-language scientific protocols into executable, verifiable embodied tasks, addressing the scalability limitations of manual task engineering in current benchmarks. The system generates a benchmark named \BenchName comprising 300 certified tasks across diverse laboratory operations, utilizing semantic grounding and multi-stage simulation certification to ensure reproducibility and step-level evaluation. Empirical results indicate significant challenges for existing models, with the strongest policy achieving only a 49.7% average success rate and revealing pronounced weaknesses in human-embodied agent coordination.

## Key Takeaways
- SciHorizon-eLab formulates embodied task construction as a compilation problem, employing an agentic pipeline that progressively transforms natural-language protocols into semantic-preserving tasks through semantic grounding, executable program synthesis, and rigorous multi-stage simulation-based certification to guarantee verifiability.
- The authors release \BenchName, a ready-to-use benchmark of 300 certified tasks supporting Human-in-the-Loop execution, reproducible generation of expert demonstrations and execution traces, and ordered step-level evaluation to enable systematic assessment of scientific embodied agents.
- Evaluation across representative tasks exposes critical performance gaps, as the best-performing policy attains an average success rate of just 49.7%, highlighting substantial deficiencies in coordinating human instructions with robotic manipulation capabilities within complex laboratory workflows.

## Context
The advancement of embodied AI for automating scientific experimentation is currently impeded by the absence of reliable, systematic evaluation environments that can scale beyond manual task creation. This work addresses a fundamental bottleneck in the field by providing a methodological framework to compile diverse protocols into executable tasks at scale, thereby enabling rigorous benchmarking of agents required to interpret complex instructions and perform precise physical operations in laboratory settings.

## Implications
The public release of SciHorizon-eLab and \BenchName provides researchers and practitioners with a standardized toolkit for developing and evaluating robotic agents capable of autonomous scientific work, facilitating

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30971v1)
