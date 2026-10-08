---
title: Cost-Efficient Theorem Proving via Agent Orchestration in Program Verification
url: http://arxiv.org/abs/2610.09681v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_08-42-24Z_Cost_EfficientTheoremProvingviaAgentOrchestrationi.md
generated_at: 2026-10-07 21:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
CoCo-Prover introduces a framework for cost-efficient program verification that reframes theorem proving as metalevel decision-making under explicit cost constraints, rather than pursuing pass rates at any computational budget. By combining two-level proof graphs with an agentic router that orchestrates heterogeneous specialist agents as separately priced computations, the system achieves the best solve rate across five Lean 4 benchmarks while reducing cost by up to 30.9% compared to the strongest baseline.

## Key Takeaways
- The paper identifies a critical gap in existing program verification research: almost all provers optimize solely for pass rates regardless of sampling or search budget, ignoring the success-versus-cost frontier. At scale, real software carries hundreds of interdependent proof obligations, making economic efficiency as important as raw provability. CoCo-Prover formalizes this as a metalevel decision problem where each step answers which open goals to select and which actions to purchase on those goals.
- The architecture rests on two-level proof graphs: an AND/OR proof hypergraph captures the internal structure of each declaration, while a lemma-dependency graph links declarations across the repository. Goal selection remains symbolic as a topological pass over these graphs, while action choice is handled through agent orchestration where an agentic router treats every bounded specialist invocation as a separately priced, best-effort computation, evolving routing rules as evidence accumulates.
- Empirical evaluation on five Lean 4 benchmarks—function-level CLEVER, VERINA, and AlgoVeri, plus repository-level NTP4VC and Vero—demonstrates that CoCo-Prover achieves the best solve rate on every benchmark, reaching up to 100% on two, while simultaneously reducing cost by up to 30.9% relative to the strongest baseline using the strongest LLM in the evaluation.

## Context
This work sits at the intersection of automated theorem proving, LLM-based program verification, and multi-agent orchestration. As large language models increasingly generate production code, the need for machine-checkable correctness guarantees has become urgent, yet current verification pipelines treat proof search as an unbounded resource problem. CoCo-Prover's contribution is to bring explicit economic reasoning into the proving loop, aligning with broader AI research trends around cost-aware planning, tool-use orchestration, and resource-constrained decision-making in agentic systems.

## Implications
For practitioners deploying LLM-generated code in safety-critical domains, CoCo-Prover offers a practical path to verifying large codebases without prohibitive computational expense, making formal guarantees feasible at repository scale rather than only at the level of individual functions. For the research community, the paper establishes a new evaluation axis—success-versus-cost frontier—that future provers and coding agents should be measured against, potentially reshaping how benchmarking and tool design evolve in the program verification and software engineering AI ecosystems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09681v1)
