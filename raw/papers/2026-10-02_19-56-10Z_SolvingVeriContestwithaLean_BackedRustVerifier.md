---
title: Solving VeriContest with a Lean-Backed Rust Verifier
published: 2026-10-02T19:56:10Z
authors: Traian Serbanuta, Jun Xu, Andrei Stefanescu, Cosmin Radoi
url: http://arxiv.org/abs/2610.03994v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Solving VeriContest with a Lean-Backed Rust Verifier

## Abstract
VeriContest is a benchmark of 1007 competitive-programming problems in Rust, each with a Verus specification, a judge-accepted solution, and a Verus proof. Its authors report that proof generation is the bottleneck for frontier models: given the specification and the code, the best model produces an accepted Verus proof for 13.95% of the problems on the first attempt. We report on solving the same proof-generation task with Rust-Prover, a verifier for Rust backed by Lean 4. The Verus specification and the Rust code are restated and translated into Lean, each specification becomes a theorem, and agents prove the theorems with Lean's kernel as the final check. All 1325 theorems of all 1007 problems were proved. 1259 of them were proved in one run of under 32 hours on Claude Opus 5.5, at a median of 3.2 minutes and $1.17 per proof, and 70% of them on the first iteration. The restated specifications were checked against the benchmark's test suites, and reviewed where no suite applies. None was wrong or weakened. The translated Lean programs were run on 21,413 of the benchmark's test cases and produced the same output as the Rust programs on every one. Across four Claude and four GPT models at five reasoning-effort settings, every current frontier model proves nearly all of a ten-theorem sample at every setting, and more effort raises the cost without raising the number of proofs. The cheapest Claude setting, Sonnet 5.5 at low effort, proves all of the 50 hardest theorems. We also rerun the benchmark's own Verus protocol with Claude Opus 5.5 on the 50 problems with the longest reference proofs. Opus 5.5 alone fails to prove one of them.

## Metadata
- **Published**: 2026-10-02T19:56:10Z
- **Authors**: Traian Serbanuta, Jun Xu, Andrei Stefanescu, Cosmin Radoi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03994v1)