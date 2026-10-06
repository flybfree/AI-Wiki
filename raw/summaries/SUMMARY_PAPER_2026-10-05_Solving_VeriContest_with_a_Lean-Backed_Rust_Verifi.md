---
title: Solving VeriContest with a Lean-Backed Rust Verifier
url: http://arxiv.org/abs/2610.03994v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-02_19-56-10Z_SolvingVeriContestwithaLean_BackedRustVerifier.md
generated_at: 2026-10-05 22:08
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a method for solving the VeriContest benchmark—a collection of 1007 competitive-programming problems in Rust with Verus specifications—by translating the specifications and code into Lean 4 theorems and proving them using a Lean-backed Rust verifier called Rust-Prover. The authors successfully proved all 1325 theorems across all 1007 problems, achieving a 70% first-iteration success rate with Claude Opus 5.5 at a median cost of $1.17 per proof, dramatically outperforming the 13.95% first-attempt rate reported for frontier models using the native Verus proof-generation pipeline.

## Key Takeaways
- The authors translated every Verus specification and Rust solution into Lean 4, converting each specification into a provable theorem checked by Lean's kernel. All 1325 theorems across 1007 problems were proved, with 1259 completed in a single 32-hour run on Claude Opus 5.5 at a median of 3.2 minutes and $1.17 per proof, and 70% succeeded on the first iteration without retries.
- Rigorous validation confirmed correctness: restated specifications were checked against the benchmark's test suites and reviewed where no suite applies, with none found wrong or weakened. The translated Lean programs were executed on 21,413 benchmark test cases and produced identical output to the original Rust programs on every single case.
- A cross-model evaluation across four Claude and four GPT models at five reasoning-effort settings revealed that every current frontier model proves nearly all of a ten-theorem sample at every setting, and increasing reasoning effort raises cost without increasing the number of proofs. Notably, the cheapest configuration—Claude Sonnet 5.5 at low effort—proved all 50 hardest theorems, while the native Verus protocol with Claude Opus 5.5 failed on at least one of the 50 problems with the longest reference proofs.

## Context
This work sits at the intersection of formal verification, large language model reasoning, and competitive-programming benchmarks. VeriContest was designed to stress-test whether frontier models can generate machine-checked proofs for program correctness, a task where the Verus toolchain proved to be a severe bottleneck. By shifting the verification substrate from Verus to Lean 4 via Rust-Prover, the authors demonstrate that the proof-generation difficulty is substantially a tooling problem rather than a fundamental reasoning limitation of current models, reframing how the community should evaluate AI-assisted formal verification.

## Implications
For practitioners building verified software pipelines, this result suggests that translating specifications into a mature proof assistant like Lean 4 can unlock near-complete automated proof generation at low cost, making formal verification of competitive-programming-scale codebases tractable with commodity LLMs. For the AI research community, the finding that additional reasoning effort does not improve proof counts implies that current frontier models already saturate the reasoning capacity needed for these verification tasks, and progress should focus on tooling, specification translation, and cost efficiency rather than scaling model reasoning budgets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03994v1)
